<<<<<<< HEAD
for i in range(1, 21, 2):
    print(i, end=' ')
print()

for j in range(0, 100, 10):
    print(j, end=' ')
print()

for k in range(20, 1, -1):
    print(k, end=' ')
print()
print()

no_of_stars = int(input("How Many Stars?: "))

print("Number of Stars:", no_of_stars)
for l in range(0, no_of_stars, 1):
    print("*", end='')
print()

for m in range(0, no_of_stars, 1):
    stars_counter = no_of_stars - (no_of_stars - m)
    for o in range(0, stars_counter + 1, 1):
        print("*", end='')
    print()
=======
for i in range(1, 21, 2):
    print(i, end=' ')
print()

for j in range(0, 100, 10):
    print(j, end=' ')
print()

for k in range(20, 1, -1):
    print(k, end=' ')
print()
print()

no_of_stars = int(input("How Many Stars?: "))

print("Number of Stars:", no_of_stars)
for l in range(0, no_of_stars, 1):
    print("*", end='')
print()

for m in range(0, no_of_stars, 1):
    stars_counter = no_of_stars - (no_of_stars - m)
    for o in range(0, stars_counter + 1, 1):
        print("*", end='')
    print()
>>>>>>> efb4c5ef487ad18a03dd9b8d1be76683032a0863
