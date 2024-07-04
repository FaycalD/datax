```python
from my_agent_library.core.api_clients.jira_client import JIRAClient
from my_agent_library.core.models.jira_issue import JIRAIssue
from my_agent_library.utilities.logger import Logger

class FetchJIRAIssues:
    def __init__(self):
        self.jira_client = JIRAClient()
        self.logger = Logger()

    def fetch_issues(self, project_id):
        try:
            response = self.jira_client.get_issues(project_id)
            issues = [JIRAIssue(issue) for issue in response['issues']]
            return issues
        except Exception as e:
            self.logger.log(f"Error fetching JIRA issues: {str(e)}")
            return None
```