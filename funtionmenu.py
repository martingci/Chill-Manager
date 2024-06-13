# Acá se van a incluir las funciones del programa. 

def menu(): #El menu que se ejecuta al final de cada acción 

    while True: 

        print("------------------------------------------")
        print("Menú: \n")
        print("1. Agregar Actividad: ")
        print("2. Buscar Actividad: ")
        print("3. Eliminar Actividad: ")
        print("4. Ver actividades: ")
        print("5. Filtrar y ver Actividades: ")
        print("6. Exportar datos a CSV: ")
        print("7. Salir \n")
        print("------------------------------------------")
        opcion = menu_election()

        if opcion == '1':

            print("1")

        elif opcion == '2':

            print("2")

        elif opcion == '3':

            print("3")

        elif opcion == '4': 

            print("4")
        
        elif opcion == '5':

            print("5")

        elif opcion == '6':

            print("6")

        elif opcion == '7':

            break

                                  
def menu_election(): #encargado de estableer los limites del input del menú

    while True: 

        option = input("Selecciona una opción: ")
        if int(option) >= 1 and int(option) <= 7:

            return option
        
        else: 

            print("Opción no válida, repita su elección")