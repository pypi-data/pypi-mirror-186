"""
CoprActionCreateProject
"""

import logging
from typing import Union

from ..actions.project_exists import CoprActionProjectExists
from ..mixins.client_mixin import CoprClientMixin
from ..copr_project_ref import CoprProjectRef
from .action import CoprAction


class CoprActionCreateProject(CoprAction, CoprClientMixin):
    """
    Make or edits a project

    Attributes:

        default_chroots (list): The default chroots to use for the project when creating
        runtime_dependencies (list): List of external repositories (== dependencies,
                                     specified as baseurls) that will be automatically
                                     enabled together with this project repository.
    """

    default_chroots = ["fedora-rawhide-x86_64"]
    runtime_dependencies = "https://download.copr.fedorainfracloud.org/results/" \
        "%40fedora-llvm-team/llvm-compat-packages/fedora-$releasever-$basearch"

    # pylint: disable=too-many-arguments
    def __init__(self,
                 proj: Union[CoprProjectRef, str],
                 description: str = "",
                 instructions: str = "",
                 chroots: list[str] = None,
                 delete_after_days: int = 0,
                 update: bool = False, **kwargs):
        """
        Initialize the make or edit project action.

        Args:
            proj (CoprProjectRef): The owner/project reference to create/edit
            description (str): A descriptive text of the project to create or edit
            instructions (str): A text for the instructions of how to enable this project
            delete_after_days (int): How many days the project shall be kept (0 equals indefinite)
            chroots (list[str]): What change roots shall be used for the project.
                                 Defaults to default_chroots (only upon creation).
            update (bool): whether to update the project if it already exists
        """
        self.__proj = CoprProjectRef(proj)
        self.__description = description
        self.__instructions = instructions
        self.__delete_after_days = delete_after_days
        self.__update = update
        if chroots is None or len(chroots) == 0:
            chroots = self.default_chroots
        self.__chroots = chroots
        super().__init__(**kwargs)
    # pylint: enable=too-many-arguments

    def run(self) -> bool:
        """ Runs the action. """
        func = None
        chroots = None
        exists = CoprActionProjectExists(proj=self.__proj).run()
        if exists and not self.__update:
            logging.info(
                f"project {self.__proj} already exists. Skipping creation.")
            return False
        if not exists:
            logging.info(f"create project {self.__proj}")
            func = self.client.project_proxy.add
            chroots = self.__chroots
        else:
            logging.info(f"project {self.__proj} already exists, updating...")
            func = self.client.project_proxy.edit
            chroots = [] if self.__chroots is None else self.__chroots

            # First get existing chroots and only add new ones
            project = self.client.project_proxy.get(
                ownername=self.__proj.owner, projectname=self.__proj.name)
            existing_chroots = project.chroot_repos.keys()
            new_chroots = set(existing_chroots)

            if (diff_chroots := set(chroots).difference(new_chroots)) != set():
                logging.info(
                    f"add these chroots to the project: {diff_chroots}")
            new_chroots.update(chroots)
            chroots = list(new_chroots)

        # NOTE: devel_mode=True means that one has to manually create the
        # repo
        func(
            ownername=self.__proj.owner,
            projectname=self.__proj.name,
            chroots=chroots,
            description=self.__description,
            instructions=self.__instructions,
            enable_net=True,
            multilib=True,
            devel_mode=True,
            appstream=False,
            runtime_dependencies=self.runtime_dependencies,
            delete_after_days=self.__delete_after_days)

        return True
