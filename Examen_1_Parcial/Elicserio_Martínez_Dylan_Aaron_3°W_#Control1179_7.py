print(" ")#imprime un espacio en blanco en la pantalla
print("Elicserio Martínez Dylan Aaron 3°W #Control:1179 este es mi examen")#imprime en la pantalla mi nombre completo, grado y grupo mas mi numero de control
print(" ")#imprime un espacio en blanco en la pantalla
# Solicitar un número entero al usuario
numero = int(input("Ingresar un número entero porfavor: "))

# Verificar si el número es divisible por 7 y mayor a 40
if numero > 40 and numero % 7 == 0:
    print(f"este número {numero} es divisible por 7 y es mayor a 40.")
else:
    print(f"este número {numero} no cumple con las condiciones.")
