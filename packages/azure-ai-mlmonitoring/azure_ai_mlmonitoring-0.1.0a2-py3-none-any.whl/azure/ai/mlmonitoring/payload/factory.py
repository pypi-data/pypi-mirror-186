# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import sys

try:
    import pandas as pd
except ImportError:
    pass
try:
    import numpy as np
except ImportError:
    pass

from ..logger import logger
from ..config import get_config
from .payload import JsonPayload, CompactPayload

class PayloadFactory:
    def __init__(self):
        pass
    
    def build_payload(self, designation, data, model_version=None, context=None):
        logger.debug("building payload for collection %s, data type: %s", designation, type(data).__name__)
        headers = {}
        timestamp = None
        correlationid = None
        if context is not None:
            correlationid = context.get_id()
            timestamp = context.get_timestamp()
            headers = context.get_headers()

        config = get_config()
        if config.compact_format():
            return CompactPayload(designation, data, model_version=model_version, correlationid=correlationid, timestamp=timestamp, headers=headers)
        else:
            return JsonPayload(designation, data, model_version=model_version, correlationid=correlationid, timestamp=timestamp, headers=headers)

def get_payload_factory():
    return PayloadFactory()