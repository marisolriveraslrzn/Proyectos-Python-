import tkinter as tk

# Función para agregar números o símbolos en la entrada
def click_boton(valor):
    actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, actual + valor)

# Función para limpiar la entrada
def limpiar():
    entrada.delete(0, tk.END)

# Función para calcular el resultado
def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

# Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x400")
ventana.resizable(False, False)

# Caja de texto (entrada)
entrada = tk.Entry(ventana, font=("Arial", 18), bd=8, relief="ridge", justify="right")
entrada.grid(row=0, column=0, columnspan=4, pady=10, padx=10, ipady=10)

# Lista de botones
botones = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3),
]

# Crear botones numéricos y de operaciones
for (texto, fila, columna) in botones:
    if texto == "=":
        b = tk.Button(ventana, text=texto, width=5, height=2, font=("Arial", 14),
                      command=calcular, bg="lightgreen")
    else:
        b = tk.Button(ventana, text=texto, width=5, height=2, font=("Arial", 14),
                      command=lambda t=texto: click_boton(t))
    b.grid(row=fila, column=columna, padx=5, pady=5)

# Botón de limpiar
boton_clear = tk.Button(ventana, text="C", width=22, height=2, font=("Arial", 14),
                        command=limpiar, bg="salmon")
boton_clear.grid(row=5, column=0, columnspan=4, pady=10)

ventana.mainloop()
