"""Borrowing and returning books."""

from dataclasses import dataclass


@dataclass
class Loan:
    isbn: str
    member: str


class Loans:
    def __init__(self):
        self._loans = {}

    def borrow(self, isbn, member):
        if isbn in self._loans:
            raise ValueError(f"{isbn} is already on loan")
        self._loans[isbn] = Loan(isbn, member)
        return self._loans[isbn]

    def return_book(self, isbn):
        self._loans.pop(isbn, None)

    def on_loan(self):
        return list(self._loans.values())
