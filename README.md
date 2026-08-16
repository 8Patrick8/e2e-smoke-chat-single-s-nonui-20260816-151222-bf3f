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
löst einheitlich `TypeError` aus. Die Funktionen sind reine Transformationen
ohne Seiteneffekte und verwenden nur die Python-Standardbibliothek.

## Tests ausführen

```bash
python3 -m pytest
```

## Features

- `slugify` (AC-01) – Kleinschreibung, Bindestrich-Konvertierung, Zusammenfassen
  aufeinanderfolgender Bindestriche, Entfernen führender/abschließender
  Bindestriche; Unicode- und Leerstring-Kantenfälle sind abgedeckt.
- `truncate` (AC-02) – kürzt auf `text[:max_len]` und hängt `'...'` an, wenn der
  Text länger als `max_len` ist; kürzere Texte bleiben unverändert.
- `word_count` (AC-03) – zählt die Wörter im Text, getrennt durch beliebiges
  Whitespace.
- `is_palindrome` (AC-04) – prüft, ob der Text rückwärts gelesen identisch ist;
  Groß-/Kleinschreibung und nicht-alphanumerische Zeichen werden ignoriert.
- `reverse_words` (AC-05) – kehrt die Reihenfolge der Wörter um; die
  Buchstabenreihenfolge innerhalb der Wörter bleibt erhalten.
- Nur Python-Standardbibliothek in Laufzeit- und Testcode (AC-07).
- Keine exponentiell aufwändigen Regex-Muster; Lang-String-Laufzeittests (AC-09).
- Unicode-Sonderzeichen, leere Zeichenfolgen und Whitespace-Kantenfälle
  werden ohne Absturz oder Endlosschleife verarbeitet (AC-10).
- Reine String-Transformationen ohne Seiteneffekte, ohne Speicherung oder
  Protokollierung verarbeiteter Texte (AC-11).
