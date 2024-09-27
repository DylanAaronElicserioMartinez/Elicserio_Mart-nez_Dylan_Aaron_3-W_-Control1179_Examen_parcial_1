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
