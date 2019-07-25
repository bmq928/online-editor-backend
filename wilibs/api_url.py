import os

AUTH_API = 'https://users.i2g.cloud' if os.environ["PYTHON_ENV"] == 'production' else 'http://admin.dev.i2g.cloud' if os.environ["PYTHON_ENV"] == 'dev' else os.environ["USER_RELATED_ROOT_URL"]
ROOT_API = 'https://api-1.i2g.cloud' if os.environ["PYTHON_ENV"] == 'production' else 'http://dev.i2g.cloud' if os.environ["PYTHON_ENV"] == 'dev' else os.environ["PROJECT_RELATED_ROOT_URL"]
EXPORT_PATH = '/app/export' if os.environ["PYTHON_ENV"] == 'production' else '/app/export'
DOWNLOAD_BASE_URL = 'https://python.i2g.cloud' if os.environ["PYTHON_ENV"] == 'production' else 'http://python.dev.i2g.cloud' if os.environ["PYTHON_ENV"] == 'dev' else os.environ["PYTHON_DOWNLOAD_BASE_URL"]
