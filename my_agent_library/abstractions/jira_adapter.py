```python
from .service_adapter import ServiceAdapter
from ..core.api_clients.jira_client import JIRAClient
from ..core.models.jira_issue import JIRAIssue

class JIRAAdapter(ServiceAdapter):
    def __init__(self, auth_manager):
        self.client = JIRAClient(auth_manager)

    def fetch_data(self, query):
        response = self.client.get_issues(query)
        return [JIRAIssue(issue) for issue in response]

    def update_data(self, issue_id, data):
        response = self.client.update_issue(issue_id, data)
        return JIRAIssue(response)
```