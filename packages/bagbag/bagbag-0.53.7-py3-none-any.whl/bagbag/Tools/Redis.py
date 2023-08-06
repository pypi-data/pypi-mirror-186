from __future__ import annotations

import redis 
import pickle
import typing
import time

try:
    from .. import Funcs
    from .. import Lg
except:
    import sys
    sys.path.append("..")
    import Funcs
    import Lg

class RedisException(Exception):
    pass 

class RedisQueueClosed(RedisException):
    pass 

def RetryOnNetworkError(func): # func是被包装的函数
    def ware(self, *args, **kwargs): # self是类的实例
        while True:
            try:
                res = func(self, *args, **kwargs)
                break
            except Exception as e:
                Lg.Trace(str(e))
                if True in map(lambda x: x in str(e), [
                    'Connection closed by server', 
                    'Error 61 connecting to ', 
                    'Connection refused',
                    'timed out'
                ]):
                    time.sleep(3)
                else:
                    raise e

        return res
    
    return ware

class redisQueue():
    def __init__(self, rdb:redis.Redis, name:str, length:int=0):
        self.rdb = rdb
        self.basename = 'rq'
        self.name = name
        self.key = '%s:%s' % (self.basename, self.name)
        self.closed = False
        self.length = length

    @RetryOnNetworkError
    def Size(self) -> int:
        """Return the approximate size of the queue."""
        return self.rdb.llen(self.key)

    @RetryOnNetworkError
    def Put(self, item:typing.Any, force:bool=False):
        """Put item into the queue."""
        if force == False:
            while self.length > 0 and self.Size() >= self.length:
                time.sleep(0.3)

        self.rdb.rpush(self.key, pickle.dumps(item, protocol=2))

    @RetryOnNetworkError
    def Get(self, block=True, timeout=None) -> typing.Any:
        """Remove and return an item from the queue. 

        If optional args block is true and timeout is None (the default), block
        if necessary until an item is available."""
        if block:
            item = self.rdb.blpop(self.key, timeout=timeout)
        else:
            item = self.rdb.lpop(self.key)

        if item:
            item = item[1]

        return pickle.loads(item)
    
    def Close(self):
        self.closed = True

    def __iter__(self):
        return self 
    
    def __next__(self):
        try:
            return self.Get()
        except RedisQueueClosed:
            raise StopIteration

class redisQueueConfirm():
    def __init__(self, rdb:redis.Redis, name:str, length:int=0, timeout:int=300):
        self.rdb = rdb
        self.basename = 'rq'
        self.name = name 
        self.key = '%s:%s' % (self.basename, self.name)
        self.closed = False
        self.length = length
        self.timeout = timeout
        self.collectorLock = self.rdb.lock("redis_lock:redisQueueConfirmCollectorLock")

        self.rdb.config_set("notify-keyspace-events", "KEA")
        self.RunExpireCollector()
    
    @RetryOnNetworkError
    def RunExpireCollector(self):
        def event_handler(msg):
            self.collectorLock.acquire()
            try:
                key = str(msg["data"].decode("utf-8"))
                if key.startswith(self.key + ":doing:shadow:"):
                    tid = key.replace(self.key + ":doing:shadow:", "")

                    if self.rdb.exists(self.key + ":doing:" + tid) == True:
                        # Lg.Trace("重新发布任务:", msg["data"])
                        value = self.rdb.get(self.key + ":doing:" + tid)
                        self.rdb.rpush(self.key, value)

                        self.rdb.delete(self.key + ":doing:" + tid)
            except Exception as exp:
                pass
            self.collectorLock.release()

        pubsub = self.rdb.pubsub()
        pubsub.psubscribe(**{"__keyevent@0__:expired": event_handler})
        pubsub.run_in_thread(sleep_time=1, daemon=True)

    @RetryOnNetworkError
    def Size(self) -> int:
        """Return the approximate size of the queue."""
        return self.rdb.llen(self.key)

    @RetryOnNetworkError
    def Put(self, item:typing.Any, block:bool=True, force:bool=False) -> bool:
        """Put item into the queue."""
        if force == False:
            if block:
                while self.length > 0 and self.Size() >= self.length:
                    time.sleep(0.3)
            else:
                if self.length > 0 and self.Size() >= self.length:
                    return False

        self.rdb.rpush(self.key, pickle.dumps(item, protocol=2))
        return True

    @RetryOnNetworkError
    def Get(self, block:bool=True, timeout:int=None) -> typing.Tuple[str, typing.Any]:
        """Remove and return an item from the queue. 

        If optional args block is true and timeout is None (the default), block
        if necessary until an item is available."""
        if block:
            item = self.rdb.blpop(self.key, timeout=timeout)
            if item != None:
                item = item[1]
        else:
            item = self.rdb.lpop(self.key)

        # Lg.Trace(item)
        if item != None:
            tid = Funcs.UUID()

            self.rdb.set(self.key + ":doing:" + tid, item)
            self.rdb.set(self.key + ":doing:shadow:" + tid, "", ex=self.timeout)

            return tid, pickle.loads(item)
        else:
            return None, None
    
    @RetryOnNetworkError
    def Done(self, tid:str):
        self.rdb.delete(self.key + ":doing:" + tid)
        self.rdb.delete(self.key + ":doing:shadow:" + tid)
    
    def Close(self):
        self.closed = True

    def __iter__(self):
        return self 
    
    def __next__(self):
        try:
            return self.Get()
        except RedisQueueClosed:
            raise StopIteration

class RedisLock():
    def __init__(self, lock):
        self.lock = lock

    @RetryOnNetworkError
    def Acquire(self):
        """
        The function Acquire() is a method of the class Lock. It acquires the lock
        """
        self.lock.acquire()
    
    @RetryOnNetworkError
    def Release(self):
        """
        The function releases the lock
        """
        self.lock.release()

class Redis():
    def __init__(self, host: str, port: int = 6379, database: int = 0, password: str = ""):
        """
        It creates a Redis object.
        
        :param host: The hostname or IP address of the Redis server
        :type host: str
        :param port: The port number of the Redis server. The default is 6379, defaults to 6379
        :type port: int (optional)
        :param database: The database number to connect to, defaults to 0
        :type database: int (optional)
        :param password: The password to use to connect to the Redis server
        :type password: str
        """
        self.rdb = redis.Redis(host=host, port=port, db=database, password=password)
    
    def Ping(self) -> bool:
        """
        This function returns a boolean value that indicates whether the connection to the Redis server
        is still alive
        :return: A boolean value.
        """
        return self.rdb.ping()
    
    # https://redis.readthedocs.io/en/v4.3.4/commands.html#redis.commands.core.CoreCommands.set
    # ttl, second
    @RetryOnNetworkError
    def Set(self, key:str, value:typing.Any, ttl:int=None) -> (bool | None):
        """
        It sets the value of a key in the database.
        
        :param key: The key to set
        :type key: str
        :param value: The value to be stored in the key
        :type value: str
        :param ttl: Time to live in seconds
        :type ttl: int
        :return: The return value is a boolean value.
        """
        return self.rdb.set(key, pickle.dumps(value, protocol=2), ex=ttl)
    
    # https://redis.readthedocs.io/en/v4.3.4/commands.html#redis.commands.core.CoreCommands.get
    @RetryOnNetworkError
    def Get(self, key:str, default:typing.Any=None) -> typing.Any:
        """
        It gets the value of a key from the redis database.
        
        :param key: The key to get the value of
        :type key: str
        :return: A string or None
        """
        res = self.rdb.get(key)
        if res != None:
            res = pickle.loads(res)
        else:
            res = default

        return res

    # https://redis.readthedocs.io/en/v4.3.4/commands.html#redis.commands.core.CoreCommands.delete
    @RetryOnNetworkError
    def Del(self, key:str) -> bool:
        """
        It deletes the key from the database
        
        :param key: The key to delete
        :type key: str
        :return: The return value is a boolean value.
        """
        return self.rdb.delete(key) == 1
    
    @RetryOnNetworkError
    def Exists(self, key:str) -> bool:
        """
        It returns True if the key exists in the database, and False if it doesn't
        
        :param key: The key to check for existence
        :type key: str
        :return: A boolean value.
        """
        return self.rdb.exists(key) == True
    
    # https://redis.readthedocs.io/en/latest/connections.html?highlight=lock#redis.Redis.lock
    @RetryOnNetworkError
    def Lock(self, key:str) -> RedisLock:
        """
        It returns a RedisLock object.
        
        :param key: The key to lock
        :type key: str
        :return: A RedisLock object.
        """
        return RedisLock(self.rdb.lock("redis_lock:" + key))
    
    @RetryOnNetworkError
    def Queue(self, name:str, length:int=0) -> redisQueue:
        """
        It creates a redisQueue object.
        
        :param key: The key of the queue
        :type key: str
        :return: redisQueue
        """
        return redisQueue(self.rdb, name, length)

    def QueueConfirm(self, name:str, length:int=0, timeout:int=300) -> redisQueueConfirm:
        """
        It creates a new redisQueueConfirm object.
        
        :param name: The name of the queue
        :type name: str
        :param length: The maximum length of the queue. If the queue is full, the oldest item will be
        removed, defaults to 0
        :type length: int (optional)
        :return: A redisQueueConfirm object.
        """
        return redisQueueConfirm(self.rdb, name, length, timeout)

if __name__ == "__main__":
    r = Redis("192.168.1.139")
    r.Ping()
    print(1, r.Get("key"))
    print(2, r.Set("key", "value"))
    print(3, r.Get("key"))
    print(4, r.Del("key"))
    print(5, r.Get("key"))
    l = r.Lock("lock_key")
    l.Acquire()
    l.Release()

    q = r.Queue('queue')
    q.Put('1')
    q.Put('2')

    for v in q:
        print("value: ", v)


