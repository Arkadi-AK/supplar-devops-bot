from sqlalchemy import Column, String, BigInteger, sql, Boolean

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    first_name = Column(String(150))
    username = Column(String(150))
    email = Column(String(100))
    telegram_id = Column(BigInteger(), unique=True)
    is_admin = Column(Boolean(), default=False)
    referral = Column(BigInteger)

    query: sql.Select
