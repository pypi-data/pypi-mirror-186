# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import logging
import json

class PayloadPrinter:
    def __init__(self):
        pass
    
    def send(self, payload):
        payload_json = json.dumps(payload.__dict__)
        logging.debug("payload json: %s", payload_json)
        return True, "done"