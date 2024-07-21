import redis
import time


requests = [{"data":1212, "provider":1}, {"data":1212, "provider":1}, {"data":1212, "provider":1}]

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

counter = len(requests)
while len(requests) > 0:
    key = f"provider::{requests[-counter]['provider']}"
    token = r.get(key)

    if not token:
        print("DOING REQUEST!")
        requests.pop()
        counter -= 1
        r.set(key, "bar", ex=5)
    else:
        print("BACK TO THE QUEUE")
    time.sleep(1)