from prac_06.guitar import Guitar


def main():
    guitar_1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 13009.25)
    guitars = guitar_1, another_guitar
    print("{} get_age() - Expected {}. Got {}".format(guitar_1.name, 98, guitar_1.get_age()))
    print("{} is_vintage() - Expected {}. Got {}".format(guitar_1.name, True, guitar_1.is_vintage()))
    print("{} get_age() - Expected {}. Got {}".format(another_guitar.name, 7, another_guitar.get_age()))
    print("{} is_vintage() - Expected {}. Got {}".format(another_guitar.name, False, another_guitar.is_vintage()))


main()
