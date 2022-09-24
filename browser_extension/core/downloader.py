import requests
import os

from browser_extension.core.constants import HEADERS
from browser_extension.core.config import CHUNK_SIZE
from browser_extension.core.config import DOWNLOAD_PATH


class Downloader:
    def __init__(self, url, file_name, params=None, folder_path=DOWNLOAD_PATH, headers=HEADERS):
        self.url = url

        self.folder_path = folder_path
        self.file_name = file_name
        self.path = f'{self.folder_path}/{self.file_name}'

        self.headers = headers
        self.params = params or {}

        self._make_dir()

    def download(self):
        r = requests.get(self.url, headers=self.headers, params=self.params, stream=True)
        self.check(r)
        print(r.url)
        content_length = int(r.headers.get("content-length", 0))  # byte
        print(f"Downloading {self.file_name}. File Size {content_length}")

        # todo: add progress bar
        # todo: add permission check
        with open(self.path, 'wb') as file:
            for chunk in r.iter_content(CHUNK_SIZE):
                file.write(chunk)
        return self.path

    def check(self, r):
        if r.status_code != 200:
            raise ValueError(f"Error in downloading {r.url}, {r.status_code}")

        content_length = int(r.headers.get("content-length", 0))  # byte
        if not content_length:
            raise ValueError(f"Error in downloading {r.url}, content is empty")

    def _make_dir(self):
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)
