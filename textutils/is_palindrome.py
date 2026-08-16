"""is_palindrome - prüfen, ob ein Text rückwärts gelesen identisch ist."""


def is_palindrome(text: str) -> bool:
    """Prüft, ob ``text`` ein Palindrom ist.

    Groß-/Kleinschreibung und nicht-alphanumerische Zeichen werden
    ignoriert (gefiltert über ``str.isalnum``, ohne Regex). Ein leerer
    String gilt als Palindrom.
    """
    if not isinstance(text, str):
        raise TypeError(f"is_palindrome() expects str, got {type(text).__name__}")
    letters = [char.lower() for char in text if char.isalnum()]
    return letters == letters[::-1]
