import logging


from collections import OrderedDict
from datetime import datetime, timedelta
from decimal import Decimal
from typing import Any

logger = logging.getLogger(__name__)


class CacheItem(object):
    def __init__(self, item: Any):
        self.item = item
        self.cache_time = datetime.now()


class OldestOutCache(OrderedDict):
    def __init__(
        self,
        ttl_seconds: Decimal = Decimal(5),
        max_size: int = 128,
    ):
        self._max_size = max_size
        self._time_to_live = timedelta(seconds=float(ttl_seconds))

        super().__init__()

    def __getitem__(self, key: Any) -> Any:
        value = super().__getitem__(key)

        if (
            value is not None and
            datetime.now() < (value.cache_time + self._time_to_live)
        ):
            return value.item

        elif value is not None:
            # Value is stale so delete it from the cache
            del self[key]

        return None

    def __setitem__(self, key: Any, value: Any) -> Any:
        if key in self:
            self.move_to_end(key)

        super().__setitem__(key, CacheItem(value))

        if len(self) > self._max_size:
            oldest = next(iter(self))

            del self[oldest]

    def get(self, key: Any) -> Any:
        try:
            return self.__getitem__(key)
        except KeyError:
            return None
