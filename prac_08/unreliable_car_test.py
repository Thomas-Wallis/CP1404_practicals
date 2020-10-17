from prac_08.unreliable_car import UnreliableCar


def main():
    my_car = UnreliableCar("Car 1", 40, 70)
    print(my_car)
    my_car.drive(35)
    print(my_car)


main()
