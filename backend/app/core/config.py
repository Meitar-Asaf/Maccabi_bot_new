from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Maccabi Fan Platform API"
    api_prefix: str = "/api"
    environment: str = "development"

    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/maccabi"

    sports_api_base_url: str = "https://example-sports-api.local"
    sports_api_key: str = ""

    highlight_search_delay_seconds: int = 120
    match_poll_interval_seconds: int = 60

    whatsapp_provider: str = "mock"
    whatsapp_access_token: str = ""
    whatsapp_phone_number_id: str = ""
    cors_allowed_origins: str = "http://localhost:5173"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
