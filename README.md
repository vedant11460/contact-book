# Contact Book (Python, OOP)

A contact book written in Python using classes. Contacts are saved to a JSON file between runs.

## Features
- Add contacts with phone validation (exactly 10 digits)
- Duplicate names are rejected (case-insensitive)
- Search by name in O(1) time using a dictionary
- Sorted listing (A to Z, ignoring capital letters)
- Delete with undo, using a stack
- Save and load contacts with JSON

## Concepts used
- Classes and objects (`Contact`, `ContactBook`)
- Hashmap (dictionary): fast lookup by name
- Sorting with `sorted(key=...)`: O(n log n)
- Stack (last in, first out): undo delete
- JSON serialization: objects to dictionaries and back

## How to run
    python contacts.py