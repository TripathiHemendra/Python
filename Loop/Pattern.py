      
# p = 1
# for i in range(1,6):
#     for n in range(p):
#         print(i,end=" ")
#     p=p+1
#     print()


# for i in range(1,6):
#     for j in range(1,6):
#         if(i==1 or i==2 or i==3 or i==4):
#             print("*",end="")
#             break
#         print("*",end=" ")
#     print()


def print_X_pattern(size):
    for row in range(size):
        for col in range(size):
            # Print '*' at the diagonals
            if col == row or col == size - row - 1:
                if(row==0 or row==6):
                    print("*", end='')
            else:
                print(' ', end='')
        print()
size = 7
print_X_pattern(size)

          
        
               