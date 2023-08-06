"""
CoprActionForkProject
"""

import logging
from typing import Union
from ..mixins.client_mixin import CoprClientMixin
from ..copr_project_ref import CoprProjectRef
from .action import CoprAction


class CoprActionForkProject(CoprAction, CoprClientMixin):
    """ Forks the project from the given source into the target project. """

    def __init__(
            self,
            source: Union[CoprProjectRef, str],
            target: Union[CoprProjectRef, str],
            **kwargs):
        """
        Intiializes the action.

        Args:
            source (CoprProjectRef): source project from which to fork
            target (CoprProjectRef): target project into which to fork
        """
        self.__source = CoprProjectRef(source)
        self.__target = CoprProjectRef(target)
        super().__init__(**kwargs)

    def run(self) -> bool:
        """ Runs the action. """
        logging.info(f"fork project {self.__source} into project {self.__target}")
        self.client.project_proxy.fork(
            ownername=self.__source.owner,
            projectname=self.__source.name,
            dstownername=self.__target.owner,
            dstprojectname=self.__target.name, confirm=True)
        return True
