import pandas as pd


def load_data(filepath="student_data_50.csv"):
    """Reads the CSV file and returns it as a pandas DataFrame (a table)."""
    return pd.read_csv(filepath)


def save_results(df, filepath="output_results.csv"):
    """Writes a DataFrame back out to a CSV file."""
    df.to_csv(filepath, index=False)
    