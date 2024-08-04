import numpy as np


def TotaVotos(m):
    Vector1 = np.zeros(5)
    for j in range (0, 5):
        suma = 0
        for i in range(0, 5):
            suma = suma + m[i,j]
        Vector1[j] = suma
    return Vector1


def TotaRegion(n):
    Vector2 = np.zeros(5)
    for i in range(0, 5):
        suma = 0
        for j in range(0, 5):
            suma = suma + n[i,j]
        Vector2[i] = suma
    return Vector2

def Mayor(p):
    Vector3 = np.zeros(5)
    for i in range(0, 5):
        mayor = -9999
        for j in range(0, 5):
            if p[i,j] > mayor:
                mayor = p[i,j]
                partido = j
        Vector3[i] = partido
    return Vector3

def Prom(V):
    prom = np.zeros(5)
    for i in range(0, 5):
        prom[i] = V[i] / 5
    return prom


matriz = np.array([[340, 345, 567, 458, 145],
                   [540, 457, 125, 104, 100],
                   [830, 910, 860, 450, 782],
                   [120, 457, 411, 555, 888],
                   [130, 140, 150, 160, 125]])

TOTAL_VOTOS = TotaVotos(matriz)
TOTA_REGION = TotaRegion(matriz)
MAY_CANTIDAD = Mayor(matriz)
PROM = Prom(TOTA_REGION)
