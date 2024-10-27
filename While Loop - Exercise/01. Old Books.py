desired_book = input()
counter_books = 0

while True:
    books_in_library = input()
    counter_books += 1
    if books_in_library == desired_book:
        print(f"You checked {counter_books - 1} books and found it.")
        break
    if books_in_library == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {counter_books - 1} books.")
        break