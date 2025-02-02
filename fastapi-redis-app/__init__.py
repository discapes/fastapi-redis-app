from fastapi import FastAPI
import redis

app = FastAPI()
redis_client = redis.Redis(host="redis", port=6379, decode_responses=True)


@app.get("/")
def read_root():
    redis_client.incr("visits")
    visits = redis_client.get("visits")
    return {"message": "Hello from version 4", "visits": visits}
