
class Project:

    def __init__(self, name, date, priority, cost, completion):
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __repr__(self):
        return f"{self.name}, start: {self.date}, priority {self.priority}, estimate ${self.cost}, completion {self.completion}%"