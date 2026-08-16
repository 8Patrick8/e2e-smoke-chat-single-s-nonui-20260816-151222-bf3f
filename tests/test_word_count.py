"""Tests für textutils.word_count (AC-03, AC-08, AC-10)."""

import pytest

from textutils import word_count


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hallo Welt", 2),
        ("  a   b  c ", 3),
        ("eins zwei drei", 3),
        ("a", 1),
    ],
)
def test_word_count_counts_words(text, expected):
    assert word_count(text) == expected


@pytest.mark.parametrize(
    "text",
    ["", "   ", "\t", "\n", "\t \n  "],
)
def test_word_count_empty_or_whitespace_only_is_zero(text):
    assert word_count(text) == 0


def test_word_count_splits_on_tabs_and_newlines():
    assert word_count("a\tb\nc") == 3
    assert word_count("  a \t b  \n  c ") == 3


def test_word_count_handles_unicode_words():
    assert word_count("Über Café à bientôt") == 4
    assert word_count("日本語 テスト 文字列") == 3


def test_word_count_handles_single_words_with_surrounding_whitespace():
    assert word_count("  Hallo  ") == 1


@pytest.mark.parametrize(
    "text",
    [None, 42, 3.14, b"bytes", ["a"], {"a": 1}, ("a",)],
)
def test_word_count_rejects_non_string(text):
    with pytest.raises(TypeError):
        word_count(text)
