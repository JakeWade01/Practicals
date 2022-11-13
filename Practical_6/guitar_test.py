from guitar import Guitar

name = "Gibson L-5 CES"
year = 1972
cost = 16035.40

info = Guitar(name, year, cost)
print(info)
print(info.get_age())
print(info.is_vintage())
