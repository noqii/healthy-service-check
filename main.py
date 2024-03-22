from config.config import load_config
from http_client.http import HttpClient
from fastapi import FastAPI

config = load_config()
http = HttpClient(config['cloudflare']['url'], {
    'X-Auth-Key': config['cloudflare']['key'],
    'X-Auth-Email': config['cloudflare']['email']
})
app = FastAPI()

# TODO: I'll complete this

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q):
    return {"item_id": item_id, "q": q}