#!/usr/bin/python3
# -*- coding: utf-8 -*-
##
## @author Edouard DUPIN
##
## @copyright 2023, Edouard DUPIN, all right reserved
##
## @license MPL v2.0 (see license file)
##
import enum
import requests
import json
from typing import Dict, Optional
from pathlib import Path


class KaranageConnection:
    def __init__(self,
                 url: Optional[str] = None,
                 group: Optional[str] = None,
                 token: Optional[str] = None,
                 config_file: Optional[str] = None,
                 default_values: Optional[str] = None) -> None:
        """ Initialize the communication class.
        :param url: URL of the karanage API server.
        :param group: Group of the message (token need to have the autorotation to published on it).
        :param token: Token to validate the access on the application.
        :param config_file: path to the configuration file if overload.
        :param default_values: Default configurations.
        """
        self.url = "http://localhost:20080/karanage/api"
        self.group = "test"
        self.token = None
        # load user default value:
        if default_values is not None:
            if "url" in default_values:
                self.url = default_values["url"]
            if "group" in default_values:
                self.group = default_values["group"]
            if "token" in default_values:
                self.token = default_values["token"]
        # keep correct config file:
        if config_file is None:   
            config_file = "/etc/karanage/connection.json"
        # check if the config exist:
        if Path(config_file).exists():
            f = open(config_file, "r")
            configuration = json.loads(f.read())
            f.close()
        else:
            configuration = {}
        # Update data with config file:
        if "url" in configuration:
            self.url = configuration["url"]
        if "group" in configuration:
            self.group = configuration["group"]
        if "token" in configuration:
            self.token = configuration["token"]
        # set user command - line configuration:
        if url is not None:
            self.url = url
        if group is not None:
            self.group = group
        if token is not None:
            self.token = token

    def get_url(self, service: str):
        return f"{self.url}/{service}/{self.group}"

    def get_header(self):
        header = {}
        if self.token is not None and len(self.token) >15:
            header['Authorization'] = f"zota {self.token}"
        return header