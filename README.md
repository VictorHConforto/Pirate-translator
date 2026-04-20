# Pirate Translator 🏴‍☠️

Tradutor que converte textos em **português (PT-BR)** para **piratês**. Arrr!

Inclui:
- Biblioteca Python (`pirate_translator.translate`)
- CLI (`python -m pirate_translator`)
- API HTTP com FastAPI (`POST /translate`)
- Imagem Docker pronta para rodar

## Requisitos

- Python 3.10+ **ou** Docker

## Rodando com Docker (recomendado)

```bash
docker compose up --build
```

A API ficará disponível em <http://localhost:8000>.

- Documentação interativa: <http://localhost:8000/docs>
- Healthcheck: <http://localhost:8000/health>

Teste rápido:

```bash
curl -X POST http://localhost:8000/translate \
  -H "Content-Type: application/json" \
  -d '{"text": "Olá amigo, vamos ao bar!"}'
```

Resposta (exemplo):

```json
{
  "original": "Olá amigo, vamos ao bar!",
  "translated": "Arrr! Ahoy marujo, zarpamos ao taverna! Yo-ho-ho!"
}
```

## Rodando localmente (sem Docker)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

### CLI

```bash
python -m pirate_translator "Olá amigo, vamos ao bar"
echo "bom dia, chefe" | python -m pirate_translator --no-interjections
```

### API

```bash
uvicorn pirate_translator.api:app --reload
```

## Testes

```bash
pip install -e ".[dev]"
pytest
```

## Estrutura

```
src/pirate_translator/
├── __init__.py
├── __main__.py       # CLI
├── api.py            # FastAPI app
└── translator.py     # Lógica de tradução
tests/                # Testes pytest
Dockerfile
docker-compose.yml
pyproject.toml
```

## Como funciona

O tradutor usa um dicionário de substituição palavra-a-palavra (ex.: `amigo → marujo`, `dinheiro → ouro`, `sim → arrr sim`), preservando capitalização e pontuação. Também adiciona interjeições típicas como *"Arrr!"*, *"Ahoy!"* e *"Yo-ho-ho!"* no início e no fim do texto.

Veja os termos suportados chamando `GET /terms` ou `pirate_translator.available_terms()`.
