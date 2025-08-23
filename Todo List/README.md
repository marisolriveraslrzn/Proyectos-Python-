# ✅ TO DO LIST – Proyecto Académico en Python con Tkinter

Este proyecto es una aplicación de escritorio desarrollada en **Python** utilizando la librería **Tkinter**. Simula una lista de tareas con interfaz gráfica, permitiendo agregar y eliminar ítems de forma dinámica. Las tareas se guardan de manera persistente en un archivo `JSON`, lo que permite conservarlas entre sesiones.

---

## 🎯 Objetivos del proyecto

- Crear una interfaz gráfica funcional con botones y listas.
- Implementar persistencia de datos usando archivos JSON.
- Aplicar lógica de eventos y manipulación de estructuras en Python.
- Servir como recurso didáctico para cursos de programación, GUI y manejo de archivos.

---

## 🧠 Funcionalidades

- 📝 **Agregar tareas**: Escribí una tarea y pulsá el botón para añadirla a la lista.
- 🗑️ **Eliminar tareas**: Seleccioná una tarea y pulsá el botón para eliminarla.
- 💾 **Persistencia automática**: Las tareas se guardan en `tasks.json` y se recuperan al iniciar la aplicación.

---

## 🛠️ Librerías utilizadas

- `tkinter`: Para crear la interfaz gráfica de usuario.
- `json`: Para leer y escribir las tareas en formato JSON.
- `os`: Para verificar la existencia del archivo de tareas.

---

## 📁 Estructura del código
```Todo List/
├── app.py # Script principal con la lógica de la aplicación
├── tasks.json # Archivo de persistencia de tareas
└── README.md # Documentación del proyecto
```
---

## 🔧 Definición de funciones principales

- `load_tasks()`: Carga las tareas desde el archivo JSON.
- `save_tasks()`: Guarda la lista de tareas en el archivo JSON.
- `add_task()`: Añade una nueva tarea a la lista y la guarda.
- `delete_task()`: Elimina la tarea seleccionada y actualiza el archivo.

---

## ▶️ Ejecución

1. Asegurate de tener Python instalado.
2. Ejecutá el programa desde la terminal o tu entorno de desarrollo:
  ```bash
  python app.py
  ```
No requiere instalación adicional: tkinter viene incluido en la mayoría de distribuciones de Python.
