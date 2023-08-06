#!/usr/bin/env python3

"""
This script simply wraps terragrunt (which is a wrapper around terraform...)
and its main function is to allow you to execute a `run-all` command but
broken up in individual steps.

This makes debugging a complex project easier, such as spotting where the
exact problem is.
"""

# idea: parse output
# - https://github.com/bcochofel/terraplanfeed/tree/main/terraplanfeed

import os
import sys
import subprocess
import shlex
import shutil
import re
import tempfile
import json
import click
import hcl
import networkx as nx

from .printer import Printer
from .terrasafe import run_terrasafe

class TgWrap():
    """
    A wrapper around terragrunt with the sole purpose to make it a bit
    (in an opiionated way) easier to use
    """
    SEPARATOR=':|:'

    def __init__(self, verbose):
        self.printer = Printer(verbose)

        # Check if the "TERRAGRUNT_SOURCE" environment variable is set
        env_var = "TERRAGRUNT_SOURCE"
        if env_var in os.environ:
            self.printer.bold(
                f"'{env_var}' environment variable is set with address: '{os.environ[env_var]}'!"
                )
        else:
            self.printer.bold(
                f"No '{env_var}' variable is set, so the sources as defined in terragrunt.hcl files will be used as is!"
                )

    def _is_installed(self, program):
        """ Checks if a program is installed on the system """
        return shutil.which(program) is not None

    def _construct_command(self, command, debug, exclude_external_dependencies,
        non_interactive=True, no_auto_approve=True, no_lock=True, update_source=False,
        planfile=None, working_dir=None, limit_parallelism=None, terragrunt_args=()):
        """ Constructs the command """
        commands = {
            'generic': '{base_command} {command} --terragrunt-non-interactive {no_auto_approve} {ignore_deps} {debug_level} {update_source} {working_dir} {parallelism} {terragrunt_args}',
            'info': '{base_command} terragrunt-info --terragrunt-non-interactive {ignore_deps} {debug_level} {update_source} {working_dir} {terragrunt_args}',
            'plan': '{base_command} {command} --terragrunt-non-interactive  -out=planfile {ignore_deps} {debug_level} {lock_level} {update_source} {working_dir} {parallelism} {terragrunt_args}',
            'apply': '{base_command} {command} {non_interactive} {no_auto_approve} {parallelism} {ignore_deps} {debug_level} {update_source} {working_dir} {parallelism} {terragrunt_args} {planfile}',
            'show': '{base_command} {command} --terragrunt-non-interactive {ignore_deps} {update_source} -json planfile', # no working dir allowed here!!!
            'destroy': '{base_command} {command} {non_interactive} {no_auto_approve} {ignore_deps} {debug_level} {working_dir} {parallelism} {terragrunt_args} {planfile}',
        }

        lock_stmt         = '-lock=false' if no_lock else ''
        update_stmt       = '--terragrunt-source-update' if update_source else ''
        ignore_deps_stmt  = '--terragrunt-ignore-external-dependencies' if exclude_external_dependencies else '--terragrunt-include-external-dependencies'
        debug_stmt        = '--terragrunt-log-level debug --terragrunt-debug' if debug else ''
        auto_approve_stmt = '--terragrunt-no-auto-approve' if no_auto_approve else ''
        interactive_stmt  = '--terragrunt-non-interactive' if non_interactive else ''
        working_dir_stmt  = f'--terragrunt-working-dir {working_dir}' if working_dir else ''
        parallelism_stmt  = f'--terragrunt-parallelism {limit_parallelism}' if limit_parallelism else ''
        planfile_stmt     = 'planfile' if planfile else ''

        base_command      = 'terragrunt run-all'

        if command not in ['clean']:
            full_command = commands.get(command, commands.get('generic')).format(
                base_command=base_command,
                command=command,
                lock_level=lock_stmt,
                update_source=update_stmt,
                ignore_deps=ignore_deps_stmt,
                debug_level=debug_stmt,
                no_auto_approve=auto_approve_stmt,
                non_interactive=interactive_stmt,
                working_dir=working_dir_stmt,
                parallelism=parallelism_stmt,
                planfile=planfile_stmt,
                terragrunt_args=' '.join(terragrunt_args),
            )
        else:
            full_command = commands.get(command, commands.get('generic'))

        # remove double spaces
        full_command = re.sub(' +', ' ', full_command)

        self.printer.verbose(f'Full command to execute:\n$ {full_command}')

        return full_command

    def _prepare_groups(self, graph, exclude_external_dependencies, working_dir):
        """ Prepare the list of groups that will be executed """

        working_dir = os.path.abspath(working_dir) if working_dir else os.getcwd()
        self.printer.verbose(f"Check for working dir: {working_dir}")

        groups = []
        for group in nx.topological_generations(graph):
            try:
                group.remove("\\n") # terragrunt is adding this in some groups for whatever reason
            except ValueError:
                pass

            for idx, directory in enumerate(group):
                common_path = os.path.commonpath([working_dir, os.path.abspath(directory)])
                # self.printer.verbose(f'Common path for dir {directory}: {common_path}')
                if common_path != working_dir \
                    and exclude_external_dependencies:
                    self.printer.verbose(
                        f"- Remove directory from group as it falls out of scope: {directory}"
                        )
                    group[idx] = None
                else:
                    self.printer.verbose(f"+ Include directory: {directory}")

            # remove the null values from the list
            group = list(filter(None, group))
            if len(group) > 0:
                groups.append(group)

        return groups

    def _get_di_graph(self, working_dir=None):
        """ Gets the directed graph of terragrunt dependencies, and parse it into a graph object """
        graph = None
        try:
            f = tempfile.NamedTemporaryFile(mode='w+', prefix='tgwrap-', delete=True)
            self.printer.verbose(f"Opened temp file for graph collection: {f.name}")

            working_dir_stmt = f'--terragrunt-working-dir {working_dir}' if working_dir else ''
            command = \
                f'terragrunt graph-dependencies --terragrunt-non-interactive {working_dir_stmt}'
            rc = subprocess.run(
                shlex.split(command),
                text=True,
                stdout=f,
            )
            self.printer.verbose(rc)

            f.flush()

            # Read the directed graph and reverse it
            graph = nx.DiGraph(nx.nx_pydot.read_dot(f.name)).reverse()
        except Exception as e:
            self.printer.error(e)
            raise click.ClickException(e)
        finally:
            f.close()

        return graph

    def _analyze_results(self, rc, messages):
        """ Checks for errors """

        error = False

        messages = messages.lower()

        if rc.returncode != 0 or 'error' in messages:
            error = True

        return error

    def _run_graph_step(self, command, working_dir, module, collect_output_file, dry_run, progress):
        """ Runs a step in the graph """

        stop_processing = False

        # if we have a specific working dir, and the dir is relative, combine the two
        if working_dir and not os.path.isabs(module):
            module = os.path.join(os.path.abspath(working_dir), module)
            self.printer.verbose(f'Executing in directory: {working_dir}')

        self.printer.header(
            f'\n\nStart processing module: {module} ({progress})\n\n',
            print_line_before=True,
            )

        try:
            if dry_run:
                self.printer.warning(
                    'In dry run mode, no real actions are executed!!'
                    )
            else:
                if collect_output_file:
                    collect_output_file.write(f'{module}{self.SEPARATOR}')
                    collect_output_file.flush()

                messages = ""

                with tempfile.NamedTemporaryFile(mode='w+', prefix='tgwrap-', delete=False) as f:
                    self.printer.verbose(f"Opened temp file for error collection: {f.name}")
                    rc = {'returncode': 0}
                    rc = subprocess.run(
                        shlex.split(command),
                        text=True,
                        cwd=module,
                        stdout=collect_output_file if collect_output_file else sys.stdout,
                        stderr=f,
                    )
                    self.printer.verbose(rc)

                with open(f.name, 'r') as f:
                    messages = f.read()

                error = self._analyze_results(
                    rc=rc,
                    messages=messages,
                    )

                if error:
                    raise Exception(
                        f'An error situation detected while processing the terragrunt dependencies graph in directory {module}'
                        )
                else:
                    self.printer.success(
                        f'Directory {module} processed successfully',
                    )

        except FileNotFoundError:
            self.printer.warning(f'Directory {module} not found, continue')
        except Exception as e:
            self.printer.error(f"Error occurred:\n{str(e)}")
            self.printer.error("Full stack:", print_line_before=True)
            self.printer.normal(messages, print_line_after=True)
            self.printer.normal(f"Directory {module} failed!")

            stop_processing = True
        finally:
            os.remove(f.name)

        return stop_processing

    def _run_di_graph(
        self, command, exclude_external_dependencies, dry_run,
        ask_for_confirmation=False, collect_output_file=None,
        working_dir=None,
        ):
        "Runs the desired command in the directories as defined in the directed graph"

        graph = self._get_di_graph(working_dir=working_dir)

        # first go through the groups and clean up where needed
        groups = self._prepare_groups(
            graph=graph,
            exclude_external_dependencies=exclude_external_dependencies,
            working_dir=working_dir,
            )

        if not groups:
            self.printer.error('No groups to process, this smells fishy!')
        elif ask_for_confirmation or self.printer.verbose:
            self.printer.header("The following groups will be processed:")
            for idx, group in enumerate(groups):
                self.printer.normal(f"\nGroup {idx+1}:")
                for module in group:
                    self.printer.normal(f"- {module}")

        if ask_for_confirmation:
            response = input("\nDo you want to continue? (y/n) ")
            if response.lower() != "y":
                sys.exit(1)

        stop_processing = False
        nbr_of_groups = len(groups)
        for idx, group in enumerate(groups):
            
            self.printer.header(f'Group {idx+1}')
            self.printer.normal(group)

            if command:
                nbr_of_modules = len(group)
                for idx2, module in enumerate(group):
                    progress = f'module #{idx2+1}/{nbr_of_modules} of group #{idx+1}/{nbr_of_groups}'
                    stop_processing = self._run_graph_step(
                        command=command,
                        working_dir=working_dir,
                        module=module,
                        collect_output_file=collect_output_file,
                        dry_run=dry_run,
                        progress=progress,
                    )

                    if stop_processing:
                        break

            if stop_processing:
                break

    def _run_sync(
        self, source_path, target_path, source_stage, target_stage, auto_approve,
        include_lock_file, dry_run, clean_up, git_source_path=None, source_domain=None,
        ):
        """ Run a sync copying files from a source to a target path """

        if not self._is_installed('rsync'):
            self.printer.error("'rsync' seems not installed. Cannot continue")
        elif not os.path.exists(source_path):
            self.printer.error(f"Cannot find {source_path}. Cannot continue.")
            if source_domain:
                self.printer.error(
                    "Please ensure you are in the directory that contains your projects, " + \
                    "or use --working-dir option"
                )
            else:
                self.printer.error(
                    "Please ensure you are in the root of your project, or use --working-dir option"
                )
        else:
            self.printer.verbose(f"Copying config: {source_path} => {target_path}")

            try:
                os.makedirs(target_path)
            except OSError:
                # directory already exists
                pass

            dry_run_stmt = '--dry-run' if dry_run else ''
            clean_stmt   = '--delete' if clean_up else ''
            env_file_stmt   = "--exclude='env.hcl'" if source_stage != target_stage else "--include='env.hcl'"
            lock_file_stmt  = "--include='.terraform.lock.hcl'" if include_lock_file \
                else "--exclude='.terraform.lock.hcl'"

            cmd = f"rsync -aim {dry_run_stmt} {clean_stmt} " + \
                f"--include='terragrunt.hcl' {lock_file_stmt} {env_file_stmt} " + \
                "--exclude='.terragrunt-cache/' --exclude='.terraform/' " + \
                "--exclude='terragrunt-debug.tfvars.json' --exclude=planfile " + \
                "--exclude='.DS_Store' " + \
                f"{source_path} {target_path}"

            cmd = re.sub(' +', ' ', cmd)

            self.printer.header("Will be deploying:", print_line_before=True)
            self.printer.normal(f"from: {git_source_path if git_source_path else source_path}")
            self.printer.normal(f"to:   {target_path}")
            self.printer.verbose(f"Using command:\n$ {cmd}")

            if not auto_approve:
                response = input("\nDo you want to continue? (y/n) ")
                if response.lower() != "y":
                    sys.exit(1)

            rc = subprocess.run(shlex.split(cmd))
            self.printer.verbose(rc)

    def run(self, command, debug, dry_run, no_lock, update_source,
        planfile, auto_approve, working_dir, terragrunt_args):
        """ Executes a terragrunt command on a single module """

        self.printer.verbose(f"Attempting to execute 'run {command}'")
        if terragrunt_args:
            self.printer.verbose(f"- with additional parameters: {' '.join(terragrunt_args)}")

        check_for_file="terragrunt.hcl"
        if working_dir:
            check_for_file = os.path.join(working_dir, check_for_file)
        if not os.path.isfile(check_for_file):
            self.printer.error(
                f"{check_for_file} not found, this seems not to be a terragrunt module directory!"
                )
            sys.exit(1)

        cmd = self._construct_command(
            command=command,
            debug=debug,
            exclude_external_dependencies=True,
            no_lock=no_lock,
            update_source=update_source,
            planfile=planfile,
            no_auto_approve=(not auto_approve),
            working_dir=working_dir,
            terragrunt_args=terragrunt_args,
        )

        if dry_run:
            self.printer.warning(f'In dry run mode, no real actions are executed!!')
        else:
            # the `posix=False` is to prevent the split command to remove quotes from strings,
            # e.g. when executing commands like this:
            # tgwrap state mv 'azuread_group.this["viewers"]' 'azuread_group.this["readers"]'
            rc = subprocess.run(shlex.split(cmd, posix=False))
            self.printer.verbose(rc)

    def run_all(self, command, debug, dry_run, no_lock, update_source,
        exclude_external_dependencies, step_by_step, planfile, auto_approve, 
        working_dir, limit_parallelism, terragrunt_args):
        """ Executes a terragrunt command across multiple modules """

        self.printer.verbose(f"Attempting to execute 'run-all {command}'")
        if terragrunt_args:
            self.printer.verbose(f"- with additional parameters: {' '.join(terragrunt_args)}")

        # auto approve is only relevant with a modifying command
        modifying_command = (command.lower() in ['apply', 'destroy'])
        auto_approve = auto_approve if modifying_command else True

        cmd = self._construct_command(
            command=command,
            debug=debug,
            exclude_external_dependencies=True if step_by_step else exclude_external_dependencies,
            non_interactive=True if step_by_step else auto_approve,
            no_lock=no_lock,
            update_source=update_source,
            planfile=planfile,
            no_auto_approve=False if step_by_step else (not auto_approve),
            working_dir=None if step_by_step else working_dir,
            terragrunt_args=terragrunt_args,
            limit_parallelism=limit_parallelism,
        )

        if step_by_step:
            self.printer.verbose(
                f'This command will be executed for each individual module:\n$ {cmd}'
                )
            self._run_di_graph(
                command=cmd,
                exclude_external_dependencies=exclude_external_dependencies,
                working_dir=working_dir,
                ask_for_confirmation=(not auto_approve),
                dry_run=dry_run,
            )
        else:
            if dry_run:
                self.printer.warning('In dry run mode, no real actions are executed!!')
            else:
                rc = subprocess.run(shlex.split(cmd))
                self.printer.verbose(rc)

    def run_import(self, address, id, dry_run, working_dir, no_lock, terragrunt_args):
        """ Executes the terragrunt/terraform import command """

        self.printer.verbose(f"Attempting to execute 'run import'")
        if terragrunt_args:
            self.printer.verbose(f"- with additional parameters: {' '.join(terragrunt_args)}")

        check_for_file="terragrunt.hcl"
        if working_dir:
            check_for_file = os.path.join(working_dir, check_for_file)
        if not os.path.isfile(check_for_file):
            self.printer.error(
                f"{check_for_file} not found, this seems not to be a terragrunt module directory!"
                )
            sys.exit(1)

        lock_stmt         = '-lock=false' if no_lock else ''
        working_dir_stmt  = f'--terragrunt-working-dir {working_dir}' if working_dir else ''

        cmd = f"terragrunt import {working_dir_stmt} {lock_stmt} {address} {id} {' '.join(terragrunt_args)}"
        cmd = re.sub(' +', ' ', cmd)
        self.printer.verbose(f'Full command to execute:\n$ {cmd}')

        if dry_run:
            self.printer.warning(f'In dry run mode, no real actions are executed!!')
        else:
            env = os.environ.copy()
            # TERRAGRUNT_SOURCE should not be present (or it should be a fully qualified path (which is typically not the case))
            try:
                value = env.pop('TERRAGRUNT_SOURCE')
                if value:
                    self.printer.verbose(
                        f'Terragrunt source environment variable with value {value} will be ignored'
                        )
            except KeyError:
                pass

            # the `posix=False` is to prevent the split command to remove quotes from strings,
            # e.g. when executing commands like this:
            # tgwrap import 'azuread_group.this["viewers"]' '123e4567-e89b-12d3-a456-426655440000'
            rc = subprocess.run(
                shlex.split(cmd, posix=False),
                env=env,
            )
            self.printer.verbose(rc)

    def analyze(self, dry_run, exclude_external_dependencies, working_dir, out, terragrunt_args):
        """ Analyzes the plan files """

        self.printer.verbose("Attempting to 'analyze'")
        if terragrunt_args:
            self.printer.verbose(f"- with additional parameters: {' '.join(terragrunt_args)}")

        # first run a 'show' and write output to file
        cmd = self._construct_command(
            command='show',
            exclude_external_dependencies=True,
            debug=False,
            terragrunt_args=terragrunt_args,
            )

        # Check if the "TERRASAFE_CONFIG" environment variable is set
        env_var = "TERRASAFE_CONFIG"
        ts_config = None
        if not env_var in os.environ:
            self.printer.warning(
                f"{env_var} environment variable is not set, this is required for running the terrasafe command!"
                )
        # and if it exists as a file
        elif not os.path.exists(os.environ.get(env_var)):
            self.printer.warning(
                f"{env_var} environment variable is set, but the file it points to does not exist!"
                )
        else:
            config_path = os.environ.get(env_var)
            self.printer.verbose(
                f"\nRun terrasafe using config {config_path}"
                )

            config_file = open(config_path)
            ts_config = json.load(config_file)

        ts_validation_successful = True
        changes = {}
        try:
            # then run it and capture the output
            with tempfile.NamedTemporaryFile(mode='w+', prefix='tgwrap-', delete=False) as f:
                self.printer.verbose(f"Opened temp file for output collection: {f.name}")

                self._run_di_graph(
                    command=cmd,
                    exclude_external_dependencies=exclude_external_dependencies,
                    dry_run=dry_run,
                    collect_output_file=f,
                    working_dir=working_dir,
                    ask_for_confirmation=False,
                )

            with open(f.name, 'r') as f:
                for line in f:
                    split_line = line.split(self.SEPARATOR)
                    module = split_line[0]
                    plan_file = split_line[1]

                    changes[module] = {
                        "deletions" : [],
                        "other" : [],
                        "unauthorized" : [],
                    }

                    try:
                        data = json.loads(plan_file)

                        if 'resource_changes' in data and len(data['resource_changes']) > 0:
                            for rc in data['resource_changes']:
                                # check if we do have actual changes
                                actions = rc['change']['actions']
                                action = f'{rc["address"]}: {", ".join(actions)}'
                                if len(actions) == 1 and (actions[0] == 'no-op' or actions[0] == 'read'):
                                    pass # ignore, just an state change
                                elif 'delete' in actions:
                                    changes[module]["deletions"].append(action)
                                else:
                                    changes[module]["other"].append(action)

                        if ts_config:
                            changes[module]["unauhhorized"] = run_terrasafe(
                                config=ts_config,
                                data=data,
                                verbose=self.printer.print_verbose,
                                )
                            if len(changes[module]["unauhhorized"]) > 0:
                                ts_validation_successful = False
                    except json.decoder.JSONDecodeError as e:
                        raise Exception(
                            f"Planfile for {module} was no proper json, further analysis not possible."
                            ) from e
        finally:
            os.remove(f.name)

        self.printer.header("Analysis results:", print_line_before=True)
        for key, value in changes.items():
            self.printer.header(f'Module: {key}')
            if not (value["deletions"] or value["other"] or value["unauthorized"]):
                self.printer.success('- No changes detected')
            if value["unauthorized"]:
                self.printer.error('- Unauthorized deletions:')
                for m in value["unauhtorized"]:
                    self.printer.error(f' -> {m}')
            if value["deletions"]:
                self.printer.warning('- Deletions:')
                for m in value["deletions"]:
                    self.printer.warning(f' -> {m}')
            if value["other"]:
                self.printer.normal('- Other:')
                for m in value["other"]:
                    self.printer.normal(f' -> {m}')

        if out:
            print(json.dumps(changes, indent=4))

        if not ts_validation_successful:
            self.printer.error("Terrasafe validation failed on one or more modules")
            sys.exit(1)

    def deploy(
        self, source_stage, target_stage, source_domain, target_domain, module,
        auto_approve, dry_run, clean_up, include_lock_file, working_dir, 
        ):
        """ Deploys the terragrunt config files from one stage to another (and possibly to a different domain) """
    
        if target_domain and not source_domain:
            raise Exception("Providing a target domain while omitting the source domain is not supported!")
        if source_domain and not target_domain:
            raise Exception("Providing a source domain while omitting the target domain is not supported!")

        if target_domain and not target_stage:
            self.printer.verbose(f"No target stage given, assume the same as source stage")
            target_stage=source_stage

        # do we have a working dir?
        working_dir = working_dir if working_dir else os.getcwd()
        # the domains will be ignored when omitted as input
        source_path = os.path.join(working_dir, source_domain, source_stage, module, '')
        target_path = os.path.join(working_dir, target_domain, target_stage, module, '')

        self._run_sync(
            source_path=source_path,
            target_path=target_path,
            source_domain=source_domain,
            source_stage=source_stage,
            target_stage=target_stage,
            include_lock_file=include_lock_file,
            auto_approve=auto_approve,
            dry_run=dry_run,
            clean_up=clean_up,
        )

    def git_deploy(
        self, git_repo, source_directory, target_domain, target_stage,
        auto_approve, dry_run, include_lock_file, working_dir, 
        ):
        """ Deploys the terragrunt config files from a git repository """

        DEFAULT_VERSION='latest'

        # first try to determine the desired version, this should be coded in
        # an `version.hcl` file in the root of the target
        version_file = os.path.join(os.getcwd(), target_domain, target_stage, "version.hcl")
        version = DEFAULT_VERSION # default
        if os.path.isfile(version_file):
            self.printer.verbose(f'Try to get desired version info from {version_file}')
            with open(version_file, 'r') as f:
                version_info = hcl.load(f)

            try:
                version = version_info['locals'].get('platform_version')
            except AttributeError as e:
                click.warning(f'Could not determine platform version from file: {e}')
        else:
            self.printer.warning(f"Version file {version_file}'' not found, use '{DEFAULT_VERSION}' as version.")
        
        self.printer.verbose(f"Using version '{version}' as source")

        try:
            temp_dir = os.path.join(tempfile.mkdtemp(prefix='tgwrap-'), "tg-source")

            # clone the repo
            cmd = f"git clone {git_repo} {temp_dir}"
            rc = subprocess.run(
                shlex.split(cmd),
                check=True,
                stdout=sys.stdout if self.printer.print_verbose else subprocess.DEVNULL,
                stderr=sys.stderr if self.printer.print_verbose else subprocess.DEVNULL,
                )
            self.printer.verbose(rc)

            # now check out the specific version if we don't want latest
            if version != DEFAULT_VERSION:
                cmd = f"git checkout -b source {version}"
                rc = subprocess.run(
                    shlex.split(cmd),
                    cwd=temp_dir,
                    check=True,
                    stdout=sys.stdout if self.printer.print_verbose else subprocess.DEVNULL,
                    stderr=sys.stderr if self.printer.print_verbose else subprocess.DEVNULL,
                    )
                self.printer.verbose(rc)

            # do we have a working dir?
            working_dir = working_dir if working_dir else os.getcwd()

            # run some sanity checks
            reversed_path = list(reversed(source_directory.split('/')))
            source_stage = reversed_path[0]
            source_type = reversed_path[1]

            if target_stage == 'global' and source_stage != target_stage:
                self.printer.error(f'You are trying to copy source stage {source_stage} to a global stage!')
                self.printer.error('This is not correct, exit.')
                sys.exit(1)

            reversed_path = list(reversed(working_dir.split('/')))
            target_type = reversed_path[0]
            if target_type.upper() == 'DLZS' and not target_domain:
                self.printer.warning(
                    f'Detected that you are targetting a landing zone project but you provided no target domain!'
                    )

            # the source stage is either 'global' (if target == global) or 'dev'
            source_stage = target_stage if target_stage == 'global' else 'dev'
            # construct the paths
            source_path = os.path.join(temp_dir, source_directory, '')
            target_path = os.path.join(working_dir, target_domain, target_stage, '')

            self._run_sync(
                source_path=source_path,
                git_source_path=f'{git_repo}//{source_directory}?ref={version}',
                target_path=target_path,
                source_stage=source_stage,
                target_stage=target_stage,
                include_lock_file=include_lock_file,
                auto_approve=auto_approve,
                dry_run=dry_run,
                clean_up=False,
            )

        finally:
            shutil.rmtree(temp_dir)

    def show_graph(self, exclude_external_dependencies, working_dir, terragrunt_args):
        """ Shows the dependencies of a project """

        self.printer.verbose(f"Attempting to show dependencies")
        if terragrunt_args:
            self.printer.verbose(f"- with additional parameters: {' '.join(terragrunt_args)}")

        "Runs the desired command in the directories as defined in the directed graph"
        graph = self._get_di_graph(working_dir=working_dir)

        # first go through the groups and clean up where needed
        groups = self._prepare_groups(
            graph=graph,
            exclude_external_dependencies=exclude_external_dependencies,
            working_dir=working_dir,
            )

        self.printer.header("The following groups will be processed:")
        for idx, group in enumerate(groups):
            self.printer.normal(f"\nGroup {idx+1}:")
            for directory in group:
                self.printer.normal(f"- {directory}")

    def clean(self, working_dir):
        """ Clean the temporary files of a terragrunt/terraform project """

        cmd = 'find . -name ".terragrunt-cache" -type d -exec rm -rf {} \; ; find . -name ".terraform" -type d -exec rm -rf {} \;'
        rc = subprocess.run(
            cmd,
            shell=True,
            check=True,
            stdout=sys.stdout if self.printer.print_verbose else subprocess.DEVNULL,
            stderr=sys.stderr if self.printer.print_verbose else subprocess.DEVNULL,
            cwd=working_dir if working_dir else None,
            )
        self.printer.verbose(rc)

