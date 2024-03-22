from fastapi import FastAPI
from services.tunnels.list_routes import fetch_list_routes
from services.tunnels.get_tunnel import fetch_tunnel
from services.tunnels.list_connections import fetch_list_connections
from services.tunnels.list_config import fetch_list_config
from services.tunnels.get_connector import fetch_connector

app = FastAPI(
    title="Health Check Service",
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}


# Tunnels
@app.get("/tunnels")
async def tunnels():
    tuns = await fetch_list_routes()
    return tuns

@app.get("/tunnel/{tunnel_id}")
async def tunnel_id(tunnel_id: str):
    tunnel = await fetch_tunnel(tunnel_id)
    return tunnel

@app.get("/tunnel/{tunnel_id}/connections")
async def connections(tunnel_id: str):
    conns = await fetch_list_connections(tunnel_id)
    return conns

@app.get("/tunnel/{tunnel_id}/config")
async def config(tunnel_id: str):
    configs = await fetch_list_config(tunnel_id)
    return configs

@app.get("/tunnel/{tunnel_id}/connections/{connector_id}")
async def connector(tunnel_id: str, connector_id: str):
    connector = await fetch_connector(tunnel_id, connector_id)
    return connector