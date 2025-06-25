import pandas as pd
print("QUESTION NO 3: Concatenate and Merge")
df1 = pd.DataFrame({
    "id": [1, 2],
    "name": ["Alice", "Bob"]
})

df2 = pd.DataFrame({
    "id": [3, 4],
    "name": ["Charlie", "David"]
})

df3 = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "marks": [85, 90, 75, 80]
})

combined = pd.concat([df1, df2], axis=0)

print("\n")
print(combined)

merged = pd.merge(combined, df3, on="id")

print("\n")
print(merged)
