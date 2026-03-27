import tkinter as tk
from ui.app_tkinter import AppTkinter

# Punto de inicio del programa
# Aquí se crea la ventana principal de Tkinter
# y se inicia la interfaz gráfica

if __name__ == "__main__":
    root = tk.Tk()  # Crear ventana principal
    app = AppTkinter(root)  # Cargar la interfaz
    root.mainloop()  # Mantener la ventana abierta