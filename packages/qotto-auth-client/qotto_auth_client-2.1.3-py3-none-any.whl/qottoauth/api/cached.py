from datetime import datetime, timezone, timedelta
from threading import Lock
from typing import Any, Tuple, Optional

from qottoauth.api.base import QottoAuthApi

__all__ = [
    'QottoAuthCachedApi',
]


class QueryInput:
    def __init__(
            self,
            name: str,
            variables: list[Tuple[str, str, Any]] = None, body: str = None,
    ):
        self.key = '||'.join((name, str(variables), str(body)))
        self.date = datetime.now(timezone.utc)
        self.result: Any = None


class QottoAuthCachedApi(QottoAuthApi):

    def __init__(
            self,
            qotto_auth_api: QottoAuthApi,
            cache_local_seconds: int = 60,
            cache_max_size: int = 100,
            cache_max_seconds: int = 3600,
    ):
        self._qotto_auth_api = qotto_auth_api

        self._cache_lock = Lock()
        self._cache: dict[str, QueryInput] = dict()

        self._cache_local_seconds = cache_local_seconds
        self._cache_max_size = cache_max_size
        self._cache_max_seconds = cache_max_seconds

        self._last_clean_cache = datetime.now(timezone.utc)

        self._cache_auth_metadata: Optional[dict] = None
        self._last_auth_metadata = datetime.now(timezone.utc)

    def _should_clean_cache(self, date: datetime) -> bool:
        with self._cache_lock:
            return self._last_clean_cache < date - timedelta(seconds=self._cache_local_seconds)

    def _clean_cache(self, since: datetime) -> None:
        with self._cache_lock:
            self._last_clean_cache = datetime.now(timezone.utc)
            for cached_input in list(self._cache.values()):
                if cached_input.date < since:
                    del self._cache[cached_input.key]

    def _get_cached(self, query_input: QueryInput) -> Any:
        with self._cache_lock:
            cached = self._cache.get(query_input.key)
            return cached.result if cached is not None else None

    def _set_cached(self, query_input: QueryInput, result: dict[str, Any]) -> None:
        with self._cache_lock:
            query_input.result = result
            self._cache[query_input.key] = query_input
            if len(self._cache) > self._cache_max_size:
                self._cache.pop(next(iter(self._cache)))

    def query(
            self,
            name: str,
            variables: list[Tuple[str, str, Any]] = None,
            body: str = None,
    ):
        # No cache for these queries
        if name in ('lastChangeDate'):
            return self._qotto_auth_api.query(name, variables, body)
        # The input
        input = QueryInput(name, variables, body)
        # Check if we need to update the cache
        if self._should_clean_cache(date=input.date):
            last_change_date = max(
                datetime.fromisoformat(self._qotto_auth_api.query('lastChangeDate')),
                input.date - timedelta(seconds=self._cache_max_seconds),
            )
            self._clean_cache(since=last_change_date)
        # Check if we have a cached result
        cached_result = self._get_cached(input)
        if cached_result is not None:
            return cached_result
        # Get the result from the API
        computed_result = self._qotto_auth_api.query(name=name, variables=variables, body=body)
        # Set the result in the cache
        self._set_cached(input, computed_result)
        # Return the result
        return computed_result

    def mutation(
            self, name: str, body: str,
            input_name: str = 'input', input_type: str = None, input_value: dict[str, Any] = None
    ):
        self._clean_cache(datetime.now(timezone.utc))
        return self._qotto_auth_api.mutation(name, body, input_name, input_type, input_value)

    def auth_metadata(self) -> dict[str, str]:
        if self._cache_auth_metadata is None or self._last_auth_metadata < datetime.now(timezone.utc) - timedelta(
                seconds=self._cache_local_seconds
        ):
            self._cache_auth_metadata = self._qotto_auth_api.auth_metadata()
        return self._cache_auth_metadata
