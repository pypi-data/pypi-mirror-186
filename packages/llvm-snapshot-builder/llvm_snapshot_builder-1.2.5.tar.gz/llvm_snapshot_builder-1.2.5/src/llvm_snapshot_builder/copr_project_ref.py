"""
CoprProjectRef
"""

from typing import Union


class CoprProjectRef:
    """ CoprProjectRef is a reference to a Copr project by ownername and projectname. """

    def __init__(
            self,
            owner_project: Union[str, "CoprProjectRef"],
            ** kwargs):
        """ Creates a new CoprProjectRef. """
        if str(owner_project) == owner_project:
            self.__ownername, self.__projectname = owner_project.split("/")
        elif isinstance(owner_project, CoprProjectRef):
            self.__ownername = owner_project.owner
            self.__projectname = owner_project.name
        else:
            raise TypeError(
                "owner_project must be a string or CoprProjectRef but is "\
                    f"{type(owner_project)}': {owner_project}")

        if self.__ownername is None or self.__ownername == "":
            raise ValueError("ownername MUST NOT be empty")
        if self.__projectname is None or self.__projectname == "":
            raise ValueError("projectname MUST NOT be empty")
        super().__init__(**kwargs)

    @property
    def owner(self) -> str:
        """ Returns the ownername that references this project """
        return self.__ownername

    @property
    def name(self) -> str:
        """ Returns the projectname that references this project """
        return self.__projectname

    @property
    def ref(self) -> str:
        """ Returns the ownername/projectname string """
        return f"{self.__ownername}/{self.__projectname}"

    def __str__(self):
        """ Returns the ownername/projectname string """
        return self.ref
