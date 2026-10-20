import unittest

from library.catalog import Book, Catalog


class SearchTest(unittest.TestCase):
    def setUp(self):
        self.catalog = Catalog()
        self.catalog.add_book(Book("9780441478125", "The Left Hand of Darkness", "Ursula K. Le Guin"))
        self.catalog.add_book(Book("9780547928227", "The Hobbit", "J. R. R. Tolkien"))

    def test_finds_books_by_part_of_the_author_name(self):
        self.assertEqual([book.title for book in self.catalog.find_by_author("le guin")], ["The Left Hand of Darkness"])

    def test_no_match_gives_an_empty_list(self):
        self.assertEqual(self.catalog.find_by_author("Austen"), [])

    def test_spaces_around_the_name_are_ignored(self):
        self.assertEqual(len(self.catalog.find_by_author("  Tolkien ")), 1)
