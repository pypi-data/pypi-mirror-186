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
from datetime import datetime, timezone
from typing import Dict, Optional, List
from .connection import KaranageConnection
from .exception import KaranageException

class GroupLogElement:
    def __init__(self, id: int, data: str, time: datetime = None):
        self.id = id
        self.time = time
        self.data = data

## Generic karanage sending system.
class KaranageLog:
    def __init__(self, connection: KaranageConnection, system: Optional[str] = None) -> None:
        """Initialize the communication class.
        :param connection: Connection interface.
        """
        self.connection = connection
        self.system = system
        self.service = "log"

    def get_url(self):
        if self.system is None:
            return self.connection.get_url(self.service)
        return f"{self.connection.get_url(self.service)}/{self.system}"

    def send(self, data: Dict, id: Optional[int] = None, uuid_group: Optional[int] = None, time: Optional[datetime] = None) -> None:
        """Send a message to the server.
        :param data: Data to send to the server
        :param id: Local internal ID
        :param uuid_group: local internal group UUID
        :param time_log: Receive time of the log
        """
        param = {}
        if id is not None:
            param["id"] = id
        if uuid_group is not None:
            param["uuid"] = uuid_group
        if time is not None:
            param["time"] = time.astimezone(timezone.utc).isoformat()
        header = self.connection.get_header()
        try:
            ret = requests.post(self.get_url(), json=data, headers=header, params=param)
        except requests.exceptions.ConnectionError as ex:
            raise KaranageException(f"Fail connect server: {self.get_url()}", 0, str(ex))
        if not 200 <= ret.status_code <= 299:
            raise KaranageException(f"Fail send message: {self.get_url()}", ret.status_code, ret.content.decode("utf-8"))

    def send_multiple(self, data_input: List[GroupLogElement], uuid_group: Optional[int]= None) -> None:
        """Send multiple log message to the server.
        :param data: Data to send to the server
        :param uuid_group: local internal group UUID
        """
        # Convert:
        data = []
        for elem in data_input:
            data.append({
                "id": elem.id,
                "time": elem.time.astimezone(timezone.utc).isoformat(),
                "data": elem.data,
            })

        param = {}
        if uuid_group is not None:
            param["uuid"] = uuid_group
        header = self.connection.get_header()
        try:
            ret = requests.post(f"{self.get_url()}/push_multiple", json=data, headers=header, params=param)
        except requests.exceptions.ConnectionError as ex:
            raise KaranageException(f"Fail connect server: {self.get_url()}", 0, str(ex))
        if not 200 <= ret.status_code <= 299:
            raise KaranageException(f"Fail send message: {self.get_url()}", ret.status_code, ret.content.decode("utf-8"))

