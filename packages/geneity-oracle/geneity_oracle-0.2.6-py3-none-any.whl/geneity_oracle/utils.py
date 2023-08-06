from __future__ import annotations

import asyncio
import logging
from concurrent.futures import Executor
from contextvars import copy_context
from functools import partial
from time import time
from typing import Callable, Optional, TypeVar

logger = logging.getLogger(__name__)


class Timer(object):

    def __init__(self, tag: Optional[str] = None):
        self.tag = tag
        self.start_time: Optional[float] = None
        self.time_taken: Optional[float] = None
        self.in_progress: bool = False
        self.exception_occurred: bool = False

    def start(self):
        if not self.in_progress:
            self.start_time = time()
            self.in_progress = True
        else:
            logger.warning("Already started timer", extra={"data": {"tag": self.tag}})

    def stop(self):
        if self.in_progress:
            self.time_taken = time() - self.start_time
            self.in_progress = False
        else:
            logger.warning("Never started timer", extra={"data": {"tag": self.tag}})

    def __enter__(self) -> Timer:
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.stop()
        if exc_type is not None:
            self.exception_occurred = True


R = TypeVar('R')


async def run_in_executor_with_context(
    loop: asyncio.AbstractEventLoop,
    executor: Executor,
    func: Callable[..., R],
) -> R:
    context = copy_context()
    results = await loop.run_in_executor(
        executor,
        partial(context.run, func),
    )
    return results
