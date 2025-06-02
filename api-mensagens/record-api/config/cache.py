import redis

def get_cache():
    return redis.Redis(host='redis', port=6379, decode_responses=True)
