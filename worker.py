from __future__ import unicode_literals
import redis
from rq import Worker, Queue, Connection
import os
from time import sleep

listen = ['default']
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
conn = redis.from_url(redis_url)




def long_running_work(arg1,arg2):
        print arg1
        sleep(2)
        return arg2
        sleep(2)
        return arg2,arg2




if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()