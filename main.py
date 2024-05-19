
import sys
import os

# Lista predeterminada de palabras
default_words = ["manzana", "pera", "naranja", "plátano", "kiwi"]

def sort_words(file_path):
    # Intenta abrir y leer el archivo
    # Intenta abrir y leer el archivo
    # Intenta abrir y leer el archivo
    # Intenta abrir y leer el archivo
    # Intenta abrir y leer el archivo
    # Intenta abrir y leer el archivo
    # Intenta abrir y leer el archivo
    # Intenta abrir y leer el archivo
    try:
        with open(file_path, 'r') as file:
            words = file.read().splitlines()
    except FileNotFoundError:
        # Si el archivo no se encuentra, usa la lista predeterminada
        print("Archivo no encontrado. Usando lista predeterminada.")
        words = default_words
    
    # Ordenar las palabras
    sorted_words = sorted(words)
    
    # Mostrar palabras ordenadas
    print("Palabras ordenadas:")
    for word in sorted_words:
        print(word)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Por favor, proporcione el nombre del archivo como parámetro.")
    else:
        sort_words(sys.argv[1])
        sort_words(sys.argv[1])
        sort_words(sys.argv[1])
        sort_words(sys.argv[1])
        sort_words(sys.argv[1])
        sort_words(sys.argv[1])
