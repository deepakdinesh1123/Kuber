import os

from dotenv import load_dotenv
from redis import Redis
from rq import Queue

load_dotenv()

r = Redis(host=os.environ.get("REDIS_HOST"), port=os.environ.get("REDIS_PORT"))
q = Queue(connection=r)
