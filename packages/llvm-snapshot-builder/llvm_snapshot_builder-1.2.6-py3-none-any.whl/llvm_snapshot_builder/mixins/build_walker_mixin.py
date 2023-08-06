"""
CoprBuildWalkerMixin
"""

from typing import Union, Callable
from ..copr_project_ref import CoprProjectRef


class CoprBuildWalkerMixin:
    """
    Allows you to walk over each build filtered by state and chroot.
    Make sure you use CoprClientMixin as well.
    """

    def __init__(
            self,
            proj: Union[CoprProjectRef, str],
            chroots: list[str] = None,
            states: list[str] = None,
            **kwargs):
        self.__proj = CoprProjectRef(proj)
        self.__chroots = chroots
        self.__states = states
        # This is where the resulting build IDs are stored
        self.__batch_ids = None
        super().__init__(**kwargs)  # forwards all unused arguments

    @property
    def filtered_build_ids(self) -> list[str]:
        """ Returns the filtered build IDs """
        return self.__batch_ids

    def walk(self, func: Callable[..., bool] = None) -> bool:
        """
        Walks over every filtered build and optionally (if given) calls `func`
        with the current build object. When `func` returns `False`, the `walk`
        function stops returns `False` as well.

        Along the way, this function populates the `filtered_build_ids` property
        with the builds that were filtered. This can be used for copr operations
        that can handle multiple build ids.
        """
        builds = self.client.build_proxy.get_list(
            self.__proj.owner, self.__proj.name)
        self.__batch_ids = []
        for build in builds:
            if self.__states and build.state not in self.__states:
                continue

            if self.__chroots is not None:
                if set(self.__chroots).isdisjoint(set(build.chroots)):
                    continue

            self.__batch_ids.append(build.id)
            if func is not None:
                if not func(build):
                    return False
        return True
