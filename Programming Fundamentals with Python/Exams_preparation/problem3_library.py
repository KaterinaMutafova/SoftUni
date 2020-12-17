def add_book(book_titles, name):
    if name not in book_titles:
        book_titles.insert(0, name)
        return book_titles


def take_book(book_titles, name):
    if name in book_titles:
        book_titles.remove(name)
        return book_titles


def swap_book(book_titles, name_1, name_2):
    if name_1 in book_titles and name_2 in book_titles:
        index_name_1 = book_titles.index(name_1)
        index_name_2 = book_titles.index(name_2)
        book_titles[index_name_1], book_titles[index_name_2] = name_2, name_1
        return book_titles


def insert_book(book_titles, name):
    book_titles.append(name)
    return book_titles


def check_book(book_titles, index):
    if 0 <= index < len(book_titles):
        chosen_book = book_titles[index]
        print(chosen_book)


books = input().split("&")

command = input()

while not command == "Done":
    command = command.split(" | ")
    if command[0] == "Add Book":
        add_book(books, command[1])

    elif command[0] == "Take Book":
        take_book(books, command[1])

    elif command[0] == "Swap Books":
        swap_book(books, command[1], command[2])

    elif command[0] == "Insert Book":
        insert_book(books, command[1])

    elif command[0] == "Check Book":
        index_book = int(command[1])
        check_book(books, index_book)

    command = input()

print(', '.join(books))
