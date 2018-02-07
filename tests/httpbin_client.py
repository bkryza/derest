from derest import RestClient
from derest import GET
from derest import header, query


@header('user-agent', 'derest user agent test')
@header('accept', 'application/json')
class HttpBinClient(RestClient):
    def __init__(self, endpoint, auth):
        super(HttpBinClient, self).__init__(endpoint, auth)

    @GET('user-agent')
    def user_agent(self):
        """Returns user-agent"""
