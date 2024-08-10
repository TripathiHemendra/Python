# l=input("Enter the string: ")
# b=list(filter(lambda a: a in 'aeiouAEIOU',l))
# if len(l)==0:
#     print("No vowel in this string")
# else:
#     print("Vowel in string is",b)

l=input("Enter the string: ")
b=list(filter(lambda a: a in 'aeiouAEIOU',l))
if len(b)==0:
    print("no vowel in string")
else:
    print("Vowel in string is: ",b)



