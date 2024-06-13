class Activity:
    def __init__(self,name,type,status,duration,comment):
        self.name = name
        self.type = type
        self.status = status
        self.duration = duration
        self.comment = comment
    
    '''def show_info(self):
        info = (
            f"Nombre: {self.name}\n"
            f"Tipo: {self.type}"
            f"Estado de visualización: {self.status}\n"
            f"Duración: {self.duration}\n"
            f"Comentarios: {self.comment}\n"
        )
        print(info)'''
    #Está desactivada esta función por si luego elegimos usar este formato.

    def __str__(self):
        return (f"Nombre: {self.name}\n Tipo: {self.type}\n Estado de visualización: {self.status}\n Duración: {self.duration}\n Comentarios: {self.comment}")

import json

class File_manager:
    @staticmethod
    def save_data(activities,filename="activities.json"):
        with open(filename, "w") as file:
            json.dump([vars(j) for j in activities],file,indent=4)
    
    @staticmethod
    def load_data(filename="activities.json"):
        try:
            with open(filename, "r") as file:
                activities_data = json.load(file)
                return [Activity(**k) for k in activities_data]
        except FileNotFoundError:
            return []
        
    
class serie(Activity): 
    def __init__(self,name,type,status,duration,comment,season,episode):
        Activity.__init__(self,name,type,status,comment)
        self.duration = duration
        self.season = season
        self.episode = episode


# Otra idea es crear una clase por cada tipo de obra audiovisual, es decir, crear por series una clase y que se guarde en json propio.
# Lo mismo con las películas, ya que, sus características son distintas, en series si se encuentra viendo la serie, se va a mostrar el episodio en el que va
# Por otro lado, para la busqueda se pueden unir los dos diccionarios en sus elementos comunes para tener todos los datos.
# 
#  
