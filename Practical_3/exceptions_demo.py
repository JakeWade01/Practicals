
"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
print("Finished.")

"""
When will a ValueError occur?
 - A value error will occur when the user inputs a non-number input
When will a ZeroDivisionError occur?
 - A zero division error will occur when the user inputs "0" for the denominator
Could you change the code to avoid the possibility of a ZeroDivisionError?
 - Make the user input denominator a 2nd time so there is no zero error
"""