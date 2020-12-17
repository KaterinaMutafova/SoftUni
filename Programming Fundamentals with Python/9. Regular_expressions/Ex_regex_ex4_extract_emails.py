# user  -- [a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@
#
# host == [a-zA-Z]+\-?[a-zA-Z]+\.[a-zA-Z]+\-?[a-zA-Z]+

import re

data = input()

pattern = r"(^|(?<=\s))[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-zA-Z]+\-?[a-zA-Z]+(\.[a-zA-Z]+\-?[a-zA-Z]+)+($|(?=\s))?"

result = re.finditer(pattern, data)

for el in result:
    print(el.group())


