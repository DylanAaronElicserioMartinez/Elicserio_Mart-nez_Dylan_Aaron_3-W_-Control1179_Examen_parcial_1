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
