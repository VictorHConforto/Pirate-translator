"""Lógica de tradução de PT-BR para piratês.

A tradução é feita por substituição palavra-a-palavra, preservando
capitalização e pontuação. Também adiciona interjeições típicas
("Arrr!", "Ahoy!") ao início e ao fim do texto.
"""

from __future__ import annotations

import random
import re
from typing import Iterable

# Dicionário de substituições: chave em minúsculas, valor em minúsculas.
# A capitalização do texto original é preservada automaticamente.
PIRATE_DICTIONARY: dict[str, str] = {
    # pronomes / saudações
    "olá": "ahoy",
    "ola": "ahoy",
    "oi": "ahoy",
    "eai": "ahoy",
    "tchau": "até a próxima maré",
    "adeus": "até a próxima maré",
    # pessoas
    "amigo": "marujo",
    "amiga": "maruja",
    "amigos": "marujos",
    "amigas": "marujas",
    "pessoal": "tripulação",
    "galera": "tripulação",
    "time": "tripulação",
    "equipe": "tripulação",
    "chefe": "capitão",
    "patrão": "capitão",
    "patrao": "capitão",
    "gerente": "capitão",
    "homem": "marujo",
    "mulher": "maruja",
    "senhor": "capitão",
    "senhora": "capitã",
    "inimigo": "traidor",
    "inimigos": "traidores",
    # lugares
    "cidade": "porto",
    "casa": "navio",
    "escritório": "navio",
    "escritorio": "navio",
    "bar": "taverna",
    "restaurante": "taverna",
    "banheiro": "porão",
    "banco": "baú do tesouro",
    # coisas
    "dinheiro": "ouro",
    "moeda": "dobrão",
    "moedas": "dobrões",
    "celular": "luneta",
    "telefone": "luneta",
    "computador": "mapa encantado",
    "carro": "carruagem",
    "barco": "navio",
    "navio": "galeão",
    "comida": "rancho",
    "bebida": "rum",
    "água": "rum",
    "agua": "rum",
    "cerveja": "rum",
    "café": "rum",
    "cafe": "rum",
    "tesouro": "ouro pirata",
    # verbos comuns
    "ir": "zarpar",
    "vou": "zarpo",
    "vai": "zarpa",
    "vamos": "zarpamos",
    "correr": "velejar",
    "chegar": "atracar",
    "chegou": "atracou",
    "trabalhar": "remar",
    "trabalho": "remo",
    "falar": "bradar",
    "falou": "bradou",
    "dizer": "bradar",
    "disse": "bradou",
    "comer": "devorar",
    "beber": "virar um copo",
    "roubar": "saquear",
    "pegar": "abordar",
    "perder": "afundar",
    "ganhar": "saquear",
    # afirmações / negações
    "sim": "arrr sim",
    "não": "nunca",
    "nao": "nunca",
    "claro": "com certeza, arrr",
    # adjetivos
    "legal": "digno de um capitão",
    "massa": "digno de um capitão",
    "ótimo": "glorioso",
    "otimo": "glorioso",
    "bom": "digno",
    "ruim": "amaldiçoado",
    "péssimo": "amaldiçoado",
    "pessimo": "amaldiçoado",
    "rápido": "veloz como o vento",
    "rapido": "veloz como o vento",
    "lento": "arrastado como lesma",
    "rico": "cheio de ouro",
    "pobre": "sem um dobrão",
    "bravo": "destemido",
    "medroso": "covarde mastro-oco",
    # exclamações
    "uau": "arrr",
    "caramba": "raios e trovões",
    "nossa": "por todos os mares",
    "cara": "marujo",
    # tempo
    "hoje": "nesta maré",
    "amanhã": "na próxima maré",
    "amanha": "na próxima maré",
    "ontem": "na maré passada",
}

INTERJECTIONS_PREFIX: tuple[str, ...] = ("Arrr!", "Ahoy!", "Yarrr!")
INTERJECTIONS_SUFFIX: tuple[str, ...] = (
    "Arrr!",
    "Yo-ho-ho!",
    "Que os ventos te guiem!",
    "Pelos sete mares!",
)

_WORD_RE = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ]+")


def _match_case(original: str, replacement: str) -> str:
    """Ajusta a capitalização de ``replacement`` para imitar ``original``."""
    if original.isupper() and len(original) > 1:
        return replacement.upper()
    if original[:1].isupper():
        return replacement[:1].upper() + replacement[1:]
    return replacement


def _translate_word(word: str) -> str:
    """Traduz uma única palavra, mantendo a capitalização."""
    key = word.lower()
    if key in PIRATE_DICTIONARY:
        return _match_case(word, PIRATE_DICTIONARY[key])
    return word


def _translate_text(text: str) -> str:
    """Substitui palavras do texto usando o dicionário pirata."""
    return _WORD_RE.sub(lambda m: _translate_word(m.group(0)), text)


def translate(
    text: str,
    *,
    add_interjections: bool = True,
    seed: int | None = None,
) -> str:
    """Traduz ``text`` de PT-BR para piratês.

    Args:
        text: Texto de entrada em português.
        add_interjections: Se ``True``, adiciona interjeições típicas de pirata
            no início e no fim do texto.
        seed: Opcional. Torna a escolha de interjeições determinística, útil
            para testes.

    Returns:
        Texto traduzido para piratês.
    """
    if not isinstance(text, str):
        raise TypeError("text deve ser uma string")

    translated = _translate_text(text)

    if not add_interjections or not translated.strip():
        return translated

    rng = random.Random(seed)
    prefix = rng.choice(INTERJECTIONS_PREFIX)
    suffix = rng.choice(INTERJECTIONS_SUFFIX)
    return f"{prefix} {translated.strip()} {suffix}"


def available_terms() -> Iterable[str]:
    """Retorna os termos conhecidos pelo tradutor (útil para debug/docs)."""
    return sorted(PIRATE_DICTIONARY.keys())
