
class GuitarList:

    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __repr__(self):
        return f"The {self.name} made in {self.year}, costs ${self.cost}"
