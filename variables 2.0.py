#desempaquetado - foma de desencapsular variables - tuplas, listas , conjuntos - NO desempaqueta numeros
""" tupla = ("Giovanna", "Roldan") 
nombre, apellido = tupla
print(nombre, apellido)

lista = ["Omar", "Roldan"]
nombre, apellido = lista
print(apellido)

conjunto = {"Gisela", "Villalba"}
nombre, apellido = conjunto
print(apellido) """

#crear tupla con tuple
""" tupla = tuple("dato1", "dato2") """

#creando tupla sin tuple
""" tupla = "dato3,", "dato4" """

#para crear una tupla de un solo dato
""" tupla = "dato5", """   #agregamos el primer dato y una coma al final

#creando conjuntos con set()
""" conjunto = set(["dato1", "dato2"]) #el dato que se le pasa debe ser entre corchetes
print(conjunto) """

#creando diccionario
""" diccionario = dict(nombre = "Giovanna", apellido = "Roldan")
print(diccionario) """

#guardamos notas de los alumnos de 3ro B en un diccionario "notas 3ro B"
notas_3ro_B = {}

keys = input("Ingrese el nombre del alumno: \n->")
value   = input(f"Ingrese la nota del alumno {keys}: \n->")

notas_3ro_B[keys] = value

print(notas_3ro_B)




            

#creando diccionario con las claves(keys) vacias
""" diccionario = dict.fromkeys(["nombre"])  #esto crea diccionarios con las clves None 
print(diccionario) #si le pasamos el dato sin corchetes creara un dict con cada letra del string recibido """

