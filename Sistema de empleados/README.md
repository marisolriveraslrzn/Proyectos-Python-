# 🧾 Sistema de Empleados – Proyecto Académico en Python (POO)

Este proyecto simula un sistema básico de gestión de empleados utilizando **Python** y los principios de **Programación Orientada a Objetos (POO)**. Fue desarrollado con fines educativos para practicar encapsulamiento, modularidad y diseño de clases aplicadas a un caso real.

---

## 🎯 Objetivos del proyecto

- Implementar clases con atributos y métodos que representen entidades reales.
- Aplicar operaciones CRUD sobre una lista de empleados.
- Diseñar una interfaz de usuario simple para interactuar con el sistema.
- Servir como recurso didáctico para cursos de POO, lógica y estructuras de datos.

---

## 🧠 Estructura del sistema

El proyecto está compuesto por tres clases principales:

### 🧍‍♂️ `Employee`
Representa a un empleado individual con los siguientes atributos:

- `name`: nombre del empleado.
- `age`: edad del empleado.
- `salary`: salario del empleado.

Incluye métodos para representar la información en formato legible y estructurado.

---

### 🗂️ `EmployeesManager`
Administra una lista de empleados. Ofrece funcionalidades para:

- Agregar un nuevo empleado.
- Listar todos los empleados existentes.
- Eliminar empleados dentro de un rango de edad.
- Buscar empleados por nombre.
- Actualizar el salario de un empleado por nombre.

---

### 🖥️ `FrontendManager`
Proporciona una interfaz de usuario en consola para interactuar con `EmployeesManager`. Permite:

- Agregar nuevos empleados.
- Mostrar la lista de empleados.
- Eliminar empleados según rango de edad.
- Actualizar salarios por nombre.

---

## 🛠️ Tecnologías utilizadas

- **Python 3.x**
- Programación Orientada a Objetos
- Interacción por consola (`input`, `print`)
- Estructura modular con archivos separados por clase

---

## 📁 Estructura del código
Sistema de empleados/ ├── Employee.py # Clase Employee ├── EmployeesManager.py # Clase EmployeesManager ├── FrontendManager.py # Clase FrontendManager ├── Main.py # Archivo principal └── README.md # Documentación del proyecto

---

## ▶️ Ejecución

Para ejecutar el sistema desde la terminal:

```bash
python Main.py
