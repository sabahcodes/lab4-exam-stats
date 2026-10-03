import pandas as pd
import numpy as np
from scipy import stats

# Exam scores of 10 students (2 missing)
scores = pd.Series([72, 65, 88, np.nan, 54, 91, 76, np.nan, 83, 69])

# (a) Descriptive statistics
print(scores.describe())

# (b) Skewness and kurtosis (after dropping missing values)
clean = scores.dropna()
print("Skewness:", stats.skew(clean))
print("Kurtosis:", stats.kurtosis(clean))

# (c) Count missing values
print("Missing values:", scores.isnull().sum())

# (d) Fill missing values with the mean
filled = scores.fillna(scores.mean())
print("Filled scores:")
print(filled)