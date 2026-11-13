# main.py
from models import Book, Member, Magazine, DVD 
book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Forbes 101", 2, 23734)
dvd= DVD("SpiderMan", 23, 170)

alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)
# 1. Borrowing with error handling
try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
    bob.borrow(book)  # should fail: already borrowed
except ValueError as e:
    print("Could not borrow:", e)

try:
    bob.borrow(magazine)
    bob.borrow(dvd)           
except ValueError as e:
    print("Could not borrow:", e)

try:
    bob.return_item(book)
except ValueError as e:
    print("Could not return:", e)


try:
    fee = alice.return_item(book, 3)
    print("Alice returned the book. Late fee: Rs", fee)
except ValueError as e:
    print("Could not return:", e)

items = [book,magazine,dvd] 
for item in items:
    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))
# 4. Class attribute shared by all objects
print("Total items created:", Book.total_items)
# 5. Encapsulation: private data cannot be read from outside the class
try:
    print(book.__available)
except AttributeError as e:
    print("Cannot read __available directly:", e)
print("Reading it the proper way, book.is_available():", book.is_available())
