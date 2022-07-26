import time
import redis

class CacheControl:
    def __init__(self) -> None:
        self.redis = redis.Redis(
            host = 'localhost',
            port = 6379)
    
    def set_cache_value(self, key, index) -> None:
        st = time.time()
        self.redis.set(key, 'Test redis cluster {0}'.format(index))
        et = time.time()
        etl = et - st
        print('Set cache execution time', etl, 'seconds')
        
    def get_from_cache(self, key):
        st = time.time()
        et = time.time()
        key_value = self.redis.get(key)
        etl = et - st
        print('Get from cache execution time', etl, 'seconds')
        return key_value
