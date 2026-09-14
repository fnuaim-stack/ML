"""
Weather Dashboard Configuration

This module contains configuration settings for the weather dashboard.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenWeatherMap API Configuration
OPENWEATHERMAP_API_KEY = os.getenv('OPENWEATHERMAP_API_KEY', 'YOUR_API_KEY_HERE')
OPENWEATHERMAP_BASE_URL = 'https://api.openweathermap.org/data/2.5'

# Weather Units
UNITS = {
    'metric': 'Celsius',
    'imperial': 'Fahrenheit'
}
DEFAULT_UNITS = 'metric'

# Default Cities
DEFAULT_CITIES = ['London', 'New York', 'Tokyo', 'Sydney', 'Paris']

# Cache Settings
CACHE_ENABLED = True
CACHE_EXPIRY = 600  # 10 minutes in seconds

# Display Settings
DISPLAY_TIMEZONE = 'UTC'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

# API Settings
TIMEOUT = 10  # Request timeout in seconds
RETRY_COUNT = 3  # Number of retries on failure

# Forecast Settings
FORECAST_DAYS = 5
FORECAST_INTERVAL = 3  # Hours between forecast points
