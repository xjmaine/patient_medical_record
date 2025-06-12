from pydantic_settings import BaseSettings
from pathlib import Path
from typing import Optional

class EmailConfig(BaseSettings):
    """
    Email configuration loaded from environment variables
    """
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int = 587
    MAIL_SERVER: str = "smtp.gmail.com"
    MAIL_STARTTLS: bool = True
    MAIL_SSL_TLS: bool = False
    TEMPLATE_FOLDER: Path = Path(__file__).parent.parent.parent / "templates"
    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS: bool = True

    class Config:
        env_file = Path(__file__).parent.parent.parent / ".env"
        env_file_encoding = 'utf-8'

# singleton instance
email_config = EmailConfig()