from asyncpg import UniqueViolationError

from data.config import ADMINS_ID
from utils.db_api.db_gino import db
from utils.db_api.schemas.user import User


async def add_user(telegram_id: int, first_name: str = None, username: str = None, email: str = None):
    try:
        user = User(telegram_id=telegram_id, first_name=first_name, username=username, email=email, is_admin=True)
        await user.create()
        ADMINS_ID.append(telegram_id)
    except UniqueViolationError:
        pass


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def select_user(id: int):
    user = await User.query.where(User.id == id).gino.first()
    return user


async def count_users():
    total = await db.func.count(User.id).gino.scalar()
    return total


async def update_user_permissions(telegram_id: int):
    user = await User.query.where(User.telegram_id == telegram_id).gino.first()
    await user.update(is_admin=True).apply()
