from fastapi import FastAPI

from .network_coverage import NetworkCoverage

app = FastAPI()


@app.get("/")
async def say_hello(q: str = None):
    coverage = NetworkCoverage(address=q).coverage
    return coverage
