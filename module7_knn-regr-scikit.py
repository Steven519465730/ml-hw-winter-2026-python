import numpy as np
from sklearn.neighbors import KNeighborsRegressor


def read_positive_int(prompt: str) -> int:
    while True:
        try:
            val = int(input(prompt))
            if val > 0:
                return val
            print("Error: please enter a positive integer.")
        except ValueError:
            print("Error: invalid input. Please enter an integer.")


def read_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: invalid input. Please enter a real number.")


def main() -> None:
    # Read N and k
    N = read_positive_int("Enter a positive integer N: ")
    k = read_positive_int("Enter a positive integer k: ")

    if k > N:
        print("Error: k must be less than or equal to N.")
        return

    # Read N (x, y) points
    x_vals = np.empty(N, dtype=float)
    y_vals = np.empty(N, dtype=float)

    for i in range(N):
        x_vals[i] = read_float(f"Enter x for point {i + 1}: ")
        y_vals[i] = read_float(f"Enter y for point {i + 1}: ")

    # Variance of labels in training set
    y_variance = float(np.var(y_vals, ddof=0))  # population variance

    # Read query X
    X = read_float("Enter query value X: ")

    # Prepare data for scikit-learn (X must be 2D: shape (N, 1))
    X_train = x_vals.reshape(-1, 1)
    y_train = y_vals
    X_query = np.array([[X]], dtype=float)

    # k-NN Regression (Scikit-learn)
    model = KNeighborsRegressor(n_neighbors=k, weights="uniform", metric="minkowski", p=2)
    model.fit(X_train, y_train)
    y_pred = float(model.predict(X_query)[0])

    # Output results
    print(y_pred)
    print(y_variance)


if __name__ == "__main__":
    main()