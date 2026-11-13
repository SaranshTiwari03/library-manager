# Library Manager

A small python program for a campus library, it keeps books, magazines and DVDs and lets members borrow and return them. If someone tries something wrong it just shows a message instead of crashing.

To run it:

```
python main.py
```

`models.py` has all the classes, `main.py` runs the demo and `output.txt` is the output from my final run.

## 1. Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?

Because there is no such thing as just an "item" in the library, it's always a book, a magazine or a DVD, so it doesn't make sense to create a plain LibraryItem. The `@abstractmethod` on `late_fee()` is basically a promise that every child class has to write its own late fee. If DVD forgets it then Python wont even let you create a DVD object, it gives a `TypeError` straight away so the mistake gets caught early.

## 2. What happens when you read item.__available from outside the class, and why do we use is_available() instead?

You get an `AttributeError`, the two underscores make it private so Python hides it from anything outside the class. I think of it like the stamp behind the library desk, a member can't just walk in and stamp a book themselves, they have to ask the librarian. So `is_available()` is the proper way to check it and only `mark_borrowed()` and `mark_returned()` can change it, that way nobody can set it to something wrong by mistake.

## 3. What is the difference between LibraryItem.total_items and self.title?

`total_items` belongs to the class so there is only one of it and every object shares it, it's like one counter on the library wall that goes up every time a new item is made. `self.title` belongs to each object on its own, so every book has its own title and changing one doesn't touch the others. In my run the counter shows 3 because I created 3 items, but each of them still has a different title.
