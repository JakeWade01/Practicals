"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Car", 180)
    my_car.drive(30)
    print(str(my_car))

    my_limo = Car("Limo", 100)
    my_limo.add_fuel(20)
    my_limo.drive(115)
    print(str(my_limo))


main()
