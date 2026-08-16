"""Tests für textutils.is_palindrome (AC-04, AC-08, AC-10)."""

import pytest

from textutils import is_palindrome


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Anna", True),
        ("A man, a plan, a canal: Panama", True),
        ("Hallo", False),
    ],
)
def test_is_palindrome_acceptance_cases(text, expected):
    assert is_palindrome(text) is expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", True),
        ("   ", True),
        ("a", True),
        ("aa", True),
        ("ab", False),
        ("Racecar", True),
        ("Was it a car or a cat I saw?", True),
        ("No 'x' in Nixon", True),
    ],
)
def test_is_palindrome_edge_cases(text, expected):
    assert is_palindrome(text) is expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Àà", True),
        ("mööm", True),
        ("naïan", True),
        ("é", True),
        ("Héllo", False),
    ],
)
def test_is_palindrome_unicode(text, expected):
    assert is_palindrome(text) is expected


@pytest.mark.parametrize(
    "text",
    [None, 42, 3.14, b"bytes", ["a"], {"a": 1}, ("a",)],
)
def test_is_palindrome_rejects_non_string(text):
    with pytest.raises(TypeError):
        is_palindrome(text)
