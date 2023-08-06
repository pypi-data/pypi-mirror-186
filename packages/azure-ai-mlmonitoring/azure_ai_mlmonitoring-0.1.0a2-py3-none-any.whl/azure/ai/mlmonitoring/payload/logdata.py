# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import time
import datetime
import uuid
import json
import io

try:
    import pandas as pd
except ImportError:
    pass
try:
    import numpy as np
except ImportError:
    pass


def get_type_fullname(o):
    klass = o.__class__
    module = klass.__module__
    if module == 'builtins':
        return "python." + klass.__qualname__ # avoid outputs like 'builtins.str'
    return module + '.' + klass.__qualname__

class LogData(dict):
    def __init__(self, data):
        self._data = data

    def type(self):
        return get_type_fullname(self._data)
    
    def to_json(self):
        pass
    
    def to_bytes(self):
        pass

class PythonListData(LogData):
    def __init__(self, data):
        super().__init__(data)

    def to_json(self):
        return json.dumps(self._data)

class NumpyArrayData(LogData):
    def __init__(self, data):
        super().__init__(data)

    def to_json(self):
        if self._data.ndim <= 1:
            # Transposing so that data is a single row not single column
            list_data = [self._data.tolist()]
        else:
            list_data = self._data.tolist()

        return json.dumps(list_data)

    def to_bytes(self):
        memfile = io.BytesIO()
        np.save(memfile, self._data)
        return memfile.getvalue()

class PandasFrameData(LogData):
    def __init__(self, data):
        super().__init__(data)

    def to_json(self):
        return self._data.to_json(orient="records")
