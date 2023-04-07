from dotenv import load_dotenv
import os

load_dotenv()

DATADOG_URL = os.getenv('DATADOG_URL')
DATADOG_API_KEY = os.getenv('DATADOG_API_KEY')
DATADOG_APP_KEY = os.getenv('DATADOG_APP_KEY')
