```python
from .data_object import DataObject

class NotionPage(DataObject):
    def __init__(self, id, title, content, last_edited):
        super().__init__(id)
        self.title = title
        self.content = content
        self.last_edited = last_edited

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_content(self):
        return self.content

    def set_content(self, content):
        self.content = content

    def get_last_edited(self):
        return self.last_edited

    def set_last_edited(self, last_edited):
        self.last_edited = last_edited
```