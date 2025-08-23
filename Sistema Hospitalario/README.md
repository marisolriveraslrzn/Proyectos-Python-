# 🏥 Sistema Hospitalario – Proyecto Académico en Python (POO)

Este proyecto es una aplicación de línea de comandos desarrollada en **Python**, que simula la gestión de colas de pacientes en un entorno hospitalario. Utiliza los principios de **Programación Orientada a Objetos (POO)** para organizar pacientes según su nivel de urgencia y especialización médica.

---

## 🎯 Objetivos del proyecto

- Representar pacientes y especializaciones mediante clases con atributos y métodos.
- Aplicar lógica de colas y prioridades en la atención hospitalaria.
- Diseñar una interfaz de usuario simple en consola.
- Servir como recurso didáctico para cursos de POO, estructuras de datos y simulación de sistemas.

---

## 🧠 Estructura del sistema

El sistema está compuesto por tres clases principales:

### 🧍‍♂️ `Patient`
Representa a un paciente individual con los siguientes atributos:

- `name`: nombre del paciente.
- `status`: nivel de urgencia (0 = normal, 1 = urgente, 2 = superurgente).

Incluye métodos para representar la información del paciente y formatear su estado.

---

### 🩺 `Specialization`
Gestiona las colas de pacientes dentro de distintas especialidades médicas. Permite:

- Agregar pacientes con distintos niveles de urgencia.
- Recuperar al siguiente paciente según prioridad.
- Eliminar pacientes por nombre.
- Verificar la capacidad de la cola.

---

### 🧑‍💼 `OperationsManager`
Actúa como interfaz de usuario para interactuar con el sistema. Permite:

- Incorporar nuevos pacientes a especializaciones.
- Listar pacientes por especialización.
- Atender al siguiente paciente.
- Retirar pacientes del sistema.
- Finalizar el programa de forma segura.

---

## 🛠️ Tecnologías utilizadas

- **Python 3.x**
- Programación Orientada a Objetos
- Interacción por consola (`input`, `print`)
- Estructura modular con clases separadas

---

## 📁 Estructura del código
```
Sistema Hospitalario/ 
├── patient.py # Clase Patient 
├── specialization.py # Clase Specialization 
├── operations_manager.py # Clase OperationsManager 
├── utility.py # Funciones auxiliares 
├── main.py # Archivo principal 
└── README.md # Documentación del proyecto
```

---

## ▶️ Ejecución

Para ejecutar el sistema desde la terminal:

```bash
python main.py
