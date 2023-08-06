# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import time
import uuid

from .logdata import LogData
from ..common import __version__

class Payload:
    def __init__(self, designation, data, model_version, timestamp, correlationid, headers):
        self._id = str(uuid.uuid4())
        self._designation = designation
        self._model_version = model_version
        self._agent = "azure-ai-mlmonitoring/"+__version__
        self._contenttype = ""

        if not isinstance(data, LogData):
            raise TypeError("argument data (%s) must be one of LogData types." % type(data).__name__)

        self._data = data
        self._correlationid = correlationid
        if timestamp is not None:
            self._time = timestamp
        else:
            self._time = int(time.time())
        self._headers = headers

    def time(self):
        return self._time

    def id(self):
        return self._id

    def designation(self):
        return self._designation
    
    def model_version(self):
        return self._model_version

    def agent(self):
        return self._agent

    def correlationid(self):
        return self._correlationid

    def headers(self):
        return self._headers

    def type(self):
        return self._data.type()

    def contenttype(self):
        return self._contenttype

    def content(self):
        pass


class JsonPayload(Payload):
    def __init__(self, designation, data, model_version=None, timestamp=None, correlationid=None, headers={}):
        super().__init__(designation, data, model_version, timestamp, correlationid, headers)
        self._contenttype = "application/json"

    def content(self):
        return self._data.to_json()


class CompactPayload(Payload):
    def __init__(self, designation, data, model_version=None, timestamp=None, correlationid=None, headers={}):
        super().__init__(designation, data, model_version, timestamp, correlationid, headers)
        self._contenttype = "application/octet-stream"

    def content(self):
        return self._data.to_bytes()