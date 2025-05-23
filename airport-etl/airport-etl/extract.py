import os
from dotenv import load_dotenv
from constraints import BASE_URL
import requests

load_dotenv()

def get_endpoint(endpoint, endpoint_id=None, params=None):

    headers = {
        "Accept": "application/json",
        "app_id": os.getenv("API_ID"),
        "app_key": os.getenv("API_KEY"),
        "ResourceVersion": "v4"
    }

    url = BASE_URL + endpoint
    if endpoint_id:
        url = url + "/" + endpoint_id

    result =  requests.get(url=url, headers=headers)
    print(result.json())
    
if __name__ == "__main__":
    get_endpoint("flights")