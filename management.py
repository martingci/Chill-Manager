import json

#Manejo de archivos.
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

#Definición de clase y herencias.
class Entertainment:
    def __init__(self, title, status, rating, comment):
        self.title = title
        self.status = status
        self.rating = rating
        self.comment = comment
    

class Movies(Entertainment):
    def __init__(self, title, status, rating, comment, duration, year):
        super().__init__(title, status, rating, comment)
        self.duration = duration
        self.year = year
        self.type = "Pelicula"

    def __str__(self):
        return f"{self.title};{self.status};{self.duration};{self.year};{self.rating};{self.comment}"
    
    def update(self, attribute, value):
            setattr(self,attribute,value) #Cambia el atributo indicado por el valor
    
class Series(Entertainment):
    def __init__(self, title, status, rating, comment, total_seasons, current_seasons, current_episode):
        super().__init__(title, status, rating, comment)
        self.total_seasons = total_seasons
        self.current_seasons = current_seasons
        self.current_episode = current_episode
        self.type = "Serie"

    def __str__(self):
        return f"{self.title};{self.status};{self.comment};{self.total_seasons};{self.current_seasons};{self.current_episode};{self.rating}"

class Games(Entertainment):
    def __init__(self, title, status, rating, comment, year, dlc):
        super().__init__(title, status, rating, comment)
        self.year = year
        self.dlc = dlc
        self.type = "Juego"

    def __str__(self):
        return f"{self.title};{self.status};{self.year};{self.dlc};{self.rating};{self.comment}"

#Funciones para el manejo de cada clase, se diferencian al no tener la "s" finalizando la palabra de la categoría y contener "saved".
class Movie_management:

    def __init__(self):
        self.movies = File_manager.load_json(Movies, "movies.json")
    
    def save_movie(self, movie): #Función para guardar en el archivo json.
        self.movies.append(movie)
        File_manager.save_json(self.movies, "movies.json")
        print("La pelicula se ha guardado correctamente")
    
    def existence_movie(self, title): #Función para comprobar existencia, se utiliza para cada clase.
        for movie in self.movies:
            if movie.title == title:
                return True
        return False
    
    def search_saved_movie(self, title):
        for movie in self.movies:
             if movie.title == title:
                return movie
        else:
            return None
    
    def del_saved_movie(self, movie):
        self.movies.remove(movie)
        File_manager.save_json(self.movies, "movies.json")
        print("Pelicula eliminada correctamente")

    def show_saved_movie(self):
        for movie in self.movies:
            print(movie)
            print("----------")
    
    def update_movie(self, title, attribute, value): #Permite actualizar las peliculas, un atributo en especifico
        movie = self.search_saved_movie(title)
        movie.update(attribute, value)
        File_manager.save_json(self.movies, "movies.json")
        print("Se ha actualizado el atributo correctamente")

class Serie_management:

    def __init__(self):
        self.series = File_manager.load_json(Series, "series.json")
    
    def save_serie(self, serie):
        self.series.append(serie)
        File_manager.save_json(self.series, "series.json")
        print("La serie se ha guardado correctamente")
    
    def existence_serie(self, title):
        for serie in self.series:
            if serie.title == title:
                return True
        return False
    
    def search_saved_serie(self, title):
        for serie in self.series:
             if serie.title == title:
                return serie
        else:
            return None
    
    def del_saved_serie(self, serie):
        self.series.remove(serie)
        File_manager.save_json(self.series, "series.json")
        print("Serie eliminada correctamente")

    def show_saved_serie(self):
        for serie in self.series:
            print(serie)
            print("----------")

class Game_management:
    
    def __init__(self):
        self.games = File_manager.load_json(Games, "games.json")
    
    def save_game(self, game):
        self.games.append(game)
        File_manager.save_json(self.games, "games.json")
        print("El videojuego se ha guardado correctamente")
    
    def existence_game(self, title):
        for game in self.games:
            if game.title == title:
                return True
        return False
    
    def search_saved_game(self, title):
        for game in self.games:
             if game.title == title:
                return game
        else:
            return None
    
    def del_saved_game(self, game):
        self.games.remove(game)
        File_manager.save_json(self.games, "games.json")
        print("Videojuego eliminada correctamente")

    def show_saved_game(self):
        for game in self.games:
            print(game)
            print("----------")

#Elección de la categoría de actividad que se quiere agregar.
def choose_to_add():
    while True:
        print("Elige una opcion a agregar:\n1. Pelicula\n2. Serie\n3. Videojuego")
        opcion = int(input())
        if opcion == 1:
            add_movies()
        elif opcion == 2:
            add_series()
        elif opcion == 3:
            add_games()
        else:
            print("Ingresa una opcion valida")

#Funciones que llaman a las propias de cada clase.
#Películas.

def add_movies(): #Pregunta los datos de la película que se quiere agregar, comprobando su existencia primero.
    title = input("Ingresa el titulo que quieras agregar:\n")
    management = Movie_management()
    existence = management.existence_movie(title)
    if existence is True:
        print("La pelicula ya se encuentra agregada.")
    else:
        status = input("Escribe el estado de visualización:\n")
        duration = input("Escribe cuanto dura:\n")
        year = input("Escribe el año de lanzamiento:\n")
        rating = input("Tu valoracion (del 1 al 10):\n")
        comment = input("Agrega algun comentario:\n")
        to_add_movie = Movies(title, status, rating, comment, duration, year)
        management.save_movie(to_add_movie)

def search_movies(): #Permite buscar una pelicula.
    title = input("Ingresa el titulo de la pelicula que buscas:\n")
    management = Movie_management()
    print(management.search_saved_movie(title))

def del_movies(): #Permite eliminar una pelicula.
    title = input("Ingresa el titulo de la pelicula que quieres eliminar:\n")
    management = Movie_management()
    existence = management.existence_movie(title)
    if existence is True:
        movie = management.search_saved_movie(title)
        management.del_saved_movie(movie)
    else:
        print("La pelicula no se encuentra guardada")

def show_movies(): #Muestra el listado de peliculas guardadas.
    print("------Peliculas------")
    management = Movie_management()
    management.show_saved_movie()
    print("------Fin del listado------")

def update_movies():#Permite actualiar valores de atributos de las peliculas guardadas
    title = input("Ingresa el titulo que quieras modificar:\n")
    management = Movie_management()
    existence = management.existence_movie(title)
    if existence is True:
        print("Que quieres modificar:\n1.Titulo\n2.Estado\n3.Año de lanzamiento\n4.Valoracion\n5.Commentario")
        opt = int(input())
        if opt == 1:
            new_title = input("Nuevo titulo:\n")
            management.update_movie(title,attribute = "title",value= new_title)
        elif opt == 2:
            new_status = input("Nuevo estado:\n")
            management.update_movie(title,attribute= "status", value = new_status)
        elif opt == 3:
            new_year = input("Nuevo año de lanzamiento:\n")
            management.update_movie(title,attribute= "year", value = new_year)
        elif opt == 4:
            new_rating = int(input("Nueva valoracion:\n"))
            management.update_movie(title,attribute= "rating",value=new_rating)
        elif opt == 5:
            new_comment = input("Nuevo comentario:\n")
            management.update_movie(title,attribute="comment",value = new_comment)
        else:
            print("Ingresa opcion correcta")
    else:
        print("La pelicula no existe")
            

update_movies()
#Series.

def add_series(): #Pregunta los datos de la serie que se quiere agregar, comprobando su existencia primero.
    title = input("Ingresa el titulo que quieras agregar:\n")
    management = Serie_management()
    existence = management.existence_serie(title)
    if existence is True:
        print("La serie ya se encuentra agregada.")
    else:
        status = input("Escribe el estado de visualización:\n")
        rating = int(input("Tu valoracion (del 1 al 10):\n"))
        comment = input("Agrega algun comentario:\n")
        total_seasons = input("Ingrese la cantidad de temporadas que tiene: \n")
        current_season = input("Ingrese la temporada en la que se encuentra: \n")
        current_episode = input("Ingrese el episodio en el que se encuentra: \n")
        to_add_serie = Series(title, status, rating, comment, total_seasons, current_season, current_episode)
        management.save_serie(to_add_serie)

def search_series(): #Permite buscar una serie.
    title = input("Ingresa el titulo de la serie que buscas:\n")
    management = Serie_management()
    print(management.search_saved_serie(title))

def del_series(): #Permite eliminar una serie.
    title = input("Ingresa el titulo de la serie que quieres eliminar:\n")
    management = Serie_management()
    existence = management.existence_serie(title)
    if existence is True:
        serie = management.search_saved_movie(title)
        management.del_saved_serie(serie)
    else:
        print("La serie no se encuentra guardada")

def show_movies(): #Muestra el listado de series guardadas.
    print("------Series------")
    management = Serie_management()
    management.show_saved_serie()
    print("------Fin del listado------")

#Videojuegos.

