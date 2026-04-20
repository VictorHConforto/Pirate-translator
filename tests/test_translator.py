from pirate_translator.translator import PIRATE_DICTIONARY, translate


def test_translate_basic_word():
    assert "marujo" in translate("amigo", add_interjections=False)


def test_translate_preserves_case_capitalized():
    out = translate("Amigo", add_interjections=False)
    assert out == "Marujo"


def test_translate_preserves_case_upper():
    out = translate("AMIGO", add_interjections=False)
    assert out == "MARUJO"


def test_translate_sentence_keeps_punctuation():
    out = translate("Olá, amigo!", add_interjections=False)
    assert out == "Ahoy, marujo!"


def test_translate_unknown_word_is_kept():
    out = translate("xyz123", add_interjections=False)
    assert out == "xyz123"


def test_translate_adds_interjections_with_seed():
    out = translate("amigo", seed=0)
    # Com seed fixo, o resultado é estável e contém a palavra traduzida.
    assert "marujo" in out.lower()
    assert out != "marujo"  # deve ter ganho prefixo/sufixo
    assert out.split()[0].endswith("!")


def test_translate_empty_string_returns_empty():
    assert translate("", add_interjections=True) == ""


def test_translate_accepts_accented_words():
    out = translate("não", add_interjections=False)
    assert out == "nunca"


def test_translate_rejects_non_string():
    import pytest

    with pytest.raises(TypeError):
        translate(123)  # type: ignore[arg-type]


def test_dictionary_values_are_lowercase():
    for key, value in PIRATE_DICTIONARY.items():
        assert key == key.lower(), f"key {key!r} deve estar em minúsculas"
        assert value == value.lower(), f"valor {value!r} deve estar em minúsculas"
