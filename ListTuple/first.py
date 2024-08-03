#Index of all element index that same to first element

fruit=['pear','orange','apple','pear','banana','apple']
print(fruit.index('orange'))

#remove all element in list

fruit=['pear','orange','apple','pear','banana','apple']
fruit.clear()
print(fruit)

#remove

fruit=['pear','orange','apple','pear','banana','apple']
fruit.remove('banana')
print(fruit)

#concrate 2 list

list1=['pear','orange','apple','pear','banana','apple']
list2=['pearr','orange','apple','banana','watermalen']
list1.extend(list2)    #l3=list1+list2
print(list1)

#add 2 list rule 2

list1=['pear','orange','apple','pear','banana','apple']
list2=['pearr','orange','apple','banana','watermalen']

for x in list2: 
    list1.append(x) 
print(list1)

