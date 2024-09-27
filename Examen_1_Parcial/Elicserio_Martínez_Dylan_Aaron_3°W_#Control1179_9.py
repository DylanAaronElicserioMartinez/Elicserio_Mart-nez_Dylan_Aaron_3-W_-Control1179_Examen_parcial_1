print(" ")#imprime un espacio en blanco en la pantalla
print("Elicserio Martínez Dylan Aaron 3°W #Control:1179 este es mi examen")#imprime en la pantalla mi nombre completo, grado y grupo mas mi numero de control
print(" ")#imprime un espacio en blanco en la pantalla
# Programa para calcular el factorial de un número entero

# Función para calcular el factorial de un número
def calcular_factorial(n):
    # Inicializar el resultado del factorial en 1
    factorial = 1
    
    # Calcular el factorial usando un bucle
    for i in range(1, n + 1):
        factorial *= i  # Multiplicar el resultado por cada número desde 1 hasta n
    
    return factorial

# Función principal del programa
def main():
    try:
        # Solicitar al usuario que ingrese un número entero
        n = int(input("Ingrese un número entero para calcular su factorial: "))
        
        # Verificar si el número es no negativo
        if n < 0:
            print("El factorial no está definido para números negativos.")
        else:
            # Llamar a la función para calcular el factorial
            resultado = calcular_factorial(n)
            # Mostrar el resultado
            print(f"El factorial de {n} es {resultado}.")
    
    except ValueError:
        # Manejo de errores si el usuario no ingresa un número válido
        print("Por favor, ingrese un número entero válido.")

# Llamar a la función principal
main()
