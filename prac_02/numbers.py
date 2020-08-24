in_file = open(FILE, "r")
contents = in_file.readlines()
total = 0
print(contents)
for content in contents:
    total += int(content)
print(total)
in_file.close()
