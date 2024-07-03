import json
class File_manager:

    @staticmethod
    def save_movie(movies, filename='movies.json'): #Crea el archivo movies.json
        with open(filename, 'w') as file:
            json.dump([vars(v) for v in movies], file, indent = 4)
    
    @staticmethod
    def save_serie(series, filename = 'series.json'): #Crea el archivo series.json
        with open(filename, 'w') as file:
            json.dump([vars(v) for v in series], file, indent = 4)
    
    @staticmethod
    def save_game(games, filename = 'games.json'): #Crea el archivo games.json
        with open(filename, 'w') as file:
            json.dump([vars(v) for v in games],file, indent = 4)
    
    @staticmethod
    def load_movie(filename = 'movies.json'): #Permite cargar el archivo movies.json
        try:
            with open(filename,'r') as file:
                movies_data = json.load(file)
                return[Movie(**data) for data in movies_data]
        except FileNotFoundError:
            return []
    
    @staticmethod
    def load_serie(filename = 'series.json'): #Permite cargar el archivo series.json
        try:
            with open(filename,'r') as file:
                series_data = json.load(file)
                return[Serie(**data) for data in series_data]
        except FileNotFoundError:
            return []
    
    @staticmethod
    def load_game(filename = 'games.json'): #Permite cargar el archivo games.json
        try:
            with open(filename,'r') as file:
                games_data = json.load(file)
                return[Game(**data) for data in games_data]
        except FileNotFoundError:
            return []

class Movie_management: #Agregar aqui funcionalidades de movies

    def __init__(self):
        self.movies = File_manager.load_movie()
    
    def add_movie(self,movie):
        self.movies.append(movie)
        File_manager.save_movie(self.movies)
        print("La pelicula se ha guardado correctamente")
    
    def existence_movie(self,title):
        for movie in self.movies:
            if movie.title == title:
                return True
        return False
    
    def search_movie(self,title):
        for movie in self.movies:
             if movie.title == title:
                return movie
        else:
            return None
    
    def delete_movie(self,movie):
        self.movies.remove(movie)
        File_manager.save_movie(self.movies)
        print("Pelicula eliminada correctamente")

    def show_saved_movies(self):
        for movie in self.movies:
            print(movie)
            print("----------")
    
        
class Movie:
    def __init__(self,title,status,duration,year,rating,comment):
        self.title = title
        self.status = status
        self.duration = duration
        self.year = year
        self.rating = rating
        self.comment = comment   
    
    def __str__(self):
        return f"Titulo: {self.title}\nEstado: {self.status}\nDuracion: {self.status}\nAño de lanzamiento: {self.year}\nValoracion: {self.rating}\nComentario: {self.comment}"

class Serie_management: #Agregar aqui funcionalidades de series

    def __init__(self):
        self.series = File_manager.load_serie()

class Game_management: #Agregar aqui funcionalidades de juegos
    
    def __init__(self):
        self.games = File_manager.load_game()

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
        to_add_movie = Movie(title,status,duration,year,rating,comment)
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
    managament = Movie_management()
    managament.show_saved_movies()
    print("------Fin del listado------")

show_movies()
    


