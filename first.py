import math
import random
#1 = int(input("Number of outcomes for 1: \n"))
#7 = int(input("Number of outcomes for 2: \n"))



sample_space = list()
setA =set()
setB =set()
for i in range(1,7):
        group = list()
        for j in range(1,7):
          group.append(i)
          group.append(j)
          copy = tuple(group.copy())
          sample_space.append(copy)
          group.clear()
for i in sample_space:
       if i[0] == i[1]:
          setA.add(i)
for i in sample_space:
      if i[0] + i[1]==6:
          setB.add(i)
A_intersect_B = setA.intersection(setB)
A_union_B = setA.union(setB)
num_sample_space =len(sample_space)  
num_setB_items =len(setB)
num_setA_items =len(setB) 
print(sample_space)
print(setA)
print(setB)  
print(A_intersect_B)  
print(A_union_B) 
print(num_sample_space)    
   



