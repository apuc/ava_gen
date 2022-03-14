import os
from dotenv import load_dotenv
load_dotenv()

MYSQL_CONF = os.getenv('MYSQL')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

ROOT_DIR = os.getcwd()