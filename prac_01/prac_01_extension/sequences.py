number_x = int(input("Please enter the first number"))
number_y = int(input("Please enter the second number"))
menu = input("(E) - Show even numbers between two numbers\n(O) - Show odd numbers between two numbers\n(S) - Show "
             "square numbers between two numbers\n(Q) - Quit program")
while menu.upper() != "Q":
    if menu.upper() == "E":
        pass
    elif menu.upper() == "O":
        pass
    elif menu.upper() == "S":
        pass
    else:
        print("Invalid selection")
    menu = input("(E) - Show even numbers between two numbers\n(O) - Show odd numbers between two numbers\n(S) - Show "
                 "square numbers between two numbers\n(Q) - Quit program")
print("Finished")
