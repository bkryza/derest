from .client import HttpMethod
from .decorators import HttpMethodDecorator


class DELETE(HttpMethodDecorator):

    def __init__(self, path):
        super(DELETE, self).__init__(path)

    def __call__(self, func):
        def delete_decorator(*args):
            func._http__method = HttpMethod.DELETE
            return super(DELETE, self).call(func, *args)

        return delete_decorator
