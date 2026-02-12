# module5_oop.py

class NumberProcessor:
    def __init__(self):
        self.numbers = []

    def insert_number(self, number):
        self.numbers.append(number)

    def search_number(self, target):
        if target in self.numbers:
            return self.numbers.index(target) + 1  # 1-based index
        else:
            return -1

def main():
    processor = NumberProcessor()

    while True:
        try:
            N = int(input("Enter a positive integer N: "))
            if N > 0:
                break
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    for i in range(N):
        while True:
            try:
                num = int(input(f"Enter number {i+1}: "))
                processor.insert_number(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    try:
        X = int(input("Enter the number to search for (X): "))
        result = processor.search_number(X)
        print(result)
    except ValueError:
        print("Invalid input for X.")

if __name__ == "__main__":
    main()
