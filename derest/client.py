import logging as LOG
import re
import six

try:
    # python2
    from urllib import urlencode
except ImportError:
    # python3
    from urllib.parse import urlencode


def render_path(path, args):
    """
    Render REST path from *args
    """
    LOG.debug('RENDERING PATH FROM: %s,  %s', path, args)
    result = path
    matches = re.search(r'{(.*)}', result)
    while matches:
        path_token = matches.group(1)
        if path_token not in args:
            raise Exception("Missing argument %s in REST call" % (path_token))
        result = re.sub('{%s}' % (path_token), args[path_token], result)
        matches = re.search(r'{(.*)}', result)
    return result


class HttpMethod(object):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'
    HEAD = 'HEAD'


class RestClient(object):
    """
    Simple REST client
    """

    def __init__(self, endpoint, auth):
        self.endpoint = endpoint
        if not self.endpoint.endswith("/"):
            self.endpoint = self.endpoint + "/"
        self.auth = auth
        self.named_auths = {}
        if hasattr(self.__class__, '_default__header__parameters'):
            self._header__parameters = self.__class__._default__header__parameters
        else:
            self._header__parameters = {}
        self._query__parameters = {}
        self._body__content = None

        pass

    def set_default_auth(self, auth):
        """
        Set default authentication, 'auth' should be a valid 'requests' library
        authentication object.
        """
        self.auth = auth

    def add_auth(self, name, auth):
        """
        Add a named authentication which can be used for specific operations
        based on the '@auth()' decorator.
        """
        self.named_auths[name] = auth

    def start_session(self):
        """
        Initializes 'requests' session object. All consecutive requests
        will go via the session object, with 

        If this method is not called on the client, the requests will be
        performed using standard requests without a session.
        """
        pass

    def stop_session(self):
        """
        Stops the requests session, i.e. all consecutive requests will be
        called using standard requests without session object.
        """
        pass

    def build_request(self, path_components=[], query_components={}):
        """
        Builds request by combining the endpoint with path
        and query components.
        """
        LOG.debug("Building request from path tokens: %s", path_components)

        req = None

        if six.PY2:
            import urlparse
            req = urlparse.urljoin(self.endpoint, "/".join(path_components))
        else:
            from urllib.parse import urljoin
            req = urljoin(self.endpoint, "/".join(path_components))

        if query_components is not None and len(query_components) > 0:
            req += "?" + urlencode(query_components)

        return req
