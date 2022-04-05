import httpx
from fastapi import FastAPI

app = FastAPI()
client = httpx.AsyncClient()


@app.get("/api/ping")
def ping():
    return "pong"


@app.get("/api/jokes")
async def jokes():
    jokes = []
    uri = 'https://api.chucknorris.io/jokes/random'

    while len(jokes) < 15:
        response = await client.get(uri)
        temp = dict(response.json())
        joke = dict(filter(lambda el: el['id'] == temp['id'], jokes))
        if not joke:
            jokes.append(
                {'id': temp['id'], 'icon_url': temp['icon_url'], 'value': temp['value']})
    return jokes
