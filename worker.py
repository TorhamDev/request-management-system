import redis
import json
import time
r = redis.Redis(host="localhost", port=6379, decode_responses=True)


while True:
    data = r.lpop("requests")

    if data:
        data = json.loads(data)
    else:
        print("NOTHING IN QUEUE")
        continue

    key = f"provider::{data['provider']}"
    token = r.get(key)

    if not token:
        print(f"DOING REQUEST => {key}")
        r.set(key, "bar", ex=data["rate_limit"])
    else:
        print(f"BACK TO QUEUE  => {key}")
        r.rpush("requests", json.dumps(data))

    time.sleep(1)