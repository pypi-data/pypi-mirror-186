from contextlib import asynccontextmanager
from typing import AsyncIterator

import aioredis  # type: ignore

from ponty import Provider
from ponty.registry import Registry


_registry = Registry[aioredis.ConnectionsPool]()


def redis_provider(*, host: str, port: str = "6379") -> Provider:

    async def provider(_) -> AsyncIterator[None]:
        pool = await aioredis.create_redis_pool((host, port))
        _registry.add("redis", pool)

        try:
            yield
        finally:
            pool.close()
            await pool.wait_closed()

    return provider


@asynccontextmanager
async def lease_redis_conn() -> AsyncIterator[aioredis.RedisConnection]:
    pool = _registry.get("redis")
    with (await pool) as conn:
        yield conn
