```python
from .data_object import DataObject

class JIRAIssue(DataObject):
    def __init__(self, issue_id, summary, description, status, assignee):
        self.issue_id = issue_id
        self.summary = summary
        self.description = description
        self.status = status
        self.assignee = assignee

    def to_dict(self):
        return {
            'issue_id': self.issue_id,
            'summary': self.summary,
            'description': self.description,
            'status': self.status,
            'assignee': self.assignee
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            issue_id=data.get('issue_id'),
            summary=data.get('summary'),
            description=data.get('description'),
            status=data.get('status'),
            assignee=data.get('assignee')
        )
```