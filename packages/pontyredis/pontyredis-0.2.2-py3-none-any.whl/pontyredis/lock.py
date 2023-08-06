import typing

from ponty.memo import SentinelStore, Lock

from pontyredis.provider import lease_redis_conn


class _RedisSentinelStore(SentinelStore):

    def __init__(self, scope: str, ttl_ms: int):
        super().__init__()
        self._scope: typing.Final[str] = scope

        if ttl_ms <= 0:
            raise ValueError("ttl must be positive")
        self._ttl_ms: typing.Final[int] = ttl_ms

    def _scoped_key(self, key: str) -> str:
        return f"lock|{self._scope}|{key}"

    async def exists(self, key: str) -> bool:
        async with lease_redis_conn() as conn:
            return await conn.exists( self._scoped_key(key) )

    async def add(self, key: str) -> None:
        async with lease_redis_conn() as conn:
            await conn.psetex(self._scoped_key(key), self._ttl_ms, 1)

    async def remove(self, key: str) -> None:
        async with lease_redis_conn() as conn:
            await conn.delete( self._scoped_key(key) )


def redislock(
    *,
    scope: str,
    ttl_ms: int = 1000,
    **kw
) -> Lock:
    """Shared lease. Use to enforce access limits on a resource across processes.

    Best-suited for efficiency purposes, i.e. helping to avoid doing the same
    work twice. The difficulties and limitations of distributed locks are
    well-documented, and this is a rather naive approach; if correctness is
    at a premium (i.e. concurrently doing the same work breaks the state of
    your system), you should choose something more robust.

    scope: prefix to avoid collisions
    ttl_ms: reduce deadlocks by auto-expiring the lock after <ttl> millis

    """
    return Lock(sentinels=_RedisSentinelStore(scope, ttl_ms), **kw)
