# Elicserio_Mart-nez_Dylan_Aaron_3-W_-Control1179_Examen_parcial_1
este es el examen del parcial 1 realizado en clase

#Codigo 1

print(" ")#imprime un espacio en blanco en la pantalla

print("Elicserio Martínez Dylan Aaron 3°W #Control:1179 este es mi examen")#imprime en la pantalla mi nombre completo, grado y grupo mas mi numero de control

print(" ")#imprime un espacio en blanco en la pantalla

a = "Elicserio "#le da a (a) el valor de la palabra que esta dentro de ""

b = "Martínez "#le da a (b) el valor de la palabra que esta dentro de ""

c = "Dylan "#le da a (c) el valor de la palabra que esta dentro de ""

d = "Aaron "#le da a (d) el valor de la palabra que esta dentro de ""

x = a + b + c + d# el valor (x) nos ayuda a concatenar el nombre en uno solo

y = "este es el resultado al Concatenar mi nombre"# (y) tiene el valor del texto que esta dentro de las ""

print("este es mi nombre:")#imprime en la pantalla el texto que esta dentro de ""

print(a)#imprime en la pantalla el valor de (a)

print(b)#imprime en la pantalla el valor de (b)

print(c)#imprime en la pantalla el valor de (c)

print(d)#imprime en la pantalla el valor de (d)

print(y)#imprime en la pantalla el valor de (y)

print(x)#imprime en la pantalla el valor de (x)

print(" ")#imprime en la pantalla un espacio en blanco

print("y haci seria mi nombre en mayusculas:")#imprime en la pantalla el texto que esta dentro de las ""

print(x.upper())#imprime en la pantalla el valor de (x) en mayusculas

![image](https://github.com/user-attachments/assets/9826109c-a118-482e-a65e-05f5a9a35629)
![image](https://github.com/user-attachments/assets/eb5bb5ff-9eac-4459-9632-38616ed59851)

#Codigo 2

#Solicitar al usuario que ingrese el primer numero

numero1=input("ingresa el primer numero:")

#Conversion del primer numero caracter entero

num1=int(numero1)

#Solicitar al usuario que ingrese el sugundo numero

numero2=input("ingresa el segundo numero:")

#Conversion del segundo numero a caracter entero

num2=int(numero2)

#Solicitar al usuario que ingrese el tercer numero

numero3=input("ingresa el tercer numero:")

#Conversion del tercer numero a caracter entero

num3=int(numero3)

#

if num1 == num2 :#si el primer y segundo numero son iguales te avisara y no te dejara continual

  print("el primer numero y el segundo numero son iguales nose puede")#imprimira en la pantalla lo que este dentro de ""
  
elif num2 == num3:#si el segundo y tercer numero son iguales te avisara y no te dejara continual

  print("el segundo numero y el tercer numero son iguales no se puede")#imprimira en la pantalla lo que este dentro de ""
  
elif num1 == num3:#si el primer y tercer numero son iguales te avisara y no te dejara continual

  print("el primer numero y el tercer numero son iguales no se puede")#imprimira en la pantalla lo que este dentro de ""
  
#

if num1 > num2 > num3 :#si el primer numero es mayor al segundo y el segundo es mayor al tercero te lo dira

    print("el primer numero es mayor al segundo y el segundo es mayor al tercero")#imprimira en la pantalla lo que este dentro de ""
    
elif num1 > num2 < num3 > num1 :#si el primer numero es mayor al segundo y el segundo es menor al tercero pero el tercero es mayor al primero te lo dira

    print("el primer numero es mayor al segundo pero el segundo es menor al tercero y el tercero es mayor al primero")#imprimira en la pantalla lo que este dentro de ""
    
elif num1 > num2 < num3 < num1 :#si el primer numero es mayor al segundo y el segundo es menor al tercero pero el tercero es menor al primero te lo dira

    print("el primer numero es mayor al segundo pero el segundo es menor al tercero y el tercero es menor al primero")#imprimira en la pantalla lo que este dentro de ""
    
exit#terminara el programa en este punto

#

if num2 > num1 > num3 :#si el segundo numero es mayor al primero y el primero es mayor al tercero te lo dira

    print("el segundo numero es mayor al primero y el primero es mayor al tercero ")#imprimira en la pantalla lo que este dentro de ""
    
elif num2 > num1 < num3 > num2 :#si el segundo numero es mayor al primero y el primero es menor al tercero pero el tercero es mayor al segundo te lo dira

 print("el segundo numero es mayor al primero pero el primero es menor al tercero y el tercero es mayor al segundo")#imprimira en la pantalla lo que este dentro de ""
 
elif num2 > num1 < num3 < num2 :#si el segundo numero es mayor al primero y el primero es menor al tercero pero el tercero es menor al segundo te lo dira

 print("el segundo numero es mayor al primero pero el primero es menor al tercero y el tercero es menor al segundo")#imprimira en la pantalla lo que este dentro de ""
 
exit#terminara el programa en este punto

#

if num3 > num2 > num1 :#si el tercer numero es mayor al segundo y el segundo es mayor al primero te lo dira

 print("el tercer numero es mayor al segundo y el segundo es mayor al primero")#imprimira en la pantalla lo que este dentro de ""
 
elif num3 > num2 < num1 > num3 :#si el tercer numero es mayor al segundo y el segundo es menor al primero pero el primero es mayor al tercero te lo dira

 print("el tercer numero es mayor al segundo y el segundo numero es menor al primer numero y el primer numero es mayor al tercero")#imprimira en la pantalla lo que este dentro de ""
 
elif num3 > num2 < num1 < num3 :#si el tercer numero es mayor al segundo y el segundo es menor al primero pero el primero es menor al tercero te lo dira

 print("el tercer numero es mayor al segundo y el segundo numero es menor al primer numero y el primer numero es menor al tercero")#imprimira en la pantalla lo que este dentro de ""
 
exit#terminara el programa en este punto

![image](https://github.com/user-attachments/assets/d4aaab03-bb2c-45dc-a7b3-0a0339d9d590)

![image](https://github.com/user-attachments/assets/52217f7d-cb7b-415d-b242-723319d7b4ad)

![image](https://github.com/user-attachments/assets/c6dcc974-f263-463d-9b3c-5dec64926b89)


#Codigo 3

#Solicitar al usuario que ingrese el primer numero

numero1=input("ingresa el primer numero:")

#Conversion del primer numero caracter entero

num1=int(numero1)

#Solicitar al usuario que ingrese el sugundo numero

numero2=input("ingresa el segundo numero:")

#Conversion del segundo numero a caracter entero

num2=int(numero2)

#

if num1 == num2 :#si el primer y segundo numero son iguales te avisara y no te dejara continual

  print("el primer numero y el segundo numero son iguales nose puede")#imprimira en la pantalla lo que este dentro de ""
  
#

if num1 > num2   :#si el primer numero es mayor al segundo te lo dira

    print("el primer numero es mayor al segundo")#imprimira en la pantalla lo que este dentro de ""
    
elif num1 < num2   :#si el primer numero es menor al segundo te lo dira

 print("el primer numero es menor al segundo")#imprimira en la pantalla lo que este dentro de ""
 
exit#terminara el programa en este punto

#

print(" ")

suma = num1 + num2

print("y el resultado de la suma es:")

print(suma)

print(" ")

![image](https://github.com/user-attachments/assets/bd1ae218-c045-4439-8c18-cec25f5a02f4)

![image](https://github.com/user-attachments/assets/899890d9-5e9a-4067-a9a1-43538886cef5)

#Codigo 4

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

 ![image](https://github.com/user-attachments/assets/08498da6-f0af-4b14-9a18-070039cbd8a5)
 ![image](https://github.com/user-attachments/assets/db890b06-b83c-435d-b62c-a6628accc06b)

#Codigo 5

print(" ")#imprime un espacio en blanco en la pantalla

print("Elicserio Martínez Dylan Aaron 3°W #Control:1179 este es mi examen")#imprime en la pantalla mi nombre completo, grado y grupo mas mi numero de control

print(" ")#imprime un espacio en blanco en la pantalla

#favor de ingresar un numero

#practica de menor a la primera docena 1-12

numero=int(input("ingrese un numero:"))#instruccion if,else para determinar

#proseso if else pqara verificar que es correcto

if numero == 12:#numero limite #if

    print("el numero es igual a cero")
    
elif numero < 12:

    print("esta bien ")#si el numero es menor a 12 esta bien

else:#else

    print("pasa el limite establecido")#sale si el numero indicado es mayor a 12

![image](https://github.com/user-attachments/assets/b0fd8eea-0688-4b82-8d45-890c339ed750)
![image](https://github.com/user-attachments/assets/c3c7577a-dcd7-49e6-a1ad-c9b1c5b37ef7)

#Codigo 6

print(" ")#imprime un espacio en blanco en la pantalla

print("Elicserio Martínez Dylan Aaron 3°W #Control:1179 este es mi examen")#imprime en la pantalla mi nombre completo, grado y grupo mas mi numero de control

print(" ")#imprime un espacio en blanco en la pantalla

#solicitar al usuario que ingrese un numero

numero=int(input("ingrese un numero:"))

#verificar si el numero es 0

if numero == 0:

    print("el mumero es cero.")
    
#verficar si el numero es par

elif numero % 2 == 0:

    print("el numero es par")
    
#si este numero es par,sera impar

else:

    print("el numero es impar")

![image](https://github.com/user-attachments/assets/d7caa272-0b44-476b-8925-ba5de8c14919)
![image](https://github.com/user-attachments/assets/8c9375c3-a0c6-4cbb-887e-b3b270ae6adf)

#Codigo 7

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
    
![image](https://github.com/user-attachments/assets/7656ad73-e624-49cb-92d3-771f470638fb)

![image](https://github.com/user-attachments/assets/45d76ce9-a825-4eeb-a3c5-43eac1e132ed)

#Codigo 8

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


![image](https://github.com/user-attachments/assets/96762f11-030e-43bc-9243-8c5a2e97e632)

![image](https://github.com/user-attachments/assets/087f4109-c198-412c-b93e-348d44d3789c)

![image](https://github.com/user-attachments/assets/4a044e83-fb73-4efa-9c26-2be5268a3b29)

![image](https://github.com/user-attachments/assets/dd73157b-70cb-487e-820c-325f72d2053b)
