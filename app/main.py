import logging

from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY, HTTP_400_BAD_REQUEST

from .network_coverage import NetworkCoverage

logging.basicConfig(level=logging.INFO)
app = FastAPI()


@app.get("/")
async def get_coverage(q: str = None):
    """
    :param str q: string address for a location in France

    This endpoint returns a json formatted like :
    { "orange": {"2G": true, "3G": false, "4G": true} ... }
    """
    if not q:
        raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="No query provided")

    try:
        coverage = NetworkCoverage(address=q).coverage
        return coverage
    except Exception as e:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=str(e))
