#diccionario (dict)
# .keys devuelve todas las llaves
diccionario = {
    "perrito" : "Tomi", #clave : valor (key : value) y se separa con comas, menos al final
    "perrita" : "Pia",
    "perrote" : "Mateo" 
}
""" print(diccionario.keys()) """

#.get devuelve todos los valores
""" print(diccionario.get("perrito")) """ #se debe agregar una clave(key) y retornara su valor(value)
""" print(diccionario.keys()) #devolvera todas las claves
print(diccionario["perrito"]) #devolvera el valor de la clave solicitada
 """

# .pop() eliminar un elemento de la lista
""" diccionario.pop("perrote")
print(diccionario) """

# .clear elimina los elementos del diccionario
""" diccionario.clear()
print(diccionario) """

# .items sirve para obtener los elementos del diccionario iterables (iterable es que se puede recorrer el interior del elemento)
""" diccionario_iterable = diccionario.items()
print(diccionario_iterable) """
