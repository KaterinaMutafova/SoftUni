age = float(input())
s = input()

title = "Everyone"

if s == "m":
  if age >= 16:
    title = "Mr."
  if age < 16:
    title = "Master"
elif s == "f":
    if age >= 16:
        title = "Ms."
    if age < 16:
        title = "Miss"

print(title)
