import requests
import json
import datetime
from .config import DATADOG_URL, DATADOG_API_KEY, DATADOG_APP_KEY


def search_metrics_list(query):
    search_query = f"/v1/search?q={query}"
    url = f"{DATADOG_URL}{search_query}"
    headers = {
        "Accept": "application/json",
        "DD-API-KEY": DATADOG_API_KEY,
        "DD-APPLICATION-KEY": DATADOG_APP_KEY,
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return None

    return response.json()


def get_time_series(aggregation, metric, limit=100, seconds_back=3600, interval_ms=5000):
    url = f"{DATADOG_URL}/v2/query/timeseries"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "DD-API-KEY": DATADOG_API_KEY,
        "DD-APPLICATION-KEY": DATADOG_APP_KEY,
    }

    now = datetime.datetime.now()
    to_ms = int(now.timestamp() * 1000)
    from_ms = to_ms - (seconds_back * 1000)

    data = {
        "data": {
            "attributes": {
                "formulas": [
                    {
                        "formula": "a",
                        "limit": {
                            "count": limit,
                            "order": "desc"
                        }
                    }
                ],
                "from": from_ms,
                "interval": interval_ms,
                "queries": [
                    {
                        "data_source": "metrics",
                        "query": f"{aggregation}:{metric}{{*}}",
                        "name": "a"
                    }
                ],
                "to": to_ms
            },
            "type": "timeseries_request"
        }
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return None

    return response.json()

