```python
import requests
from .token_store import TokenStore

class AuthManager:
    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.token_store = TokenStore()

    def get_authorization_url(self, scope):
        params = {
            "client_id": self.client_id,
            "response_type": "code",
            "redirect_uri": self.redirect_uri,
            "scope": scope
        }
        url = "https://login.microsoftonline.com/common/oauth2/v2.0/authorize"
        response = requests.get(url, params=params)
        return response.url

    def get_token_from_code(self, auth_code):
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": auth_code,
            "redirect_uri": self.redirect_uri,
            "grant_type": "authorization_code"
        }
        url = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
        response = requests.post(url, data=data)
        response_json = response.json()
        self.token_store.save_token(response_json)
        return response_json

    def get_token(self):
        token = self.token_store.get_token()
        if not token:
            raise Exception("No token found")
        return token
```