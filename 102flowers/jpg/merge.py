import pandas as pd
excel1  ="single.xlsx"
excel2 = "multi_core.xlsx"
excel3 = "multi_thread.xlsx"

df1 = pd.read_excel(excel1)
df2 = pd.read_excel(excel2)
df3 = pd.read_excel(excel3)

print(df3)

dataframe = [df1, df2]

join = pd.concat(dataframe)
join.to_excel("output.xlsx")