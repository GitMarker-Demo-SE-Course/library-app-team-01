import unittest

from library.loans import Loans


class LoansTest(unittest.TestCase):
    def test_a_book_cannot_be_borrowed_twice(self):
        loans = Loans()
        loans.borrow("9780441013593", "sam")
        with self.assertRaises(ValueError):
            loans.borrow("9780441013593", "alex")

    def test_returned_books_are_no_longer_on_loan(self):
        loans = Loans()
        loans.borrow("9780441013593", "sam")
        loans.return_book("9780441013593")
        self.assertEqual(loans.on_loan(), [])
