import json

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

    def __str__(self) -> str:
        return f"{self.title};{self.status};{self.comment};{self.dlc};{self.rating};{self.comment}"

class Movies(Entertainment):
    def __init__(self, title, status, rating, comment, duration, year):
        super().__init__(title, status, rating, comment)
        self.duration = duration
        self.year = year
        self.type = "Película"

    def __str__(self) -> str:
        return f"{self.title};{self.status};{self.duration}{self.rating};{self.comment}"

class Games(Entertainment):
    def __init__(self, title, status, rating, comment, year, dlc):
        super().__init__(title, status, rating, comment)
        self.year = year
        self.dlc = dlc
        self.dlc = "Juego"

    def __str__(self) -> str:
        return f"{self.title};{self.status};{self.year};{self.dlc};{self.rating};{self.comment}"

class File_manager:

    @staticmethod
    def save_json(list, filename):
        with open(filename, 'w') as file: 
            json.dump([vars(elements) for elements in list], file, indent = 4)

    @staticmethod
    def load_json(type, filename):
        try:
            with open(filename, 'r') as file:
                json_elements = json.load(file)
                return[type(**data) for data in json_elements]
        except FileNotFoundError:
            return []

