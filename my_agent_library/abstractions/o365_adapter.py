```python
from .service_adapter import ServiceAdapter
from ..core.api_clients.o365_client import O365Client
from ..core.models.notion_page import NotionPage

class O365Adapter(ServiceAdapter):
    def __init__(self, auth_manager):
        self.client = O365Client(auth_manager)

    def fetch_data(self, query):
        raw_data = self.client.get_data(query)
        return [NotionPage(data) for data in raw_data]

    def update_data(self, data_object):
        if not isinstance(data_object, NotionPage):
            raise TypeError("data_object must be an instance of NotionPage")
        return self.client.update_data(data_object.to_dict())
```