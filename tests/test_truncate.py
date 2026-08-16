"""Tests für textutils.truncate (AC-02, AC-08, AC-10)."""

import pytest

from textutils import truncate


def test_truncate_longer_text_is_shortened():
    assert truncate("Das ist ein langer Text", 10) == "Das ist ei..."


@pytest.mark.parametrize(
    ("text", "max_len"),
    [
        ("Kurz", 10),
        ("genau", 5),
        ("", 10),
    ],
)
def test_truncate_short_text_unchanged(text, max_len):
    assert truncate(text, max_len) == text


def test_truncate_max_len_zero():
    assert truncate("abc", 0) == "..."
    assert truncate("", 0) == ""


@pytest.mark.parametrize(
    ("text", "max_len", "expected"),
    [
        ("Überraschung für alle", 6, "Überra..."),
        ("   ", 1, " ..."),
        ("emoji 🚀 rocket", 7, "emoji 🚀..."),
    ],
)
def test_truncate_unicode_and_whitespace(text, max_len, expected):
    assert truncate(text, max_len) == expected


@pytest.mark.parametrize(
    "text",
    [None, 42, 3.14, b"bytes", ["a"], {"a": 1}, ("a",)],
)
def test_truncate_rejects_non_string(text):
    with pytest.raises(TypeError):
        truncate(text, 10)
