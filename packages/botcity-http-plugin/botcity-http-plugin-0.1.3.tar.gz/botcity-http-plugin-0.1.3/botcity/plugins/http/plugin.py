from __future__ import annotations

from typing import Dict

import requests
from requests import Response


class BotHttpPlugin:
    def __init__(self, url: str, params: Dict = None) -> None:
        """
        BotHttpPlugin

        Args:
            url (str): The URL to send requests to.
            params (dict, Optional): Additional parameters to send with your requests. Defaults to None.

        Attributes:
            url (str): The URL to send requests to.
            params (dict, Optional): Additional parameters to send with your requests. Defaults to None.
        """
        self.url = url
        self.params = params
        ...

    def set_url(self, url) -> BotHttpPlugin:
        self.url = url
        return self

    def set_params(self, params: dict) -> BotHttpPlugin:  # TODO Union w/ List(str) or List(Tuple(str, str))?
        self.params = params
        return self

    def add_param(self, key: str, value: object) -> BotHttpPlugin:
        """
        Adds a parameter to the parameters dictionary.

        Args:
            key (str): Header key.
            value (object): Header value.

        Returns:
            self (allows Method Chaining)
        """
        self.params[key] = value
        return self

    def get(self) -> Response:
        """
        Sends an http get request to the URL defined in this class.

        Returns:
            The content of the server response in its raw format.
        """
        return requests.get(self.url, self.params)

    def get_as_json(self) -> Dict:  # Typing | Delete this?
        """
        Sends an http get request to the URL defined in this class, and returns the JSON formatted answer.
        This method is equivalent to get().json().

        Returns:
            The content of the server response in json format
        """
        return self.get().json()

    def get_bytes(self) -> bytes:
        """
        Sends an http get request to the URL defined in this class, and returns the answer as bytes.
        This method is equivalent to get().content

        Returns:
            The content of the server response in bytes
        """
        return self.get().content

    def get_as_file(self, file_name: str) -> str:  # Change return?
        """
        Performs an http get request, then saves its response as a file.

        Args:
            file_name (str): The name of the file.

        Returns:
            (str) The resulting file_name.
        """
        # Performs the GET request
        response = self.get()

        # Saves the file
        with open(file_name, 'wb') as file:
            file.write(response.content)

        # Returns the file name
        return file_name

    def post(self) -> Response:
        """
        Sends an http post request to the URL defined in this class.

        Returns:
            The content of the server response in its raw format.
        """
        return requests.post(self.url, self.params)

    def post_as_json(self) -> Dict:  # Delete this?
        """
        Sends an http post request to the URL defined in this class, and returns the JSON formatted answer.
        This method is equivalent to post().json().

        Returns:
            The content of the server response in json format.
        """
        return self.post().json()
