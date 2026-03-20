import numpy as np
import matplotlib.pyplot as plt
import csv

def resolver_sistema():
    print("Resolviendo un sistema de ecuaciones lineales ... ")

    # Definir una matriz de coeficientes y un vector de términos independientes
    A = np.array([[3, 1, -1], [2, 4, 1], [-1, 2, 5]])
    b = np.array([4, 1, 1])

    # Resolver el sistema Ax = b
    try:
        x = np.linalg.solve(A, b)
        print("Solución del sistema:")
        for i, valor in enumerate(x, start=1):
            print(f"x{i} = {valor :. 4f}")
        return x
    except np.linalg.LinAlgError:
        print("El sistema no tiene solución o tiene infinitas soluciones.")
        return None

def graficar_soluciones(soluciones):
    if soluciones is not None:
        print("Generando gráfico de las soluciones ... ")

    # Crear un gráfico de barras para visualizar las soluciones
    etiquetas = [f"x{i}" for i in range(1, len(soluciones) + 1)]
    plt.bar(etiquetas, soluciones, color=['blue', 'green', 'red' ])
    plt.title("Soluciones del Sistema de Ecuaciones")
    plt.xlabel("Variables")
    plt.ylabel("Valores")
    plt.grid(axis='y', linestyle=' -- ', alpha=0.7)