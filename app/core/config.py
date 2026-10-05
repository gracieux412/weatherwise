from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Application
    app_name: str = "WeatherWise API"
    app_version: str = "1.0.0"
    app_env: str = "development"
    api_v1_prefix: str = "/api/v1"

    # External API
    open_meteo_base_url: str = "https://api.open-meteo.com/v1"

    # Machine learning
    model_path: str = "app/ml/models/weather_model.joblib"

    # HTTP configuration
    request_timeout: float = 10.0

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()