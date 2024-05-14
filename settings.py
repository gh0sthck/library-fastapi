from os import getenv
from pydantic_settings import BaseSettings


class DatabaseSetting(BaseSettings):
    USER: str = getenv("DB_USER")
    PASSWORD: str = getenv("DB_PASSWORD")
    HOST: str = getenv("DB_HOST")
    NAME: str = getenv("DB_NAME")
    PORT: int = int(getenv("DB_PORT"))
    
    @property
    def dsn(self) -> str:
        return \
            f"postgresql+asyncpg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.NAME}"


class Setting(BaseSettings):
    app_name: str = "The Library API"
    debug: bool = True
    description: str = "Easy and Fast API to control books and visits.s"
    summary: str = "Api to library"
    
    db: DatabaseSetting = DatabaseSetting()
    
    docs_url: str = "/api/docs"
    openapi_url: str = "/api/openapi.json"


setting = Setting()
