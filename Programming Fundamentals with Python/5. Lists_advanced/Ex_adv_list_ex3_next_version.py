version = input()

next_version_list = []

# def next_version(version):
version = version.split(".")
version = list(map(int, version))


version[2] += 1
if version[2] == 10:
    version[2] = 0
    version[1] += 1
    if version[1] == 10:
        version[1] = 0
        version[0] += 1


print(".".join(str(x) for x in version))








