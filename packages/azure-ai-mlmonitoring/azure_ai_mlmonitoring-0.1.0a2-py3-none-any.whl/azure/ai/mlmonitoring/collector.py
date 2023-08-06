# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from .collector_json import JsonCollector
from .context import CorrelationContext

class Collector:
    def __init__(
        self,
        *,
        name: str,
        column_names: list=None
        ):
        self._impl = JsonCollector(name=name, column_names=column_names)

    def collect(
        self,
        data, # supported type: Union[np.array, pd.DataFrame]
        correlation_context: CorrelationContext=None) -> CorrelationContext:
        return self._impl.collect(data, correlation_context)