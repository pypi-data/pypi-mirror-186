from time import sleep
from typing import Callable

from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.utils.timezone import now

ResponseGetter = Callable[[HttpRequest], HttpResponse]


class NowMiddleware:
    """
    This middleware adds a "now()" method to request objects, this way a
    common timestamp is available within the scope of the request. That's
    useful by example for token validity: if a token expires at a given time
    it allows to consider that the request conceptually happens instantly and
    every time you measure the token's validity you do so based on the
    request's global timestamp and not the actual time (which is just
    milliseconds away).
    """

    def __init__(self, get_response: ResponseGetter):
        """
        Storing away
        """

        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        """
        Monkey-patching the request object with the custom now() function
        """

        fixed_now = now()
        object.__setattr__(request, "now", lambda: fixed_now)

        return self.get_response(request)


class SlowMiddleware:
    """
    That's a middleware that will simulate a latency on all requests.

    Notes
    -----
    You can set it by putting the number of seconds you want to sleep in the
    SLOW_MIDDLEWARE_LATENCY Django settings.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        to_sleep = getattr(settings, "SLOW_MIDDLEWARE_LATENCY", None)

        if to_sleep:
            sleep(to_sleep)

        return self.get_response(request)
