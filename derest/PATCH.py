from .client import HttpMethod
from .decorators import HttpMethodDecorator


class PATCH(HttpMethodDecorator):

    def __init__(self, path):
        super(PATCH, self).__init__(path)

    def __call__(self, func):
        def patch_decorator(*args):
            func._http__method = HttpMethod.PATCH
            return super(PATCH, self).call(func, *args)
        return patch_decorator
