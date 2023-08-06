"""
PayPack Client module

"""
import time
from paypack.http_client import client
from paypack.config import base_url

token_keys = {}
creadentials = {}

# client class that is used as a wrapper for the http client
class HttpClient(object):

    """
     The client class that is used as a wrapper for the http client 
     is used to make different api calls to the paypack api.

    """

    def __init__(self,client_id, client_secret, access_token=None, refresh_token=None, expires_at=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = base_url
        self.client = client 
        self.date_format = '%Y-%m-%d %H:%M:%S'
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.expires_at = expires_at
        self.set_client_crendential()
    
    def _makeRequest(self,method=None, url=None, json=None, headers=None, params=None, files=None):
        """
        Makes the http request to the paypack api

        Args:
            method (str, optional): [The http method to be used]. Defaults to None.
            url (str, optional): [The url to be used]. Defaults to None.
            data (str, optional): [The data to be used]. Defaults to None.
            headers (str, optional): [The headers to be used]. Defaults to None.
            params (str, optional): [The params to be used]. Defaults to None.
            files (str, optional): [The files to be used]. Defaults to None.

        Returns:
            [Response]: [The response from the paypack api]
        """
        if(self.client.headers.get('Authorization') is None):
            if(token_keys.get("access") is not None):
                if(self.is_expired() is False):
                    self.update_headers({
                        'Authorization': f'Bearer {token_keys.get("access")}',
                        'Content-Type': 'application/json'
                    })                    

        return self.client.request(method=method, url=url, json=json, headers=headers, params=params, files=files)
                    

    def get(self, url, params=None):
        return self._makeRequest(method='GET', url=url, params=params)

    def post(self, url, json=None):
        return self._makeRequest(method='POST', url=url, json=json)

    def put(self, url, json=None):
        return self._makeRequest(method='PUT', url=url, json=json)

    def delete(self, url, json=None):
        return self._makeRequest(method='DELETE', url=url, json=json)
        
    def update_headers(self, headers):
        self.client.headers.update(headers)

    def set_client_token(self):
        global token_keys
        token_keys.update({
            'access': self.access_token,
            'refresh': self.refresh_token,
            'expires': self.expires_at
        })
    
    def set_client_crendential(self):
        """
        Sets the client crendential to be used in the http request

        Returns:
            [Dict]: [The client crendential]
        """
        global creadentials
        creadentials.update({
            'client_id': self.client_id,
            'client_secret': self.client_secret
        })
        return creadentials
    
    def is_expired(self)->bool:
        """
        Checks if the access token is expired

        Returns:
            [bool]: [True if expired, False if not]
        """
        if(token_keys.get('expires') is not None):
            return token_keys.get('expires') < (int(time.time()) + 60)
        else:
            return True