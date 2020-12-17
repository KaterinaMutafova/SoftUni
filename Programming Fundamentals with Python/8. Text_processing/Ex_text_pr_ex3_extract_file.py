# File path extraction

file_path = input().split("\\")
file_info = file_path[-1].split(".")

file_name = file_info[-2]
file_extension = file_info[-1]

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")
