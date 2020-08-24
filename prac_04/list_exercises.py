# Basic list operations
numbers = []
total = 0
for value in range(0, 5):
    number = int(input("Number {}: ".format(value + 1)))
    numbers.append(number)
for number in numbers:
    total += number
average = total / len(numbers)
print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the numbers is {}".format(average))