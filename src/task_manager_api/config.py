from pydantic_settings import BaseSettings, SettingsConfigDict 
from pydantic import Field, PostgresDsn
from dotenv import find_dotenv


class Settings(BaseSettings):
    migration_db_url: PostgresDsn = Field(validation_alias="MIGRATION_DATABASE_URL")
    app_db_url: PostgresDsn = Field(validation_alias="APPLICATION_DATABASE_URL")

    model_config = SettingsConfigDict(env_file=find_dotenv(".env"))

settings = Settings()
