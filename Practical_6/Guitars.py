from guitar import Guitar

print("My guitars!")
guitars = []

choice = input("Would you like to add a guitar? (Y/N): ").upper()
while choice != "N":
    if choice == "Y":
        name = input("Enter Guitar Name: ")
        year = int(input("Enter Guitar Year: "))
        cost = float(input("Enter Guitar Cost: "))

        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:,.2f} added.")

        choice = input("Would you like to add a guitar? (Y/N): ").upper()
    else:
        choice = input("Please enter Y or N: ").upper()

print()
print("These are my guitars:")


counter = 1
for guitar in guitars:
    if guitar.is_vintage():
        vintage_check = "(vintage)"
    else:
        vintage_check = ""
    print(f"Guitar {counter}: {guitar.name:>20} {guitar.year}), worth ${guitar.cost:>10,.2f} {vintage_check}")
    counter += 1
