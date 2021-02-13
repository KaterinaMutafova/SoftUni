import re


def count_all(pattern, line):
    return re.findall(pattern, line)


def get_file_content():
    with open("text.txt", "r") as file:
        lines = file.readlines()[:-1]
        pattern_symbols = r"[,.!?'-]"
        pattern_chars = r"[a-zA-Z]"
        counter = 0
        for line in lines:
            count_symbols = count_all(pattern_symbols, line)
            count_chars = count_all(pattern_chars, line)
            counter += 1
            print(f"Line {counter}: {line[:-1]} ({len(count_chars)})({len(count_symbols)})")


get_file_content()

