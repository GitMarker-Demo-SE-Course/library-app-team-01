"""A catalogue of library books."""

from dataclasses import dataclass


@dataclass
class Book:
    isbn: str
    title: str
    author: str


class Catalog:
    def __init__(self):
        self._books = {}

    def add_book(self, book):
        if book.isbn in self._books:
            raise ValueError(f"A book with ISBN {book.isbn} is already in the catalogue")
        self._books[book.isbn] = book

    def get(self, isbn):
        return self._books.get(isbn)

    def find_by_title(self, text):
        text = text.lower()
        return [book for book in self._books.values() if text in book.title.lower()]

    def find_by_author(self, name):
        name = name.lower()
        return [book for book in self._books.values() if name in book.author.lower()]

    def all_books(self):
        return sorted(self._books.values(), key=lambda book: book.title)
