```python
import requests
from abc import ABC, abstractmethod

class BaseClient(ABC):
    """
    Abstract base class for API clients.
    """

    def __init__(self, base_url):
        self.base_url = base_url

    @abstractmethod
    def get(self, endpoint, params=None):
        """
        Abstract method for HTTP GET requests.
        """
        pass

    @abstractmethod
    def post(self, endpoint, data=None):
        """
        Abstract method for HTTP POST requests.
        """
        pass

    @abstractmethod
    def put(self, endpoint, data=None):
        """
        Abstract method for HTTP PUT requests.
        """
        pass

    @abstractmethod
    def delete(self, endpoint):
        """
        Abstract method for HTTP DELETE requests.
        """
        pass
```