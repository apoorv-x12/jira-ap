from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Environment variables for the application."""
    DATABASE_URL: str
    JWT_SECRET: str
    JWT_REFRESH_SECRET: str
    APP_ENV: str 
    
    class Config:
        env_file = ".env"
        
settings = Settings()