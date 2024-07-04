```python
from abc import ABC, abstractmethod

class DataObject(ABC):
    """
    Abstract base class for data models.
    """

    @abstractmethod
    def to_dict(self):
        """
        Convert the data object to a dictionary.
        """
        pass

    @abstractmethod
    def from_dict(self, data_dict):
        """
        Populate the data object from a dictionary.
        """
        pass
```