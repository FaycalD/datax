```python
import os
import json

class ConfigLoader:
    def __init__(self, config_path='config.json'):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                config = json.load(f)
        else:
            config = self.load_env_vars()
        return config

    def load_env_vars(self):
        config = {
            'O365_API_KEY': os.getenv('O365_API_KEY'),
            'JIRA_API_KEY': os.getenv('JIRA_API_KEY'),
            'NOTION_API_KEY': os.getenv('NOTION_API_KEY'),
            # Add more as needed
        }
        return config

    def get(self, key, default=None):
        return self.config.get(key, default)
```