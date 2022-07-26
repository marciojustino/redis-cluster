import time
from CacheControl import CacheControl

cache_control = CacheControl()
index = 1
srt = time.time()
for i in range(100000):
    try:
        cache_control.set_cache_value('my_key_{index}', index)
        value = cache_control.get_from_cache('my_key_{index}')
        # print(value)
    except ConnectionError as err:
        print('Can\'t connect to redis. Seems redis is offline')
    except Exception as err:
        print('An exception occurred when trying to connect to redis | Error={0}'.format(err))
    finally:
        index += 1

ert = time.time()
evaluated_time = ert-srt
print('Evaluated time', evaluated_time, 'seconds')
