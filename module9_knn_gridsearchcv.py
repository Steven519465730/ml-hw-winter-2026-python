# module9_knn_gridsearchcv.py
# Mini kNN Classifier + hyperparameter search (k from 1..10) using GridSearchCV
# Data handling: NumPy
# ML + hyperparameter search: scikit-learn

import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier


def read_positive_int(prompt: str) -> int:
    while True:
        try:
            v = int(input(prompt))
            if v > 0:
                return v
            print("Error: please enter a positive integer.")
        except ValueError:
            print("Error: invalid input. Please enter an integer.")


def read_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: invalid input. Please enter a real number.")


def read_nonneg_int(prompt: str) -> int:
    while True:
        try:
            v = int(input(prompt))
            if v >= 0:
                return v
            print("Error: please enter a non-negative integer.")
        except ValueError:
            print("Error: invalid input. Please enter an integer.")


def read_pairs(num: int, set_name: str):
    """Read num pairs (x, y) from user into NumPy arrays."""
    X = np.empty((num, 1), dtype=float)  # 2D for sklearn
    y = np.empty(num, dtype=int)

    for i in range(num):
        x_val = read_float(f"Enter x for {set_name} pair {i + 1}: ")
        y_val = read_nonneg_int(f"Enter y (class label) for {set_name} pair {i + 1}: ")
        X[i, 0] = x_val
        y[i] = y_val

    return X, y


def main() -> None:
    # Read training set
    N = read_positive_int("Enter a positive integer N (training size): ")
    X_train, y_train = read_pairs(N, "TrainS")

    # Read test set
    M = read_positive_int("Enter a positive integer M (test size): ")
    X_test, y_test = read_pairs(M, "TestS")

    # Define model + hyperparameter grid
    model = KNeighborsClassifier()
    param_grid = {"n_neighbors": list(range(1, 11))}

    # Hyperparameter search via GridSearchCV (as in typical Module 9 readings)
    # Note: cv=5 requires enough samples per class; we choose cv safely.
    # We'll use up to 5 folds, but never more than N.
    cv_folds = min(5, N)
    if cv_folds < 2:
        # Not enough data for CV; fall back to a simple search without CV
        best_k = 1
        best_acc = -1.0
        for k in range(1, 11):
            if k > N:
                continue
            clf = KNeighborsClassifier(n_neighbors=k)
            clf.fit(X_train, y_train)
            acc = float(clf.score(X_test, y_test))
            if acc > best_acc:
                best_acc = acc
                best_k = k
        print(best_k)
        print(best_acc)
        return

    grid = GridSearchCV(
        estimator=model,
        param_grid=param_grid,
        scoring="accuracy",
        cv=cv_folds,
        n_jobs=None,
        refit=True,  # refit best model on full training set
    )

    # Fit grid search on training data
    grid.fit(X_train, y_train)

    # Best k found
    best_k = int(grid.best_params_["n_neighbors"])

    # Evaluate best estimator on test set
    test_accuracy = float(grid.best_estimator_.score(X_test, y_test))

    # Output: best k and corresponding test accuracy
    print(best_k)
    print(test_accuracy)


if __name__ == "__main__":
    main()