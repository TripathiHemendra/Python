import pandas as pd

data={"Name":["Ansh","Himanshu","Riya"],
       "Age":[20,21,19],
       "Salary":[33000,50000,20000]}
print(pd.DataFrame(data)) 

#data from taken excel file or csv file

#data=pd.read_csv("customer.csv")
data2=pd.read_excel("D:\student.xlsx")
# print(data2)
# print(data2.info())
#print(data2.describe())
print(data2.isnull().sum())

