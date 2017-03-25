import functools
import signal

from ..defaults import ENABLE_TIMEOUTS, DEFAULT_TIMEOUT
from ..exceptions import TimeoutException, InvalidArgumentException


def waiting_for(func=None, *, timeout=DEFAULT_TIMEOUT):
    def _alarm_handler(signal_number, stack_frame):
        raise TimeoutException('Timeout exceed')

    if func is None:
        return lambda f: waiting_for(f, timeout=timeout)

    if not callable(func):
        raise InvalidArgumentException(
            f'Use @waiting_for(timeout={func}) instead of @waiting_for({func})'
        )

    @functools.wraps(func)
    def inner(*args, **kwargs):
        signal.signal(signal.SIGALRM, _alarm_handler)
        signal.alarm(timeout)
        return func(*args, **kwargs)

    return inner if ENABLE_TIMEOUTS else func

