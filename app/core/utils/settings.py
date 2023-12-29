from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import EmailStr, HttpUrl
import os


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=os.path.abspath('.env'), env_file_encoding='utf-8')
    
    # API meta info
    api_name: str
    api_version: str
    api_description: str
    api_terms_of_service: str
    api_company_name: str
    api_prefix: str
    api_company_url: HttpUrl
    api_company_email: EmailStr

    # ACCOUNT API info
    api_entry_point: str
    api_port: int
    api_reload: bool
    api_host: str
    api_lifespan: str

    # DB credentials
    api_db_url: str

    # Cache credentias
    api_redis_host: str
    api_redis_port: int
    api_redis_password: str
    api_redis_decode_response: bool
    api_redis_host_local: str

    # API constants
    min_password_length: int
    password_regex: str

    # API model versions
    account_model_version: int
    
    # Streaming topic
    api_cache_topic: str

    # Event Streaming Server
    api_event_streaming_host: str
    api_event_streaming_client_id: str
    
    # API Externa Url
    api_verify_access_token_url: str
    api_login_for_access_token_url: str

settings = Settings()
