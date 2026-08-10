from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):

    mongo_url: str

    database_name: str

    basic_auth_username: str

    basic_auth_password: str

    class Config:
        env_file = ".env"


settings = Settings()