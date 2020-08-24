from math import sqrt
number_x = int(input("Please enter the first number"))
number_y = int(input("Please enter the second number"))
menu = input("(E) - Show even numbers between two numbers\n(O) - Show odd numbers between two numbers\n(S) - Show "
             "square numbers between two numbers\n(Q) - Quit program")
while menu.upper() != "Q":
    if menu.upper() == "E":
        for number in range(number_x, number_y):
            if number % 2:
                pass
            else:
                print(number)
    elif menu.upper() == "O":
        for number in range(number_x, number_y):
            if number % 2:
                print(number)
            else:
                pass
    elif menu.upper() == "S":
        for number in range(number_x, number_y):
            if (sqrt(number)) in range(number_x, number_y):
                print(number)
            else:
                pass
    else:
        print("Invalid selection")
    menu = input("(E) - Show even numbers between two numbers\n(O) - Show odd numbers between two numbers\n(S) - Show "
                 "square numbers between two numbers\n(Q) - Quit program")
print("Finished")
