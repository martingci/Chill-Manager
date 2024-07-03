import json

class File_manager:

    @staticmethod
    def save_json(list, filename):
        with open(filename, 'w') as file: 
            json.dump([vars(elements) for elements in list], file, indent=4)

    @staticmethod
    def load_json(type, filename):
        try:
            with open(filename, 'r') as file:
                json_elements = json.load(file)
                return [type(**{k: v for k, v in data.items() if k != 'type'}) for data in json_elements]
        except FileNotFoundError:
            return []

class Entertainment:
    def __init__(self, title, status, rating, comment):
        self.title = title
        self.status = status
        self.rating = rating
        self.comment = comment

class Series(Entertainment):
    def __init__(self, title, status, rating, comment, total_seasons, current_seasons, current_episode):
        super().__init__(title, status, rating, comment)
        self.total_seasons = total_seasons
        self.current_seasons = current_seasons
        self.current_episode = current_episode
        self.type = "Serie"

    def __str__(self):
        return f"{self.title};{self.status};{self.comment};{self.total_seasons};{self.current_seasons};{self.current_episode};{self.rating}"

class Movies(Entertainment):
    def __init__(self, title, status, rating, comment, duration, year):
        super().__init__(title, status, rating, comment)
        self.duration = duration
        self.year = year
        self.type = "Película"

    def __str__(self):
        return f"{self.title};{self.status};{self.duration};{self.year};{self.rating};{self.comment}"

class Games(Entertainment):
    def __init__(self, title, status, rating, comment, year, dlc):
        super().__init__(title, status, rating, comment)
        self.year = year
        self.dlc = dlc
        self.type = "Juego"

    def __str__(self):
        return f"{self.title};{self.status};{self.year};{self.dlc};{self.rating};{self.comment}"

class Movie_management: #Agregar aqui funcionalidades de movies

    def __init__(self):
        self.movies = File_manager.load_json(Movies, "movies.json")
    
    def add_movie(self, movie):
        self.movies.append(movie)
        File_manager.save_json(self.movies, "movies.json")
        print("La pelicula se ha guardado correctamente")
    
    def existence_movie(self, title):
        for movie in self.movies:
            if movie.title == title:
                return True
        return False
    
    def search_movie(self, title):
        for movie in self.movies:
             if movie.title == title:
                return movie
        else:
            return None
    
    def delete_movie(self, movie):
        self.movies.remove(movie)
        File_manager.save_json(self.movies, "movies.json")
        print("Pelicula eliminada correctamente")

    def show_saved_movies(self):
        for movie in self.movies:
            print(movie)
            print("----------")

class Serie_management: #Agregar aqui funcionalidades de series

    def __init__(self):
        self.series = File_manager.load_json(Series, "series.json")

class Game_management: #Agregar aqui funcionalidades de juegos
    
    def __init__(self):
        self.games = File_manager.load_json(Games, "games.json")







def add(): #ARREGLAR ESTO, NO SE QUE HACE ERROR
    while True:
        print("Elige una opcion a agregar:\n1. Pelicula\n2. Serie\n3. Videojuego")
        opcion = int(input())
        if opcion == 1:
            add_movies()
        elif opcion == 2:
            print()
        elif opcion == 3:
            print()
        else:
            print("Ingresa una opcion valida")

def add_movies(): #FUNCIONA, realizar uno para cada tipo
    #Añadir restricciones
    title = input("Ingresa el titulo que quieras agregar:\n")
    management = Movie_management()
    existence = management.existence_movie(title)
    if existence is True:
        print("La pelicula ya se encuentra agregada.")
    else:
        status = input("Escribe el estado:\n")
        duration = input("Escribe cuanto dura:\n")
        year = input("Escribe el año de lanzamiento:\n")
        rating = input("Tu valoracion (del 1 al 10):\n")
        comment = input("Agrega algun comentario:\n")
        to_add_movie = Movies(title, status, rating, comment, duration, year)
        management.add_movie(to_add_movie)

def search_movies():#Permite buscar peliculas que esten guardadas en el json
    title = input("Ingresa el titulo de la pelicula que buscas:\n")
    management = Movie_management()
    print(management.search_movie(title))

def delete_movies():#Permite eliminar las peliculas
    title = input("Ingresa el titulo de la pelicula que quieres eliminar:\n")
    management = Movie_management()
    existence = management.existence_movie(title)
    if existence is True:
        movie = management.search_movie(title)
        management.delete_movie(movie)
    else:
        print("La pelicula no se encuentra guardada")

def show_movies():#Muestra el listado de peliculas guardadas
    print("------Peliculas------")
    management = Movie_management()
    management.show_saved_movies()
    print("------Fin del listado------")


show_movies()
