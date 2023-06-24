from generarMatriz import calcular_suma_columnas, calcular_suma_filas


def test_programa():
    # Prueba con una matriz 3x3.
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    suma_filas = calcular_suma_filas(matriz)
    suma_columnas = calcular_suma_columnas(matriz)

    assert suma_filas == [6, 15, 24]
    assert suma_columnas == [12, 15, 18]

    test_programa()
