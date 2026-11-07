
from typing import Dict
from repositories import AtivoRepository
from clients import CoinGeckoClient

class CarteiraService:
    def __init__(self, repository: AtivoRepository, api_client: CoinGeckoClient):
        self.repo = repository
        self.api_client = api_client

    def calcular_lucro_carteira(self) -> dict:
        ativos = self.repo.listar_todos()
        
        tickers_usuario = list(set(ativo.ticker for ativo in ativos))
        
        precos_reais = self.api_client.obter_precos_reais(tickers_usuario)
        
        valor_investido = 0.0
        valor_atual = 0.0

        for ativo in ativos:
            valor_investido += ativo.custo_total
            
            preco_mercado = precos_reais.get(ativo.ticker, ativo.preco_compra)
            valor_atual += ativo.quantidade * preco_mercado

        lucro_absoluto = valor_atual - valor_investido
        variacao_percentual = (lucro_absoluto / valor_investido * 100) if valor_investido > 0 else 0

        return {
            "total_investido": round(valor_investido, 2),
            "valor_atual_mercado": round(valor_atual, 2),
            "lucro_prejuizo": round(lucro_absoluto, 2),
            "variacao_percentual": f"{round(variacao_percentual, 2)}%",
            "precos_utilizados": precos_reais 
        }
