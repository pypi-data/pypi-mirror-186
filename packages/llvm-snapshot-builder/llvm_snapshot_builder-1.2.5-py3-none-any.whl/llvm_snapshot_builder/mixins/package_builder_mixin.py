
#!/usr/bin/env python3

"""
CoprPackageBuilderMixin
"""

import logging
from typing import Union
from copr.v3 import CoprRequestException
from ..copr_project_ref import CoprProjectRef


# pylint: disable=too-few-public-methods
class CoprPackageBuilderMixin:
    """
    The base class for package building Actions in Copr

    Attributes:
        default_build_timeout (int): the default build timeout in seconds
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def adjust_chroot(self, proj: Union[CoprProjectRef, str], chroot: str):
        """
        Adjusts the chroot to have --with=snapshot_build and llvm-snapshot-builder package installed.

        Keyword arguments:
            proj -- the project to adjust the chroot for
            chroot -- the chroot to adjust
        """
        logging.info(
            f"adjust chroot {chroot} to have --with=snapshot_build and llvm-snapshot-builder package installed")
        # pylint: disable=line-too-long
        self.client.project_chroot_proxy.edit(
            ownername=proj.owner,
            projectname=proj.name,
            chrootname=chroot,
            with_opts="snapshot_build",
            additional_repos=[
                f"https://download.copr.fedorainfracloud.org/results/%40fedora-llvm-team/llvm-snapshot-builder/{chroot}/",
                f"https://download.copr.fedorainfracloud.org/results/%40fedora-llvm-team/llvm-compat-packages/{chroot}/"
            ],
            additional_packages="llvm-snapshot-builder")
        # pylint: enable=line-too-long

    # pylint: disable=too-many-arguments
    def build(
            self,
            proj: Union[CoprProjectRef, str],
            package_name: str,
            chroots: list[str],
            build_after_id: int = None,
            timeout: int = None):
        """
        Builds a package in Copr

        Args:
            proj (CoprProjectRef): the project to build in
            package_name (str): the package to build
            chroots (list[str]): the chroots to build in
            build_after_id (int): the build to build after
            timeout (int): the build timeout in seconds

        Raises:
            CoprRequestException: if the build could not be created
        """
        build = None
        proj = CoprProjectRef(proj)
        try:
            logging.info(
                f"build package {package_name} in {proj} for chroots {chroots} (build after: {build_after_id})")

            build = self.client.package_proxy.build(
                ownername=proj.owner,
                projectname=proj.name,
                packagename=package_name,
                # See
                # https://python-copr.readthedocs.io/en/latest/client_v3/build_options.html
                buildopts={
                    "timeout": timeout,
                    "chroots": list(set(chroots)),
                    "after_build_id": build_after_id
                },
            )
        except CoprRequestException as ex:
            logging.exception(ex)
            raise ex
        return build
    # pylint: enable=too-many-arguments
