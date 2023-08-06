# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import logging
import requests
import json
import os

class MdcSender:
    def __init__(self, host, port):
        self.logger = logging.getLogger("mdc.sender")
        self.host = host
        self.port = port
        self.path = "/modeldata/log"
    
    def send(self, payload):
        designation = payload.designation()
        self.logger.debug("sending payload to mdc: %s@%s", designation, payload.id())

        event_type = "azureml.inference.%s" % designation
        headers = {
            "Accept": "*/*",
            "Content-Type": payload.contenttype(),
            # MDC use trace id to track the id for request/payload
            #"x-request-id": payload.id(),
            "trace-id": payload.id(),
            # event attributes
            "ce-time": str(payload.time()),
            "ce-type": event_type,
            # collected data type, eg: 'numpy.ndarray','python.list','pandas.core.frame.DataFrame'
            "ce-collect-data-type": payload.type(),
            "ce-agent": payload.agent(),
        }
        correlation_id = payload.correlationid()
        if correlation_id is not None:
            headers["ce-x-request-id"] = correlation_id
        model_version = payload.model_version()
        if model_version is not None:
            headers["ce-model-version"] = model_version

        merged_headers = {}
        # add prefix "ce-" on each header from payload
        for key, value in payload.headers().items():
            merged_headers["ce-%s" % key] = str(value)
        # overwrite during merge if has duplicate headers
        for key in headers:
            merged_headers[key] = headers[key]

        content = payload.content()
        if payload.contenttype() == "application/json":
            return self._send_json(merged_headers, content)
        else:
            return self._send_binary(merged_headers, content)
    
    def _send_json(self, headers, json_data):
        if not isinstance(json_data, str):
            raise TypeError("json_data: str type expected")

        try:
            status, msg = self._post_request(self._build_url(), json_data, headers)
            if not self._is_success(status):
                self.logger.error("failed to send json payload: %d, %s", status, msg)
                return False, "%d: %s" % (status, msg)
            else:
                return True, "%d: %s" % (status, msg)
        except Exception as ex:
            self.logger.error("mdc request raise exception: {0}".format(ex))
            return False, str(ex)

    def _send_binary(self, headers, binary_data):
        if not isinstance(binary_data, bytes):
            raise TypeError("binary_data: bytes type expected, actual - %s" % type(binary_data).__name__)
        
        size = len(binary_data)
        # TODO: split payload if it is large?
        try:
            status, msg = self._post_request(self._build_url(), binary_data, headers)
            if not self._is_success(status):
                self.logger.error("failed to send binary payload: %d, %s", status, msg)
                return False, "%d: %s" % (status, msg)
            else:
                return True, "%d: %s" % (status, msg)
        except Exception as ex:
            self.logger.error("mdc request raise exception: {0}".format(ex))
            return False, str(ex)

    def _build_url(self):
        return "http://%s:%d%s" % (self.host, self.port, self.path)

    def _post_request(self, url, payload, headers=None):
        self.logger.debug("posting request to %s", url)
        self.logger.debug("request headers: %s", headers)
        self.logger.debug("request payload(%s): %s", type(payload), payload)
        
        r = requests.post(url, data = payload, headers=headers)
        self.logger.debug("response: %d, %s", r.status_code, r.text)
        return (r.status_code, r.text)

    def _is_success(self, status_code):
        return status_code >= 200 and status_code < 300