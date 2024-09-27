# Algoritmo tablaDeNumero

# Solicitar la tabla de multiplicar y el límite de la multiplicación
delNumero = int(input("Ingrese la tabla que desea ver: "))
multiplicador = int(input("Ingrese el límite de la multiplicación: "))

# Bucle for para generar la tabla de multiplicar
for multiplicando in range(0, multiplicador + 1):
    resultado = multiplicando * delNumero
    print(delNumero, "X", multiplicando, "=", resultado)
