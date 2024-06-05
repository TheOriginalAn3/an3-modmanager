
import logging

def setup_logger():
    logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s : %(message)s')

def get_logger(name):
    return logging.getLogger(name)