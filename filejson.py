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


