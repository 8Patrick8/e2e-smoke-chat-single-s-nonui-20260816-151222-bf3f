# textutils

Eine eigenständige, minimale Python-Bibliothek mit fünf unabhängigen
String-Hilfsfunktionen: `slugify`, `truncate`, `word_count`, `is_palindrome`
und `reverse_words`. Die Funktionen sind reine String-Transformationen ohne
Seiteneffekte – sie greifen auf keine Dateien, kein Netzwerk und keine
Umgebungsvariablen zu, speichern und protokollieren nichts.

## Tech-Stack

- Python 3 (CPython 3.x)
- nur die Standardbibliothek – keine externen Laufzeit-Abhängigkeiten
- Tests mit pytest

## Installation

Voraussetzung ist ein Python 3.x-Interpreter. Es gibt keine externen
Pakete zu installieren – die Bibliothek nutzt ausschließlich die
Standardbibliothek:

```bash
pip install pytest
```

## Nutzung

```python
import textutils
from textutils import slugify, truncate, word_count, is_palindrome, reverse_words
```

### Öffentliche API

| Funktion | Signatur | Beschreibung |
| --- | --- | --- |
| `slugify` | `slugify(text: str) -> str` | Erzeugt einen Slug: Kleinschreibung, nicht-alphanumerische Zeichen werden zu Bindestrichen, aufeinanderfolgende Bindestriche werden zusammengefasst, führende/abschließende Bindestriche werden entfernt. |
| `truncate` | `truncate(text: str, max_len: int) -> str` | Kürzt auf `text[:max_len]` und hängt `'...'` an, wenn `len(text) > max_len`. |
| `word_count` | `word_count(text: str) -> int` | Zählt die Wörter im Text. |
| `is_palindrome` | `is_palindrome(text: str) -> bool` | Prüft, ob der Text ein Palindrom ist. |
| `reverse_words` | `reverse_words(text: str) -> str` | Kehrt die Reihenfolge der Wörter um. |

Beispiel:

```python
>>> import textutils
>>> textutils.slugify("Hello, World!")
'hello-world'
```

Alle fünf Funktionen akzeptieren ausschließlich `str`; ein Nicht-String-Argument
löst einheitlich `TypeError` aus. `truncate`, `word_count`, `is_palindrome` und
`reverse_words` werden im laufenden Sprint implementiert und antworten bis dahin
mit `NotImplementedError`.

## Tests ausführen

```bash
python3 -m pytest
```

## Features

- `slugify` – vollständig implementiert (AC-01): Kleinschreibung,
  Bindestrich-Konvertierung, Zusammenfassen aufeinanderfolgender Bindestriche,
  Entfernen führender/abschließender Bindestriche; Unicode- und
  Leerstring-Kantenfälle sind abgedeckt.
- `truncate`, `word_count`, `is_palindrome`, `reverse_words` – Stubs mit
  korrekter Signatur, Implementierung folgt in eigenen Tickets.
- Nur Python-Standardbibliothek in Laufzeit- und Testcode (AC-07).
- Keine exponentiell aufwändigen Regex-Muster; Lang-String-Laufzeittests (AC-09).
- Unicode-Sonderzeichen, leere Zeichenfolgen und Whitespace-Kantenfälle
  werden ohne Absturz oder Endlosschleife verarbeitet (AC-10).
- Reine String-Transformationen ohne Seiteneffekte, ohne Speicherung oder
  Protokollierung verarbeiteter Texte (AC-11).
