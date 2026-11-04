from cachetools import TTLCache

class CacheService:
    def __init__(self):
        # 最多存 100 个问题，每个答案 1 小时后过期
        self.cache = TTLCache(maxsize=100, ttl=3600)

    def get(self, key: str):
        return self.cache.get(key)

    def set(self, key: str, value: str):
        self.cache[key] = value

# 实例化一个全局缓存对象
cache_service = CacheService()