import requests
from typing import Dict, List

class CoinGeckoClient:
    def __init__(self):
        self.base_url = "https://api.coingecko.com/api/v3"

        self._ticker_map ={
            "BTC": "bitcoin",
            "ETH": "etherium",
            "SOL": "solana",
            "ADA": "cardano"
        }

    def obter_precos_reais(self, tickers: List[str]) -> Dict[str, float]:

        gecko_ids = [self._ticker_map[t] for t in tickers if t in self._ticker_map]

        if not gecko_ids:
            return {}

        parametros = {
            "ids": ",".join(gecko_ids),
            "vs_currencies": "usd"
        }

        try:
            response = requests.get(f"{self.base_url}/simple/price", params=parametros, timeout=10)
            response.raise_for_status()
            dados = response.json()

            conversao_precos = {}
            for ticker, gecko_ids in self._ticker_map.items():
                if gecko_ids in dados:
                    conversao_precos[ticker] = dados[gecko_ids]["usd"]
            return conversao_precos

        except requests.RequestException as e:
            print(f"Erro ao conectar com a API do CoinGecko: {e}")
            return {}
        