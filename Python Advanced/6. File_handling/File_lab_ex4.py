import os

try:
    os.remove("fileToDelete.txt")
    print("Deleted")
except FileNotFoundError:
    print("File already deleted!")



