from typing import Dict
import redis
import json

class CacheManager:
    def __init__(self):
        self.client = redis.StrictRedis(host="localhost", port=6379, db=0)

    def get(self, key: str):
        data = self.client.get(key)
        return json.loads(data) if data else None

    def set(self, key: str, value: Dict, ttl: int = 3600):
        self.client.setex(key, ttl, json.dumps(value))
