```python
from abc import ABC, abstractmethod

class PluginBase(ABC):
    """
    Abstract base class for plugins.
    """

    @abstractmethod
    def load(self):
        """
        Method to load the plugin.
        """
        pass

    @abstractmethod
    def execute(self):
        """
        Method to execute the plugin.
        """
        pass

    @abstractmethod
    def unload(self):
        """
        Method to unload the plugin.
        """
        pass
```