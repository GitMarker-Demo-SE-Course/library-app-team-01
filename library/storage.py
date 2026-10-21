"""Saving the catalogue between runs."""

import json
from pathlib import Path

from library.catalog import Book, Catalog

DEFAULT_FILE = Path("library-data.json")


def save(catalog, path=DEFAULT_FILE):
    books = [vars(book) for book in catalog.all_books()]
    Path(path).write_text(json.dumps(books, indent=2))


def load(path=DEFAULT_FILE):
    catalog = Catalog()
    if not Path(path).exists():
        return catalog
    for item in json.loads(Path(path).read_text()):
        catalog.add_book(Book(**item))
    return catalog
