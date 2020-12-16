book_name = input()

is_found = False
count = 0

line = input()
while line != "No More Books":
    current_book_name = line

    if current_book_name == book_name:
        is_found = True
        print(f"You checked {count} books and found it.")
        break
    count += 1
    line = input()

if not is_found:
    print(f"The book you search is not here!")
    print(f"You checked {count} books.")




