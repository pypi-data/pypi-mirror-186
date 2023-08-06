import asyncio
import logging
import sys
import time
from asyncio import Queue
from typing import Optional

import pandas as pd
from fastapi_websocket_pubsub import PubSubClient
from meshd_agent.exceptions import DatabaseConnectionError
from meshd_agent.model import (
    DataSourceRegistrationResponse,
    HeartbeatResponse,
    InteractionType,
    IntrospectRequest,
    QueryRequest,
    WsResponse,
    _ConnectedDatabase,
)
from meshd_agent.settings import (
    AGENT_RESPONSE_TOPIC,
    DEFAULT_DF_ORIENT,
    HEARTBEAT_TOPIC,
    Agent2Settings,
)
from meshd_agent.util import parse_data
from requests import HTTPError

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s:%(lineno)d - %(levelname)8s - %(message)s")
log = logging.getLogger(__name__)


class MeshdAgent:
    _background_tasks = set()
    local_queue = Queue()
    _connected_db_namespace = None

    def __init__(self, settings: Optional[Agent2Settings] = None, client: Optional[PubSubClient] = None):
        self.settings = settings if settings else Agent2Settings()  # type: ignore
        self.client = client if client else PubSubClient(extra_headers=self.settings.api_headers)

        # Set up client subscriptions as required
        self._connected_db = self._setup_db_event_subscriptions()
        self.start_time = None

    async def start(self):
        self.start_time = time.perf_counter()
        # start client for websocket events
        self.client.start_client(self.settings.ws_connect_path)
        await self.client.wait_until_ready()
        log.info(f"agent startup complete, awaiting query requests for db id {self._connected_db_namespace}")
        done, pending = await asyncio.wait(
            [self.client.wait_until_done(), self._do_heartbeat_loop()],
            # neither of these will complete unless the process is killed; then the client disconnects semi-gracefully
            return_when=asyncio.FIRST_COMPLETED,
        )
        for task in pending:
            task.cancel()
        await self.client.disconnect()

    async def _do_publish_task(self, topic: list[str], publish_data: WsResponse | HeartbeatResponse):
        task = asyncio.create_task(self.client.publish(topic, publish_data))
        # stops garbage collection of task before completion
        self._background_tasks.add(task)
        task.add_done_callback(self._background_tasks.discard)

    def _setup_db_event_subscriptions(self) -> _ConnectedDatabase:
        try:
            connected_db = self.settings.db_connection_url.to_connected_database(self.settings.db_connection_nickname)
            log.info(f"successfully connected to {connected_db.url_masked()}")
        except DatabaseConnectionError as e:
            log.error("failed to connect to database!")
            raise e

        # Send API Request to register DB against user & store token locally
        with self.settings.api_session() as s:
            log.info(f"Fetching database event topic details {self.settings.api_register_source_path}")
            req_json = {"incoming_source": connected_db.dict(exclude={"database_connection_parameters"})}
            res = s.put(self.settings.api_register_source_path, json=req_json)
            try:
                res.raise_for_status()
            except HTTPError as e:
                log.fatal(f"bad request to registration endpoint: {e.response}")
                log.fatal(f"response json: {res.json()}")
                log.fatal(f"exiting.")
                sys.exit(1)
            json_ = res.json()
            reg_response = DataSourceRegistrationResponse(**json_)

        database_namespace = reg_response.ws_topic_namespace
        self._connected_db_namespace = database_namespace

        query_topic = f"{database_namespace}.{InteractionType.Query.value}"
        introspection_topic = f"{database_namespace}.{InteractionType.Introspection.value}"
        test_topic = f"{database_namespace}.{InteractionType.ConnectionTest.value}"

        self.client.subscribe(query_topic, self.on_trigger_query)  # type: ignore
        self.client.subscribe(introspection_topic, self.on_trigger_introspection)  # type: ignore
        log.info(f"subscribed to topics: {query_topic, introspection_topic, test_topic}")
        return connected_db

    async def _do_heartbeat_loop(self):
        while True:
            await asyncio.gather(asyncio.sleep(60), self._do_heartbeat())

    async def _do_heartbeat(self):
        await self.client.wait_until_ready()
        response = HeartbeatResponse(
            uptime_s=(time.perf_counter() - self.start_time), datasource_id=self._connected_db.oid()
        )
        log.info(f"heartbeat ok, uptime {response.uptime_s:.3f}s")
        await self._do_publish_task([HEARTBEAT_TOPIC], response)

    ##############################
    # ws Callbacks
    ##############################

    async def on_trigger_query(self, data: dict, topic: str, *_args, **_kwargs):
        data: QueryRequest = parse_data(data, QueryRequest)
        log.info(f"Trigger on_trigger_query via topic {topic} was accessed with id={data.interaction_id}")
        if not data.sql:
            log.warning("No SQL was sent through for the query!")
            response_data = {}
        else:
            with self._connected_db.engine().connect() as conn:
                df: pd.DataFrame = pd.read_sql(data.sql, conn)
            response_data = {"query_result": df.to_dict(orient=DEFAULT_DF_ORIENT)}

        response = WsResponse(
            interaction_id=data.interaction_id,
            result_data=response_data,
        )
        log.info("sending query response back")
        await self._do_publish_task([AGENT_RESPONSE_TOPIC], response)

    async def on_trigger_introspection(self, data, topic: str, *_args, **_kwargs):
        data: IntrospectRequest = parse_data(data, IntrospectRequest)
        log.info(f"Trigger on_trigger_query via topic {topic} was accessed with id={data.interaction_id}")
        inspector = self._connected_db.inspector()
        response = WsResponse(interaction_id=data.interaction_id, result_data={"schemas": inspector.get_schema_names()})
        log.info("sending introspection response back")
        log.info(data)
        await self._do_publish_task([AGENT_RESPONSE_TOPIC], response)
