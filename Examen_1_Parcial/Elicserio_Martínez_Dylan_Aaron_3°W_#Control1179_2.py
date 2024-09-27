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
