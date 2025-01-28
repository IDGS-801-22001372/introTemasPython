from io import open
import math

texto=open("Archivo.txt","w")
texto.write("Hola, soy un archivo de texto\n")
texto.write("Hola mundo\n")
texto.close()