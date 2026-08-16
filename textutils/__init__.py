"""textutils - kleine Python-String-Hilfsbibliothek.

Stellt fünf unabhängige String-Hilfsfunktionen bereit: ``slugify``,
``truncate``, ``word_count``, ``is_palindrome`` und ``reverse_words``.
Nur Python-Standardbibliothek, keine externen Abhängigkeiten.
"""

from textutils.is_palindrome import is_palindrome
from textutils.reverse_words import reverse_words
from textutils.slugify import slugify
from textutils.truncate import truncate
from textutils.word_count import word_count

__all__ = ["is_palindrome", "reverse_words", "slugify", "truncate", "word_count"]
