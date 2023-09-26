cadena1 = "Giovanna Valentina"
cadena2 = "hola soy vanteee"

#print(dir(cadena1)) #muestra todos los metodos de los strings (dir es funcion)

#los metodos se utilizan luego del dato seguido por un punto y luego ()

"print(cadena1.upper())" # esto convierte todo el String a MAYUSCULAS
"print(cadena1.lower())" # esto convierte todo el Sting a minusculas

# .capitalize() usamos ara convertir la primer letra del string a mayuscula usamos 
"print(cadena2.capitalize())" #convierte todo a minuscula y devuelve la primer letra en mayuscula

#  .find() usamos para buscar un string o caracter usamos
"print(cadena2.find())" #si el caracter o string buscado, se encuentra nos devuelve el indice donde esta alojado, sino devuelve -1

"print(cadena1.index())" #este metodo .index si no encuentra un valor devuelve una excepcion

# .isnumeric() o . isalpha() se usa para saber si el valor es numerico o es alfanumerico
""" print(cadena1.isnumeric()) """ #si es numerico devolvera True sino devolvera False

""" print(cadena1.isalpha()) """ #devuelve True solo si hay letras, no numeros y no caracteres especiales incluyendo ESPACIOS

# .count cuenta las coincidencias que hay de algo que buscamos. indefectiblemente se debe pasar un valor
""" print(cadena1.count("a")) """

# len() contamos la cantidad de caracteres, incluyendo los especiales, que se encuentran en un determinado string
""" print(len(cadena1)) """ #tener en cuenta que len no es un metodo en si, mas bien es una funcion que se pone antes que la varible

#.startswitch sirve para saber si un string comienza con un determinado string, se debe pasar un valor
""" print(cadena1.startswith("g")) """ #esto devuelve True o False


#.endswitch sirve para saber si un String termina con un determinado String, se le debe pasar un valor
""" print(cadena1.endswith("na")) """ #esto devuelve True o False

# .replace() reemplaza un string dado por otro string dado. se debe pasar dos valores, el que sera reemplazado por el que se va a reemplazar.
""" print(cadena1.replace("Valentina", "Roldan")) """ #en este caso reemplazamos el nombre Valentina por el apellido Roldan

#.split sirve para separar los strings por , o / segun lo requerido
