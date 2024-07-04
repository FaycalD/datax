```python
import os
import importlib

from .plugin_base import PluginBase

class PluginLoader:
    def __init__(self, plugin_directory):
        self.plugin_directory = plugin_directory
        self.plugins = []

    def load_plugins(self):
        for file in os.listdir(self.plugin_directory):
            if file.endswith(".py") and file != "plugin_base.py":
                module_name = file[:-3]  # remove .py extension
                module = importlib.import_module(f".{module_name}", package="my_agent_library.plugins")
                for item in dir(module):
                    obj = getattr(module, item)
                    if isinstance(obj, type) and issubclass(obj, PluginBase) and obj is not PluginBase:
                        self.plugins.append(obj())

    def run_plugins(self):
        for plugin in self.plugins:
            plugin.run()
```