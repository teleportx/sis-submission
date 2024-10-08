from os import environ

from dotenv import load_dotenv

load_dotenv()

token = environ.get('TOKEN')
db_url = environ.get('DB_URL')
table_page_url = environ.get('PAGE_URL')
