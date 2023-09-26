#las listas [list]
lista = list(["Giovanna", "Valentina", 8, "35 kilos"]) #las listas se crean entre corchetes
""" print(lista) """

#con len() podemos saber la cantidad de elementos que tiene una lista
""" len(lista) """

# .append se usa para agregar un elemento a la lista, lo agrega en el ultimo indice, es decir al final de la lista
""" lista.append("loro") #se le pasa el elemento solo entre parentesis
print(lista) """
#.insert() se usa para agregar un elemento a la lista, en el indice que se quiere. se le pasa dos valores, indice y elemento
""" lista.insert(0, "bella") #primero le pasamos el indice y luego el valor. le pasamos los datos entre parentesis 
print(lista) """

#.extend usamos para agregar varios elementos a una lista, se le debe pasar otra lista []
""" lista.extend(["tarambanita", "9/10", 2014])
print(lista) """

# .pop() se usa para eliminar un elemento de la lista.
""" lista.pop(0) #se le pasa el indice del elemento que queremos eliminar. si pasamos el indice (-1) elimina el ultimo elemento de la lista 
print(lista)
lista.pop(-2) #(-1) elimina el anteultimo, (-2) el antepenultimo
print(lista) """

# .remove() se usa para eliminar un elemento por su valor
""" lista.remove(8)
print(lista)
lista.remove("Valentina")
print(lista) """

# .clear para vaciar la lista
""" print(lista)
lista.clear()
print(lista) """

# .sort() ordena la lista numerica, incluye Trues y Falses, de manera ascendente poniendo primero Trues y Falses
""" lista1 = list([1, 2, 10, 8, 7, 1000, 100])
lista1.sort() #si hay caracteres alfanumericos dara error. para ordenarlos al reves, de mayor a menor se agrega .sort(reverse = True)
print(lista1) """

# .reverse invierte la la lista
""" lista.reverse()
print(lista) """

# .index busca elementos completos en las listas
""" print(lista.index("Valentina")) """

#cambiar un valor en dentro de la lista
lista["numero del index del elemento que sera modificado"] = "nuevo elemento"

