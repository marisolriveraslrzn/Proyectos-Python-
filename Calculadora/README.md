# 🧮 Calculadora Gráfica en Python

Este proyecto implementa una **calculadora básica con interfaz gráfica** utilizando Python y la biblioteca estándar `Tkinter`. Permite realizar operaciones aritméticas simples como suma, resta, multiplicación y división, mostrando los resultados en una interfaz amigable y funcional.

---

## 🎯 Objetivos del proyecto

- Aplicar conceptos de GUI en Python con `Tkinter`.
- Desarrollar lógica de eventos y evaluación de expresiones.
- Crear una herramienta didáctica para cursos introductorios de programación.
- Servir como base para extender funcionalidades (científica, historial, teclado virtual).

---

## 🛠️ Librerías utilizadas

- `tkinter`: Para construir la ventana principal, botones y caja de entrada.
- `eval()`: Función nativa de Python para evaluar expresiones matemáticas (usada con precaución).

---

## 📁 Estructura del proyecto
```Calculadora/
├── calculadora.py # Script principal con la lógica de la calculadora
├── README.md # Documentación del proyecto
```
---

## 🔧 Funciones principales

- `click_boton(valor)`: Agrega el número o símbolo presionado al campo de entrada.
- `limpiar()`: Elimina todo el contenido del campo de entrada.
- `calcular()`: Evalúa la expresión matemática y muestra el resultado. Si hay error, muestra `"Error"`.

---

## ▶️ Uso

1. Ejecutá el archivo `calculadora.py` desde tu terminal o entorno de desarrollo:
```bash
python calculadora.py
```
2. Se abrirá una ventana con botones numéricos y de operaciones.
3. Escribí operaciones usando los botones.
4. Presioná "=" para obtener el resultado.
5. Usá "C" para limpiar la entrada.
