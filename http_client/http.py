from aiohttp import ClientSession, CookieJar, TraceConfig
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

    def start_request(self):
        self.session = ClientSession(
            self.base_url,
            headers=self.heads,
            cookie_jar=self.cookie_jar
        )

    def close_request(self):
        if self.session != None:
            self.session.close()

    async def _on_request_start(self, session: ClientSession, trace_config, params):
        print(params, trace_config)