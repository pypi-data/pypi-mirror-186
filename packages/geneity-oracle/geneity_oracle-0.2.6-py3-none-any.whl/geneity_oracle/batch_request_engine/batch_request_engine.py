from __future__ import annotations

import asyncio
import sys
import logging
from decimal import Decimal
from dataclasses import dataclass
from collections import defaultdict
from typing import cast, List, Set, Dict, Tuple, Optional, Union
from asyncio import (
    Future,
    Queue,
    create_task,
    sleep,
    Task,
)

from geneity_oracle.interface.ora_base import DatabaseInterface
from geneity_oracle.query.results import (
    DBResultsRow,
    DBResultsSQLQuery,
)

from .oldest_out_cache import OldestOutCache

logger = logging.getLogger(__name__)


RequestIdentityType = Union[int, str, tuple]


@dataclass
class DatabaseInfo(object):
    pass


class BatchRequestError(Exception):
    pass


class BatchRequestEngine(object):
    BATCH_REQUEST_ENGINE_INSTANCE = None

    def __init__(
        self,
        odb: DatabaseInterface,
        max_batch_size: int,
        batch_period_seconds: float,
        max_cache_size: int,
        cache_ttl_seconds: Decimal = Decimal(0),
    ):
        self._batch_reqs: Queue = Queue(max_batch_size)
        self._batch_res: Dict = defaultdict(lambda: defaultdict(Future))

        self.odb = odb

        self._entity_cache: Dict = defaultdict(dict)

        self._batch_period_seconds = batch_period_seconds

        self._max_cache_size = max_cache_size
        self._cache_ttl_seconds = cache_ttl_seconds

    def start(self) -> Task:
        return create_task(self._run())

    async def _run(self) -> None:
        while True:
            await self._batch_get_request_info()
            await sleep(self._batch_period_seconds)

    @classmethod
    def get_instance(cls) -> BatchRequestEngine:
        if cls.BATCH_REQUEST_ENGINE_INSTANCE is None:
            raise BatchRequestError('No batch request engine instance set')

        return cls.BATCH_REQUEST_ENGINE_INSTANCE

    @classmethod
    def set_instance(
        cls,
        odb: DatabaseInterface,
        max_batch_size: int,
        batch_process_period: float,
        max_cache_size: int,
        cache_ttl_seconds: Decimal = Decimal(0),
    ) -> BatchRequestEngine:
        cls.BATCH_REQUEST_ENGINE_INSTANCE = cls(
            odb,
            max_batch_size,
            batch_process_period,
            max_cache_size,
            cache_ttl_seconds,
        )
        return cls.BATCH_REQUEST_ENGINE_INSTANCE

    def _cache_get(self, entity: BatchRequestBase) -> Optional[BatchRequestBase]:
        cache = self._entity_cache.get(type(entity))

        if cache is not None:
            return cast(BatchRequestBase, cache.get(entity.identity))

        return None

    def _cache_item(
        self,
        request_entity: BatchRequestBase,
        cache_item: DBResultsRow,
        cache_ttl_seconds: Decimal,
    ) -> None:
        if type(request_entity) not in self._entity_cache:
            self._entity_cache[type(request_entity)] = OldestOutCache(
                ttl_seconds=cache_ttl_seconds,
                max_size=self._max_cache_size,
            )

        self._entity_cache[type(request_entity)][request_entity.identity] = cache_item

    async def process_request(self, request_entity: BatchRequestBase, cache_ttl_seconds: Decimal = None) -> List[DatabaseInfo]:
        result = None

        if cache_ttl_seconds is None:  # If no value is passed, use the value default value
            cache_ttl_seconds = self._cache_ttl_seconds

        if cache_ttl_seconds > 0:
            result = self._cache_get(request_entity)

        if result is None:
            logger.debug(
                'Adding request to batch queue.',
                extra={'data': {
                    'type': str(type(request_entity)),
                    'identity': request_entity.identity,
                }},
            )

            try:
                reqs_fut = self._batch_reqs.put(request_entity)
                result_fut = self._batch_res[type(request_entity)][request_entity.identity]
                _, result = await asyncio.gather(reqs_fut, result_fut)
            except Exception:
                logger.error(
                    "Error while processing batch engine request",
                    exc_info=True,
                )
                raise

            if cache_ttl_seconds > 0:
                self._cache_item(request_entity, result, cache_ttl_seconds)

        return request_entity.create_response(result)

    async def _batch_get_request_info(self) -> None:
        """
        All the requests are batched and executed
        periodically by this coroutine.
        """
        reqs = defaultdict(set)

        # empty the queue
        while not self._batch_reqs.empty():
            entity = self._batch_reqs.get_nowait()

            reqs[type(entity)].add(entity)

        # entity_type will be BatchRequestBase or a class inherited from it
        for entity_type, entity_reqs in reqs.items():
            try:
                batch_result = await entity_type.get_batch_request_info(
                    self.odb,
                    entity_reqs,
                )

            except AttributeError:
                # re-raise the error in the caller
                exc_info = sys.exc_info()
                batch_result = {
                    req: exc_info for req in entity_reqs
                }

            for request_entity, res in batch_result.items():
                future = self._batch_res[entity_type][request_entity.identity]

                if future.done():
                    del self._batch_res[entity_type][request_entity.identity]
                    continue

                # check if it contains exc_info
                if isinstance(res, tuple):
                    future.set_exception(
                        BatchRequestError(f'DBError: {res}')
                    )
                else:
                    future.set_result(res)

                del self._batch_res[entity_type][request_entity.identity]

            # Set an exception for any entities that were not found
            for entity in entity_reqs:
                if entity.identity in self._batch_res[entity_type]:
                    future = self._batch_res[entity_type][entity.identity]
                    if not future.done():
                        future.set_exception(BatchRequestError(
                            f'No result found for {entity_type.request_tag} with '
                            f'{entity_type.request_id}={entity.identity}'
                        ))
                        del self._batch_res[entity_type][entity.identity]


class BatchRequestBase(object):
    request_tag = 'BASE_REQUEST'
    request_id = 'ID'

    def __init__(self, identity: RequestIdentityType):
        self.identity = identity

        self.result = None

    @classmethod
    async def get_batch_request_info(
        cls,
        odb: DatabaseInterface,
        batch_requests: Set[BatchRequestBase],
    ) -> Dict[BatchRequestBase, DBResultsRow | Tuple]:
        query_ids = [req.identity for req in batch_requests]

        try:
            rs = await cls.get_info_from_db(odb, query_ids)

            batch_result = cls.match_query_result_to_request(rs, batch_requests)
        except Exception:  # pylint: disable=broad-except
            # re-raise the error in the caller
            exc_info = sys.exc_info()
            batch_result = {req: exc_info for req in batch_requests}

        return batch_result

    @staticmethod
    async def get_info_from_db(
        odb: DatabaseInterface,
        query_ids: List[RequestIdentityType]
    ) -> DBResultsSQLQuery:
        raise NotImplementedError()

    @classmethod
    def match_query_result_to_request(
        cls,
        query_rs: DBResultsSQLQuery,
        entities: Set[BatchRequestBase],
    ) -> Dict[BatchRequestBase, DBResultsRow]:
        raise NotImplementedError()

    @classmethod
    def create_response(cls, rs: DBResultsRow) -> List[DatabaseInfo]:
        raise NotImplementedError()
