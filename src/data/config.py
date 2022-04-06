import asyncio
import os

from dotenv import load_dotenv

from utils.db_api.sqlalchemy_commnds import select_admins

load_dotenv()
BOT_TOKEN = os.environ.get('BOT_TOKEN')

SUPERUSER = os.environ.get('SUPERUSER')

PG_USER = os.environ.get('PG_USER')
PG_PASSWORD = os.environ.get('PG_PASSWORD')
DATABASE = os.environ.get('DATABASE')
ip = os.environ.get('IP')

POSTGRES_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{ip}/{DATABASE}"

# TODO Пока есть проблема. При добавлении юзера в список админов в БД, бот в дальнейшем
#  не видет его в числе админов, пока не будет перезапущет бот и не выполниться запрос в БД

# Получение списка администраторов из .env
# ADMINS_ID = os.environ.get('ADMINS_ID').split(',')

# Получение списка админов из БД
ADMINS_ID = select_admins()
