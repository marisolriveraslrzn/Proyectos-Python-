# 🎨 Paint – Proyecto Académico en Python con Tkinter

Este proyecto es una aplicación de escritorio desarrollada en **Python** utilizando la librería **Tkinter**. Simula una herramienta básica de dibujo, ideal para introducir conceptos de **interfaces gráficas de usuario (GUI)** y **eventos del mouse** en programación.

---

## 🎯 Objetivos del proyecto

- Crear una interfaz gráfica funcional con botones, lienzo y controles.
- Implementar eventos del mouse para dibujar en pantalla.
- Explorar el uso de clases y métodos en proyectos visuales.
- Servir como recurso didáctico para cursos de Python, GUI y diseño interactivo.

---

## 🧠 Estructura del sistema

El proyecto se basa en una única clase principal:

### 🖌️ `Paint`
Encargada de inicializar la interfaz y gestionar las herramientas de dibujo. Incluye:

#### 🛠️ Herramientas de dibujo
- `use_pen()`: activa el lápiz.
- `use_brush()`: activa el pincel.
- `use_eraser()`: activa el borrador.

#### 🎨 Selección de color
- `choose_color()`: abre un selector para elegir el color de dibujo.

#### 📏 Tamaño del trazo
- `choose_size_button`: deslizador horizontal para definir el grosor del trazo.

#### 🖼️ Lienzo
- Área de 600x600 píxeles donde el usuario puede pintar con el mouse.

#### 🖱️ Eventos del mouse
- `paint(event)`: dibuja líneas siguiendo el movimiento del cursor.
- `reset(event)`: reinicia la posición para que los trazos se dibujen correctamente.

---

## 🛠️ Tecnologías utilizadas

- **Python 3.x**
- **Tkinter** (incluido por defecto en la mayoría de distribuciones de Python)
- Programación orientada a objetos
- Eventos y manejo de interfaz gráfica

---

## 📁 Estructura del código
```Paint/
├── Paint.py # Script principal con la clase Paint
├── README.md # Documentación del proyecto
└── .venv/ # Entorno virtual (opcional)
   ```
---

## ▶️ Ejecución

1. Crear entorno virtual (opcional):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Linux/Mac
   .venv\Scripts\activate     # En Windows
2. Ejecutar el programa:
   ```bash
   python Paint.py
También puede ejecutarse directamente desde el entorno de desarrollo dando “play” al archivo.
