# Algoritmo conteoDigitos

# Solicitar el número hasta donde se va a contar
cantidad = int(input("Ingrese un número hasta donde va a contar: "))
print("Los números son:")

# Bucle for desde 0 hasta la cantidad ingresada
for i in range(0, cantidad + 1):
    print(i, end=" ")  # Mostrar los números sin salto de línea
