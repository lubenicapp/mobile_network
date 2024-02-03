from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from .network_coverage import NetworkCoverage

app = FastAPI()


@app.get("/")
async def say_hello(q: str = None):
    """
    :param str q: string address for a location in France

    This endpoint returns a json formatted like :
    { "orange": {"2G": true, "3G": false, "4G": true} ... }
    """
    if not q:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="No query provided"
        )
    coverage = NetworkCoverage(address=q).coverage
    return coverage
