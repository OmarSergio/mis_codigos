""" #dato compuestos
lista = ["aca", "se agregan los datos", "que queremos"] #los elementos de las listas se pueden modificar. se usan corchetes para crearlas

tupla = ("aca", "se agregan los datos", "que queremos") #los elementos de las tuplas no se pueden modificar se usan parentesis para crearlas """

#cada palabra debe llevar "" y se separan con ,


#print(lista["ubicacion de lo que queremos"]) #cuando se llama a imprimir un indice de la tupla o lista, se usa corchetes (elemento1 = indice0) 
#para poder imprimir un recorte de la lista se debe pasar el dato entre corchetes y desde que numero de indice hasta que numero, separados por :
#print(0:2) asi imprimimos desde el indice 0 al 2 / print(2:) asi imprimimos desde el indice numero 2 hasta el final de la lista
#conjunto o set
""" conjunto = {"aca", "se agregan los datos", "que queremos"} #se usan llaves para crearlas y no se puede modificar su contenido.
#pero se puede redefinir. no se puede imprimir por indice y no se repiten los valores.
#print(conjunto[2]) esto no se puede hacer, ya que no se accede a su indice. """

#diccionario (dict)
""" diccionario = {
    "perrito" : "Tomi", #clave : valor (key : value) y se separa con comas, menos al final
    "perrita" : "Pia",
    "perrote" : "Mateo" 
}  """

#lista_de_compras = [input("listado de cosas para comprar:\n->")]


#reloj alarma
""" alarma_debe_sonar = float(input("ingrese aqui la hora:\n->"))
if alarma_debe_sonar == 7.00:
    print("Hora de levantarse")
elif alarma_debe_sonar > 7.00:
    print("te dormiste, pescado")
elif alarma_debe_sonar < 7.00:
    print("duerme un rato mas") """

#cambiar la primer letra del String a mayuscula si es que no la tiene
""" if cadena1.startswith("g"):
    print(cadena1.capitalize())
else:
    print("no es necesario convertir la primera letra en mayuscula porque ya lo es") """
    
    
#metodos para que el usuario ingrese datos a una lista
""" frutas = []

ingreso1 = input("Ingrese aqui su fruta favorita: \n->")
#ingreso2 = input("Ingrese aqui su fruta favorita: \n->")
#ingreso3 = input("Ingrese aqui su fruta favorita: \n->")

frutas.append(ingreso1)
#frutas.append(ingreso2)
#frutas.append(ingreso3)

print(frutas) """

""" cosas = []

ingreso = input("ingresa aqui lo que queres guardar: \n->")
cosas.append(ingreso)

print(cosas) """

#Registro de notas y solicitud de recuperatorio
""" notas_alumnos_aprobados = {}
recuperatorio = {}
print("--------------------------------------------------------------------------------------------------------")
print("Bienvenido, Aqui podra registrar su nota si aprobo el examen o solicitar recuperatorio si es necesario")
print("--------------------------------------------------------------------------------------------------------")
nota_del_alumno = int(input("Por favor ingrese la nota de su examen: \n->"))

if nota_del_alumno >= 6:
    print("a continuacion ingrese los datos que le seran solicitados para poder registrarse como alumno aprobado")
    nombre_del_alumno = input("Ingrese su nombre completo: \n->")
    nota = int(input("ingrese su nota obtenida en el examen: \n->"))
    
    notas_alumnos_aprobados[nombre_del_alumno] = nota
    print(f"Registro exitoso. Felicitaciones {nombre_del_alumno} por aprobar el ultimo examen del curso de programacion. Muchos exitos en tu nueva etapa")
    print("--------vemos en el siguiente print que quedo registrado con exito.--------")
    print(notas_alumnos_aprobados)

else:
    print("a continuacion ingrese los datos que le seran solicitados para poder solicitar un recuperatorio")
    print("recuerde tener a mano su DNI")
    print("-------------------------------------------------------------------------------------------------------")
    nombre_del_alumno_que_recupera = input("ingrese nombre del completo del alumno que solicita recuperar el examen: \n->")
    dni_del_alumno_que_recupera = int(input("ingrese el numero de DNI del alumno que solicita recuperar el examen: \n->"))
    
    recuperatorio[nombre_del_alumno_que_recupera] = dni_del_alumno_que_recupera
    print(f"Sr {nombre_del_alumno_que_recupera}, ud ha sido registrado para el proximo examen recuperatorio")
    print("el dia y horario del examen les seran enviados a su correo registrado en el sistema.")
    print("recuerde que el dia del examen debe traer su DNI, caso contario no podra cursar el examen")
    print("--en el siguiente print vemos que el registro se realizo con exito--")
    print(recuperatorio) """
    


""" notas_alumnos_aprobados = {}
recuperatorio = {}
print("--------------------------------------------------------------------------------------------------------")
print("Bienvenido, Aqui podra registrar su nota si aprobo el examen o solicitar recuperatorio si es necesario")
print("--------------------------------------------------------------------------------------------------------")
que_desea_hacer = input("Ud desea registarse en la lista de alumnos aprobados? responda SI o No: \n->")

if que_desea_hacer.lower() == "si":
    print("a continuacion ingrese los datos que le seran solicitados para poder registrarse como alumno aprobado")
    nombre_del_alumno = input("Ingrese su nombre completo: \n->")
    nota = int(input("ingrese su nota obtenida en el examen: \n->"))
    
    notas_alumnos_aprobados[nombre_del_alumno] = nota
    print(f"Registro exitoso. Felicitaciones {nombre_del_alumno} por aprobar el ultimo examen del curso. Muchos exitos en tu nueva etapa")
    print("--------vemos en el siguiente print que quedo registrado con exito.--------")
    print(notas_alumnos_aprobados)

elif que_desea_hacer.lower() == "no": 
    print("a continuacion ingrese los datos que le seran solicitados para poder solicitar un recuperatorio")
    print("recuerde tener a mano su DNI")
    print("-------------------------------------------------------------------------------------------------------")
    nombre_del_alumno_que_recupera = input("ingrese nombre del completo del alumno que solicita recuperar el examen: \n->")
    dni_del_alumno_que_recupera = int(input("ingrese el numero de DNI del alumno que solicita recuperar el examen: \n->"))
    
    recuperatorio[nombre_del_alumno_que_recupera] = dni_del_alumno_que_recupera
    print(f"Sr {nombre_del_alumno_que_recupera}, ud ha sido registrado para el proximo examen recuperatorio")
    print("el dia y horario del examen les seran enviados a su correo registrado en el sistema.")

    print("recuerde que el dia del examen debe traer su DNI, caso contario no podra cursarlo")
    print("--en el siguiente print vemos que el registro se realizo con exito--")
    print(recuperatorio)

else:
    print("la respuesta solicitada no es correcta. Debe ingresar Si o No como respuesta") """
    
    #adivina el color
""" print("-----ADIVINA EL COLOR DEL VEHICULO-----")

auto = input("Ingrese el color que Ud cree que es el auto: \n->")
    
if auto.lower() == "rojo":
    print("win")
    
else:
    print("looser")
    print("----------------------------------------------------------------------------------------------------------------")

moto = input("Ingrese el color que Ud cree que es la moto: \n->")

if moto.lower() == "blanca":
    print("win")

else:
    print("looser") """