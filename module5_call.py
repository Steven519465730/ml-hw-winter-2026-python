# module5_call.py

from module5_mod import NumberProcessor

def main():
    processor = NumberProcessor()

    # Ask user for N
    while True:
        try:
            N = int(input("Enter a positive integer N: "))
            if N > 0:
                break
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Read N numbers
    for i in range(N):
        while True:
            try:
                num = int(input(f"Enter number {i+1}: "))
                processor.insert_number(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    # Ask for X and search
    try:
        X = int(input("Enter the number to search for (X): "))
        result = processor.search_number(X)
        print(result)
    except ValueError:
        print("Invalid input for X.")

if __name__ == "__main__":
    main()
