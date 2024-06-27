class Serie:
    def __init__(self,name,status,total_seasons,current_season,current_episode,rating,comment):
        self.name = name
        self.status = status
        self.total_seasons = total_seasons
        self.current_season = current_season
        self.current_episode = current_episode
        self.rating = rating
        self.comment = comment
        self.type = "Serie"

    def update_serie(self):
        while True:
            print("\nIngrese el número de la característica que quiere actualizar, tome en cuenta de que esto reemplazará a lo que tenía en esa categoría.")
            print("1)Actualizar nombre.")
            print("2) Actualizar estado de visualización.")
            print("3) Actualizar cantidad de temporadas totales.")
            print("4) Actualizar temporada actual.")
            print("5) Actualizar episodio actual.")
            print("6) Actualizar clasificación.")
            print("7) Actualizar comentario.")
            print("7) Volver al menú.\n")
            opc = input("Ingrese la opción a modificar: ")
            if opc == "1":
                self.name = input("\nNuevo nombre: ")
                #función para guardar el cambio en el archivo serie.json
            elif opc == "2":
                self.status = input("\nNuevo estado de visualización: ")
            elif opc == "3":
                self.total_seasons = input("\nNueva cantidad de temporadas totales: ")
            elif opc == "4":
                self.current_season = input("\nNueva temporada actual: ")
            elif opc == "5":
                self.current_episode = input("\nNuevo episodio actual: ")
            elif opc == "6":
                self.rating = input("\nNueva clasificación: ")
            elif opc == "7":
                self.comment = input("\nNuevo comentario: ")
            elif opc == "8":
                print("Cerrando menú de modificaciones... Hasta la próxima ^^")
                break
            else:
                print("Opción inválida, inténtelo de nuevo.")

class Movie:
    def __init__(self,name,status,duration,year,rating,comment):
        self.name = name
        self.status = status
        self.duration = duration
        self.year = year
        self.rating = rating
        self.comment = comment
        self.type = "Película"

class Game:
    def __init__(self,name,status,year,rating,comment,dlcs=False):
        #preguntar porque no acepta escribir parámetros después del False.
        self.name = name
        self.status = status
        self.year = year
        self.dlcs = dlcs
        self.rating = rating
        self.comment = comment
        self.type = "Videojuego"