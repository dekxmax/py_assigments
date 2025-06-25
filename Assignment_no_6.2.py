print("QUESTION NO 2 : dataframe merge and join  ")
import pandas as pd
df1 = pd.DataFrame({"name":["A1","A2","A3"],
                      "sub":["s1","s2","s3"],
                      "id":[1,2,3]},
                     index=[1,2,3])
df2  = pd.DataFrame({"name":["r1","r2","r3"],
                      "sub":["s2","s4","s7"],
                      "id":[1,2,3]},
                     index=[1,2,3])
print("inner join ")
inner = df2.merge(df1,on="id",how="inner")
print(inner)
print("\n")
print("left join ")
left = df2.merge(df1,on="id",how="left")
print(left)
print("\n")
right = df2.merge(df1,on="id",how="right")
print(right)
print("\n")
df1_index = df1.set_index("id")
df2_index = df2.set_index("id")
indexs = df2_index.join(df1_index, how="inner", lsuffix='_df2', rsuffix='_df1')
print(indexs)