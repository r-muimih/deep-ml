import pandas as pd

def solution(df):
    df = df.copy()

    # Step 1: trim whitespace and title-case the name column
    df['name'] = df['name'].str.strip().str.title()

    # Step 2: standardize date to YYYY-MM-DD
    df['date'] = pd.to_datetime(df['date'].str.strip()).dt.strftime('%Y-%m-%d')

    # Step 3: drop duplicate rows, keep first occurrence, reset index
    df = df.drop_duplicates(keep='first').reset_index(drop=True)

    # Step 4: fill remaining missing values in 'value' with the mean
    # of non-missing values remaining after step 3
    mean_value = df['value'].mean()
    df['value'] = df['value'].fillna(mean_value)

    return df