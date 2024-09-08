import numpy as np
import statistics as stats
fd = [23,54,6,76,75,64,78,34,5,77]

a=np.array(fd)

print(np.mean(fd))# sum of all number/ num of element
print(np.median(fd)) #center value after sorting
print(stats.mode(fd)) # more time comming value
print(np.std(fd)) # standered deviation
print(np.var(fd)) # varience (square of std)


#print(np.corrcoef([a,b]))


