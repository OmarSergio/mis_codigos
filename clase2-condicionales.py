#condicionales simples
""" if True :
    print("este mensaje se imprime porque el valor es verdadero") """

#condicionales en cadena
""" x = int(input("ingrese aqui su numero: \n->"))

if x == 10:
    print("el valor es correcto")
if x < 10:
    print("el valor elegido debe ser mayor")
if x > 10:
    print("el valor elegido debe ser menor") """
    
#condicoinales anidados
a = 10
b = 20

""" if a == 10:                          #si el valor de la variable no coincide, no se ejecutara el siguiente if.
    print("valor correcto")
    if b == 20:                      #si este valor coincide, se ejecuta el print, sino lo ignora.
        print("valor correcto") """

#condicionales multiples
#   and
""" a = 10
b = 20
if a == 10 and b == 20: #si el primer valor no coincide, el segundo valor ya no sera analizado y no se ejecutara la orden.
    print("ambos son verdaderos")   """  

#or
"""a = 10
b = 20
if a == 10 or b == 10: 
    print("uno de los dos es verdadero")"""

#luego el not que cambia el rol de la expresion False o True

#condicionales multiples
#el else (sino)
"""a = 10
if a == 10:
    print("correcto")
else :
    print("incorrecto")"""
    
#elif (else + if = sino si)
"""numero = int(input("ingrese aqui su numero del 1 al 5: \n->"))
if numero == 1:
    print("el numero ingresado es 1")
elif numero == 2:
    print("el numero ingresado es 2")
elif numero == 3:
    print("el numero ingresado es 3")
elif numero == 4:
    print("el numero ingresado es 4")
elif numero == 5:
    print("el numero ingresado es 5")
else :
    print("el numero ingresado es mayor a 5")"""
#calculadora
"""print("-----calculadora basica-----")
num1 = int(input("Ingrese aqui su primer numero: \n->"))
num2 = int(input("Ingrese aqui su segundo numero: \n->"))
operador = input("ingrese aqui que tipo de operacion desea realizar +, -, *, /: \n->")

if operador == "+":
    print(num1 + num2)

elif operador == "-":
    print(num1 - num2)

elif operador == "*":
    print(num1 * num2)
    
elif operador == "/":
    print(num1 / num2)"""


#Ejercicios

#1-Escribir un programa que pida al usuario su edad y muestre por pantalla si es mayor de edad (18 años o más) o no.
"""print("--Aqui sabras sabras si sos mayor de edad--")
edad_de_usuario = int(input("Ingresa aqui tu edad: \n->"))
if edad_de_usuario >= 18:
    print("Ud ya es mayor de edad, sea un adulto responsable.")
else:
    print("Aun eres un menor de edad, disfruta!")"""
    
#2-Escribir un programa que pida al usuario un número entero y muestre por pantalla si es positivo, negativo o cero.
"""numero = int(input("ingrese aqui su numero: \n->"))
if numero > 0:
    print("el numero ingresado es positivo")
elif numero < 0:
    print("el numero ingresado es negativo")
elif numero == 0:
    print("el numero ingresado es 0")"""

#3-Escribir un programa que pida al usuario dos números y muestre por pantalla cuál de ellos es mayor.
"""num1 = int(input("ingrese su primer numero: \n->"))
num2 = int(input("ingrese su segundo numero: \n->"))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
else:
    print(f"{num2} es mayor que {num1}")"""

#4-Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por pantalla si está aprobado (5 o más) o no.
""" print("--ingresa tu calificacion y averigua si aprobaste--")
calificacion = int(input("ingrese su calificacion para saber si aprobo: \n->"))
if calificacion == 10:
    print("aprobado")
elif calificacion == 9:
    print("aprobado")
elif calificacion == 8:
    print("aprobado")
elif calificacion == 7:
    print("aprobado")
elif calificacion == 6:
    print("aprobado")
else:
    print("desaprobado") """
    
#5-Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
""" numero = int(input("Ingrese un numero entero: \n->"))
if numero % 2 == 0:
    print(f"{numero} es un numero PAR.")
else:
    print(f"{numero} es un numero IMPAR.") """
    
#6-Escribir un programa que pida al usuario un número entero y muestre por pantalla si es múltiplo de 2 y de 3 a la vez.
""" numero = int(input("ingrese su numero entero: \n->"))
if numero % 2 == 0 and numero % 3 == 0:
    print("el numero ingresado es multiplo de 2 y 3")
else:
    print("este numero no es multiplo de 2 ni de 3") """
    
#7-Escribir un programa que pida al usuario un carácter y muestre por pantalla si es una letra mayúscula, una letra minúscula, un número o un carácter especial.
""" caracter = input("ingrese un caracter: \n->")
if caracter.isupper():
    print("este caracter es una letra MAYUSCULA")
elif caracter.islower():
    print("este caracter es una letra minuscula")
elif caracter.isdigit():
    print("este caracter es un numero")
else:
    print("este es un caracter especial") """
    
#8-Escribir un programa que pida al usuario una cadena de caracteres y muestre por pantalla si contiene la letra "a"
"""palabra = input("ingrese su palabra aqui: \n->")
if "a" in palabra:
    print("la palabra contiene la letra a")
elif "A" in palabra:
    print("la palabra contiene la letra A ni a")
else:
    print("la palabra no contiene una letra A ni a")"""
    
#9-Escribir un programa que pida al usuario tres números y muestre por pantalla el mayor de ellos.
""" num1 = int(input("Ingrese su 1er numero: \n->"))
num2 = int(input("Ingrese su 2do numero: \n->"))
num3 = int(input("Ingrese su 3er numero: \n->"))

if num1 > num2 and num1 > num3:
    print(f"el {num1}es mayor que {num2} y que {num3}")
elif num2 > num1 and num2 > num3:
    print(f"el {num2} es mayor que {num1} y que {num3}")
elif num3 > num1 and num3 > num2:
    print(f"el {num3} es mayor que {num1} y y que {num2}") """
    
#10-Escribir un programa que pida al usuario una letra y muestre por pantalla si es una vocal o una consonante.
""" letra = input("por favor ingrese una sola letra: \n->")
if "a" in letra or "e" in letra or "i" in letra or "o" in letra or "u" in letra:
    print("La letra ingresada es una Vocal")
elif "A" in letra or "E" in letra or "I" in letra or "O" in letra or "U" in letra:
    print("La letra ingresada es una Vocal")
else:
    print("La letra ingresada es una Consonante") """
    
#11-Escribir un programa que pida al usuario dos números y muestre por pantalla la suma de ellos solo si ambos son pares.
""" num1 = int(input("ingrese su 1er numero: \n->"))
num2 = int(input("ingrese su 2do numero: \n->"))

if num1 % 2 == 0 and num2 % 2 == 0:
    print(num1 + num2)
elif num1 % 2 != 0:
    print("No es posible realizar la operacion ya que el 1er numero ingresado no es un numero par")
elif num2 % 2 != 0:
    print("No es posible realizar la operacion ya que el 2do numero ingresado no es un numero par")
 """
""" #cuadro de login
usuario = "omarsergio"
contrasenia = "falcon779"

usuario = input("ingrese su usuario: \n->")
contrasenia = input("ingrese su contrasenia: \n->")
if usuario == "omarsergio" and contrasenia == "falcon779":
    print("acceso correcto, bienvenido al sistema")
elif usuario != "omarsergio":
    print("usuario incorrecto")
elif contrasenia != "falcon779":
    print("contrasenia incorrecta") """
