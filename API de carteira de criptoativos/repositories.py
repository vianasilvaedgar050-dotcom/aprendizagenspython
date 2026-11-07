from typing import List,Optional
from models import Ativo

class AtivoRepository:
    def __init__(self):
        self._banco_dados: List[Ativo] = []
        self._id_atual = 1

    def salvar(self, ativo: Ativo) -> Ativo:
        ativo.id = self._id_atual
        self._banco_dados.append(ativo)
        self._id_atual += 1
        return ativo
    #aqui eu salvo o ativo e cada id do ativo recebe um valor id mais 1 :)

    def listar_todos(self) -> List[Ativo]:
        return self._banco_dados
    #mostro todos os ativos do banco de dados 

    def buscar_id (self, ativo_id: int) -> Optional[Ativo]:
        for ativo in self._banco_dados:
            if ativo.id == ativo_id:
                return ativo
        return None
    # aqui vou buscar o id se id = id retorna valor, senao nothing :)
    