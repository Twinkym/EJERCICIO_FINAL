import random

def generar_matriz(n):
    """
    Genera una matriz de tamaño NxN y la llena de nums aleatorios del 0 - 9;
    Args n (int): Tamaño de la matriz.
    devuelve list de matriz generada.
    """

    matriz = []
    for _ in range(n): 
        fila = []
        for __ in range(n):
                fila.append(random.randint(0, 9))
        matriz.append(fila)
    return matriz

"""
  Imprime en pantalla el contenido de una lista de matrices
"""
def imprimir_matriz(matriz):
    for fila in matriz:    
        print(fila)

"""
     Calcula y devuelve la  suma de los elementos 
     de cada fila de una matriz dada.
     Args matriz (list of lists
"""
def calcular_suma_filas(matriz): 
     # Creamos un vector
    suma_filas = [0] * len(matriz[0]) 
    for fila in matriz:
          for i in range(len(suma_filas)):
             suma_filas[i]+=fila[i]
    return  suma_filas

"""
   Calcula y devuelve la  suma de los elementos 
   de cada columna

"""
def calcular_suma_columnas(matriz):
    suma_columnas=[0]*len(matriz[0])
    for fila in matriz:
         for i in range(len(suma_columnas)):
            suma_columnas[i] += fila[i]
            return suma_columnas


"""
Imprime la suma de cada fila en pantalla.
"""
def imprimir_suma_filas(suma_filas):
    print("La suma de las columnas es:", end=" ")
    for elemento in enumerate(suma_filas):
         if elemento != len(suma_filas)-1 :
                    print("%d + ")

"""
Imprime la suma de cada columna en pantalla.
"""
def imprimir_suma_columnas(suma_columnas):
    print("\nLa suma de las filas es:",end="")
    for elemento in enumerate(suma_columnas):
     if elemento!=len(suma_columnas)-1:
                 print("%d + ")

try:
    n = int(input('Ingrese el tamaño de la matriz: ')) 
    matriz = generar_matriz(n)

    imprimir_matriz(matriz)

    suma_filas = calcular_suma_filas(matriz)
    suma_columnas = calcular_suma_columnas(matriz)

    imprimir_suma_filas(suma_filas)
    imprimir_suma_columnas(suma_columnas)

except ValueError as e:
        print ("Error, ingrese un número válido")