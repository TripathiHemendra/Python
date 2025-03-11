from datetime import datetime

now=datetime.now()

date=now.strftime("%d-%m-%Y")
print(date)

time=now.strftime("%H:%M:%S")
print(time)