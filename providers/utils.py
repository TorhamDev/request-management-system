import redis
import json

r = redis.Redis(host="localhost", port=6379, decode_responses=True)


def add_request_to_queue(provider: int, p_rate_limit: int, requst: str) -> None:
    r.rpush("requests", json.dumps({"provider": provider, "data": requst, "rate_limit": p_rate_limit}))
