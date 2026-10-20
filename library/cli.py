"""Command-line interface for the library app."""

import argparse

from library.catalog import Book, Catalog


def build_parser():
    parser = argparse.ArgumentParser(prog="library")
    commands = parser.add_subparsers(dest="command", required=True)
    add = commands.add_parser("add", help="add a book")
    add.add_argument("isbn")
    add.add_argument("title")
    add.add_argument("author")
    commands.add_parser("list", help="list all books")
    return parser


def main(argv=None, catalog=None):
    catalog = catalog or Catalog()
    args = build_parser().parse_args(argv)
    if args.command == "add":
        catalog.add_book(Book(args.isbn, args.title, args.author))
        print(f"Added {args.title}")
    elif args.command == "list":
        for book in catalog.all_books():
            print(f"{book.isbn}  {book.title} by {book.author}")
    return catalog


if __name__ == "__main__":
    main()
