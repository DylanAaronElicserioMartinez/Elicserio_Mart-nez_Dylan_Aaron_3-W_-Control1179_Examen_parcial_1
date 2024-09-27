print(" ")#imprime un espacio en blanco en la pantalla
print("Elicserio Martínez Dylan Aaron 3°W #Control:1179 este es mi examen")#imprime en la pantalla mi nombre completo, grado y grupo mas mi numero de control
print(" ")#imprime un espacio en blanco en la pantalla
# Función para calcular el perímetro y el área de un rectángulo
def calcular_rectangulo(base, altura):
    # Calcula el área del rectángulo
    area = base * altura
    # Calcula el perímetro del rectángulo
    perimetro = 2 * (base + altura)
    return area, perimetro

# Solicitar al usuario que ingrese la base y la altura
try:
    base = float(input("Ingrese la base del rectángulo (b): "))
    altura = float(input("Ingrese la altura del rectángulo (h): "))
    
    # Llamar a la función para calcular área y perímetro
    area, perimetro = calcular_rectangulo(base, altura)
    
    # Mostrar los resultados
    print(f"Área del rectángulo: {area}")
    print(f"Perímetro del rectángulo: {perimetro}")

except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")
    