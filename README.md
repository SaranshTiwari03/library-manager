# Library Manager

A small Python program for a campus library that lends books, magazines and DVDs.
Members can borrow and return items. Invalid actions are refused with clear messages instead of crashing.

Run it with:

```
python main.py
```

Files: `models.py` (the classes), `main.py` (the demo), `output.txt` (output of the final run).

## 1. Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?

`LibraryItem` is abstract because a plain "item" should never exist on its own: every real item is a Book, Magazine or DVD, and each one must define its own late fee. The `@abstractmethod` on `late_fee()` is a rule that every child class has to follow. If `DVD` forgot to write `late_fee()`, Python would raise a `TypeError` as soon as we tried to create a DVD object, so the mistake is caught immediately.

## 2. What happens when you read item.__available from outside the class, and why do we use is_available() instead?

Reading `item.__available` from outside the class raises an `AttributeError`, because the two leading underscores make the attribute private (Python renames it internally). This protects the item's status so outside code can't set it to a wrong value by accident. We use the `is_available()` method instead, which reads the value safely, while `mark_borrowed()` and `mark_returned()` are the only ways to change it.

## 3. What is the difference between LibraryItem.total_items and self.title?

`LibraryItem.total_items` is a class attribute: there is only one copy, shared by every object, and it counts how many items have been created in total. `self.title` is an instance attribute: each object has its own title, stored only on that object. Changing one book's title does not affect any other item, but creating any new item increases `total_items` for all of them.
