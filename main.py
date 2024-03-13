bandas=[]


#Construyendo la interfaz
print("***ALTAVOZ ES TU VOZ***")
print("***********************")

opcion=100
while(opcion!=5):

    print("1. Registrar Banda")
    print("2. Buscar información de una Banda")
    print("3. Agenda de evento")
    print("4. Modificar una Banda")
    print("5. SALIR")

    opcion=int(input("Digite una opcion"))

    if opcion==1:
        banda={}
        #creando los datos del diccionario
        banda["id"]=int(input("Digite el id: "))
        banda["nombre"]=input("Nombre de la banda: ")
        banda["genero"]=input("Genero: ")
        banda["clasificacion"]=input("Clasificacion: ")
        banda["tiempo"]=int(input("Tiempo: "))
        banda["costo"]=int(input("Costo: $"))
        print(banda)

        #Agregando un diccionario a una lista

        bandas.append(banda)
    elif opcion==2:
        bandaBuscada=input("Digitan el nombre de la banda que estas buscando: ")
        for bandaAuxiliar in bandas:
            print(bandaAuxiliar["nombre"])
            if bandaAuxiliar["nombre"]==bandaBuscada:
                #Como lo encontre muestro los datos de bandaAuxiliar
                print(f"id: {bandaAuxiliar["id"]} --- nombre {bandaAuxiliar["nombre"]}")
            else:
                print("parce siga buscando....")
    elif opcion==3:
        print(bandas)
    elif opcion==4:
        
    elif opcion ==5:
        pass
    else:
        pass