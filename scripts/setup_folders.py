import os
from toa3_modmanager.utils import create_directory
from toa3_modmanager.logger import get_logger

logger = get_logger(__name__)

def setup_env(base_path):
    modpacks_path = os.path.join(base_path, 'modpacks')
    create_directory(modpacks_path)
    print(f'Created modpacks folder at {modpacks_path}')
    logger.info(f'Created modpacks folder at {modpacks_path}')
    
if __name__ == '__main__':
    base_path = input('Enter the Stardew Valley game path: ')
    setup_env(base_path)