import unittest

from library.catalog import Book, Catalog


class CatalogTest(unittest.TestCase):
    def setUp(self):
        self.catalog = Catalog()
        self.catalog.add_book(Book("9780441013593", "Dune", "Frank Herbert"))
        self.catalog.add_book(Book("9780547928227", "The Hobbit", "J. R. R. Tolkien"))

    def test_find_by_title_ignores_case(self):
        self.assertEqual([book.title for book in self.catalog.find_by_title("hobbit")], ["The Hobbit"])

    def test_adding_the_same_isbn_twice_fails(self):
        with self.assertRaises(ValueError):
            self.catalog.add_book(Book("9780441013593", "Dune", "Frank Herbert"))


if __name__ == "__main__":
    unittest.main()
