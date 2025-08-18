from pydantic_settings import SettingsConfigDict, BaseSettings

class Settings(BaseSettings):
    DEBUG: bool = False

    # Valor por defecto a SQLite, se puede sobreescribir con variable de entorno
    SQLALCHEMY_DB_URL: str = "sqlite:///dev.db" #"postgresql+psycopg2://user:pass@127.0.0.1:5432/db_name"

    DB_POSTGRES_HOST: str = ""
    DB_POSTGRES_PORT: int = 5432
    DB_POSTGRES_NAME: str = ""
    DB_POSTGRES_USER: str = ""
    DB_POSTGRES_PASS: str = ""

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()