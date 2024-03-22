from config.load import loaded_config
from http_client.http import HttpClient

http_cf_service = HttpClient(
    base_url=loaded_config['cloudflare']['url'],
    headers={
        'X-Auth-Email': loaded_config['cloudflare']['email'],
        'X-Auth-Key': loaded_config['cloudflare']['key']
    }
)

http_cf_team_service = HttpClient(
    base_url='https://api.teams.cloudflare.com',
    headers={
        'X-Auth-Email': loaded_config['cloudflare']['email'],
        'X-Auth-Key': loaded_config['cloudflare']['key']
    }
)
