
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

SEARCH_QUERY = 'quantum neural networks'
API_RESPONSE = 'arxiv_api'
JSON_RAW_RESPONSE = 'arxiv_raw'
AUTHORS_TABLE_NAME = 'arxiv_authors'
LINKS = 'arxiv_links'
CATEGORIES_TABLE_NAME = 'arxiv_categories'
SEARCH_LIMIT = 100

MYSQL_DB_NAME = 'arxiv'
MYSQL_HOST = os.environ.get('MYSQL_HOST')
MYSQL_USER = os.environ.get('MYSQL_ARXIV_USER')
MYSQL_PASSWORD = os.environ.get('MYSQL_ARXIV_PASSWORD')
