# Algoritmo triaPascal

# Solicitar el número de filas
filas = int(input("Ingrese las filas que desea ver: "))

print("!!Triángulo de Pascal con ciclo for!!")

# Bucle para generar las filas del triángulo de Pascal
for i in range(filas):
    coef = 1
    
    # Imprimir los espacios antes de los números
    for j in range(filas - i, 0, -1):
        print(" ", end="")
    
    # Imprimir los coeficientes del triángulo de Pascal
    for j in range(i + 1):
        print(int(coef), end=" ")  # Convertimos coef a entero para que no muestre decimales
        coef = coef * (i - j) // (j + 1)  # Actualizar coeficiente usando división entera
        
    print()  # Saltar a la siguiente línea
