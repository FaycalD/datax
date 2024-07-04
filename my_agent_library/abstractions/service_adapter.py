```python
from abc import ABC, abstractmethod

class ServiceAdapter(ABC):
    """
    Abstract base class for service adapters.
    """

    @abstractmethod
    def connect(self):
        """
        Connect to the service.
        """
        pass

    @abstractmethod
    def disconnect(self):
        """
        Disconnect from the service.
        """
        pass

    @abstractmethod
    def fetch_data(self):
        """
        Fetch data from the service.
        """
        pass

    @abstractmethod
    def update_data(self):
        """
        Update data on the service.
        """
        pass
```