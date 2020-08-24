numbers = [3, 1, 4, 1, 5, 9, 2]

# Assumed answers
# numbers[0] = 3
# numbers[-1] = 2
# numbers[3] = 1
# numbers[:-1] = no idea
# numbers[3:4] = 1:5
# 5 in numbers = 5
# 7 in numbers = 2
# "3" in numbers = 3
# numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Actual answers if wrong
# numbers[:-1] = [3, 1, 4, 1, 5, 9]
# numbers[3:4] = [1]
# 5 in numbers = True
# 7 in numbers = False
# "3" in numbers = False

print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(numbers[3:4])
print(5 in numbers)
print(7 in numbers)
print("3" in numbers)
print(numbers + [6, 5, 3])