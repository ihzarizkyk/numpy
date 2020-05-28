import numpy as np

# Indexing & Slicing

# Array 1 Dimensi

h = np.array([1,2,3])

print(h[0])

#Output = 1

# Array 2 Dimensi 

i = np.array([[1,2,3],[4,5,6]])

print(i[0][1])

# i[element array][index ke berapa]
#Output = 2

#Slicing 

j = np.array([1,2,3,4])

print(j[:1])
print(j[:2])
print(j[2:])
print(j[1:])
print(j[1:3])

'''
Output :
[1] 
[1 2]
[3 4]
[2 3 4]
[2 3]
'''
