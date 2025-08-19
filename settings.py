from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SQLITE_URL: str = "sqlite+aiosqlite:///./temperature.db"
    SQLITE_SYNC_URL: str = "sqlite:///./temperature.db"

    model_config = SettingsConfigDict(case_sensitive=True, env_file=".env")


def get_settings():
    return Settings()
