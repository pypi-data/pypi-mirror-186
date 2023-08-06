"""
    oauth2.py - paypack-py oauth2 module
"""

import calendar
from datetime import datetime, timedelta
from paypack.client import HttpClient, token_keys, creadentials;

"""
    Oauth class which inhert HttpClient that is used to make api calls to the paypack api for authentication and authorization.
"""
class Oauth(HttpClient):
    """ Authentication endpoints """

    def __init__(self):
        HttpClient.__init__(self, client_id=creadentials.get('client_id'), client_secret=creadentials.get('client_secret'))

    def auth(self):
        """
        Authorize client
        :return: access_token, refresh_token, expires_at
        """
        if(self.client_id is None or self.client_secret is None):
            raise Exception("Client id or client secret of the application is missing")
        
        uri = '/auth/agents/authorize'

        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }

        url = f"{self.base_url}{uri}"
        res = self.post(url=url, json=data)
        now = datetime.utcnow() + timedelta(minutes=14)
        self.access_token = res.json()['access']
        self.refresh_token = res.json()['refresh']
        self.expires_at = calendar.timegm(now.timetuple())

        self.update_headers({
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        })
        self.set_client_token()
        return res.json()
    
    def refresh_access_token(self, refresh_token=None):

        """
        Refresh access token
        :return: access_token, refresh_token, expires_at
        """            
        if(refresh_token is None):
            if(token_keys.get('refresh') is None):
                return self.auth()
            else:
                refresh_token = token_keys.get('refresh')
        
        uri = '/auth/refresh'
        url = f"{self.base_url}{uri}/{refresh_token}"
        res = self.get(url=url)

        now = datetime.utcnow() + timedelta(minutes=14)
        self.access_token = res.json()['access']
        self.refresh_token = res.json()['refresh']
        self.expires_at = calendar.timegm(now.timetuple())

        self.update_headers({
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        })

        self.set_client_token()
        return res.json()

    def get_access_token(self):
        """
        Returns access, refresh and expires time from authorization
        :return: access_token
        """
        if(token_keys.get('access') is None):
            if(token_keys.get('refresh') is not None):
                if(self.is_expired):
                    self.refresh_access_token(refresh_token=token_keys.get('refresh'))
            self.auth()      
        
        if(self.is_expired is False):
            self.refresh_access_token(refresh_token=token_keys.get('refresh'))

        access_token = {
            "access":token_keys.get('access'),
        }
        return access_token

    def get_refresh_token(self):
        """
        Returnsrefresh  from authorization
        :return: access_token

        """
        if(token_keys.get('refresh') is None):
            self.auth()

        refresh_token = {
            "refresh":token_keys.get('refresh')
        }
        return refresh_token

