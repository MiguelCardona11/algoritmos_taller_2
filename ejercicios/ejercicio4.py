import random
import time
import tracemalloc

def ejecutarEjercicioCuatro():
    # Número de muestras/puntos
    N = 10**6  # 1 millón

    def monte_carlo_pi(n):
        inside = 0
        for _ in range(n):
            x = random.random()
            y = random.random()
            if x*x + y*y <= 1:
                inside += 1
        return (4 * inside) / n

    def exhaustive_pi(grid_size):
        inside = 0
        total = 0
        step = 1.0 / grid_size
        for i in range(grid_size):
            for j in range(grid_size):
                x = i * step
                y = j * step
                if x*x + y*y <= 1:
                    inside += 1
                total += 1
        return (4 * inside) / total

    # ---- MONTE CARLO ----
    print("Monte Carlo:")
    tracemalloc.start()
    start = time.time()
    pi_mc = monte_carlo_pi(N)
    end = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"π ≈ {pi_mc}")
    print(f"Tiempo: {end - start:.4f} segundos")
    print(f"Memoria pico: {peak / 1024:.2f} KB")

    # ---- ENFOQUE EXHAUSTIVO ----
    print("\nExhaustivo:")
    grid = int(N**0.5)  # Para igualar el total de puntos (N ≈ grid^2)
    tracemalloc.start()
    start = time.time()
    pi_ex = exhaustive_pi(grid)
    end = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"π ≈ {pi_ex}")
    print(f"Tiempo: {end - start:.4f} segundos")
    print(f"Memoria pico: {peak / 1024:.2f} KB")