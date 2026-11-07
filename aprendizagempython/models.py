from pydantic import BaseModel
from typing import Optional

class Ativo(BaseModel):
    id: Optional[int] = None
    nome: str
    ticker: str
    quantidade: float
    preco_compra: float

    @property
    def custo_total(self) -> float:
        return self.quantidade * self.preco_compra

    #encapsulamento calculo do custo inicial