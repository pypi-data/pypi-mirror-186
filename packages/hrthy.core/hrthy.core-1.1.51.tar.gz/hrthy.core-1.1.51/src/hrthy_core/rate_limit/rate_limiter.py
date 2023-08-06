from datetime import datetime, timezone

from starlette.requests import Request

from hrthy_core.rate_limit.exceptions import TooManyRequestsException
from hrthy_core.rate_limit.rate_limit_configuration import RateLimiterConfig
from hrthy_core.security.security import RequesterType
from hrthy_core.utils.utils import logger


class RateLimiter:

    def __init__(
        self,
        endpoint: str,
        times: int,
        seconds: int = 0,
        minutes: int = 0,
        hours: int = 0,
        days: int = 0
    ):
        """
        :param cache_key_prefix: request prefix
        :param limit: expressed in "number/seconds"
        """
        self.endpoint = endpoint
        if not any([seconds, minutes, hours, days]) or times <= 0:
            raise Exception('Wrong Rate Limit configuration')
        self.period = seconds + minutes * 60 + hours * 3600 + days * 86400
        self.times = times

    def __call__(self, request: Request):
        # Apply rate limit on user ID if it is an authenticated request, otherwise via IP
        # Service requests are not considered
        requester = getattr(request, 'requester', None)
        if requester:
            if requester.requester_type == RequesterType.service:
                return
            self._apply_rate_limit(requester.requester_id)
        else:
            ip = request.headers.get('X-Forwarded-For') or request.client.host
            self._apply_rate_limit(ip)

    def _apply_rate_limit(self, rate_limit_identifier: str):
        cache_key: str = f"rate-limit:{RateLimiterConfig.service_name}:{self.endpoint}:{rate_limit_identifier}"
        call_counter: int = RateLimiterConfig.redis.get(cache_key) or 0
        call_counter = int(call_counter) + 1
        if call_counter > self.times:
            expire_at: int = RateLimiterConfig.redis.expiretime(cache_key)
            now = int(datetime.utcnow().replace(tzinfo=timezone.utc).timestamp())
            logger.info(
                'Rate limit hit. Cache Key: %s, Times: %s, Period: %s' % (cache_key, self.times, self.period)
            )
            raise TooManyRequestsException(
                detail="Too many requests",
                headers={
                    'Retry-After': str(expire_at - now)
                }
            )
        RateLimiterConfig.redis.set(name=cache_key, value=call_counter, ex=self.period)
