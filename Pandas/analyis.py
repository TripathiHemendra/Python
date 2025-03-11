import pandas as pd
from ydata_profiling import ProfileReport


#data from taken excel file or csv file

data=pd.read_csv("D:\himanshu\housing.csv")
print(data)

profile = ProfileReport(data)
profile.to_file(output_file="housing.html")

