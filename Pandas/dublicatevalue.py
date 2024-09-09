import pandas as pd
data2=pd.read_excel("D:\student.xlsx")

print(data2.duplicated(["department"]).sum())
