import os

from dotenv import load_dotenv
from src.core.constants import HOME_ROOT_PATH


def str2bool(value):
    return value.lower() in ['true', '1']


load_dotenv()

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
DOWNLOAD_PATH = os.getenv("DOWNLOAD_PATH", HOME_ROOT_PATH)
