from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from .network_coverage import NetworkCoverage

app = FastAPI()


@app.get("/")
async def say_hello(q: str = None):
    if not q:
        raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail='No query provided')
    coverage = NetworkCoverage(address=q).coverage
    return coverage
