import pandas as pd
import numpy as np

def linear_regression(X, y):
    
    # Testing input and output types
    if (type(X) != np.ndarray and type(X) != pd.core.frame.DataFrame):
        raise Exception("Please provide either NumPy array or Pandas DataFrame as input variable.")
    
    if (type(y) != np.ndarray and type(y) != pd.core.series.Series):
        raise Exception("Please provide either NumPy array or Pandas Series as output variable.")

    # Turning data types into NumPy Array
    X = np.array(X)
    y = np.array(y)
    
    # Testing data types
    if (X.dtype != "float" and X.dtype != "int"):
        raise Exception("Please provide numeric inputs.")
    if (y.dtype != "float" and y.dtype != "int"):
        raise Exception("Please provide numeric outputs.")

    N = X.shape[0]
    K = X.shape[1]
    
    # Find and drop NaN values
    y_nan_indices = [i for i in range(len(y)) if np.isnan(y[i])]
    X_nan_indices = [item[0] for item in np.argwhere(np.isnan(X))]
    nan_indices = list(set(X_nan_indices).union(set(y_nan_indices)))
    X = X[[i for i in range(len(X)) if i not in nan_indices], :]
    y = y[[i for i in range(len(y)) if i not in nan_indices]]
    
    # Adding constant variable
    X = np.concatenate([np.ones(X.shape[0], dtype=np.int64).reshape(X.shape[0], 1), X], axis=1)

    # Calculate coefficients, standard errors and confidence intervals
    coefficients = (np.linalg.inv(X.T @ X) @ X.T) @ y
    e = y - (X @ coefficients)
    sigma_squared = (e.T @ e) / (N - K - 1)
    variance_beta_hat = sigma_squared * np.linalg.inv(X.T @ X)
    standard_errors = np.sqrt(variance_beta_hat.diagonal())
    confidence_intervals = np.array([[coefficients[i] - (2.0 * (standard_errors[i])), coefficients[i] + (2.0 * (standard_errors[i]))] for i in range(3)])
    
    return [coefficients, standard_errors, confidence_intervals]