import pandas as pd


df = pd.read_csv("customers-500000.csv", nrows=100)

print("Data Overview:")
print(df.head())
print("\nData Info:")
print(df.info())


for col in df.columns:
    if "date" in col.lower() or "time" in col.lower():
        try:
            df[col] = pd.to_datetime(df[col], dayfirst=True)

            print(f"Converted '{col}' to datetime.")
        except:
            print(f"Could not convert '{col}'.")

print("\nMissing Values:")
print(df.isnull().sum())

df = df.drop_duplicates()


if 'gender' in df.columns:
    print("\n Gender Distribution:")
    print(df['gender'].value_counts())

if 'city' in df.columns:
    print("\nTop 10 Cities by Customer Count:")
    print(df['city'].value_counts().head(10))
