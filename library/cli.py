"""Command-line interface for the library app."""

import argparse

from library import storage
from library.catalog import Book


def build_parser():
    parser = argparse.ArgumentParser(prog="library")
    commands = parser.add_subparsers(dest="command", required=True)
    add = commands.add_parser("add", help="add a book")
    add.add_argument("isbn")
    add.add_argument("title")
    add.add_argument("author")
    commands.add_parser("list", help="list all books")
    search = commands.add_parser("search", help="find books by title or author")
    search.add_argument("text")
    return parser


def show(books):
    for book in books:
        print(f"{book.isbn}  {book.title} by {book.author}")


def main(argv=None):
    catalog = storage.load()
    args = build_parser().parse_args(argv)
    if args.command == "add":
        catalog.add_book(Book(args.isbn, args.title, args.author))
        storage.save(catalog)
        print(f"Added {args.title}")
    elif args.command == "list":
        show(catalog.all_books())
    elif args.command == "search":
        found = {book.isbn: book for book in catalog.find_by_title(args.text) + catalog.find_by_author(args.text)}
        show(found.values())


if __name__ == "__main__":
    main()
