"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When the Value given is not unable to be used by the input. e.g. inputing 0.5 with an
int while int only accepts whole numbers.
2. When will a ZeroDivisionError occur? When trying to divide by zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError? Yes by adding another line to acknowledge
when the user inputs zero for the "denominator" variable and account for it with a "while" loop
"""


try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")