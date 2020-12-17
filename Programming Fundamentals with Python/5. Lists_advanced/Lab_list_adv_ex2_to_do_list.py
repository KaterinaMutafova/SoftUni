todo_list = [0 for _ in range(10)]

todo_notes = input()

while not todo_notes == "End":
    data = todo_notes.split("-")
    importance = int(data[0])
    task = data[1]
    todo_list.insert(importance, task)

    todo_notes = input()

result = [el for el in todo_list if not el == 0]

print(result)


