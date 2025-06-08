import pandas as pd

def load_data(filepath):
    """Load data from a CSV file."""
    return pd.read_csv(filepath)

def save_data(data, filepath):
    """Save data to a CSV file."""
    data.to_csv(filepath, index=False)

def display_head(data, n=5):
    """Display the first n rows of the DataFrame."""
    return data.head(n)

def check_missing_values(data):
    """Check for missing values in the DataFrame."""
    return data.isnull().sum()