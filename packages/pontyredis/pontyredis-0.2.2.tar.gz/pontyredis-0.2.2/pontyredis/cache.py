import functools
import json
import typing

from ponty.memo import CacheStore, cache, cachemiss, Stampede

from pontyredis.lock import redislock
from pontyredis.provider import lease_redis_conn


T = typing.TypeVar("T")


class _RedisStore(CacheStore[T]):

    def __init__(self, scope: str, ttl_ms: int):
        super().__init__()
        self._scope: typing.Final[str] = scope

        if ttl_ms <= 0:
            raise ValueError("ttl must be positive")
        self._ttl_ms: typing.Final[int] = ttl_ms

    def _scoped_key(self, key: str) -> str:
        return f"cacheitem|{self._scope}|{key}"

    async def get(self, key: str) -> typing.Union[T, type[cachemiss]]:
        key = self._scoped_key(key)
        async with lease_redis_conn() as conn:
            if serialized := await conn.get(key):
                return json.loads(serialized)
        return cachemiss

    async def set(self, key: str, data: T) -> None:
        key = self._scoped_key(key)
        serialized = json.dumps(data)

        async with lease_redis_conn() as conn:
            if self._ttl_ms:
                await conn.psetex(key, self._ttl_ms, serialized)
            else:
                await conn.set(key, serialized)

    async def remove(self, key: str) -> bool:
        async with lease_redis_conn() as conn:
            return await conn.delete( self._scoped_key(key) )


def rediscache(
    *,
    scope: str,
    ttl_ms: int,
    maxwait_ms: int = 1000,
    pulse_ms: int = 50,
    name: str = "",
):
    """Redis-backed memoizer with antistampede.

    NB: Unlike "localcache", does NOT take a <maxsize> parameter. Redis's key
    eviction behavior can be controlled with the "maxmemory" and
    "maxmemory-policy" configuration directives.

    scope: prefix to avoid keyspace collisions
    ttl_ms: millis to expiry. Must be positive
    maxwait_ms: millis to wait for a lock to resolve.
                Throws "Stampede" error when (n * pulse) > maxwait
    pulse_ms: antistampede recheck frequency
    name: providing a name registers the cache, so it can be used by 'invalidate'

    """
    antistampede = redislock(
        scope=scope,
        maxwait_ms=maxwait_ms,
        pulse_ms=pulse_ms,
        timeout_error=Stampede,
    )

    return cache(
        store=_RedisStore(scope, ttl_ms),
        antistampede=antistampede,
        name=name,
    )
