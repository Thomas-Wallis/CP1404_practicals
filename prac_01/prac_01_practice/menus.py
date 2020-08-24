name = input("Please enter your name")
menu = input("H - Hello\nG - Goodbye\nQ - Quit\nPlease choose from the options above: ")
while menu.upper() != "Q":
    if menu.upper() == "H":
        print("Hello {}".format(name))
    elif menu.upper() == "G":
        print("Goodbye {}".format(name))
    else:
        print("Invalid")
    menu = input("H - Hello\nG - Goodbye\nQ - Quit\nPlease choose from the options above: ")
print("Finished")
