# API de carteira de criptoativos

Projeto de estudo em Python que disponibiliza uma API REST com FastAPI para cadastrar ativos, listar a carteira e consultar um resumo do investimento. O resumo compara o valor investido com as cotações consultadas no CoinGecko e apresenta lucro ou prejuízo e variação percentual.

## Endpoints

- `POST /ativos/`: cadastra um ativo com `nome`, `ticker`, `quantidade` e `preco_compra`.
- `GET /ativos/`: lista os ativos cadastrados.
- `GET /carteira/consolidado/`: retorna o total investido, o valor de mercado, o resultado e as cotações utilizadas.

Os dados são mantidos apenas em memória e são perdidos quando a aplicação é reiniciada. As cotações são solicitadas ao CoinGecko em USD.

## Como executar

Com Python 3.9 ou superior:

```powershell
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

Depois, acesse `http://127.0.0.1:8000/docs` para explorar e testar a API.
