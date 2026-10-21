# Library App

A small command-line app for a library. You work on it in a team of two.

## How to work

Use GitHub Flow:

1. Create a branch for each change.
2. Push the branch and open a pull request.
3. Ask your teammate to review it. Discuss and fix what they find.
4. Your teammate merges the pull request, and you delete the branch.

Do not push to `main` directly.

## Run

```
python -m library.cli add 9780441013593 "Dune" "Frank Herbert"
python -m library.cli list
python -m library.cli search tolkien
```

## Test

```
python -m unittest
```
