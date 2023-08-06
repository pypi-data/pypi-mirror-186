"""
Notification Helper

For each user (id is wallet) and _type, system push notifications to the user.
Once this user reads his notification, the notification will be gone from system. The notification can be read only once.
The notificaiton has a default TTL to 1 hour.

"""

from typing import Dict, Any, List
import redis.asyncio as redis
from time import time, sleep

from bdating_common.api_common import settings
redis_client = redis.Redis(
    host=settings.redis_host,
    port=settings.redis_port,
    db=settings.in_app_notif_cache_id,
    password=settings.redis_password
)


async def push(wallet: str, _type: str, message: str, timestamp: Any = None, ttl: int = 3600):
    """TTL in milli-seconds
    """
    if timestamp is None:
        timestamp = int(time())
    await redis_client.setex(
        f"{wallet}:{_type}:{timestamp}", ttl, message
    )


async def pop(wallet: str, _type: str, delete: bool = True) -> List[Dict[str, str]]:
    """Return notification for this user, ordered by timestamp
    If not exist, return empty list.

    when _type is set to None, it will get all notifications for a wallet.
    """
    search_key = f"{wallet}:"
    if _type is not None:
        search_key = f"{search_key}{_type}:"

    keys = (await redis_client.scan(
        cursor=0, match=f"{search_key}*"
    ))[-1]
    if not keys:
        return []
    else:
        result = []
        keys.sort()

        for obj_key in keys:

            if delete:
                r = await redis_client.getdel(obj_key)
            else:
                r = await redis_client.get(obj_key)
            if r is not None:  # concurreny protection
                result.append(r.decode('utf8'))

        return [r for r in result if r is not None]


async def _local_test():
    await push('3', 'consumer', "hello222", 222, 12)
    await push('3', 'provider', "hello221", 221, 12)
    await push('3', 'consumer', "hello231", 231, 12)
    await push('3', 'provider', "hello232", 232, 12)
    sleep(2)
    assert ['hello222', 'hello231'] == (await pop('3', 'consumer', delete=False))
    assert ['hello221', 'hello232'] == (await pop('3', 'provider', delete=False))
    # order by type first.
    assert ['hello222', 'hello231', 'hello221', 'hello232'] == (await pop('3', None, delete=False))
    assert ['hello222', 'hello231'] == (await pop('3', 'consumer', delete=True))
    assert ['hello221', 'hello232'] == (await pop('3', None, delete=False))

    await push('3', 'consumer', "hello222", 222, 12)
    await push('3', 'provider', "hello221", 221, 12)
    await push('3', 'consumer', "hello231", 231, 12)
    await push('3', 'provider', "hello232", 232, 12)
    assert ['hello222', 'hello231'] == (await pop('3', 'consumer'))
    assert ['hello221', 'hello232'] == (await pop('3', 'provider'))

    assert [] == (await pop('3', 'consumer'))
    assert [] == (await pop('3', 'provider'))
    assert [] == (await pop('3', None))

    await push('3', 'consumer', "hello222", 222, 12)
    sleep(20)
    assert [] == (await pop('3', None))

if __name__ == "__main__":
    import asyncio
    asyncio.run(_local_test())
