"""
Taxi Simulator program
"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    print("Let's drive!")
    taxi_choice = -1
    bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    menu = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()
    while menu != "q":
        if menu == "c":
            try:
                taxi_choice = int(input("Taxis available\n0 - {}\n1 - {}\n2 - {}\nChoose taxi: ".format(taxis[0], taxis[1], taxis[2])))
                if taxi_choice in range(0, len(taxis)):
                    print("Bill to date: ${}".format(bill))
                    menu = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()
                else:
                    print("Please choose a valid taxi.")
            except ValueError:
                print("Must choose a valid taxi.")
        elif menu == "d":
            if taxi_choice in range(0, len(taxis)):
                distance = int(input("Drive how far?: "))
                taxis[taxi_choice].start_fare()
                taxis[taxi_choice].drive(distance)
                print("Your {} trip will cost you ${:,.2f}".format(taxis[taxi_choice].name, taxis[taxi_choice].get_fare()))
                bill += taxis[taxi_choice].get_fare()
                menu = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()
            else:
                print("You must select a taxi before driving.")
                menu = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()
        else:
            print("Invalid input.")
            menu = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()
    else:
        print("Total trip cost: ${:,.2f}\nTaxis are now:\n0 - {}\n1 - {}\n2 - {}".format(bill, taxis[0], taxis[1], taxis[2]))


main()
