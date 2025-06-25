print("QUESTION NO 2 : data frame ")
import pandas as pd
# make dataframe
d = [
    [2,3,4],
    [1,4,5],
    [2,9,0]
]
ps = pd.DataFrame(d)
print(ps)

print(" using dictionary")
dic = ({
    "day1":'football',
    "day2":"baseball",
    "day3":[30,50,60]
})
t  = pd.DataFrame(dic)
print(t)
print("using list of lists")
ls = [
    [10,20,30],
    [35,60,40]
]
lt = pd.DataFrame(ls)
print(lt)
# using list of turple
print("using list of turple")
tl = [
    (1,3),
    (5,8)
]
tls = pd.DataFrame(tl)
print(tls)
print("using list of dicts")
dy = [
    {"name":"sanat","marks":75},
    {"name":"vipul","marks":99}
]
dys = pd.DataFrame(dy)
print(dys)