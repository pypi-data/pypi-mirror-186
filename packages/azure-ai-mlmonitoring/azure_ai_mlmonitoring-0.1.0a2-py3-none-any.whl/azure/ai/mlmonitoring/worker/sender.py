# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import logging
from .mdcsender import MdcSender
from .printer import PayloadPrinter

def create_sender(config):
    if config.use_printer():
        return PayloadPrinter()

    return MdcSender(config.host(), config.port())
