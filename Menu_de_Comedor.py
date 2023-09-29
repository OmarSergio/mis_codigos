#Lineas de menu

menu_de_comidas = ["-Milanesa a la Napolitana-", "-Costillas de Cerdo-", "-Matambre a la pizza-", "-guisito de arroz-", "-Alto guiso de fideo moñito-", "-hamburguesas-", "-empanadas-"]

menu_de_guarniciones = ["-Ensalada rusa-", "-Ensalada mixta-", "-Ensalada Cesar-", "-Papa y Huevo-", "-Tomate y huevo-"]

menu_de_postres = ["-Dulce de batata o membrillo con queso-", "-Arroz con leche-", "-Tiramisu-", "-Helados-"]

menu_de_helados = ["-Dulce de leche-", "-Vainilla-", "-Granizado-", "-Crema del cielo-", "-Chocolate-", "-Banana Split-"]

menu_de_bebidas = ["-Coca Cola-", "-Sprite-", "-Fanta-", "-Vinos, varias marcas-", "-Gancia-", "-Fernet-", "-Cervezas, varias marcas-"]

#Sub-menu de bebidas (vinos y cervezas)

lista_de_cervezas = ["-Miller-", "-Brahma-", "-Heineken-"]
lista_de_vinos = ["-Balbo-", "-Termidor-", "-Santa Julia-"]

#listas a rellenar con los pedidos
encargo_de_comidas = []
encargo_de_guarnicion = []
encargo_de_postres = []
encargo_de_bebidas = []

#portada Menu del Comedor

print("||||||||||||||||||||||||||||||||||||||||||||||||")
print("||||||||||||||||||||COMEDOR|||||||||||||||||||||")
print("|||||||||||||||*'COMO EN CASA'*|||||||||||||||||")
print("||||||||||||||||||||||||||||||||||||||||||||||||")
print("||||||||||||||ES USTED BIENVENIDO|||||||||||||||")
print("||||||||||||||||||||||||||||||||||||||||||||||||")

print()
print("----------------------------------------------------------------------")
print("A continuacion Ud podra elegir lo que desea consumir en nuestro local")
print("Disponemos de 1 menu de comidas caseras, 1 menu de guarniciones, 1 menu de postres y 1 menu de bebidas,")
print("al cual podra acceder mediante nuestro mas novedoso sistema de menu digital. Solo debe responder las preguntas segun el sistema se las hace,")
print("ahorrandose asi mucho tiempo de espera. Es genial!!!!")
print("----------------------------------------------------------------------")
print()

#menu de comidas------------------------------------------------------------------------

ver_menu = input("Desea ver el menu de comidas? responda si o no: \n->")
if ver_menu.lower() == "si":
    print("-------------------------------------------------------------------------")
    print("----------------------Menu de comidas caseritas--------------------------")
    print("-------------------------------------------------------------------------")
    print()
    for comidas in menu_de_comidas:
        print(comidas)
        print("---------------------------------------------------------------------")
        print()
    consulta = input("desea encargar algo del menu de comidas? ingrese si o no: \n->")
    if consulta.lower() == "si":
        print("---------------------------------------------------------------------")
        print()
        encargo = input("Ingrese aqui lo que desea encargar: \n->")
        print("---------------------------------------------------------------------")
        print("Exelente eleccion, su pedido de esta en camino.")
        print("---------------------------------------------------------------------")
        print()
        encargo_de_comidas.append(encargo)
    else:
        print("---------------------------------------------------------------------")
        print("En la siguiente pagina podra ver el menu de guarniciones")
else:
    print("-------------------------------------------------------------------------")
    print("En la siguiente pagina podra ver el menu de guarniciones")

#menu de guarniciones

ver_menu2 = input("Desea ver el menu de guarniciones? responda si o no: \n->")
if ver_menu2.lower() == "si":
    print("-------------------------------------------------------------------------")
    print("--------------------------Menu de guarniciones---------------------------")
    print("-------------------------------------------------------------------------")
    print()
    for ensalada in menu_de_guarniciones:
        print(ensalada)
        print("---------------------------------------------------------------------")
    consulta2 = input("desea encargar algo del menu de guarniciones? ingrese si o no: \n->")
    if consulta2.lower() == "si":
        print("---------------------------------------------------------------------")
        print()
        encargo2 = input("Ingrese aqui lo que desea encargar: \n->")
        print("---------------------------------------------------------------------")
        print("Exelente eleccion, su pedido de esta en camino.")
        print("---------------------------------------------------------------------")
        print()
        encargo_de_guarnicion.append(encargo2)
    else:
        print("---------------------------------------------------------------------")
        print("En la siguiente pagina podra ver el menu de bebidas")
else:
    print("-------------------------------------------------------------------------")
    print("En la siguiente pagina podra ver el menu de bebidas")

#menu de bebidas------------------------------------------------------------------------

ver_menu3 = input("Desea ver el menu de bebidas? responda si o no: \n->")
if ver_menu3.lower() == "si":
    print("-------------------------------------------------------------------------")
    print("----------------------------Menu de Bebidas------------------------------")
    print("-------------------------------------------------------------------------")
    print()
    for bebidas in menu_de_bebidas:
        print(bebidas)
        print("----------------------------------------------------------------------")
    consulta3 = input("desea encargar algo del menu de bebidas? ingrese si o no: \n->")
    if consulta3.lower() == "si":
        print()
        encargo3 = input("Ingrese aqui lo que desea encargar: \n->")
        if encargo3.lower() == "vinos" or encargo3.lower() == "vino":
            print("------------------------------------------- ----------------------")
            print("---------menu de Vinos---------")
            for vinos in lista_de_vinos:
                    print(vinos)
                    print("---------------------------------- -----------------------")
            seleccion1 = input("ingrese su eleccion de vino y la cantidad de botellas que desea: \n->")
            encargo_de_bebidas.append(seleccion1)
            print("-------------------------------------------------------------------")
            print("Exelente eleccion, su pedido de esta en camino.")
            print("-------------------------------------------------------------------")        
        elif encargo3.lower() == "cervezas" or encargo3.lower() == "cerveza": 
                print("---------------------------------------------------------------")                      
                print("---------menu de Cervezas---------")
                for cerveza in lista_de_cervezas:
                    print(cerveza)
                    print("-----------------------------------------------------------")
                seleccion2 = input("ingrese su eleccion de cerveza y la cantidad de botellas que desea: \n->")
                encargo_de_bebidas.append(seleccion2)
                print("---------------------------------------------------------------")
                print("Exelente eleccion, su pedido de esta en camino.")
                print("---------------------------------------------------------------")
        else: encargo_de_bebidas.append(encargo3)
        print("---------------------------------------------------------------------------")
        print()

#menu de postres------------------------------------------------------------------------

ver_menu4 = input("Desea ver el menu de postres? responda si o no: \n->")
if ver_menu4.lower() == "si":
    print("---------------------------------------------------------------------------")
    print("-----------------------------Menu de postres-------------------------------")
    print("---------------------------------------------------------------------------")
    print()
    for postres in menu_de_postres:
        print(postres)
        print("----------------------------------------------------------------------")
    consulta4 = input("desea encargar algo del menu de postres? ingrese si o no: \n->")
    if consulta4.lower() == "si":
            print("------------------------------------------------------------------")
            print()
            encargo4 = input("Ingrese aqui lo que desea encargar: \n->")
            if encargo4.lower() == "helado" or encargo4.lower() == "helados":
                print("--------------------------------------------------------------")
                print("------------------Sabores de Helados--------------------------")
                for helado2 in menu_de_helados:
                    print(helado2)
                    print("--- -------------------------------------------------------")
                seleccion3 = input("Ingrese 2 sabores de helados: \n->")
                encargo_de_postres.append(encargo4)
                encargo_de_postres.append("de " + seleccion3)
                print("---- -----------------------------------------------------------")
                print("Exelente eleccion, su pedido esta en camino.")
                print("----------------------------------------------------------------")
            else: encargo_de_postres.append(encargo4)        
    print("----------------------------------------------------------------------------")
    print("Exelente eleccion, su pedido esta en camino.")
    print("---------------------------------------------------------------------------")
    print("Muchas gracias por su compra y deseamos que sea de su agrado, Buen Provecho")
else:
        print("-----------------------------------------------------------------------")
        print("Muchas gracias por su visita")
        print("-----------------------------------------------------------------------")
    



print()
print()
print("<<<<<<<<<<<<<<<<<SU PEDIDO>>>>>>>>>>>>>>>>>>>>>>>")
print("-------------------------------------------------")    
print(f"*------->Para comer pidio {encargo_de_comidas}")
print("-------------------------------------------------")
print(f"*------->Para acompañar pidio {encargo_de_guarnicion}")
print("-------------------------------------------------")
print(f"*------->Para tomar encargo {encargo_de_bebidas}")
print("-------------------------------------------------")
print(f"*------->Para postre pidio {encargo_de_postres}")
print("-------------------------------------------------")
