import redis
import os
import json

r = redis.Redis.from_url(os.getenv("REDIS_URL"))

def set_cache(key, value, expiry=60):
    r.set(key, json.dumps(value), ex=expiry)

def get_cache(key):
    data = r.get(key)
    if data:
        return json.loads(data)
    return None
