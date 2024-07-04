```python
import requests
from .base_client import BaseClient

class JIRAClient(BaseClient):
    def __init__(self, base_url, auth_manager):
        super().__init__(base_url, auth_manager)

    def get_issue(self, issue_id):
        headers = self._get_auth_headers()
        response = requests.get(f"{self.base_url}/rest/api/2/issue/{issue_id}", headers=headers)
        self._handle_response(response)
        return response.json()

    def create_issue(self, issue_data):
        headers = self._get_auth_headers()
        response = requests.post(f"{self.base_url}/rest/api/2/issue", headers=headers, json=issue_data)
        self._handle_response(response)
        return response.json()

    def update_issue(self, issue_id, issue_data):
        headers = self._get_auth_headers()
        response = requests.put(f"{self.base_url}/rest/api/2/issue/{issue_id}", headers=headers, json=issue_data)
        self._handle_response(response)
        return response.json()

    def delete_issue(self, issue_id):
        headers = self._get_auth_headers()
        response = requests.delete(f"{self.base_url}/rest/api/2/issue/{issue_id}", headers=headers)
        self._handle_response(response)
        return response.status_code
```