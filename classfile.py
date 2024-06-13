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