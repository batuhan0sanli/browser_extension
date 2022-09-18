import os
import sys

ROOT_FOLDER_NAME = ".browext"

PROJECT_ROOT_PATH = os.path.join(sys.path[0], ROOT_FOLDER_NAME)
HOME_ROOT_PATH = os.path.join(os.path.expanduser("~"), ROOT_FOLDER_NAME)

USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"

HEADERS = {
    "User-Agent": USER_AGENT
}
