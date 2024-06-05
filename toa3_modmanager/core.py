from .logger import get_logger
from .utils import create_directory

logger = get_logger(__name__)

class Core:
    def setup_environment(self, base_path):
        create_directory(base_path)
        logger.info(f"Environment setup at {base_path}")
        
