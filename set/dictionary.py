data={
    "name":"Himanshu",
    "age":23,
    "course":"data science"
}
print(data)

print(data["age"])

for x in data:
    print(x)

for x in data.values():
    print(x)


for x,y in data.items():
    print(x,"=",y)
