"""API HTTP para o tradutor pirata, baseada em FastAPI."""

from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel, Field

from pirate_translator import __version__
from pirate_translator.translator import available_terms, translate


class TranslateRequest(BaseModel):
    text: str = Field(..., description="Texto em português a ser traduzido.")
    add_interjections: bool = Field(
        True,
        description="Se deve adicionar interjeições piratas antes e depois do texto.",
    )
    seed: int | None = Field(
        None,
        description="Seed opcional para tornar as interjeições determinísticas.",
    )


class TranslateResponse(BaseModel):
    original: str
    translated: str


app = FastAPI(
    title="Pirate Translator",
    description="Traduz texto em português para piratês. Arrr!",
    version=__version__,
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "version": __version__}


@app.get("/terms")
def terms() -> dict[str, list[str]]:
    return {"terms": list(available_terms())}


@app.post("/translate", response_model=TranslateResponse)
def translate_endpoint(req: TranslateRequest) -> TranslateResponse:
    translated = translate(
        req.text,
        add_interjections=req.add_interjections,
        seed=req.seed,
    )
    return TranslateResponse(original=req.text, translated=translated)


@app.get("/")
def root() -> dict[str, str]:
    return {
        "message": "Ahoy! Envie POST /translate com {\"text\": \"...\"} para traduzir.",
        "docs": "/docs",
    }
