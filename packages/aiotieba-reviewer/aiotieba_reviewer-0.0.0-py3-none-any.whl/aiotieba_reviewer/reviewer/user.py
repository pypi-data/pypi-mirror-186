from typing import Optional

from .._typing import TypeObj
from ..classdef import Punish
from ..client import get_db
from ..enum import Ops


def user_checker(func):
    """
    装饰器: 检查发帖用户的黑白名单状态

    发现黑名单用户则删帖并封十天
    """

    async def _(obj: TypeObj) -> Optional[Punish]:
        db = await get_db()
        permission = await db.get_user_id(obj.user.user_id)
        if permission <= -5:
            return Punish(obj, Ops.DELETE, 10, "黑名单")
        if permission >= 1:
            return Punish(obj, Ops.WHITE)
        return await func(obj)

    return _
