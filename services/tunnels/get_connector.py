from services import http_cf_service, loaded_config

async def fetch_connector(tunnel_id: str, connector_id: str):
    await http_cf_service.start_request()

    # Variables
    account_id = loaded_config['cloudflare']['account_id']

    response = await http_cf_service.session.get('/client/v4/accounts/' + account_id + '/cfd_tunnel/' + tunnel_id + '/connectors/' + connector_id)
    json = await response.json()

    await http_cf_service.close_request()
    return json['result']
