import logging as LOG
import requests
import inspect

from .client import RestClient, HttpMethod, render_path
from .utils import merge_dicts, dict_from_args


def query(name, value=None):
    """
    Query parameter decorator
    """
    def query_decorator(f):
        if not hasattr(f, '_query__parameters'):
            f._query__parameters = {}
        f._query__parameters[name] = value
        return f
    return query_decorator


def header(name, value):
    """
    Header class and method decorator
    """
    def header_decorator(t):
        if inspect.isclass(t):
            if not hasattr(t, '_default__header__parameters'):
                t._default__header__parameters = {}
            t._default__header__parameters[name.lower()] = value
        else:
            if not hasattr(t, '_header__parameters'):
                t._header__parameters = {}
            t._header__parameters[name.lower()] = value
        return t
    return header_decorator


def body(name, value=None):
    """
    Body parameter decorator
    """
    def body_decorator(f):
        f._body__content = value
        return f
    return body_decorator

def auth(


class HttpMethodDecorator(object):
    """
    Abstract decorator for HTTP method decorators
    """

    def __init__(self, path):
        self.path_template = path

    def call(self, func, *args):
        http_method = func._http__method
        rest_client = args[0]
        args_dict = dict_from_args(func, *args)
        req_path = render_path(self.path_template, args_dict)
        query_parameters = None
        header_parameters = rest_client._header__parameters
        body_content = args_dict.get('body')

        try:
            query_parameters = func._query__parameters
        except:
            pass
        try:
            header_parameters = merge_dicts(
                header_parameters, func._header__parameters)
        except:
            pass
        try:
            body_content = func._body__content
        except:
            pass

        req = rest_client.build_request(
            req_path.split('/'), query_parameters)

        if 'content-type' not in header_parameters:
            header_parameters['content-type'] = 'application/json'

        if 'accept' not in header_parameters:
            header_parameters['accept'] = 'application/json'

        LOG.debug('REQUEST: {method} {request}'.format(
            method=http_method, request=req))

        result = None

        if http_method == HttpMethod.GET:
            result = requests.get(req, auth=rest_client.auth,
                                  headers=header_parameters, data=body_content)
        elif http_method == HttpMethod.POST:
            result = requests.post(req, auth=rest_client.auth,
                                   headers=header_parameters, data=body_content)
        elif http_method == HttpMethod.PUT:
            result = requests.put(req, auth=rest_client.auth,
                                  headers=header_parameters, data=body_content)
        elif http_method == HttpMethod.DELETE:
            result = requests.delete(req, auth=rest_client.auth,
                                     headers=header_parameters, data=body_content)
        elif http_method == HttpMethod.UPDATE:
            result = requests.update(req, auth=rest_client.auth,
                                     headers=header_parameters, data=body_content)
        elif http_method == HttpMethod.HEAD:
            result = requests.head(req, auth=rest_client.auth,
                                   headers=header_parameters, data=body_content)
        else:
            raise 'Unsupported HTTP method: {method}'.format(
                method=http_method)

        result.raise_for_status()

        content_type = result.headers.get('content-type')
        if content_type == 'application/json':
            return result.json()
        elif content_type == 'application/octet-stream':
            return result.content
        else:
            return result.text

        return result.json()
