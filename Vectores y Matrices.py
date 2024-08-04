# n = int(input('ingrese el tamaño:'))
# m = int(input('Ingrese el numero de multiplos: '))
# A = []

# for i in range (0, n):
#     A.append(i * m)
    
# print(A)

#------------------------------------------------------------------------------

# import numpy as np

# a = np.array([6,7,1,2,3])

# vec = a.shape[0]

# print(vec)
# print(a[4])

#------------------------------------------------------------------------------

# ejercicio a

# import numpy as np

# numero = np.zeros(10)

# for i in range(0,10):
#     numero[i] = input("Ingrese un numero: ")
    
# print(numero)

#------------------------------------------------------------------------------

# import numpy as np

# numero = []

# for i in range(0,10):
#     numero.append (input("Ingrese un numero: "))
    
# print(numero)

#------------------------------------------------------------------------------

# import numpy as np
# suma = 0 
# prom = 0
# mayor = 000
# menor = 999999
# cont = 0
# edad = []

# for i in range (0, 10):
#     edad.append (int(input("ingrese la edad del estudiante: ")))
#     cont = cont + 1
#     suma = suma + edad[i]
#     prom = suma / cont
    
#     if edad[i] > mayor:
#         mayor = edad[i]
        
#     if edad[i] < menor:
#         menor = edad[i]
    
    
# print(suma)
# print(prom)
# print(mayor)
# print(menor)

# -----------------------------------------------------------------------------
# import numpy as np


# # Creamos la matriz de 5x5 con datos enteros aleatorios entre 1 y 10
# matriz = np.random.randint(1, 10, (5, 5))

# print(matriz)

# # Obtenemos los valores en la diagonal principal usando slicing
# diagonal_principal = np.diagonal(matriz)

# # Calculamos la suma y el promedio de los valores en la diagonal principal
# suma_diagonal = np.sum(diagonal_principal)
# promedio_diagonal = np.mean(diagonal_principal)

# # Mostramos la suma y el promedio
# print("\nSuma de la diagonal principal:", suma_diagonal)
# print("Promedio de la diagonal principal:", promedio_diagonal)

#------------------------------------------------------------------------------

# a = 1234

# b = a % 10
# c = a % 100 // 10
# d = a % 1000 // 100
# e = a % 10000 // 1000







