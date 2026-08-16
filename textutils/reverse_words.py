"""reverse_words - die Reihenfolge der Wörter in einem Text umkehren."""


def reverse_words(text: str) -> str:
    """Kehrt die Reihenfolge der Wörter in ``text`` um.

    Die Buchstabenreihenfolge innerhalb der Wörter bleibt unverändert.
    Führende, abschließende und mehrfache Whitespaces werden auf einzelne
    Leerzeichen normalisiert; leerer oder Whitespace-only-Text ergibt ``''``.
    """
    if not isinstance(text, str):
        raise TypeError(f"reverse_words() expects str, got {type(text).__name__}")
    return " ".join(reversed(text.split()))
