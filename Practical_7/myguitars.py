
from guitar_info_file import GuitarList
from operator import attrgetter
import csv


def main():
    guitars = []
    in_file = open('guitars.csv', 'r')

    for line in in_file:
        parts = line.strip().split(',')
        guitar_info = GuitarList(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar_info)
    in_file.close()

    guitars.sort(key=attrgetter("year"))

    for guitar_info in guitars:
        print(guitar_info)

    print()
    query = input("Would you like to add a new guitar? (Y/N): ").upper()

    while query != "N":
        if query == "Y":
            guitar_name = input("Enter guitar Name: ")
            guitar_year = input("Enter guitar Year: ")
            guitar_cost = input("Enter guitar Cost: ")
            new_guitar = [guitar_name, int(guitar_year), float(guitar_cost)]

            with open('guitars.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(new_guitar)

            query = input("Would you like to add a new guitar? (Y/N): ").upper()
        else:
            query = input("Invalid Input. Please enter Y or N: ").upper()
    "Goodbye"


main()
