# 🌐 Traductor Multilenguaje – Proyecto Académico en Python

Este proyecto es un traductor simple desarrollado en **Python**, que permite traducir texto entre distintos idiomas utilizando la librería `deep-translator`. El resultado se muestra en formato de tabla para facilitar la lectura y comparación.

---

## 🎯 Objetivos del proyecto

- Utilizar librerías externas para procesamiento de texto.
- Implementar traducción automática entre idiomas.
- Mostrar resultados en formato tabular con `tabulate`.
- Servir como recurso didáctico para clases de Python, APIs y manipulación de texto.

---

## 🧠 Funcionalidades

- Traducción de frases desde cualquier idioma detectado automáticamente.
- Selección del idioma de destino mediante código ISO (ejemplo: `'it'` para italiano).
- Visualización clara del texto original y traducido en formato de tabla.
- Código fácilmente modificable para adaptarlo a otros idiomas o interfaces.

---

## 🛠️ Tecnologías utilizadas

- **Python 3.x**
- [`deep-translator`](https://pypi.org/project/deep-translator/) – Traducción automática
- [`tabulate`](https://pypi.org/project/tabulate/) – Formato tabular en consola

---

## 📁 Estructura del código
 ```
Traductor/ 
├── Translator.py # Script principal
├── README.md # Documentación del proyecto
└── .venv/ # Entorno virtual (opcional)
 ```
## ▶️ Ejecución

1. Crear entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Linux/Mac
   .venv\Scripts\activate     # En Windows
2. Instalar dependencias:
   ```bash
   pip install deep-translator tabulate
   ```
3. Ejecutar el traductor:
   ```bash
   python Translator.py
    ```
4. Modificar el idioma de destino en el código si lo deseás:
   ```python
   language = 'it'  # Traducir a italiano
