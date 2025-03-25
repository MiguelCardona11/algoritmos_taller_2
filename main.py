from ejercicios.ejercicio1 import ejecutarEjercicioUno
from ejercicios.ejercicio2 import ejecutarEjercicioDos
from ejercicios.ejercicio3 import ejecutarEjercicioTres

def main():
    while True:
        print("\nMenú:")
        print("1 - Ejecutar ejercicio 1")
        print("2 - Ejecutar ejercicio 2")
        print("3 - Ejecutar ejercicio 3")
        print("4 - Ejecutar ejercicio 4")
        print("5 - Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            ejecutarEjercicioUno()
        elif opcion == "2":
            ejecutarEjercicioDos()
        elif opcion == "3":
            ejecutarEjercicioTres()
        elif opcion == "99":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()