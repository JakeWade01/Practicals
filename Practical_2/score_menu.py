def main():

    MENU = """G - Get Score, between 0 and 100 (inclusive)
P - Print Result
S - Show Stars
Q - Quit"""

    score = None
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = int(input("Enter Score: "))
        elif choice == "P":
            if score is None:
                "Please Input a Score"
                score = int(input("Enter Score: "))
            else:
                get_result(score)
                print(result)
        elif choice == "S":
            if score is None:
                "Please Input a Score"
                score = int(input("Enter Score: "))
            else:
                for i in range(0, int(score), 1):
                    print("*", end='')

        else:
            print("Invalid option")
        print()
        print(MENU)
        choice = input(">>> ").upper()

    print("Goodbye.")


def get_result(score):
    global result
    if score < 0 or score > 100:
        result = "Invalid Score"
    elif score > 90:
        result = "Excellent"
    elif score > 50:
        result = "Passable"
    else:
        result = "Bad"

main()