from .client import HttpMethod
from .decorators import HttpMethodDecorator


class OPTIONS(HttpMethodDecorator):

    def __init__(self, path):
        super(OPTIONS, self).__init__(path)

    def __call__(self, func):
        def options_decorator(*args):
            func._http__method = HttpMethod.OPTIONS
            return super(OPTIONS, self).call(func, *args)
        return options_decorator
