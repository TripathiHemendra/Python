import pandas as pd

data={"Name":["Ansh","Himanshu","Riya"],
       "Age":[20,21,19],
       "Salary":[33000,50000,20000]}
print(pd.DataFrame(data)) 

#data from taken excel file or csv file

data=pd.read_csv("customer.csv")
data=pd.read_excel("customer.xlsx")
