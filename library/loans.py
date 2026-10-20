"""Borrowing and returning books."""

from dataclasses import dataclass
from datetime import date, timedelta

LOAN_DAYS = 14


@dataclass
class Loan:
    isbn: str
    member: str
    due: date


class Loans:
    def __init__(self):
        self._loans = {}

    def borrow(self, isbn, member, today=None):
        if isbn in self._loans:
            raise ValueError(f"{isbn} is already on loan")
        today = today or date.today()
        self._loans[isbn] = Loan(isbn, member, today + timedelta(days=LOAN_DAYS))
        return self._loans[isbn]

    def return_book(self, isbn):
        self._loans.pop(isbn, None)

    def on_loan(self):
        return list(self._loans.values())

    def overdue(self, today=None):
        today = today or date.today()
        late = [loan for loan in self._loans.values() if loan.due < today]
        return late
