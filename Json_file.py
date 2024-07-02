import json

x = '{ "name":"Himanshu", "age":21, "city":"mumbai"}'

y = json.loads(x)

print(y["name"])