import pandas as pd
import mysql.connector

con =mysql.connector.connect(host="localhost",
                            user="root",
                            password="1234",
                            database="pizza")


cur =con.cursor()

query = 'select * from pizzas'
cur.execute(query)
data = cur.fetchall()
print(data)

#df = pd.read_sql(quiry)
#print(df)
# con.close()
# print("Connection successfuly created")

