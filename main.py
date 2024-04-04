from fastapi import FastAPI
from contextlib import asynccontextmanager

from settings import setting


@asynccontextmanager
async def project_lifespan(app: FastAPI):
    yield


app = FastAPI(
    title=setting.app_name,
    debug=setting.debug,
    summary=setting.summary,
    description=setting.description,
    
    docs_url=setting.docs_url,
    openapi_url=setting.openapi_url,
    
    lifespan=project_lifespan,
)
