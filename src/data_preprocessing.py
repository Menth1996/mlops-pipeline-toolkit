import pandas as pd
from sklearn.model_selection import train_test_split

def preprocess_data(data_path):
    """
    Loads raw data, performs basic preprocessing, and splits into train/test sets.
    """
    df = pd.read_csv(data_path)
    # Example preprocessing: fill missing values, one-hot encode categorical features
    df = df.fillna(df.mean(numeric_only=True))
    # Assuming the last column is the target variable
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test
