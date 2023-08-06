from redis.client import Redis


class RateLimiterConfig:
    redis: Redis = None
    service_name: str = 'hrthy-service'

    @classmethod
    def init(
        cls,
        redis: Redis,
        service_name: str
    ):
        cls.redis = redis
        cls.service_name = service_name
