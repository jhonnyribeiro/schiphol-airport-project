import os
from dotenv import load_dotenv

load_dotenv()

def get_endpoint(endpoint, endpoint_id=None, params=None):

    headers = {
        "Accept": "application/json",
        "app_id": os.getenv("API_ID"),
        "app_key": os.getenv("API_KEY"),
        "ResourceVersion": "v4"
    }
    print(headers)

if __name__ == "__main__":
    get_endpoint("flights")