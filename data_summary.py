import pandas as pd
import numpy as np

# Function to view data summary
def basic_summary(df):
    print("Shape of data:", df.shape)
    print("\nDataFrame Info:")
    print("-" * 50)
    print(df.info())
    print("\nDescriptive Statistics:")
    print("-" * 50)
    print(df.describe(include=[np.number]))
    print("\nMissing Values Summary:")
    print("-" * 50)
    #print(df.isnull().sum())
    missing = df.isnull().sum()
    missing_percent = (missing / len(df)) * 100
    missing_df = pd.DataFrame({
        'Missing Values': missing,
        'Percentage (%)': missing_percent.round(2)
    })
    print(missing_df)
    print("\nNo. of Duplicates")
    print("-" * 50)
    #print("Number of duplicate rows:", df.duplicated().sum())

    duplicate_count = df.duplicated(subset=['odometer', 'vin']).sum()
    print("Number of duplicate rows (by odometer, vin):", duplicate_count)



