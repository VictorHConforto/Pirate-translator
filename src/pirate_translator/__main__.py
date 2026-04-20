"""Interface de linha de comando do tradutor pirata.

Exemplos:
    echo "Olá amigo, vamos ao bar" | python -m pirate_translator
    python -m pirate_translator "Olá amigo, vamos ao bar"
    python -m pirate_translator --no-interjections "bom dia"
"""

from __future__ import annotations

import argparse
import sys

from pirate_translator import __version__
from pirate_translator.translator import translate


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pirate-translator",
        description="Traduz texto em português para piratês. Arrr!",
    )
    parser.add_argument(
        "text",
        nargs="*",
        help="Texto a ser traduzido. Se omitido, lê da entrada padrão (stdin).",
    )
    parser.add_argument(
        "--no-interjections",
        action="store_true",
        help="Não adiciona 'Arrr!' / 'Ahoy!' antes e depois do texto.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Seed para tornar a escolha de interjeições determinística.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"pirate-translator {__version__}",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.text:
        source = " ".join(args.text)
    else:
        source = sys.stdin.read()

    output = translate(
        source,
        add_interjections=not args.no_interjections,
        seed=args.seed,
    )
    print(output)
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
