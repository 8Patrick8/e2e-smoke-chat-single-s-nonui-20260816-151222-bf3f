"""slugify - einen Text in einen url-freundlichen Slug verwandeln."""

import re

# Läuft über Buchstaben und Ziffern (Unicode-bewusst) und ignoriert den
# Unterstrich, damit er als Trenner behandelt wird statt im Slug zu bleiben.
_WORD_RE = re.compile(r"[^\W_]+")


def slugify(text: str) -> str:
    """Wandelt ``text`` in einen Slug um (Kleinschreibung, Bindestriche).

    Nicht-alphanumerische Zeichen werden zu Bindestrichen, aufeinanderfolgende
    Bindestriche werden zusammengefasst, führende und abschließende
    Bindestriche werden entfernt.
    """
    if not isinstance(text, str):
        raise TypeError(f"slugify() expects str, got {type(text).__name__}")
    return "-".join(_WORD_RE.findall(text.lower()))
