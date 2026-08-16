"""word_count - die Anzahl der Wörter in einem Text zählen."""


def word_count(text: str) -> int:
    """Zählt die Wörter in ``text``.

    Wörter sind durch beliebiges Whitespace getrennt; mehrere aufeinanderfolgende
    Whitespace-Zeichen zählen nicht doppelt. Leerer oder Whitespace-only-Text
    ergibt 0.
    """
    if not isinstance(text, str):
        raise TypeError(f"word_count() expects str, got {type(text).__name__}")
    return len(text.split())
