from .client import HttpMethod
from .decorators import HttpMethodDecorator


class UPDATE(HttpMethodDecorator):

    def __init__(self, path):
        super(UPDATE, self).__init__(path)

    def __call__(self, func):
        def update_decorator(*args):
            func._http__method = HttpMethod.UPDATE
            return super(UPDATE, self).call(func, *args)
        return update_decorator
