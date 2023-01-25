from fastapi import FastAPI
import uvicorn
from mylib.logic import wiki as wikilogic
from mylib.logic import search_wiki
from mylib.logic import phrases as wikiphrases


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wikipedia API. Call /search or /wiki"}


@app.get("/search/{name}")
async def search(name: str):
    """Page to search in Wikipedia"""

    result = search_wiki(name)
    return {"result": result}


@app.get("/wiki/{name}")
async def wiki(name: str):
    """Retrieve Wikipedia Page"""

    result = wikilogic(name)
    return {"result": result}


@app.get("/phrases/{name}")
async def phrases(name: str):
    """Retrieve Wikipedia page and return Phrases"""

    result = wikiphrases(name)
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
