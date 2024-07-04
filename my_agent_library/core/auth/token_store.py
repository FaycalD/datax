```python
import os
import json
from cryptography.fernet import Fernet

class TokenStore:
    def __init__(self, store_path):
        self.store_path = store_path
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def store_token(self, service_name, token):
        try:
            if os.path.exists(self.store_path):
                with open(self.store_path, 'r') as f:
                    tokens = json.load(f)
            else:
                tokens = {}

            encrypted_token = self.cipher_suite.encrypt(token.encode())
            tokens[service_name] = encrypted_token.decode()

            with open(self.store_path, 'w') as f:
                json.dump(tokens, f)

        except Exception as e:
            print(f"Failed to store token: {str(e)}")

    def retrieve_token(self, service_name):
        try:
            with open(self.store_path, 'r') as f:
                tokens = json.load(f)

            if service_name in tokens:
                encrypted_token = tokens[service_name]
                token = self.cipher_suite.decrypt(encrypted_token.encode())
                return token.decode()

        except Exception as e:
            print(f"Failed to retrieve token: {str(e)}")

        return None
```