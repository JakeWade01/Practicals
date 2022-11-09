#  Program 1
user_name = input("What is your name?:")
user_name_file = open("name.txt", 'w')
print(user_name, file=user_name_file)
user_name_file.close()

input("Press any key to continue... ")

#  Program 2
user_name_file = open("name.txt", 'r')
user_name = user_name_file.readline()
print(f"Your name is: {user_name}")

input("Press any key to continue... ")

#  Program 3
number_file = open("numbers.txt", 'r')
number_one = int(number_file.readline())
number_two = int(number_file.readline())
number_total = number_one + number_two
print(number_total)
number_file.close()

input("Press any key to continue... ")

#  Program 4
total = 0
with open("numbers.txt") as n:
    for line in n:
        total += int(line)
print(total)
