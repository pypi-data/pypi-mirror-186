from urllib.error import ContentTooShortError
from http.client import RemoteDisconnected
from urllib.error import ContentTooShortError, URLError

from greatawesomeutils.lang import is_errors_instance

NETWORK_ERRORS = [RemoteDisconnected, URLError,
                  ConnectionAbortedError, ContentTooShortError,  BlockingIOError]


def is_error(errs):
    def fn(e):
        result, index = is_errors_instance(errs, e)
        return result
    return fn


is_network_error = is_error(NETWORK_ERRORS)
