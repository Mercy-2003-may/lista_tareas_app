# Servicio encargado de manejar la lógica de negocio
# Aquí se agregan, eliminan y completan tareas

from modelos.tarea import Tarea


class TareaServicio:

    def __init__(self):
        self.tareas = []  # Lista donde se almacenan las tareas
        self.contador = 1  # Generador automático de ID

    # Agregar una nueva tarea
    def agregar_tarea(self, descripcion):
        tarea = Tarea(self.contador, descripcion)
        self.tareas.append(tarea)
        self.contador += 1

    # Marcar tarea como completada
    def completar_tarea(self, id):
        for tarea in self.tareas:
            if tarea.id == id:
                tarea.completada = True

    # Eliminar tarea
    def eliminar_tarea(self, id):
        self.tareas = [t for t in self.tareas if t.id != id]

    # Obtener todas las tareas
    def obtener_todos(self):
        return self.tareas