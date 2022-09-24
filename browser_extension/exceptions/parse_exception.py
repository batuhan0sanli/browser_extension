from browser_extension.exceptions.base import BrowserExtensionError


class ParseException(BrowserExtensionError):
    """Exception raised when parsing fails."""
    def __init__(self):
        super().__init__("Parsing url failed.")