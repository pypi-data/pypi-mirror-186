from typing import Optional

from sqlalchemy.exc import OperationalError


class AgentSetupException(Exception):
    pass


class DatabaseConnectionError(Exception):
    underlying_sqlalchemy_op_ex: OperationalError
    username: Optional[str]

    def __init__(self, cause: OperationalError, username: Optional[str]):
        self.underlying_sqlalchemy_op_ex = cause
        self.username = username
