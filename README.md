# Aplicación Lista de Tareas con Tkinter

Este proyecto es una aplicación de escritorio desarrollada en **Python** utilizando la biblioteca **Tkinter**.  
La aplicación permite gestionar una lista de tareas diarias mediante una interfaz gráfica simple e interactiva.

---

# Objetivo del proyecto

Desarrollar una aplicación GUI aplicando **arquitectura modular por capas**, manejo de **eventos de usuario** y generación de un **ejecutable (.exe)** utilizando PyInstaller.

---

# Funcionalidades

- Agregar nuevas tareas.
- Marcar tareas como completadas.
- Eliminar tareas de la lista.
- Visualización de tareas en una tabla.
- Cambio visual cuando una tarea es completada.

---

# Manejo de Eventos

La aplicación utiliza eventos para mejorar la interacción del usuario:

### Evento de teclado
Presionar la tecla **Enter** permite agregar una nueva tarea rápidamente.

### Evento de ratón
Al hacer **doble clic sobre una tarea**, esta se marca automáticamente como completada.

---

# Estructura del Proyecto

```
lista_tareas_app/
│
├── main.py
│
├── modelos/
│   └── tarea.py
│
├── servicios/
│   └── tarea_servicio.py
│
└── ui/
    └── app_tkinter.py
```

---

# Tecnologías Utilizadas

- Python
- Tkinter
- PyInstaller
- Git
- GitHub

---

# Ejecutar el Proyecto

Para ejecutar el proyecto desde el código fuente:

```bash
python main.py
```

---

# Ejecutable

El proyecto fue compilado utilizando **PyInstaller** para generar un archivo ejecutable:

```
ListaTareas.exe
```

Esto permite ejecutar la aplicación sin necesidad de tener Python instalado.

---

# Autor

Proyecto desarrollado por:

**Mercy Amaya**

Como parte de una actividad académica sobre desarrollo de aplicaciones GUI en Python.
