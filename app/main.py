from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
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

@app.middleware("http")
async def global_exception_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except HTTPException as http_exception:
        return JSONResponse(
            status_code=http_exception.status_code,
            content={"error": "Client Error", "message": str(http_exception.detail)},
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": "Internal Server Error", "message": "An unexpected error occurred."},
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)