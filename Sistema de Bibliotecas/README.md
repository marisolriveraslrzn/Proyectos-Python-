# 📚 Sistema de Gestión de Bibliotecas – Proyecto Académico en Python (POO)

Este proyecto es una aplicación de línea de comandos desarrollada en **Python**, que simula la administración básica de una biblioteca. Utiliza los principios de **Programación Orientada a Objetos (POO)** para gestionar libros, usuarios y actividades de préstamo de forma eficiente.

---

## 🎯 Objetivos del proyecto

- Representar entidades reales mediante clases y atributos.
- Aplicar lógica de negocio para préstamos y devoluciones.
- Diseñar una interfaz de usuario simple en consola.
- Servir como recurso didáctico para cursos de POO, estructuras de datos y lógica aplicada.

---

## 🧠 Estructura del sistema

El sistema está compuesto por tres clases principales:

### 📖 `Book`
Representa un libro en la biblioteca con los siguientes atributos:

- `id`: identificador único del libro.
- `name`: título del libro.
- `quantity`: cantidad de ejemplares disponibles.

---

### 🧑‍🎓 `User`
Representa a un usuario de la biblioteca con los siguientes atributos:

- `id`: identificador único del usuario.
- `name`: nombre del usuario.

---

### 🛠️ `Admin`
Administra el sistema de bibliotecas y proporciona funcionalidades como:

- Agregar nuevos libros.
- Imprimir todos los libros disponibles.
- Buscar libros por nombre (con prefijo).
- Agregar nuevos usuarios.
- Prestar libros.
- Devolver libros.
- Imprimir usuarios que tomaron prestados libros.
- Imprimir todos los usuarios registrados.

---

## 🛠️ Tecnologías utilizadas

- **Python 3.x**
- Programación Orientada a Objetos
- Interacción por consola (`input`, `print`)
- Estructura modular con clases separadas

---

## 📁 Estructura del código

```📁 SistemaDeBibliotecas/
├── 📄 Book.py         # Define la clase Book (libros)
├── 📄 User.py         # Define la clase User (usuarios)
├── 📄 Admin.py        # Define la clase Admin (administradores)
├── 📄 Main.py         # Archivo principal de ejecución
└── 📄 README.md       # Documentación del proyecto
```
---

## ▶️ Ejecución

Para ejecutar el sistema desde la terminal:

```bash
python Main.py
