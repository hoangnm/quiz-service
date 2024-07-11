from fastapi import FastAPI, Request
from app.api.main import api_router
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)


app = FastAPI()
app.include_router(api_router)


@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    # This is a simple example of how you can use middleware to authenticate users. We can swap to use jwt decode here
    request.state.user_id = 1
    response = await call_next(request)
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)