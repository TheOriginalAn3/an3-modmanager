from .core import Core
from .manager import ModManager
from .utils import *
from .config import Config
from .logger import setup_logger
from .modpack import ModpackManager
from .nexus_api import NexusAPI

setup_logger()
config = Config()

PROGRAM_NAME = "\033[1;32;40mTheOriginalAn3 Modpack Manager\033[0m"
PROGRAM_VERSION = "\033[0;32;40mV0.1.0\033[0m"
PROGRAM_AUTHOR = "\033[0;33;40mAuthor: TheOriginalAn3\033[0m"