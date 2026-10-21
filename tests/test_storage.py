import tempfile
import unittest
from pathlib import Path

from library import storage
from library.catalog import Book, Catalog


class StorageTest(unittest.TestCase):
    def test_saved_books_load_again(self):
        catalog = Catalog()
        catalog.add_book(Book("9780441013593", "Dune", "Frank Herbert"))
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "books.json"
            storage.save(catalog, path)
            self.assertEqual(storage.load(path).all_books(), catalog.all_books())
