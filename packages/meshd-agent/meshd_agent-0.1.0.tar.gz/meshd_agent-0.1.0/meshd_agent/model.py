from __future__ import annotations

import logging
import uuid
from abc import ABC
from datetime import datetime
from enum import Enum
from typing import Any, Optional, Union
from urllib.parse import quote_plus

from meshd_agent.exceptions import DatabaseConnectionError
from pydantic import AnyUrl, BaseModel
from sqlalchemy import create_engine, exc, inspect
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine.reflection import Inspector

logger = logging.getLogger(__name__)


class DatabaseType(str, Enum):
    Postgres = "postgresql"
    MySQL = "mysql"
    MariaDB = "mariadb"
    Oracle = "oracle"
    MicrosoftSqlServer = "sqlserver"

    @property
    def driver(self):
        # these are the drivers we have selected to run our introspection with
        if self == DatabaseType.Postgres:
            driver = "postgresql+psycopg2"
        elif self == DatabaseType.MySQL or self == DatabaseType.MariaDB:
            driver = "mysql+mysqlconnector"
        elif self == DatabaseType.Oracle:
            driver = "oracle+cx_oracle"
        elif self == DatabaseType.MicrosoftSqlServer:
            driver = "mssql+pyodbc"
        else:
            raise Exception(
                f"Could not identify databases type {self}. "
                f"Must be one of ({', '.join([x for x in DatabaseType])})"
            )
        return driver


class DatabaseConnectionParameters(BaseModel):
    username: Optional[str]
    password: Optional[str]  # todo: change me to use google secrets mgr

    class Config:
        orm_mode = True


class Database(BaseModel):
    """
    Pre Connected Database object that stored metadata bout the object and also utilities for connecting to the database.
    """

    nickname: str

    # the below attributes should be defined uniqueness
    type: DatabaseType
    host: str
    port: Optional[int]
    database_path: Optional[str] = None

    def connect(
        self, database_connection_parameters: DatabaseConnectionParameters
    ) -> "_ConnectedDatabase":
        return _ConnectedDatabase(
            **self.dict(), database_connection_parameters=database_connection_parameters
        )

    def oid(self) -> uuid.UUID:
        # Standardize the object ID with the url as unmasked as possible
        # Note, this is not the same ID as we store in the database;
        # todo: look into that more & make more betterer
        return uuid.uuid5(uuid.NAMESPACE_OID, self.url_unmasked(None, None))

    def url_unmasked(
        self, username: Optional[str] = None, password: Optional[str] = None
    ) -> str:
        _username = quote_plus(username) if username else None
        _password = quote_plus(password) if password else None

        if self.database_path and not self.database_path.startswith("/"):
            path = "/" + self.database_path
        else:
            path = self.database_path

        return DataBaseUrl.build(
            scheme=self.type.driver,
            user=_username,
            password=_password,
            host=self.host,
            port=str(self.port) if self.port else None,
            path=path,
        )


class ColumnInformation(BaseModel):
    """
    Maps to the SQLAlchemy record info
    """

    name: str
    type: str
    nullable: bool
    default: Optional[str] = None
    autoincrement: Optional[Union[str, bool]] = None
    comment: Optional[str] = None
    computed: Optional[dict] = None
    identity: Optional[dict] = None


class _ConnectedDatabase(Database):
    """
    Once connected this class stores utility functions that interact with the database tooling
    do not init directly, use Database class
    """

    database_connection_parameters: DatabaseConnectionParameters

    def __init__(self, **data: Any):
        super().__init__(**data)
        self.validate_connection()

    def validate_connection(self):
        try:
            with self.engine().connect() as _:
                pass  # tests connection to database
        except exc.OperationalError as e:
            logger.info(f"Could not connect to database {e.detail}")
            raise DatabaseConnectionError(
                e, self.database_connection_parameters.username
            )

    def engine(self) -> Engine:
        return create_engine(self.url_unmasked())

    def inspector(self) -> Inspector:
        return inspect(self.engine())

    def url_masked(self) -> str:
        if self.database_connection_parameters.password is not None:
            return str(self.engine().url).replace(
                self.database_connection_parameters.password, "***"
            )
            # return self.url_unmasked().replace(self.database_connection_parameters.password, "***")
        else:
            return str(self.engine().url)

    def url_unmasked(self, *kwargs) -> str:
        return super().url_unmasked(
            self.database_connection_parameters.username,
            self.database_connection_parameters.password,
        )


class DataBaseUrl(AnyUrl):
    allowed_schemes = {d.lower() for d in DatabaseType}

    @property
    def connection_parameters(self):
        return DatabaseConnectionParameters(username=self.user, password=self.password)

    def to_database(self, nickname: str) -> Database:
        return Database(
            nickname=nickname,
            type=DatabaseType(self.scheme),
            host=self.host,
            port=self.port,
            database_path=self.path.replace("/", "", 1) if self.path else None,
        )

    def to_connected_database(self, nickname: str) -> _ConnectedDatabase:
        return self.to_database(nickname).connect(self.connection_parameters)


class DataSourceRegistrationResponse(BaseModel):
    id: uuid.UUID
    # when a Data Source is connected via an meshd_agent we respond with a ws_topic that allows listening to events
    ws_topic_namespace: Optional[uuid.UUID]

    class Config:
        orm_mode = True


class InteractionType(str, Enum):
    ConnectionTest = "connection test"
    Query = "query"
    Introspection = "introspect"


class EventBase(ABC, BaseModel):
    last_update = datetime.now()

    def __setattr__(self, name, value):
        self.last_update = datetime.now()
        super().__setattr__(name, value)


class HeartbeatResponse(EventBase):
    uptime_s: float
    datasource_id: uuid.UUID


class InteractionRequest(EventBase):
    interaction_id: uuid.UUID
    type: InteractionType


class IntrospectRequest(InteractionRequest):
    type = InteractionType.Introspection


class ConnectionTestRequest(InteractionRequest):
    type = InteractionType.ConnectionTest


class QueryRequest(InteractionRequest):
    type = InteractionType.Query
    sql: str | None


class InteractionResponse(EventBase):
    interaction_id: uuid.UUID


# todo: well defined response classes
class WsRequestReceived(InteractionResponse):
    pass


class WsResponse(InteractionResponse):
    result_data: dict | None
