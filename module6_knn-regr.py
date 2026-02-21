# module6_knn-regr.py
# k-NN Regression (1D input X -> output Y) using NumPy

import numpy as np


class KNNRegressor1D:
    def __init__(self):
        self.x = np.array([], dtype=float)
        self.y = np.array([], dtype=float)

    def fit(self, x_vals, y_vals):
        self.x = np.asarray(x_vals, dtype=float)
        self.y = np.asarray(y_vals, dtype=float)

    def predict(self, x_query, k):
        if k <= 0:
            raise ValueError("k must be a positive integer.")
        if self.x.size == 0:
            raise ValueError("No training data provided.")
        if k > self.x.size:
            raise ValueError("k cannot be greater than N (number of points).")

        xq = float(x_query)
        # distances in 1D: |x_i - xq|
        dists = np.abs(self.x - xq)

        # indices of k nearest neighbors (use argpartition for efficiency)
        knn_idx = np.argpartition(dists, k - 1)[:k]

        # simple k-NN regression: average of neighbor y values
        return float(np.mean(self.y[knn_idx]))


def read_positive_int(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val > 0:
                return val
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a real number.")


def main():
    N = read_positive_int("Enter a positive integer N: ")
    k = read_positive_int("Enter a positive integer k: ")

    # Read N (x, y) points
    x_vals = np.empty(N, dtype=float)
    y_vals = np.empty(N, dtype=float)

    for i in range(N):
        x_vals[i] = read_float(f"Enter x for point {i + 1}: ")
        y_vals[i] = read_float(f"Enter y for point {i + 1}: ")

    X = read_float("Enter query value X: ")

    model = KNNRegressor1D()
    model.fit(x_vals, y_vals)

    if k > N:
        print("Error: k must be less than or equal to N.")
        return

    try:
        y_pred = model.predict(X, k)
        print(y_pred)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()