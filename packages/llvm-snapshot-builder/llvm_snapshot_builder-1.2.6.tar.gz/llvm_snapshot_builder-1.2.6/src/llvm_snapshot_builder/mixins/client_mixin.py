"""
CoprClientMixin
"""

import logging
import os
from copr.v3 import Client


# pylint: disable=too-few-public-methods
class CoprClientMixin:
    """ Any class that needs a copr client property can derive from this class
    """

    def __init__(self, client: "CoprClientMixin" = None, **kwargs):
        """
        Initializes the mixin.

        Keyword Arguments:
            client (Client): Copr client to use. If None, a client is created
        """
        self.__client = client
        super().__init__(**kwargs)

    @property
    def client(self):
        """
        Property for getting the copr client.
        Upon first call of this function, the client is instantiated.
        """
        if not self.__client:
            self.__client = self.__make_client()
        return self.__client

    def __make_client(self) -> Client:
        """
        Instatiates the copr client. Make sure to use the "client" property for
        accessing the client and creating it.

        If the environment contains COPR_URL, COPR_LOGIN, COPR_TOKEN, and
        COPR_USERNAME, we'll try to create a Copr client from those environment
        variables; otherwise, A Copr API client is created from the config file
        in ~/.config/copr. See https://copr.fedorainfracloud.org/api/ for how to
        create such a file.
        """
        client = None
        if {"COPR_URL", "COPR_LOGIN", "COPR_TOKEN",
                "COPR_USERNAME"} <= set(os.environ):
            logging.debug(
                "create copr client config from environment variables")
            config = {'copr_url': os.environ['COPR_URL'],
                      'login': os.environ['COPR_LOGIN'],
                      'token': os.environ['COPR_TOKEN'],
                      'username': os.environ['COPR_USERNAME']}
            client = Client(config)
            assert client.config == config
        else:
            logging.debug("create copr client config from file")
            client = Client.create_from_config_file()
        return client
