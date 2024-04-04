from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSetting(BaseSettings):
    USER: str
    PASSWORD: str
    HOST: str
    NAME: str
    PORT: str
    
    @property
    def dsn(self) -> str:
        return \
            f"postgresql+aiopg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.NAME}"

    model_config = SettingsConfigDict(env_file=".env")



class Setting(BaseSettings):
    app_name: str = "My Library API"
    debug: bool = True
    description: str = "Easy and Fast api to control library"
    summary: str = "Easy api to library"
    
    db: DatabaseSetting = DatabaseSetting()
    
    docs_url: str = "/api/docs"
    openapi_url: str = "/api/openapi.json"


setting = Setting()
