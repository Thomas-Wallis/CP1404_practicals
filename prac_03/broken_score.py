def main():
    score = float(input("Enter score: "))
    result = score_checker(score)
    print(result)
    import random
    score = random.randint(0, 100)
    result = score_checker(score)
    print(result)


def score_checker(score):
    if score < 0 or score > 100:
        result = "Invalid score"
    elif 50 <= score < 90:
        result = "Passable"
    elif score >= 90:
        result = "Excellent"
    else:
        result = "Bad"
    return result


main()