from browser_extension.core.downloader import Downloader
import urllib.parse as urlparse


class ChromeExtension:
    netloc = "chrome.google.com"
    base_url = "https://clients2.google.com/service/update2/crx"

    def __init__(self, extension_url, chrome_version="105.0.5195"):
        self.extension_url = extension_url  # chrome store url
        self.parsed_url = None
        self.extension_name = None
        self.extension_id = None
        self.chrome_version = chrome_version

    def parse(self):
        try:
            self.parsed_url = urlparse.urlparse(self.extension_url)
            *_, self.extension_name, self.extension_id = self.parsed_url.path.split("/")
        except ValueError:
            raise ValueError("Not a valid URL %s" % self.extension_url)

        return self

    @property
    def params(self):
        params = {
            "response": "redirect",
            "prodversion": self.chrome_version,
            "acceptformat": "crx2,crx3".encode('ascii'),
            "x": f"id={self.extension_id}&uc",
            # "x": {
            #     "id": self.extension_id,
            #     "uc": None
            # }
        }
        return params

    @property
    def file_name(self):
        return f'{self.extension_name}-{self.chrome_version}.crx'

    # @property
    # def path(self):
    #     return f'{DOWNLOAD_PATH}/{self.file_name}'

    def download(self):
        self.parse()
        self.check()
        path = Downloader(self.base_url, self.file_name, self.params).download()
        return path

    def check(self):
        if not self.parsed_url:
            raise ValueError(f"Url not parsed. Please call parse() method first.")

        if self.parsed_url.netloc != self.netloc:
            raise ValueError("Not a valid URL %s" % self.extension_url)
