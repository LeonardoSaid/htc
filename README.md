# Hash Tech Challenge - Backend

Repositório dedicado à resolução do desafio: [https://github.com/hashlab/hiring/tree/master/challenges/pt-br/new-backend-challenge](https://github.com/hashlab/hiring/tree/master/challenges/pt-br/new-backend-challenge)

O arquivo `swagger.yaml` presente na raiz do projeto descreve a API desenvolvida no formato OpenAPI Specification.

## **Requisitos**

- [Docker](https://docs.docker.com/install/)
- [Docker-compose](https://docs.docker.com/compose/install/)
- Arquivo .env para configurar as variáveis default do projeto
- Ambiente Unix/Linux-based para utilizar os comandos do Makefile
## Setup

1. Configurar o arquivo .env na raiz do projeto com os valores da porta e host dos serviços descritos no `docker-compose.yml`, exemplo:
```
# Cart Service
CART_SERVICE_HOST=0.0.0.0
CART_SERVICE_PORT=3000

# Discount Service
DISCOUNT_SERVICE_PORT=50051
```

2. Para gerar as imagens dos containers execute o comando do Makefile:
```
make build
```

## Execução
Com as imagens geradas execute o comando:
```
make up
```
Para monitorar os logs:
```
make watch
```

## Exemplo
Com os containers ativos, a API estará disponível para receber requests localmente, um exemplo com curl:
```
curl --location --request POST 'http://localhost:3000/cart-management/v1/cart/checkout' \
--header 'Content-Type: application/json' \
--data-raw '{
    "products": [
        {
            "id": 2,
            "quantity": 5
        },
        {
            "id": 2,
            "quantity": 4
        }
    ]
}'
```

## Comandos úteis

O arquivo Makefile que acompanha o projeto também possui outros comandos úteis para o desenvolvimento e monitoramento da aplicação, como:

- `make stop` - Interrompe a execução de todos os containers ativos
- `make remove-containers` - Interrompe a execução e remove todos os containers ativos
- `make restart` - Reinicia os containers ativos
- `make shell` - Abre um terminal shell dentro do container ativo para execução de comandos
- `make fix` - Executa autopep8 fix para correção de erros de linting
- `make lint` - Aplica o lint no código  com base na configuração do arquivo .pylintrc
- `make test` - Executa os testes unitários e de integração
- `make coverage` - Gera o relatório de code coverage

## **Desenvolvido com**

- `[starlette] (https://www.starlette.io)`
- `[uvicorn] (https://www.uvicorn.org)`
- `[pydantic] (https://pydantic-docs.helpmanual.io)`
- `[grpcio] (https://grpc.io/docs/languages/python/quickstart)`
- `[requests] (https://requests.kennethreitz.org/en/master)`
- `[pytest] (https://docs.pytest.org/en/latest)`
