import os

AUTH_API = 'https://users.i2g.cloud' if os.environ["NODE_ENV"] == 'production' else 'https://users.i2g.cloud'
ROOT_API = 'https://api-1.i2g.cloud' if os.environ["NODE_ENV"] == 'production' else 'https://api-1.i2g.cloud'
EXPORT_PATH = '/app/export' if os.environ["NODE_ENV"] == 'production' else '/app/export'
DOWNLOAD_BASE_URL = 'https://python.i2g.cloud' if os.environ["NODE_ENV"] == 'production' else 'https://python.i2g.cloud'
