from sqlalchemy import create_engine, MetaData, Table, Column
from sqlalchemy import select

engine = create_engine("postgresql+psycopg2://postgres:29111986@localhost/supplar_devops_bot")
engine.connect()

metadata = MetaData()

user = Table('users', metadata,
             Column('id'),
             Column('telegram_id'),
             Column('is_admin'),
             )

conn = engine.connect()


def select_admins():
    s = select([user.c.telegram_id]).where(user.c.is_admin == True)
    r = conn.execute(s).fetchall()
    return [i[0] for i in r]
