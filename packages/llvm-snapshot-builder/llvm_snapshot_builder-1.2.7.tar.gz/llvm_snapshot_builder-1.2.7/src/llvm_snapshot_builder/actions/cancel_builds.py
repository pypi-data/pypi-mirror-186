"""
CoprActionCancelBuilds
"""

import logging
from ..mixins.build_walker_mixin import CoprBuildWalkerMixin
from ..mixins.client_mixin import CoprClientMixin
from .action import CoprAction


class CoprActionCancelBuilds(
        CoprAction,
        CoprClientMixin,
        CoprBuildWalkerMixin):
    """
    Cancels builds with particular states.

    Attributes:

        cancel_states (list): states to cancel
    """

    cancel_states = ["pending", "waiting", "running", "importing"]

    def __init__(self, states: list[str] = None, ** kwargs):
        """
        Initializes the action.

        Args:
            states (list): States of build to cancel. Defaults to cancel_states.
        """
        if states is None:
            states = self.cancel_states
        super().__init__(states=states, **kwargs)

    def run(self) -> bool:
        """ Runs the action. """
        logging.info(f"cancel builds with these states: {self.cancel_states}")

        def cancel_build(build) -> bool:
            logging.info(f"cancel build {build.id}")
            self.client.build_proxy.cancel(build.id)
            return True
        self.walk(func=cancel_build)
        return True
