# el bucle for sirve para iterar (recorrer) una lista, es decir llama a cada valor por separado, cuando se itera toda la lista el bucle se detiene
animales = ["perro", "gato","loro", "chivo"]
numeros = [15, 13, 12, 21]

""" for animal in animales:  #se agrega for, el nombre que se le va a dar a cada valor, in y el nombre de la lista
    print(f"el animal es {animal}")"""
    
#se puede iterar dos listas al mismo tiempo usando la funcion zip(). importante, las listas deben tener la misma cantidad de elementos
""" for animal, numero in zip(animales, numeros):
    print(f"el animal es {animal}")
    print(f"el numero es {numero}") """
    
#recorrer lista por indice con enumerate

""" for numero in enumerate(numeros):
    print(numero) 
    # esto nos devuelve el indice y el valor se parados por , """

""" for animal in enumerate(animales):
    indice = animal[0] #0 para llamar al indice, porque es el primer dato que devuelve
    valor = animal[1] #1 para llamar al valor, porque es el segundo valor que devuelve
    print(f"el indice es el {indice} y el valor {valor}")
    #esto nos devuelve el indice por separado al valor """
    
   