# manejando una excepción
from typing import final

x = 4

# no se inicia la x, por lo cual siempre salta el error
try: 
    print(x)
except:
    print("excepción debido a que no hemos inicializado la x")
    x = 1

# manejando más de una excepción

try: 
    y = "texto" + 1
except NameError: 
    print("NameError")
except: 
    print("Es otro tipo de error")

try: 
    f = open("exmple_file.txt", "r")
    f.write("cosas que escribir")
except: 
    print("no se ha podido escribir el fichero")
finally: 
    f.close()
    print("cerrando fichero")


num = -2

if num < 0: 
    raise Exception("Error producido cerrando programa")