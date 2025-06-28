print("QUESTION NO 2: date time")
import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "join_date": ["2023-01-15", "2022-12-30", "2021-05-10", "2024-06-01"],
    "last_login": ["2025-06-01", "2025-06-25", "2025-05-20", "2025-06-26"]
}

df = pd.DataFrame(data)


df["join_date"] = pd.to_datetime(df["join_date"])
df["last_login"] = pd.to_datetime(df["last_login"])

print("Original DataFrame with datetime columns:")
print(df)
print()

# Extract parts from datetime
df["year"] = df["join_date"].dt.year
df["month"] = df["join_date"].dt.month
df["day"] = df["join_date"].dt.day
df["weekday"] = df["join_date"].dt.day_name()

print(" Extracted date components:")
print(df[["name", "join_date", "year", "month", "day", "weekday"]])
print()


filtered = df[df["join_date"] > "2022-01-01"]
print("Users who joined after Jan 1, 2022:")
print(filtered)
print()


df["days_since_join"] = (pd.Timestamp.now() - df["join_date"]).dt.days
print(" Days since each user joined:")
print(df[["name", "join_date", "days_since_join"]])
print()

df["days_between_login"] = (df["last_login"] - df["join_date"]).dt.days
print(" Days between joining and last login:")
print(df[["name", "join_date", "last_login", "days_between_login"]])
print()

df_ts = df.set_index("join_date")
monthly_users = df_ts.resample("M").count()["name"]
print(" User count by join month:")
print(monthly_users)
