"""Worker."""
import os

import redis
from rq import Worker, Queue, Connection

listen = [os.environ['QUEUE_NAME']]

redis_url = os.getenv('REDISTOGO_URL')

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
