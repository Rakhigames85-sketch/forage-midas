import pandas as pd

def test_output_file_exists():
    df = pd.read_csv('output.csv')
    assert len(df) > 0  # file khali nahi honi chahiye

def test_columns():
    df = pd.read_csv('output.csv')
    assert list(df.columns) == ['Date', 'Region', 'Sales']