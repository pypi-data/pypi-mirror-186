import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from lnhub_rest.routers import user

root_path = "/" + os.getenv("ROOT_PATH", "")
port = os.getenv("PORT", 8000)


app = FastAPI(openapi_prefix=root_path)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=port, root_path=root_path)
