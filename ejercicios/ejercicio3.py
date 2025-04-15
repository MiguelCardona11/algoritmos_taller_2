from multiprocessing import Pool
import numpy as np
import time
import os
import tracemalloc
from ejercicios.ejercicio1 import crear_y_guardar_matriz
from scipy.sparse import load_npz

def procesar_bloque(args):
    """
    Calcula el promedio de tráfico en un bloque de intersecciones.
    """
    matriz, filas = args
    promedios = matriz[filas, :].mean(axis=1)  # Promedio de autos por intersección
    print(f"Procesado bloque de intersecciones {filas[0]} a {filas[-1]}")
    return np.array(promedios).flatten()

def procesamiento_en_bloques(matriz, tam_bloque):
    """
    Divide la matriz en bloques de filas y los procesa en paralelo.
    """
    n_filas = matriz.shape[0] # shape[0]: obtener el número de filas de la matriz
    bloques = [list(range(i, min(i + tam_bloque, n_filas))) for i in range(0, n_filas, tam_bloque)]
    print(f"bloques: {bloques}")

    with Pool() as pool:
        resultados = pool.map(procesar_bloque, [(matriz, filas) for filas in bloques])

    return np.concatenate(resultados)

def ejecutarEjercicioTres():
    n_intersecciones = int(input("Ingrese la cantidad de intersecciones (filas) que tiene la ciudad, la cantidad de calles será 2^intersecciones: "))
    tam_bloque = max(1, int(n_intersecciones/4))

    nombre_archivo_npz = os.path.join("matrices", f"matriz_dispersa_{n_intersecciones}.npz")

    if os.path.exists(nombre_archivo_npz):
        print(f"\nCargando matriz desde {nombre_archivo_npz}...")
        matriz_trafico = load_npz(nombre_archivo_npz)
    else:
        print(f"\nNo se encontró la matriz, generando una nueva...")
        crear_y_guardar_matriz(n_intersecciones)
        matriz_trafico = load_npz(nombre_archivo_npz)

    print(f"\nSe utiliza una matriz de tamaño {n_intersecciones}x{2**n_intersecciones} con valores aleatorios\n{matriz_trafico}\n")
    
    # Procesar tráfico en bloques
    inicio = time.time()
    tracemalloc.start()
    promedio_trafico = procesamiento_en_bloques(matriz_trafico, tam_bloque)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    fin = time.time()

    print(f"\nPromedio de tráfico por intersección: \n{promedio_trafico}")
    print(f"\nTiempo de ejecución: {fin - inicio:.4f} segundos")
    print(f"Memoria pico: {peak / 1024:.2f} KB")
    