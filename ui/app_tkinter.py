import tkinter as tk
from tkinter import ttk
from servicios.tarea_servicio import TareaServicio


class AppTkinter:

    def __init__(self, root):

        # Ventana principal
        self.root = root
        self.root.title("Lista de Tareas")

        # Servicio que maneja la lógica del programa
        self.servicio = TareaServicio()

        # Campo de texto para escribir nuevas tareas
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        # Evento de teclado:
        # Permite agregar una tarea presionando la tecla ENTER
        self.entry.bind("<Return>", self.agregar_tarea)

        # Botón para agregar tarea
        tk.Button(root, text="Añadir Tarea", command=self.agregar_tarea).pack(pady=5)

        # Botón para marcar tarea completada
        tk.Button(root, text="Marcar Completada", command=self.marcar_completada).pack(pady=5)

        # Botón para eliminar tarea
        tk.Button(root, text="Eliminar", command=self.eliminar_tarea).pack(pady=5)

        # Tabla para mostrar las tareas
        self.tree = ttk.Treeview(root, columns=("ID", "Descripción"), show="headings")

        self.tree.heading("ID", text="ID")
        self.tree.heading("Descripción", text="Descripción")

        self.tree.pack(pady=10)

        # Evento de ratón:
        # Permite marcar una tarea como completada con doble clic
        self.tree.bind("<Double-1>", self.doble_click)

    # ---------------- FUNCIONES ---------------- #

    # Agregar tarea
    def agregar_tarea(self, event=None):
        descripcion = self.entry.get().strip()

        if descripcion == "":
            return

        self.servicio.agregar_tarea(descripcion)
        self.entry.delete(0, tk.END)

        self.actualizar_tabla()

    # Marcar tarea como completada
    def marcar_completada(self):

        seleccion = self.tree.selection()

        if not seleccion:
            return

        item = self.tree.item(seleccion)
        id = item["values"][0]

        self.servicio.completar_tarea(id)

        self.actualizar_tabla()

    # Eliminar tarea
    def eliminar_tarea(self):

        seleccion = self.tree.selection()

        if not seleccion:
            return

        item = self.tree.item(seleccion)
        id = item["values"][0]

        self.servicio.eliminar_tarea(id)

        self.actualizar_tabla()

    # Evento doble clic
    def doble_click(self, event):
        # Permite completar tarea con doble clic
        self.marcar_completada()

    # Actualizar tabla de tareas
    def actualizar_tabla(self):

        # Limpiar tabla
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insertar tareas nuevamente
        for tarea in self.servicio.obtener_todos():

            descripcion = tarea.descripcion

            # Cambiar apariencia si la tarea está completada
            if tarea.completada:
                descripcion = "[✔] " + descripcion

            self.tree.insert("", "end", values=(tarea.id, descripcion))