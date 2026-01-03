import json
import requests
from typing import Dict, Any

BASE_URL = 'https://dummyjson.com/products'

def fetch_products(limit: int = 10, skip: int = 10) -> Dict[str, Any]:

    params = {
        'limit': limit,
        'skip': skip
    }

    r = requests.get(BASE_URL,params=params)
    r.raise_for_status() 

    return r.json()

if __name__ == '__main__':
    data = fetch_products(1,0)
    print(json.dumps(data['products'],indent = 4))