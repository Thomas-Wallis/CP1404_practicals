CURRENT_YEAR = 2020
VINTAGE = 50

class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        return self.get_age() >= VINTAGE


