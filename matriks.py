import numpy as np

matriksA = np.array([[1,2],
                     [2,1]])
matriksB = np.array([[2,2],
                     [1,1]])   

perkalian_biasa = matriksA*matriksB
perkalian_matriks = np.dot(matriksA,matriksB)

print("Perkalian Biasa Matriks : ")
print(perkalian_biasa)

print("Perkalian Matriks : ")
print(perkalian_matriks)

'''
Output :



'''
