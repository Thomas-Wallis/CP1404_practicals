import random

NUMBERS_PER_LINE = 8
MAX_NUMBER = 45
MIN_NUMBER = 1


quick_pick = int(input("How many quick picks "))
for pick in range(0, quick_pick):
    quick_pick_numbers = []
    for value in range(0, NUMBERS_PER_LINE):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while number in quick_pick_numbers:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
        quick_pick_numbers.append(number)
    quick_pick_numbers.sort()
    print(" ".join("{}".format(number) for number in quick_pick_numbers))
