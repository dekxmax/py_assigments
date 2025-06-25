print("QUESTION NO 1: convert data into time series")
import pandas as pd
df = pd.DataFrame( {"col1":range(6),
                    "col2":["A","B"] * 3,
                    "date":pd.to_datetime(["2010-01-02","2020-06-07"] * 3)})
print(df)
