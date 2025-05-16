from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        env_file_encoding="utf-8"
    )

    DATABASE_URL: str
    ENVIRONMENT: str = "local"
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Método para verificar se está em produção
    @property
    def is_production(self):
        return self.ENVIRONMENT.lower() == "production"

settings = Settings()