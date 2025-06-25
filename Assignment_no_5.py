print("QUESTION NO 1 : panda series")
import pandas as pd
#for dictionary :
sports  = {"football":"day1",
           "basketball":"day2",
           "volleyball":"day3"
           }
sp = pd.Series(sports)
print(sp)

#for list :
ls = [1,2,10,]
dp = pd.Series(ls)
print("panda series")
print(dp)
print(type(dp))
print("list")
print(dp.tolist())
print(type(dp.tolist()))

#Access element in series
print("in dictionary:",sp[0])
print("in list ",dp[1])
print("slicing :",dp.iloc[1:3])