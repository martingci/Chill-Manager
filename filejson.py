import json
class Movie:
    def __init__(self,name,status,duration,year,rating,comment):
        self.name = name
        self.status = status
        self.duration = duration
        self.year = year
        self.rating = rating
        self.comment = comment
        self.type = "Película"
    def __str__(self):
        return (f"Titulo: {self.name}\n Estado: {self.status}\n Duración: {self.duration}\n Año: {self.year}\n Rating: {self.rating}\n Comentario: {self.comment}")
class file_manager:

    @staticmethod
    def save_movie(movies, filename='movies.json'):
        with open(filename, 'w') as file:
            json.dump([vars(v) for v in movies], file, indent = 4)
    
    @staticmethod
    def save_serie(series, filename = 'series.json'):
        with open(filename, 'w') as file:
            json.dump([vars(v) for v in series], file, indent = 4)
    
    @staticmethod
    def save_game(games, filename = 'series.json'):
        with open(filename, 'w') as file:
            json.dump([vars(v) for v in games],file, indent = 4)
    @staticmethod
    def load_movie(filename = 'movies.json'):
        try:
            with open(filename,'r') as file:
                movies_data = json.load(file)
                return[Movie(**data) for data in movies_data]
        except FileNotFoundError:
            return []

class Movie_management:
    def __init__(self):
        self.movies = file_manager.load_movie()
    def save_movie(self,movie):
        self.movies.append(movie)
        file_manager.save_movie(self.movies)

movie1 = Movie("asss","no completada","1:30",2014,"1/5","wena")
movie_manage= Movie_management()
movie_manage.save_movie(movie1)