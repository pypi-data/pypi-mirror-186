import os
import sys
import pkg_resources

from dotenv import load_dotenv

if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
    ENV_FILE_PATH = os.path.abspath(
        os.path.join(
            os.path.split(
                os.path.split(os.path.split(os.path.dirname(__file__))[0])[0]
            )[0],
            ".env",
        )
    )
else:
    ENV_FILE_PATH = pkg_resources.resource_filename("cgc", ".env")

load_dotenv(dotenv_path=ENV_FILE_PATH, verbose=True)

API_HOST = os.getenv("API_HOST")
API_PORT = os.getenv("API_PORT")
API_URL = f"http://{API_HOST}:{API_PORT}"
CGC_SECRET = os.getenv("CGC_SECRET")
CONFIG_FILE_NAME = os.getenv("CONFIG_FILE_NAME")
TMP_DIR = os.getenv("TMP_DIR")
RELEASE = int(os.getenv("RELEASE"))
MAJOR_VERSION = int(os.getenv("MAJOR_VERSION"))
MINOR_VERSION = int(os.getenv("MINOR_VERSION"))
