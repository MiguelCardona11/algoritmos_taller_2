import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse import save_npz
import os

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

def crear_y_guardar_matriz(n):
    """
    Crea una matriz dispersa de tamaño n x 2^n con valores aleatorios y la guarda en un archivo NPZ.
    """
    matriz_dispersa = crear_matriz_dispersa_aleatoria(n)
    carpeta_destino = "matrices"
    # Crear la carpeta si no existe
    os.makedirs(carpeta_destino, exist_ok=True)
    
    nombre_archivo = os.path.join(carpeta_destino, f"matriz_dispersa_{n}.npz") # Construir la ruta completa del archivo
    save_npz(nombre_archivo, matriz_dispersa) # Guardar como NPZ (formato disperso, más eficiente)
    
    print(f"--> Matriz dispersa guardada en {nombre_archivo} en formato CSR")
    return matriz_dispersa

def ejecutarEjercicioUno():
    n = int(input("Ingrese la cantidad de filas de la matriz dispersa (n): "))
    matriz_dispersa = crear_y_guardar_matriz(n)
    
    print(f"\nSe crea una matriz de tamaño {n}x{2**n} con valores aleatorios\n{matriz_dispersa}\n")

    vector = np.random.rand(2**n)
    print(f"A manera de ejemplo, se crea un vector de longitud {2**n} con valores aleatorios\n{vector}")

    # Multiplicación de matriz dispersa por vector denso
    resultado = matriz_dispersa @ vector  # Equivalente a matriz_dispersa.dot(vector)
    print("\nSe multiplica la matriz dispersa por el vector, resultado:\n", resultado)
