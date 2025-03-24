import numpy as np
from scipy.sparse import lil_matrix

def crear_matriz_dispersa_aleatoria(cantidad_filas):
    """
    Crea una matriz dispersa de tamaño n x 2^n con valores aleatorios y de una densidad estipulada, usando el formato LIL para facilitar la inserción.
    Luego la convierte a formato CSR para eficiencia en cálculos.
    """
    densidad = 0.3
    cantidad_columnas = 2 ** cantidad_filas
    matriz_dispersa = lil_matrix((cantidad_filas, cantidad_columnas), dtype=np.float32)
    num_datos = max(1, int(cantidad_filas * cantidad_columnas * densidad)) # si el resultado es 0, devolver 1

    filas = np.random.randint(0, cantidad_filas, num_datos)
    columnas = np.random.randint(0, cantidad_columnas, num_datos)
    valores = np.random.randint(1, 100, num_datos)

    matriz_dispersa[filas, columnas] = valores

    return matriz_dispersa.tocsr()

def ejecutarEjercicioUno():
    n = int(input("Ingrese la cantidad de filas de la matriz dispersa (n): "))
    matriz_dispersa = crear_matriz_dispersa_aleatoria(n)
    
    print(f"\nSe crea una matriz de tamaño {n}x{2**n} con valores aleatorios\n{matriz_dispersa}\n")

    vector = np.random.rand(2**n)
    print(f"A manera de ejemplo, se crea un vector de longitud {2**n} con valores aleatorios\n{vector}")

    # Multiplicación de matriz dispersa por vector denso
    resultado = matriz_dispersa @ vector  # Equivalente a matriz_dispersa.dot(vector)
    print("\nSe multiplica la matriz dispersa por el vector, resultado:\n", resultado)
