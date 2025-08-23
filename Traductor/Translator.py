from deep_translator import GoogleTranslator
from tabulate import tabulate

def main():
    # Idioma destino(puedes cambiarlo a 'en' para inglés, 'hi' para hindi, etc.)
    language = 'it'  # Italiano

    # Texto del usuario
    texto = input("Ingrese el texto a traducir: ")

    # Traducir con deep-translator
    resultado = GoogleTranslator(source='auto', target=language).translate(texto)

    # Mostrar resultados
    tabla = [
        ["Texto original", texto],
        ["Texto traducido", resultado],
        ["Idioma destino", language]
    ]
    print(tabulate(tabla, headers=["Descripción", "Valor"], tablefmt="fancy_grid"))

if __name__ == "__main__":
    main()

#Algunos ejemplos de idiomas disponibles:
#'en' → Inglés
#'es' → Español
#'fr' → Francés
#'de' → Alemán
#'it' → Italiano
#'pt' → Portugués