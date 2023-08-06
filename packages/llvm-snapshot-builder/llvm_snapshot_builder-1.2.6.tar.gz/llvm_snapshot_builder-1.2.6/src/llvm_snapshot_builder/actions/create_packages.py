"""
CoprActionCreatePackages
"""

import logging
from typing import Union
from ..mixins.client_mixin import CoprClientMixin
from ..copr_project_ref import CoprProjectRef
from .action import CoprAction


class CoprActionCreatePackages(CoprAction, CoprClientMixin):
    """
    Make or edits packages in a copr project.
    NOTE: This doesn't build the packages!

    Attributes:

        default_package_names (list[str]): the default packages to create/edit if not specified
    """

    default_package_names = [
        "python-lit",
        "llvm",
        "compiler-rt",
        "lld",
        "clang",
        "mlir",
        "libomp"
    ]

    def __init__(
            self,
            proj: Union[CoprProjectRef, str],
            packagenames: list[str] = None,
            update: bool = False,
            **kwargs):
        """
        Initialize the make or edit project action.

        Args:
            ownername (str): the owner or group in which to create/edit the packages
            projectname (str): the project's name to in which to create/edit the packages
            packagenames (list[str]): the packages to create/edit
        """
        self.__proj = CoprProjectRef(proj)
        self.__packagenames = packagenames
        self.__update = update
        if packagenames is None:
            self.__packagenames = self.default_package_names
        super().__init__(**kwargs)

    def run(self) -> bool:
        """ Runs the action. """
        packages = self.client.package_proxy.get_list(
            ownername=self.__proj.owner, projectname=self.__proj.name)
        existingpackagenames = [p.name for p in packages]

        for packagename in self.__packagenames:
            packageattrs = {
                "ownername": self.__proj.owner,
                "projectname": self.__proj.name,
                "packagename": packagename,
                # See
                # https://python-copr.readthedocs.io/en/latest/client_v3/package_source_types.html#scm
                "source_type": "scm",
                "source_dict": {
                    "clone_url": "https://src.fedoraproject.org/rpms/" + packagename + ".git",
                    "committish": "upstream-snapshot",
                    "spec": packagename + ".spec",
                    "scm_type": "git",
                    "source_build_method": "make_srpm",
                }
            }
            if packagename in existingpackagenames:
                if not self.__update:
                    logging.warning(f"package already exists and is not updated: {packagename}")
                    continue
                logging.info(
                    f"reset and editing package {packagename} in {self.__proj}")
                self.client.package_proxy.reset(
                    ownername=self.__proj.owner,
                    projectname=self.__proj.name,
                    packagename=packagename)
                self.client.package_proxy.edit(**packageattrs)
            else:
                logging.info(
                    f"create package {packagename} in {self.__proj}")
                self.client.package_proxy.add(**packageattrs)
        return True
