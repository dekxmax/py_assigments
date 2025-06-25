print("QUESTION NO 3: data iteration")
import pandas as pd
print("data iteration")
data = {
    "name":["sagar","vipul","tapesh"],
    "marks":[70,80,90]}
df = pd.DataFrame(data)
print("1:Using iterrows():")
for index, row in df.iterrows():
    print(index, row["name"], row["marks"])

print("2:select row with condition")
ds = df[df["marks"] == 90]
print(ds)

print("3: select any row using iloc")
diloc = df.iloc[1:2]
print(diloc)

print("4:limited rows selection with column")
selc = df.loc[1:2,"marks"]
print(selc)

print("5: drop the rows")
dr = df[df["marks"] != 90]
print(dr)

print("6:insert ")
new_row = pd.DataFrame([{"name": "amit", "marks": 95}])
dyz = pd.concat([df.iloc[:1], new_row, df.iloc[1:]]).reset_index(drop=True)
print(dyz)

print("7: list")
ls = df.values.tolist()
print(ls)