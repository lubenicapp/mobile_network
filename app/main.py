from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def say_hello(q: str = None):
    return {"pong": q}
