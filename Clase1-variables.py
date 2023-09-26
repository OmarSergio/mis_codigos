"""n = "hola" #comentario...
print(n)
n = 15
print(n)
n = "perrito"
print(n)

i = 12
print(i)
print(type(i))
nombre = "Omar \'Loco' Roldan" #para podr colocar comillas, en un string
print(nombre)


x = 5
respuesta = "el numero es " + str(x)
print(respuesta)"""
#1-Escribe un programa que solicite al usuario su nombre y lo imprima en la pantalla
"""nombre = input("Ingrese aqui su nombre: ")
print(nombre)"""

#2-Escribe un programa que solicite al usuario su nombre y luego imprima un mensaje de bienvenida
"""nombre = input("ingrese aqui su nombre: ")
respuesta = "bienvenido/a " + nombre + " a la Comunidad"
print(respuesta)"""
#3-Crea un programa que pida al usuario su edad y lo imprima en pantalla.
"""edad = input("ingrese aqui su edad ")
respuesta = f"su edad es {edad}"
print(respuesta)"""

#4-Crea un programa que calcule la suma de dos números y lo imprima en pantalla.
"""numero1 = int(input("ingrese aqui su 1er numero: "))
numero2 = int(input("ingrese aqui su 2do numero: "))
print(numero1 + numero2)"""

#5-Crea un programa que pida al usuario dos números enteros y muestre en pantalla su cociente y su resto.
"""numero1 = int(input("Ingrese aqui su 1er numero: "))
numero2 = int(input("Ingrese aqui su 2do numero: "))
resultado = f"El cociente es {numero1 / numero2} y el resto es {numero1 % numero2}."
print(resultado)"""

#6-Crea un programa que pida al usuario el radio de un círculo y calcule su área.
# La fórmula A = pi * r^2. Luego, muestra en pantalla el resultado. Supongamos que pi = 3.1416
"""radio = float(input("Ingrese aqui el radio: "))
area = f"el area de su circulo es {3.1416 * radio**2}."
print(area)"""

#7-Escribe un programa que calcule el área de un triángulo a partir de la base y la altura dadas. El área de un triángulo es igual a base por altura partido por 2.
"""base = float(input("ingrese aqui la base: "))
altura = int(input("ingrese aqui la altura: "))
area = f"el area del triangulo es de {base * altura / 2}"
print(area)"""

#8-Crea un programa que pida al usuario el radio de un círculo y muestre su diámetro, su circunferencia y su área. Supón que pi es aproximadamente 3.14159.
""" radio = float(input("Ingrese aqui el radio: \n->"))
diametro = 2 * radio
circunferencia = 2 * 3.14159 * radio
area = radio**2 * 3.14159
print(f"el diametro es de {diametro}cm, la circunferencia es de {circunferencia}cm y el area es de {area}cm") """


#10-Crea un programa que pida al usuario una cantidad en dólares y la convierta a euros. Supón que el tipo de cambio es de 0.84 euros por dólar.
"""dolares_cantidad = float(input("Ingrese cantidad de dolares a convertir: \n->"))
euro_coti = 0.84
cantidad_de_euros =  dolares_cantidad * euro_coti
print(cantidad_de_euros)"""

#11-Crea un programa que pida al usuario una palabra y muestre en pantalla cuántas letras tiene.
"""cantidad_de_caracteres = input("Ingrese aqui su palabra: ")
print(len(cantidad_de_caracteres))"""

#12-Escribe un programa que solicite al usuario su fecha de nacimiento en formato dd/mm/aaaa y luego imprima su edad en años.
""" edad_del_usuario = input("Ingrese aqui su fechade nacimiento en formato dd/mm/aaaa: ")
dia, mes, anio = edad_del_usuario.split("/")
dia = int(dia)
mes = int(mes)
anio = int(anio)
respuesta = f"la edad del usuario segun su fecha de nacimiento ingresada es {2023 - anio} años"
print(respuesta)"""

#13-Escribe un programa que solicite al usuario su nombre y su edad, y luego imprima un mensaje que indique cuántos años tendrá el usuario en 10 años más.
"""nombre_del_usuario = input("ingrese aqui su nombre: ")
edad_del_usuario = int(input("Ingrese aqui su edad: "))
respuesta = f"el usuario {nombre_del_usuario} tiene {edad_del_usuario} años y en 10 años mas tendra {edad_del_usuario + 10} años de edad"
print(respuesta)"""

#14-Escribe un programa que solicite al usuario un número entero y luego imprima el doble y el triple de ese número.
""" numero_entero = int(input("Ingrese aqui su numero: "))
resultado = f"el doble del numero {numero_entero} es {numero_entero * 2} y el triple de dicho numero es {numero_entero * 3}"
print(resultado) """

#15-Escribe un programa que solicite al usuario una temperatura en grados Celsius y luego imprima la temperatura equivalente en grados Fahrenheit.
# La fórmula para convertir de Celsius a Fahrenheit es: F = (C * 1.8) + 32.
""" print("-----conversor de temperatura C a F-----")
temperatura_Celsius = int(input("ingrese aqui la temperatura en grados Celsius: "))
resultado = f"la temperatura de {temperatura_Celsius} grados Celsius, es igual a {(temperatura_Celsius * 1.18) + 32} grados Fahrenheit"
print(resultado) """

#16-Escribe un programa que solicite al usuario su peso y su altura, y luego calcule e imprima su índice de masa corporal (IMC).
#La fórmula para calcular el IMC es: IMC = peso / (altura ** 2).
""" print("-----calculadora de masa corporal-----")
peso = float(input("Ingrese aqui su peso: \n->"))
altura = float(input("Ingrese aqui su altura: \n->"))
masa_corporal = f"Su indice de masa corporal es {peso / (altura ** 2)}."
print(masa_corporal) """

#17-Escribe un programa que solicite al usuario dos palabras y luego las imprima en orden inverso.
#Por ejemplo, si el usuario ingresa "hola" y "mundo", el programa debe imprimir
#"mundo hola".
""" print("-----bienvenido al inversor de texto-----")
palabra1 = input("ingrese aqui su primer palabra: \n->")
palabra2 = input("ingrese aqui su segunda palabra: \n ->")
print(palabra2 + " " + palabra1) """

#18-Crea un programa que pida al usuario su nombre, su edad y su ciudad de residencia, y lo muestre en pantalla Utilizando una sola línea de código.
""" nombre = input("ingrese aqui su nombre: \n->")
edad = int(input("ingrese aqui su edad: \n->"))
ciudad = input("ingrese aqui su ciudad: \n ->")
respuesta = f"su nombre es {nombre}, tiene {edad} anios de edad y su ciudad de residencia es {ciudad}."
print(respuesta) """

#19-Escribe un programa que solicite al usuario un número decimal y luego imprima la parte entera y decimal por separado.
""" numero_decimal = float(input("Ingrese aqui su numero decimal: \n->"))
parte_entera = int(numero_decimal)
parte_decimal = float(numero_decimal - parte_entera)
respuesta = f"el numero {parte_entera} es la parte entera y el {parte_decimal} es la parte decimal."
print(respuesta) """

