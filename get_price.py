import requests
from typing import Dict, Any, Optional

def get_price(carteira:Dict[str, Any]) -> Optional[Dict[str, Any]]:
    coins = ','.join(carteira.keys())
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': coins,
        'vs_currencies': 'usd'
    }
    try:
        response = requests.get(url, params = params)
        if response.status_code == 200:
            return response.json()
        else:
            print (f"Erro na API: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print (f"Erro ao comunicar com a API: {e}")
        return None