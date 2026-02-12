# module5_mod.py

class NumberProcessor:
    def __init__(self):
        self.numbers = []

    def insert_number(self, number):
        self.numbers.append(number)

    def search_number(self, target):
        if target in self.numbers:
            return self.numbers.index(target) + 1  # Return 1-based index
        else:
            return -1
