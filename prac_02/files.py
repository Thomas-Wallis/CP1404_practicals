FILE = "name"
name = input("What is your name? ")
out_file = open(FILE, "w")
print("Your name is {}".format(name), file=out_file)
out_file.close()

in_file = open(FILE, "r")
name = in_file.read()
print(name)
in_file.close()
