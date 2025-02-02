from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "AFS WMS"
    API_VERSION: str = "1.0"

    class Config:
        env_file = ".env"

settings = Settings()
