"""
    transactions.py - paypack-py Transactions module
"""
from paypack.client import HttpClient, creadentials
from paypack.oauth2 import Oauth

"""
    Transaction class which inherits from the HttpClient class and implements the transactions endpoint methods.
"""
class Transaction(HttpClient):

    def __init__(self):
        HttpClient.__init__(self, client_id=creadentials.get('client_id'), client_secret=creadentials.get('client_secret'))

    """ Cashin implementation """
    def cashin(self, amount, phone_number,access_token=None,mode=None):
        """
        Cashin implementation
        :param amount: Amount to be deposited
        :param phone_number: number to be deducted
        :return: Response object
        """
        uri = '/transactions/cashin'
        data = {
            'amount': int(amount),
            'number': str(phone_number),
        }

        url = f"{self.base_url}{uri}"

        if(access_token is not None):
            if(self.client.headers.get('Authorization') is None):
                self.update_headers({
                    'Authorization': f'Bearer {access_token}',
                    'Content-Type': 'application/json'
                })
        if(mode is not None):
            if(self.client.headers.get('X-Webhook-Mode') is None):
                self.update_headers({
                    'X-Webhook-Mode': f'{mode}',
                })
            
        res = self.post(url=url, json=data)
        if (res.status_code == 401):
            Oauth().refresh_access_token()
            res = self.post(url=url, json=data)
        return res.json()

    """ cashout implementation """
    def cashout(self, amount, phone_number,access_token=None,mode=None):
        """
        Cashout implementation
        :param amount: Amount to be deducted
        :param phone_number: number to be deducted
        :return: Response object
        """
        if(access_token is not None):
            if(self.client.headers.get('Authorization') is None):
                self.update_headers({
                    'Authorization': f'Bearer {access_token}',
                    'Content-Type': 'application/json'
                })
        if(mode is not None):
            if(self.client.headers.get('X-Webhook-Mode') is None):
                self.update_headers({
                    'X-Webhook-Mode': f'{mode}',
                })
        uri = '/transactions/cashout'
        data = {
            'amount': int(amount),
            'number': str(phone_number),
        }

        url = f"{self.base_url}{uri}"

        res = self.post(url=url, json=data)
        if (res.status_code == 401):
            Oauth().refresh_access_token()
            res = self.post(url=url, json=data)
        return res.json()
    
    """ List transactions implementation with parametes """
    def list(self, access_token=None, **kwargs):
        """
        List transactions implementation with parameters
        :param kwargs:
        :return: Response object
        """

        if(access_token is not None):
            if(self.client.headers.get('Authorization') is None):
                self.update_headers({
                    'Authorization': f'Bearer {access_token}',
                })

        uri = '/transactions/list'
        url = f"{self.base_url}{uri}"      
        res = self.get(url=url,params=kwargs)
        if (res.status_code == 401):
            Oauth().refresh_access_token()
            res = self.get(url=url, params=kwargs)
        return res.json()

    """ Find transaction implementation """
    def find(self, ref, access_token=None):
        """
        Find transaction implementation
        :param ref: Transaction id
        :return: Response object
        """
        if(access_token is not None):
            if(self.client.headers.get('Authorization') is None):
                self.update_headers({
                    'Authorization': f'Bearer {access_token}',
                })

        uri = f'/transactions/find/{ref}'
        url = f"{self.base_url}{uri}"


        res = self.get(url=url)
        if (res.status_code == 401):
            Oauth().refresh_access_token()
            res = self.get(url=url)
        return res.json()

