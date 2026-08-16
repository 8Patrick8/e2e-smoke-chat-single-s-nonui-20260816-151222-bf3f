"""Tests für textutils.reverse_words (AC-05, AC-08, AC-10)."""

import pytest

from textutils import reverse_words


def test_reverse_words_ac05_basic_sentence():
    assert reverse_words("eins zwei drei") == "drei zwei eins"


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hallo Welt", "Welt Hallo"),
        ("   führendes Leerzeichen", "Leerzeichen führendes"),
        ("Trailing-Leerzeichen   ", "Trailing-Leerzeichen"),
        ("  Mehrfache    Leerzeichen  ", "Leerzeichen Mehrfache"),
        ("a   b   c", "c b a"),
        ("", ""),
        ("   ", ""),
        ("\t\n  ", ""),
        ("Wort", "Wort"),
        ("Über Café à la carte", "carte la à Café Über"),
        ("日本語 ドイツ語 Ελληνικά", "Ελληνικά ドイツ語 日本語"),
        ("emoji 🚀 test", "test 🚀 emoji"),
    ],
)
def test_reverse_words_edge_cases(text, expected):
    assert reverse_words(text) == expected


@pytest.mark.parametrize(
    "text",
    [None, 42, 3.14, b"bytes", ["a"], {"a": 1}, ("a",)],
)
def test_reverse_words_rejects_non_string(text):
    with pytest.raises(TypeError):
        reverse_words(text)


def test_reverse_words_preserves_word_letter_order():
    assert reverse_words("hello world") == "world hello"
    assert reverse_words("abc def ghi") != "ihg fed cba"
