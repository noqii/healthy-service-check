from aiohttp import ClientSession, CookieJar, TraceConfig, TraceRequestStartParams
from logger.logger import create_logger

class HttpClient:
    def __init__(self, base_url: str, headers: dict):
        self.cookie_jar = CookieJar()
        self.trace_config = TraceConfig()
        self.base_url = base_url
        self.heads = headers
        self.session = None

        self.trace_config.on_request_start.append(self._on_request_start)
        self.logger = create_logger("HttpClient", "logs/http_client.log")

    async def start_request(self):
        self.session = ClientSession(
            self.base_url,
            headers=self.heads,
            trace_configs=[self.trace_config],
            cookie_jar=self.cookie_jar
        )

    async def close_request(self):
        if self.session != None:
            await self.session.close()

    async def _on_request_start(self, session: ClientSession, trace_config, params: TraceRequestStartParams):
        self.logger.info(f"Requesting to {params.url} with method {params.method}")