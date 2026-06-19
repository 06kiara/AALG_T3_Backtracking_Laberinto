laberinto = [
['F', 1, 1, 1, 0, 1, 1, 1, 1],
[-2, 0, 0, -1, 0, 1, 0, 1, 0],
[1, 1, 0, 1, 1, 1, 0, 1, 0],
[0, 1, 0, -1, 0, 0, 0, -1, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 0],
[-1, 0, 0, 0, 0, 0, 0, 1, 1],
[1, 1, 1, 1, -1, 1, 1, 1, 0],
[1, 0, 0, 1, 0, 1, 0, 1, 0],
['I', 1, -1, 1, 1, 1, 0, 1, 1]
]

print("LABERINTO ORIGINAL:\n")

for fila in laberinto:
    print(fila)

FILAS = 9
COLUMNAS = 9

solucion = [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)]

movimientos = [
    (1, 0),   # abajo
    (0, 1),   # derecha
    (-1, 0),  # arriba
    (0, -1)   # izquierda
]

def es_valido(fila, columna, visitados):
    return (
        0 <= fila < FILAS and
        0 <= columna < COLUMNAS and
        laberinto[fila][columna] != 0 and
        (fila, columna) not in visitados
    )

def costo_vida(valor):
    if valor == -1:
        return 1
    elif valor == -2:
        return 2
    return 0    

def backtracking(fila, columna, vidas, visitados):

    print(f"Posición: ({fila},{columna}) | Vidas: {vidas}")

    if fila == 0 and columna == 0:
        solucion[fila][columna] = 1
        return True

    visitados.add((fila, columna))
    solucion[fila][columna] = 1

    for df, dc in movimientos:

        nueva_fila = fila + df
        nueva_columna = columna + dc

        if es_valido(nueva_fila, nueva_columna, visitados):

            valor = laberinto[nueva_fila][nueva_columna]

            if valor == 'F' or valor == 'I':
                perdida = 0
            else:
                perdida = costo_vida(valor)

            nuevas_vidas = vidas - perdida

            if nuevas_vidas > 0:

                if backtracking(
                    nueva_fila,
                    nueva_columna,
                    nuevas_vidas,
                    visitados
                ):
                    return True

    solucion[fila][columna] = 0
    visitados.remove((fila, columna))

    return False

print("\nBuscando salida...\n")

if backtracking(8, 0, 3, set()):

    print("\nSALIDA ENCONTRADA\n")

    for fila in solucion:
        print(fila)

else:

    print("\nNO EXISTE CAMINO VÁLIDO")