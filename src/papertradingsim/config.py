"""Application configuration loaded from environment variables."""

import os

from dotenv import load_dotenv


load_dotenv()


class Config:
    """Default configuration for the paper-trading application."""

    MARKET_API_KEY = os.getenv("MARKET_API_KEY")
    TESTING = False
