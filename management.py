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
    def __init__(self, title, status, rating, comment, total_seasons, current_season, current_episode):
        super().__init__(title, status, rating, comment)
        self.total_seasons = total_seasons
        self.current_season = current_season
        self.current_episode = current_episode
        self.type = "Serie"

    def __str__(self):
        return f"{self.title};{self.status};{self.comment};{self.total_seasons};{self.current_season};{self.current_episode};{self.rating}"

    def update(self, attribute, value):
            setattr(self,attribute,value)
        
class Games(Entertainment):
    def __init__(self, title, status, rating, comment, year, dlc):
        super().__init__(title, status, rating, comment)
        self.year = year
        self.dlc = dlc
        self.type = "Videojuego"

    def __str__(self):
        return f"{self.title};{self.status};{self.year};{self.dlc};{self.rating};{self.comment}"

    def update(self, attribute, value):
            setattr(self,attribute,value)

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
    
    def update_serie(self,title,attribute,value):
        serie = self.search_saved_serie(title)
        serie.update(attribute, value)
        File_manager.save_json(self.series, "series.json")
        print("Se ha actualizado el atributo correctamente")

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
    
    def update_game(self,title,attribute,value):
        game = self.search_saved_game(title)
        game.update(attribute, value)
        File_manager.save_json(self.games, "games.json")
        print("Se ha actualizado el atributo correctamente")

#Elección de la categoría de actividad que se quiere agregar.
def choose_to_add():
    while True:
        print("Elija una opción a agregar:\n1.Película\n2.Serie\n3.Videojuego.")
        opcion = int(input())
        if opcion == 1:
            add_movies()
        elif opcion == 2:
            add_series()
        elif opcion == 3:
            add_games()
        else:
            print("Por favor, ingrese una opción válida.")

#Funciones que llaman a las propias de cada clase.
#Películas.

def add_movies(): #Pregunta los datos de la película que se quiere agregar, comprobando su existencia primero.
    title = input("Ingrese el título de la película que quiera agregar: \n")
    management = Movie_management()
    existence = management.existence_movie(title)
    if existence is True:
        print("La película ya se encuentra agregada.")
    else:
        status = input("Ingrese el estado de visualización: \n")
        duration = input("Ingrese la duración de la película (Formato: Xh Xmin): \n")
        year = input("Ingrese el año de lanzamiento: \n")
        rating = input("Ingrese la valoración (del 1 al 10): \n")
        comment = input("Ingrese un comentario: \n")
        to_add_movie = Movies(title, status, rating, comment, duration, year)
        management.save_movie(to_add_movie)

def search_movies(): #Permite buscar una pelicula.
    title = input("Ingrese el título de la película que busca: \n")
    management = Movie_management()
    print(management.search_saved_movie(title))

def del_movies(): #Permite eliminar una pelicula.
    title = input("Ingrese el título de la película que quiera eliminar: \n")
    management = Movie_management()
    existence = management.existence_movie(title)
    if existence is True:
        movie = management.search_saved_movie(title)
        management.del_saved_movie(movie)
    else:
        print("La película no se encuentra guardada.")

def show_movies(): #Muestra el listado de peliculas guardadas.
    print("------Películas------")
    management = Movie_management()
    management.show_saved_movie()
    print("------Fin del listado------")

def update_movies():#Permite actualiar valores de atributos de las peliculas guardadas.
    title = input("Ingrese el título de la película que quiera modificar: \n")
    management = Movie_management()
    existence = management.existence_movie(title)
    if existence is True:
        print("¿Qué quiere modificar?:\n1.Título.\n2.Estado.\n3.Duración.\n4.Año de lanzamiento.\n5.Valoración.\n6.Comentario.")
        opt = int(input())
        if opt == 1:
            new_title = input("Nuevo título: \n")
            management.update_movie(title,attribute = "title",value= new_title)
        elif opt == 2:
            new_status = input("Nuevo estado: \n")
            management.update_movie(title,attribute= "status", value = new_status)
        elif opt == 3:
            new_duration = input("Nueva duración: \n")
            management.update_movie(title,attribute= "duration",value=new_duration)
        elif opt == 4:
            new_year = input("Nuevo año de lanzamiento: \n")
            management.update_movie(title,attribute= "year", value = new_year)
        elif opt == 5:
            new_rating = int(input("Nueva valoración: \n"))
            management.update_movie(title,attribute= "rating",value=new_rating)
        elif opt == 6:
            new_comment = input("Nuevo comentario: \n")
            management.update_movie(title,attribute="comment",value = new_comment)
        else:
            print("Por favor, ingrese una opción válida.")
    else:
        print("La película no existe.")
            
#Series.

def add_series(): #Pregunta los datos de la serie que se quiere agregar, comprobando su existencia primero.
    title = input("Ingrese el título de la serie que quiera agregar: \n")
    management = Serie_management()
    existence = management.existence_serie(title)
    if existence is True:
        print("La serie ya se encuentra agregada.")
    else:
        status = input("Ingrese el estado de visualización: \n")
        total_seasons = input("Ingrese la cantidad de temporadas totales: \n")
        current_season = input("Ingrese la temporada que se encuentra viendo: \n")
        current_episode = input("Ingrese el episodio en el que se encuentra viendo: \n")
        rating = int(input("Ingrese la valoración (del 1 al 10): \n"))
        comment = input("Ingrese un comentario: \n")
        to_add_serie = Series(title, status, rating, comment, total_seasons, current_season, current_episode)
        management.save_serie(to_add_serie)

def search_series(): #Permite buscar una serie.
    title = input("Ingrese el título de la serie que busca: \n")
    management = Serie_management()
    print(management.search_saved_serie(title))

def del_series(): #Permite eliminar una serie.
    title = input("Ingrese el título de la serie que quieres eliminar: \n")
    management = Serie_management()
    existence = management.existence_serie(title)
    if existence is True:
        serie = management.search_saved_serie(title)
        management.del_saved_serie(serie)
    else:
        print("La serie no se encuentra guardada.")

def show_series(): #Muestra el listado de series guardadas.
    print("------Series------")
    management = Serie_management()
    management.show_saved_serie()
    print("------Fin del listado------")

def update_series():#Permite actualiar valores de atributos de las series guardadas.
    title = input("Ingrese el título del videojuego que quiera modificar:\n")
    management = Serie_management()
    existence = management.existence_serie(title)
    if existence is True:
        print("¿Qué quiere modificar?:\n1.Título\n2.Estado\n3.Temporadas totales\n4.Temporada actual\n5.Episodio actual\n6.Valoración\n7.Comentario")
        opt = int(input())
        if opt == 1:
            new_title = input("Nuevo título: \n")
            management.update_serie(title,attribute = "title",value= new_title)
        elif opt == 2:
            new_status = input("Nuevo estado: \n")
            management.update_serie(title,attribute= "status", value = new_status)
        elif opt == 3:
            new_total_seasons = input("Nuevas temporadas totales: \n")
            management.update_serie(title,attribute= "total_seasons", value = new_total_seasons)
        elif opt == 4:
            new_current_season = input("Nueva temporada actual: \n")
            management.update_serie(title,attribute= "current_season", value = new_current_season)
        elif opt == 5:
            new_current_episode = input("Nuevo episodio actual: \n")
            management.update_serie(title,attribute= "current_episode", value = new_current_episode)
        elif opt == 6:
            new_rating = int(input("Nueva valoración: \n"))
            management.update_serie(title,attribute= "rating",value=new_rating)
        elif opt == 7:
            new_comment = input("Nuevo comentario: \n")
            management.update_serie(title,attribute="comment",value = new_comment)
        else:
            print("Por favor, ingrese una opción válida.")
    else:
        print("La serie no existe.")

#Videojuegos.

def add_games(): #Pregunta los datos del videojuego que se quiere agregar, comprobando su existencia primero.
    title = input("Ingrese el título del videojuego que quiera agregar: \n")
    management = Game_management()
    existence = management.existence_game(title)
    if existence is True:
        print("El videojuego ya se encuentra agregado.")
    else:
        status = input("Ingrese el estado de visualización: \n")
        duration = input("Ingrese la duración de la película: (Formato: Xh Xmin): \n")
        year = input("Ingrese el año de lanzamiento: \n")
        dlc = input("Ingrese el dlc que posee (Dejar vacío si no aplica): \n")
        rating = input("Ingrese la valoración (del 1 al 10): \n")
        comment = input("Ingrese un comentario: \n")
        to_add_game = Games(title, status, rating, comment, duration, year)
        management.save_game(to_add_game)

def search_games(): #Permite buscar un videojuego.
    title = input("Ingrese el título del videojuego que busca: \n")
    management = Game_management()
    print(management.search_saved_game(title))

def del_games(): #Permite eliminar un videojuego.
    title = input("Ingrese el título del videojuego que quiera eliminar: \n")
    management = Game_management()
    existence = management.existence_game(title)
    if existence is True:
        game = management.search_saved_game(title)
        management.del_saved_game(game)
    else:
        print("El videojuego no se encuentra guardado.")

def show_games(): #Muestra el listado de videojuegos guardados.
    print("------Videojuegos------")
    management = Game_management()
    management.show_saved_game()
    print("------Fin del listado------")

def update_games():#Permite actualiar valores de atributos de los videojuegos guardados.
    title = input("Ingrese el título del videojuego que quiera modificar: \n")
    management = Game_management()
    existence = management.existence_game(title)
    if existence is True:
        print("¿Qué quiere modificar?:\n1.Título.\n2.Estado.\n3.Año de lanzamiento.\n4.Valoración.\n5.Comentario.")
        opt = int(input())
        if opt == 1:
            new_title = input("Nuevo título: \n")
            management.update_game(title,attribute = "title",value= new_title)
        elif opt == 2:
            new_status = input("Nuevo estado: \n")
            management.update_game(title,attribute= "status", value = new_status)
        elif opt == 3:
            new_year = input("Nuevo año de lanzamiento: \n")
            management.update_game(title,attribute= "year", value = new_year)
        elif opt == 4:
            new_rating = int(input("Nueva valoración: \n"))
            management.update_game(title,attribute= "rating",value=new_rating)
        elif opt == 5:
            new_comment = input("Nuevo comentario: \n")
            management.update_game(title,attribute="comment",value = new_comment)
        else:
            print("Por favor, ingrese una opción válida.")
    else:
        print("El videojuego no existe.")