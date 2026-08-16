"""Integrations- und Kohärenz-Tests für das textutils-Paket (AC-06, AC-08).

Sichert die gemeinsame Paket-Schnittstelle des Sprints ab: alle fünf Namen
werden vom Paket re-exportiert, jede Funktion hat die vereinbarte Signatur
und lehnt Nicht-String-Argumente einheitlich mit ``TypeError`` ab.
"""

import pytest

import textutils
from textutils import (
    is_palindrome,
    reverse_words,
    slugify,
    truncate,
    word_count,
)


def test_package_exposes_all_five_public_names():
    for name in ("slugify", "truncate", "word_count", "is_palindrome", "reverse_words"):
        assert hasattr(textutils, name)
        assert callable(getattr(textutils, name))


def test_all_matches_public_api():
    assert sorted(textutils.__all__) == [
        "is_palindrome",
        "reverse_words",
        "slugify",
        "truncate",
        "word_count",
    ]


def test_functions_are_callable_and_return_typed_results():
    assert isinstance(slugify("Hello, World!"), str)
    assert isinstance(truncate("langer Text", 10), str)
    assert isinstance(word_count("Hallo Welt"), int)
    assert isinstance(is_palindrome("Anna"), bool)
    assert isinstance(reverse_words("eins zwei drei"), str)


@pytest.mark.parametrize(
    "func",
    [slugify, truncate, word_count, is_palindrome, reverse_words],
)
@pytest.mark.parametrize(
    "non_str",
    [None, 42, 3.14, b"bytes", ["a"], {"a": 1}, ("a",)],
)
def test_every_function_rejects_non_string_uniformly(func, non_str):
    with pytest.raises(TypeError):
        func(non_str)
