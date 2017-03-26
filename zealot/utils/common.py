import functools
import signal

from zealot.conf import settings
from zealot.exceptions import TimeoutException, InvalidArgumentException


def waiting_for(func=None, *, timeout=settings.DEFAULT_TIMEOUT):
    """ Set maximum execution time for a function 
    
    :param func: function to decorate
    :param timeout: maximum allowed execution time
    :return: result of the func
    """
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
        initial = signal.getsignal(signal.SIGALRM)
        signal.signal(signal.SIGALRM, _alarm_handler)
        signal.alarm(timeout)
        try:
            return func(*args, **kwargs)
        finally:
            signal.signal(signal.SIGALRM, initial)

    return inner if settings.ENABLE_TIMEOUTS else func

