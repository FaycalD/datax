```python
from my_agent_library.core.api_clients.notion_client import NotionClient
from my_agent_library.core.models.notion_page import NotionPage
from my_agent_library.utilities.logger import Logger
from my_agent_library.utilities.error_handler import ErrorHandler

class UpdateNotionPage:
    def __init__(self):
        self.notion_client = NotionClient()
        self.logger = Logger().get_logger(__name__)
        self.error_handler = ErrorHandler()

    def update_page(self, page_id: str, updated_content: dict):
        try:
            page = NotionPage(page_id, updated_content)
            self.notion_client.update_page(page)
            self.logger.info(f"Page {page_id} updated successfully.")
        except Exception as e:
            self.error_handler.handle_error(f"Failed to update Notion page {page_id}.", e)
```