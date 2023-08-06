#!/usr/bin/env python3

"""
CoprActionBuildPackages
"""

import logging
from typing import Union
from ..copr_project_ref import CoprProjectRef
from ..mixins.package_builder_mixin import CoprPackageBuilderMixin
from ..mixins.client_mixin import CoprClientMixin
from .action import CoprAction
from .create_packages import CoprActionCreatePackages
from .create_project import CoprActionCreateProject


class CoprActionBuildPackages(
        CoprAction,
        CoprClientMixin,
        CoprPackageBuilderMixin):
    """
    Builds a list of packages for the given chroots in the order they are given.

    NOTE: We kick-off builds for each chroot individually so that an x86_64
    build doesn't have to wait for a potentially slower s390x build.
    """

    # pylint: disable=too-many-arguments
    def __init__(
            self,
            proj: Union[CoprProjectRef, str],
            package_names: list[str] = None,
            chroots: list[str] = None,
            wait_on_build_id: int = None,
            timeout:int=None,
            **kwargs):
        """
        Initializes the action.

        Args:
            package_names (list): Packages to build. Defaults to default packages from CoprActionMakeOrEditPackages.
            chroots (list): Chroots to build in. Defaults to default chroots from CoprActionMakeOrEditProject.
            wait_on_build_id (int): Wait for this build to finish before starting the build.
        """
        self.__proj = CoprProjectRef(proj)
        if package_names is None:
            package_names = CoprActionCreatePackages.default_package_names
        self.__package_names = package_names
        if len(chroots) == 0:
            logging.info(f"no chroots given, using default chroots {CoprActionCreateProject.default_chroots}")
            chroots = CoprActionCreateProject.default_chroots
        self.__chroots = chroots
        self.__timeout = timeout
        self.__wait_on_build_id = wait_on_build_id
        super().__init__(**kwargs)
    # pylint: enable=too-many-arguments

    def run(self) -> bool:
        """ Runs the action. """
        logging.info(f"building packages {self.__package_names} in chroots {self.__chroots}")
        for chroot in self.__chroots:
            self.adjust_chroot(proj=self.__proj, chroot=chroot)
            logging.info(
                f"build packages ({self.__package_names}) in chroot: {chroot}")
            previous_build_id = self.__wait_on_build_id
            for package_name in self.__package_names:
                build = self.build(
                    proj=self.__proj,
                    package_name=package_name,
                    chroots=[chroot],
                    build_after_id=previous_build_id,
                    timeout=self.__timeout)
                if build != {}:
                    previous_build_id = build.id
                    logging.info(
                        f"URL: https://copr.fedorainfracloud.org/coprs/{self.__proj.owner}"
                        f"/{self.__proj.name}/build/{previous_build_id}/")
                else:
                    logging.warning(
                        f"skipped build of package {package_name} in chroot {chroot}")
        return True
