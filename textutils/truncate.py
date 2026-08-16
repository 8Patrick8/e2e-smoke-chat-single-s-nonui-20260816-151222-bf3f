"""truncate - einen Text auf ``max_len`` Zeichen kürzen und mit '...' enden."""


def truncate(text: str, max_len: int) -> str:
    """Kürzt ``text`` auf ``text[:max_len]`` und hängt '...' an.

    Texte, die nicht länger als ``max_len`` sind, bleiben unverändert.
    Nicht-String-Eingaben lösen einen ``TypeError`` aus.
    """
    if not isinstance(text, str):
        raise TypeError(f"truncate() expects str, got {type(text).__name__}")
    if len(text) > max_len:
        return text[:max_len] + "..."
    return text
