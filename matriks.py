import numpy as np

# Matriks

matriksA = np.array([[1,2],
                     [2,1]])
matriksB = np.array([[2,2],
                     [1,1]])   

perkalian_biasa = matriksA*matriksB
perkalian_matriks1 = np.dot(matriksA,matriksB)
perkalian_matriks2 = matriksA.dot(matriksB)

print("Perkalian Biasa Matriks : ")
print(perkalian_biasa)

print("Perkalian Matriks Cara 1 : ")
print(perkalian_matriks1)

print("Perkalian Matriks Cara 2 : ")
print(perkalian_matriks2)

'''
Output :

Perkalian Biasa Matriks : 
[[2 4]
 [2 1]]
Perkalian Matriks Cara 1 : 
[[4 4]
 [5 5]]
Perkalian Matriks Cara 2 : 
[[4 4]
 [5 5]]

'''
