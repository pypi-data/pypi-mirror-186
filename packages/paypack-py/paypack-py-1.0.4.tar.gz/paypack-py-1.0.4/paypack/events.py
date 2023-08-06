
"""
    events.py - Events module for paypack-py.
"""

from paypack.client import HttpClient, creadentials
from paypack.oauth2 import Oauth

"""
    Event that inherits from the HttpClient class.
"""

class Event(HttpClient):

    def __init__(self):
        """
        Constructor for the  HttpClient class
        :return:
        """
        HttpClient.__init__(self, client_id=creadentials.get('client_id'), client_secret=creadentials.get('client_secret'))

    """ List all events implementation with query parameters """
    def list(self, access_token=None, **kwargs):
        """
        List all events implementation with query parameters
        :param kwargs:
        :return: Response object list

        """
        if(access_token is not None):
            if(self.client.headers.get('Authorization') is None):
                self.update_headers({
                    'Authorization': f'Bearer {access_token}',
                    'Content-Type': 'application/json'
                })

        uri = '/events/transactions'
        url = f"{self.base_url}{uri}"
        res = self.get(url=url, params=kwargs)
        if (res.status_code == 401):
            Oauth().refresh_access_token()
            res = self.get(url=url, params=kwargs)
        return res.json()

