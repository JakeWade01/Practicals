"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():

    score = float(input("Enter score: "))
    get_result(score)
    print(result)
    score = random.randint(0, 100)
    print(score)
    get_result(score)
    print(result)


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



