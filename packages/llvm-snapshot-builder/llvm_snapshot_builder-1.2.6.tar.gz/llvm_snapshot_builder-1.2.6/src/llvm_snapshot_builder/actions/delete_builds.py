"""
CoprActionDeleteBuilds
"""

import logging
from ..mixins.client_mixin import CoprClientMixin
from ..mixins.build_walker_mixin import CoprBuildWalkerMixin
from .action import CoprAction


class CoprActionDeleteBuilds(
        CoprAction,
        CoprClientMixin,
        CoprBuildWalkerMixin):
    """
    Deletes builds with particular states.

    Attributes:

        delete_states (list): states to cancel
    """

    delete_states = ["pending", "waiting", "running", "importing"]

    def __init__(self, states: list[str] = None, **kwargs):
        """
        Initializes the action.

        Args:
            states (list): Build states of builds to delete. Defaults to delete_states.
        """
        if states is None:
            states = self.delete_states
        super().__init__(states=states, **kwargs)

    def run(self) -> bool:
        """ Runs the action. """
        logging.info(f"delete builds with these states: {self.delete_states}")
        self.walk(func=None)
        logging.info(f"delete these filtered builds {self.filtered_build_ids}")
        self.client.build_proxy.delete_list(self.filtered_build_ids)
        return True
