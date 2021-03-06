from .client import HttpMethod
from .decorators import HttpMethodDecorator


class PUT(HttpMethodDecorator):

    def __init__(self, path):
        super(PUT, self).__init__(path)

    def __call__(self, func):
        def put_decorator(*args):
            func._http__method = HttpMethod.PUT
            return super(PUT, self).call(func, *args)
        return put_decorator
