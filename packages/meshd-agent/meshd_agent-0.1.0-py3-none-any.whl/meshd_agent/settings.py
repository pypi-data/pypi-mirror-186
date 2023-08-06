from __future__ import annotations

import logging
from contextlib import contextmanager
from typing import Generator

from meshd_agent.model import DataBaseUrl
from pydantic import BaseSettings, SecretStr
from requests import Response, Session

MESHD_USER_ID = "MESHD-USER-ID"
MESHD_USER_TOKEN = "MESHD-USER-TOKEN"
HEARTBEAT_TOPIC = "heartbeat"
AGENT_RESPONSE_TOPIC = "results"
AGENT_REQUEST_RECEIVED_TOPIC = "received"
DEFAULT_DF_ORIENT = "list"


class Agent2Settings(BaseSettings):
    #####################
    # Initial DB settings
    #####################
    db_connection_url: DataBaseUrl
    db_connection_nickname: str

    ########################
    # WS connection settings
    ########################
    start_ws_connection = True
    agent_owner_id: str
    agent_owner_token: SecretStr

    ##########################
    # local meshd_agent API settings
    ##########################
    start_local_api = False

    ##########################
    # URL Settings - todo: update to https & wss before release
    ##########################
    server_url = "localhost"
    api_root_path = f"http://{server_url}/rest/v1"
    api_register_source_path = f"{api_root_path}/data_source"

    ws_connect_path = f"ws://{server_url}/ws/v2/connect"

    @property
    def api_headers(self):
        return {
            MESHD_USER_ID: self.agent_owner_id,
            MESHD_USER_TOKEN: self.agent_owner_token.get_secret_value() if self.agent_owner_token else None,
        }

    @contextmanager
    def api_session(self) -> Generator[Session, None, None]:
        session = Session()
        session.headers = self.api_headers

        def print_resp_url(resp: Response, *args, **kwargs):
            logging.info(f"made request ({resp.status_code}) to {resp.url}")

        session.hooks["response"].append(print_resp_url)

        yield session
        session.close()

    class Config:
        env_file = ".meshd_agent.env"
