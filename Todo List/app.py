import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"

# Función para cargar tareas
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            try:
                return json.load(file)  # Intentamos leer
            except json.JSONDecodeError:
                return []  # Si está vacío o mal, volvemos a lista vacía
    return []

# Función para guardar tareas
def save_tasks():
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)

# Función para agregar tarea
def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Atención", "No puedes agregar una tarea vacía")

# Función para eliminar tarea
def delete_task():
    selected = listbox.curselection()
    if selected:
        task_index = selected[0]
        tasks.pop(task_index)
        listbox.delete(task_index)
        save_tasks()
    else:
        messagebox.showwarning("Atención", "Selecciona una tarea para eliminar")

# Interfaz
root = tk.Tk()
root.title("To-Do List (con JSON)")
root.geometry("400x400")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

add_button = tk.Button(root, text="Agregar tarea", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Eliminar tarea", command=delete_task)
delete_button.pack(pady=5)

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

# Cargar tareas existentes
tasks = load_tasks()
for task in tasks:
    listbox.insert(tk.END, task)

root.mainloop()
