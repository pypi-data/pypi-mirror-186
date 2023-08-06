# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import uuid
import time

class CorrelationContext:
    def __init__(self):
        pass

    def _get_id(self) -> str:
        return None

    def __str__(self):
        return self._get_id()

    def __repr__(self):
        return self.__str__()

class BasicCorrelationContext(CorrelationContext):
    def __init__(self, id: str = None, timestamp: int = None, headers: dict = {}):
        self.id = id if id else str(uuid.uuid4())
        self.timestamp = timestamp if timestamp else int(time.time())
        self.headers = headers

    def _get_id(self) -> str:
        return self.id

    def get_id(self) -> str:
        return self._get_id()

    def get_timestamp(self) -> int:
        return self.timestamp

    def get_headers(self) -> dict:
        return self.headers

class WrapperContext(CorrelationContext):
    def __init__(self, correlation_context: CorrelationContext, success: bool, message: str):
        self._context = correlation_context
        self._success = success
        self._message = message

    def _get_id(self) -> str:
        return self._context._get_id()

    def get_id(self) -> str:
        return self._context._get_id()

    def get_timestamp(self) -> int:
        return self._context.get_timestamp()

    def get_headers(self) -> dict:
        return self._context.get_headers()

    def is_success(self) -> bool:
        return self._success

    def get_message(self) -> str:
        return self._message

def get_context() -> CorrelationContext:
    return BasicCorrelationContext()

# test purpose
def get_context_wrapper(ctxt: CorrelationContext, success: bool, message: str) -> CorrelationContext:
    return WrapperContext(ctxt, success, message)