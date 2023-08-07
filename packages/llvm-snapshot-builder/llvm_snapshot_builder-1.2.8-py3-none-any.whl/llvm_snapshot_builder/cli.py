#!/bin/env python3

"""
llvm_snapshot_builder.cli provides a CLI interface to the llvm_snapshot_builder
"""

import argparse
import sys
import logging

from .actions.action import CoprAction
from .actions.build_all_packages import CoprActionBuildAllPackages
from .actions.build_packages import CoprActionBuildPackages
from .actions.cancel_builds import CoprActionCancelBuilds
from .actions.delete_builds import CoprActionDeleteBuilds
from .actions.delete_project import CoprActionDeleteProject
from .actions.fork_project import CoprActionForkProject
from .actions.create_packages import CoprActionCreatePackages
from .actions.create_project import CoprActionCreateProject
from .actions.project_exists import CoprActionProjectExists
from .actions.regenerate_repos import CoprActionRegenerateRepos
from .copr_project_ref import CoprProjectRef
from .__init__ import __version__


# pylint: disable=too-few-public-methods
class HelpAction(CoprAction):
    """ Prints the help message. """

    def __init__(self, arg_parser: argparse.ArgumentParser, **kwargs):
        self.__arg_parser = arg_parser
        super().__init__(**kwargs)

    def run(self) -> bool:
        """ Runs the action. """
        self.__arg_parser.print_help()
        return True
# pylint: enable=too-few-public-methods


CMD_BUILD_ALL_PACKAGES = 'build-all-packages'
CMD_BUILD_PACKAGES = 'build-packages'
CMD_CREATE_PACKAGES = 'create-packages'
CMD_CANCEL_BUILDS = 'cancel-builds'
CMD_DELETE_BUILDS = 'delete-builds'
CMD_DELETE_PROJECT = 'delete-project'
CMD_FORK_PROJECT = 'fork-project'
CMD_CREATE_PROJECT = 'create-project'
CMD_PROJECT_EXISTS = 'project-exists'
CMD_REGENERATE_REPOS = 'regenerate-repos'

cmd_action_map = {
    CMD_BUILD_ALL_PACKAGES: CoprActionBuildAllPackages,
    CMD_BUILD_PACKAGES: CoprActionBuildPackages,
    CMD_CANCEL_BUILDS: CoprActionCancelBuilds,
    CMD_CREATE_PACKAGES: CoprActionCreatePackages,
    CMD_CREATE_PROJECT: CoprActionCreateProject,
    CMD_DELETE_BUILDS: CoprActionDeleteBuilds,
    CMD_DELETE_PROJECT: CoprActionDeleteProject,
    CMD_FORK_PROJECT: CoprActionForkProject,
    CMD_PROJECT_EXISTS: CoprActionProjectExists,
    CMD_REGENERATE_REPOS: CoprActionRegenerateRepos,
}


def get_action(
        arg_parser: argparse.ArgumentParser,
        arguments: list = None) -> CoprAction:
    """
    Parses all arguments set up by build_main_parser() and returns the
    action to execute.

    Keyword Arguments:
        arg_parser {argparse.ArgumentParser} -- The argument parser to use.
        arguments {list} -- The arguments to parse. If None, sys.argv is used.
    """

    args = arg_parser.parse_args(arguments)
    if not args.command:
        return HelpAction(arg_parser)
    if (cmd := args.command) not in cmd_action_map:
        return HelpAction(arg_parser)

    # Sanitize action arguments
    # -------------------------
    # We pass all arguments to the action as keyword arguments. That's why we
    # fist need to clean up the variables a bit.
    vargs = dict(vars(args))
    del vargs["command"]
    if "proj" in vargs:
        vargs["proj"] = CoprProjectRef(vargs["proj"])
    if "description_file" in vargs:
        if vargs["description_file"] is not None:
            vargs["description"] = vargs["description_file"].read()
        del vargs["description_file"]
    if "instructions_file" in vargs:
        if vargs["instructions_file"] is not None:
            vargs["instructions"] = vargs["instructions_file"].read()
        del vargs["instructions_file"]
    if "log_level" in vargs:
        logging.basicConfig(level=vargs["log_level"])
        del vargs["log_level"]
    return cmd_action_map[cmd](**vargs)


def build_main_parser() -> argparse.ArgumentParser:
    """ Returns the main parser for command line arguments """

    proj_kwargs = {
        "dest": 'proj',
        "metavar": '"OWNER/PROJECT"',
        "type": str,
        "required": True,
        "help": "owner (or group) and project name of the copr project to "
        "work with (e.g. 'foo/bar')"
    }
    chroots_kwargs = {
        "dest": 'chroots',
        "metavar": 'CHROOT',
        "nargs": '+',
        "default": "",
        "type": str,
        "help": "list of chroots to work on"
    }
    timeout_kwargs = {
        "dest": 'timeout',
        "default": 30 * 3600,
        "type": int,
        "help": "build timeout in seconds for each package (defaults to: 30*3600=108000)"
    }
    parser = argparse.ArgumentParser(
        description='Interact with the LLVM snapshot builds on Fedora Copr.',
        allow_abbrev=True)

    parser.add_argument(
        '--version',
        action='version',
        version=f"llvm_snapshot_builder {__version__}")

    logging_group = parser.add_mutually_exclusive_group()
    logging_group.add_argument(
        '--debug',
        action="store_const",
        dest="log_level",
        const=logging.DEBUG,
        default=logging.WARNING)
    logging_group.add_argument(
        '--verbose',
        action="store_const",
        dest="log_level",
        const=logging.INFO)

    # Subparsers

    subparsers = parser.add_subparsers(
        help='sub-command --help', dest="command")

    # FORK

    subparser = subparsers.add_parser(
        CMD_FORK_PROJECT, help='fork from a given project and then exit')
    subparser.add_argument(
        '--source',
        dest='source',
        required=True,
        type=str,
        help="the project to fork from (e.g. @fedora-llvm-team/llvm-snapshots-incubator")

    subparser.add_argument(
        '--target',
        dest='target',
        required=True,
        type=str,
        help="the project to fork to (e.g. foo/bar")

    # BUILD ALL PACKAGES

    subparser = subparsers.add_parser(
        CMD_BUILD_ALL_PACKAGES, help='build packages')
    subparser.add_argument('--proj', **proj_kwargs)
    subparser.add_argument('--chroots', **chroots_kwargs)
    subparser.add_argument('--timeout', **timeout_kwargs)

    # CREATE PACKAGES

    subparser = subparsers.add_parser(
        CMD_CREATE_PACKAGES, help='creates or edits the LLVM packages in Copr')
    subparser.add_argument('--proj', **proj_kwargs)
    subparser.add_argument(
        '--packagenames',
        dest='packagenames',
        metavar='PACKAGENAME',
        required=False,
        nargs='+',
        type=str,
        help="list of LLVM packagenames to create in order")
    subparser.add_argument(
        '--update',
        dest='update',
        action='store_true',
        help="will update an already existing packages")

    # BUILD PACKAGES

    subparser = subparsers.add_parser(
        CMD_BUILD_PACKAGES, help='build packages')
    subparser.add_argument('--proj', **proj_kwargs)
    subparser.add_argument('--chroots', **chroots_kwargs)
    subparser.add_argument(
        '--packagenames',
        dest='package_names',
        metavar='PACKAGENAME',
        required=True,
        nargs='+',
        type=str,
        help="list of LLVM packagenames to build in order")
    subparser.add_argument('--timeout', **timeout_kwargs)
    subparser.add_argument(
        '--wait-on-build-id',
        dest='wait_on_build_id',
        default=None,
        type=int,
        help="wait on the given build ID before starting the build")

    # CANCEL BUILDS

    subparser = subparsers.add_parser(
        CMD_CANCEL_BUILDS,
        help="""
        cancel builds with these states before creating new ones and
        then exits: "pending", "waiting", "running", "importing"
        """)
    subparser.add_argument('--proj', **proj_kwargs)
    subparser.add_argument('--chroots', **chroots_kwargs)

    # DELETE BUILDS

    subparser = subparsers.add_parser(
        CMD_DELETE_BUILDS,
        help='cancel running builds and delete all builds afterwards')
    subparser.add_argument('--proj', **proj_kwargs)
    subparser.add_argument('--chroots', **chroots_kwargs)

    # PROJECT EXISTS

    subparser = subparsers.add_parser(
        CMD_PROJECT_EXISTS,
        help='checks if the project exists in copr, then exit')
    subparser.add_argument('--proj', **proj_kwargs)

    # DELETE PROJECT

    subparser = subparsers.add_parser(
        CMD_DELETE_PROJECT, help='Deletes the project')
    subparser.add_argument('--proj', **proj_kwargs)

    # REGENERATE REPOS

    subparser = subparsers.add_parser(
        CMD_REGENERATE_REPOS, help='Regenerates the repo for the project')
    subparser.add_argument('--proj', **proj_kwargs)

    # CREATE PROJECT

    subparser = subparsers.add_parser(
        CMD_CREATE_PROJECT, help='Creates or edits a project')
    subparser.add_argument('--proj', **proj_kwargs)
    subparser.add_argument('--chroots', **chroots_kwargs)
    subparser.add_argument(
        '--description-file',
        dest='description_file',
        required=False,
        type=argparse.FileType('r', encoding='UTF-8'),
        help="file containing the project description in markdown format")
    subparser.add_argument(
        '--instructions-file',
        dest='instructions_file',
        required=False,
        type=argparse.FileType('r', encoding='UTF-8'),
        help="file containing the project instructions in markdown format")
    subparser.add_argument(
        '--delete-after-days',
        dest='delete_after_days',
        default=0,
        type=int,
        help="delete the project to be created after a given number of days "
        "(default: 0 which means \"keep forever\")")
    subparser.add_argument(
        '--update',
        dest='update',
        action='store_true',
        help="will update an already existing project")

    return parser


def main(arguments=None) -> bool:
    """ Main function """
    return get_action(
        arg_parser=build_main_parser(),
        arguments=arguments).run()


if __name__ == "__main__":
    sys.exit(0 if main(sys.argv[1:]) else 1)
