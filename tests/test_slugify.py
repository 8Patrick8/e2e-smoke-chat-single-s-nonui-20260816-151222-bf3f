"""Tests für textutils.slugify (AC-01, AC-08, AC-09, AC-10)."""

import ast
import pathlib
import sys
import time

import pytest

import textutils
from textutils import slugify


def test_slugify_basic_sentence():
    assert slugify("Hello, World!") == "hello-world"


def test_slugify_collapses_spaces():
    assert slugify("  Multiple   spaces  ") == "multiple-spaces"


@pytest.mark.parametrize(
    "text",
    [None, 42, 3.14, b"bytes", ["a"], {"a": 1}, ("a",)],
)
def test_slugify_rejects_non_string(text):
    with pytest.raises(TypeError):
        slugify(text)


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", ""),
        ("   ", ""),
        ("A", "a"),
        ("a--b", "a-b"),
        ("- leading", "leading"),
        ("trailing -", "trailing"),
        ("hello_world", "hello-world"),
        ("Über Café!", "über-café"),
        ("héllo wörld", "héllo-wörld"),
        ("Déjà vu 123", "déjà-vu-123"),
        ("!!!", ""),
    ],
)
def test_slugify_edge_cases(text, expected):
    assert slugify(text) == expected


def test_slugify_long_input_finishes_quickly():
    long_word = "a" * 500_000
    payload = "#" * 500_000 + long_word + "!" * 500_000
    start = time.monotonic()
    result = slugify(payload)
    elapsed = time.monotonic() - start
    assert result == long_word
    assert elapsed < 1.0


def test_slugify_repeated_special_characters_finish_quickly():
    tokens = 50_000
    payload = "ab!" * tokens
    start = time.monotonic()
    result = slugify(payload)
    elapsed = time.monotonic() - start
    assert result == ("ab-" * (tokens - 1)) + "ab"
    assert elapsed < 1.0


def test_textutils_imports_only_stdlib():
    package_dir = pathlib.Path(textutils.__file__).parent
    stdlib = set(sys.stdlib_module_names)
    for path in sorted(package_dir.glob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    top = alias.name.split(".")[0]
                    assert top in stdlib or top == "textutils", (
                        f"{path.name} imports non-stdlib module {alias.name}"
                    )
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ""
                top = module.split(".")[0]
                assert top in stdlib or top == "textutils", (
                    f"{path.name} imports non-stdlib module {module}"
                )
