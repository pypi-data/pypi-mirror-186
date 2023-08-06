"""
CoprAction
"""

from abc import ABC, abstractmethod


# pylint: disable=too-few-public-methods
class CoprAction(ABC):
    """ The base class for all actions. """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @abstractmethod
    def run(self) -> bool:
        """ Runs the action. """
# pylint: enable=too-few-public-methods
