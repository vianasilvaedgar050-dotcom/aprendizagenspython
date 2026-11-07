from fastapi import FastAPI
from models import Ativo
from repositories import AtivoRepository
from services import CarteiraService
from clients import CoinGeckoClient

app = FastAPI(title = "API de investimento do ed com preços em real time baby")

ativo_repo = AtivoRepository()
gecko_client = CoinGeckoClient()
carteira_service = CarteiraService(ativo_repo, gecko_client)

@app.post("/ativos/", response_model = Ativo, status_code = 201)
def criar_ativo(ativo:Ativo):
    return ativo_repo.salvar(ativo)

@app.get("/ativos/", response_model = list[Ativo])
def listar_ativos():
    return ativo_repo.listar_todos()
@app.get("/carteira/consolidado/")
def obter_resumo_carteira():
    return carteira_service.calcular_lucro_carteira()

