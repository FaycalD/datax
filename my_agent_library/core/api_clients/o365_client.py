```python
from .base_client import BaseClient

class O365Client(BaseClient):
    def __init__(self, auth_manager):
        super().__init__(auth_manager)
        self.service_name = 'O365'

    def get(self, endpoint, params=None):
        headers = self._get_auth_header()
        response = self._send_request('GET', endpoint, headers=headers, params=params)
        return response

    def post(self, endpoint, data=None):
        headers = self._get_auth_header()
        response = self._send_request('POST', endpoint, headers=headers, data=data)
        return response

    def put(self, endpoint, data=None):
        headers = self._get_auth_header()
        response = self._send_request('PUT', endpoint, headers=headers, data=data)
        return response

    def delete(self, endpoint):
        headers = self._get_auth_header()
        response = self._send_request('DELETE', endpoint, headers=headers)
        return response

    def _get_auth_header(self):
        token = self.auth_manager.get_token(self.service_name)
        return {'Authorization': f'Bearer {token}'}
```