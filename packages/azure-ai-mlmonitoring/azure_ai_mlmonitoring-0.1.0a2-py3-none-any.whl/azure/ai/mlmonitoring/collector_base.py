# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import sys
import logging

from .init import init, is_sdk_ready
from .config import get_config
from .context import CorrelationContext, get_context_wrapper

class CollectorBase:
    def __init__(
        self,
        model_version: str):
        if not is_sdk_ready():
            init(model_version)

        self.logger = logging.getLogger("mdc.collector")
        self.config = get_config()

    def _response(
        self,
        ctxt: CorrelationContext,
        success: bool,
        message: str) -> CorrelationContext:
        if self.config.is_debug():
            return get_context_wrapper(ctxt, success, message)
        else:
            if not success:
                self.logger.error("collect data failed: %s", message)
            return ctxt
