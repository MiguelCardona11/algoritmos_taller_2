import numpy as np
from multiprocessing import Pool

from ejercicio1 import crear_matriz_dispersa_aleatoria

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
    n_filas = matriz.shape[0]
    bloques = [list(range(i, min(i + tam_bloque, n_filas))) for i in range(0, n_filas, tam_bloque)]

    with Pool() as pool:
        resultados = pool.map(procesar_bloque, [(matriz, filas) for filas in bloques])

    return np.concatenate(resultados)

def ejecutarEjercicioDos():
    n_intersecciones = int(input("Ingrese la cantidad de intersecciones (filas) que tiene la ciudad, la cantidad de calles será 2^intersecciones: "))
    cant_intersecciones_por_bloque = max(1, int(n_intersecciones/4))

    # 🚦 Generar matriz dispersa de tráfico
    matriz_trafico = crear_matriz_dispersa_aleatoria(n_intersecciones)
    print(f"\nSe crea una matriz de tamaño {n_intersecciones}x{2**n_intersecciones} con valores aleatorios\n{matriz_trafico}\n")
    
    # 🏎️ Procesar tráfico en bloques
    promedio_trafico = procesamiento_en_bloques(matriz_trafico, cant_intersecciones_por_bloque)

    # 📊 Resultados finales
    print("\nPromedio de tráfico por intersección:")
    print(promedio_trafico)
    