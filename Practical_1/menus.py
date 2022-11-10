<<<<<<< HEAD

name = input("What is your name: ")

MENU = """
H(ello)
G(oodbye)
Q(uit)
"""

print(MENU)
choice = input(">>>").upper()
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid Option")
    choice = input(">>>").upper()
=======

name = input("What is your name: ")

MENU = """
H(ello)
G(oodbye)
Q(uit)
"""

print(MENU)
choice = input(">>>").upper()
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid Option")
    choice = input(">>>").upper()
>>>>>>> efb4c5ef487ad18a03dd9b8d1be76683032a0863
