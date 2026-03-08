# module8_metrics-scikit.py
# Reads N (x, y) pairs where:
#   x = ground truth label (0 or 1)
#   y = predicted label (0 or 1)
# Outputs Precision and Recall using scikit-learn.
# Uses NumPy for data storage.

import numpy as np
from sklearn.metrics import precision_score, recall_score


def read_positive_int(prompt: str) -> int:
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
            print("Error: please enter a positive integer.")
        except ValueError:
            print("Error: invalid input. Please enter an integer.")


def read_binary(prompt: str) -> int:
    while True:
        try:
            val = int(input(prompt))
            if val in (0, 1):
                return val
            print("Error: please enter 0 or 1.")
        except ValueError:
            print("Error: invalid input. Please enter 0 or 1.")


def main() -> None:
    N = read_positive_int("Enter a positive integer N: ")

    y_true = np.empty(N, dtype=int)
    y_pred = np.empty(N, dtype=int)

    for i in range(N):
        x = read_binary(f"Enter x (ground truth 0/1) for point {i + 1}: ")
        y = read_binary(f"Enter y (prediction 0/1) for point {i + 1}: ")
        y_true[i] = x
        y_pred[i] = y

    # Handle edge cases: if no positive predictions or no positive labels,
    # sklearn can warn; zero_division=0 makes it return 0.0 instead.
    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred, zero_division=0)

    print(precision)
    print(recall)


if __name__ == "__main__":
    main()