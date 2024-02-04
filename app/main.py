from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY, HTTP_406_NOT_ACCEPTABLE

from .network_coverage import NetworkCoverage
from .government_locator import LocatorError

app = FastAPI()


@app.get("/")
async def say_hello(q: str = None):
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
    except LocatorError as e:
        raise HTTPException(
            status_code=HTTP_406_NOT_ACCEPTABLE, detail=str(e)
        )
