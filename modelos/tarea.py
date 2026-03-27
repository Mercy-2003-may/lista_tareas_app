# Clase que representa una tarea del sistema
# Contiene los datos básicos de una tarea

class Tarea:
    def __init__(self, id, descripcion):
        self.id = id  # Identificador único de la tarea
        self.descripcion = descripcion  # Texto de la tarea
        self.completada = False  # Estado de la tarea