"""
    merchant.py - paypack-py merchant module
"""
from paypack.client import HttpClient,creadentials
from paypack.oauth2 import Oauth

""" Merchant that is used to make api calls to the paypack api for mechant account """
class Merchant(HttpClient):

        
        def __init__(self):
            HttpClient.__init__(self, client_id=creadentials.get('client_id'), client_secret=creadentials.get('client_secret'))

        """
        The merchant class that is used to make api calls to the paypack api for merchant account
        """

        def me(self,access_token=None):
            """
            Get merchant account
            :param access: access token which is in header
            :return: merchant account

            """            
            if(access_token is not None):
                if(self.client.headers.get('Authorization') is None):
                    if(self.is_expired() is True):
                        self.update_headers({
                            'Authorization': f'Bearer {access_token}',
                            'Content-Type': 'application/json'
                        })
            
            uri = '/merchants/me'
            url = f"{self.base_url}{uri}"
            res = self.get(url=url)  
            if(res.status_code == 401):
                Oauth().refresh_access_token()
                res = self.get(url=url)
            return res.json()
