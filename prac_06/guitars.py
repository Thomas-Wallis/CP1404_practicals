from prac_06.guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add)
        name = str(input("Name: "))
    if guitars:
        print("These are my guitars:")
        iteration = 0
        for guitar in guitars:
            iteration += 1
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print("Guitar {}: {} ({}), worth ${}{}".format(iteration, guitar.name, guitar.year, guitar.cost, vintage_string))

    else:
        print("No guitars :( Quick, go and buy one!")


main()
