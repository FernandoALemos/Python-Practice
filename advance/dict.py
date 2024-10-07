# Estructura de datos clave valor. Nos permite manejar Json
# nombre_dictionary= {"clave": valor, "clave":valor, ...}
carBmw = {"brand": "bmw", "potencia": 158, "precio": 3400000}
carPorsche = {"brand": "porsche", "potencia": 215, "precio": 4800000}
libro_rol = {"titulo": "starfinder", "tipo": "reglas basicas", "tapa": "dura", "editorial": "devir", "precio": "13000"}
boardgame = {"nombre": "sanctum", "idioma": "español", "editorial": "devir", "precio": "14000"}
#  es posible encadenar diccionarios.
carsToBuy = {"coches": [carBmw, carPorsche]}
lista_compra = {"comprar": [libro_rol, boardgame]}

# Acceso al dato 
print (carsToBuy["coches"])
print (carBmw["brand"])
print(libro_rol["titulo"])
print(lista_compra["comprar"])
print("..................")


# accede a los valores que tienen las variables del diccionario
for value in carBmw.values():
    print(value)
print("..................")
for value in libro_rol.values():
    print(value)
# accede a las variables del diccionario
for key in carBmw.keys():
    print(key)
print("..................")
for key in lista_compra.keys():
    print(key)

# acceder a la clave y su valor indistintamente, si el valor es un dict, lo muestra todo.
for itemKey, itemValue in carBmw.items():
    print(itemKey, itemValue)
print("..................")
for item_key, item_value in lista_compra.items():
    print(item_key, item_value)

for item_key1, item_value1 in libro_rol.items():
    print(item_key1, item_value1)

print(carBmw)
print("..................")
# modificación del dato
carBmw["brand"]= "ferrari"
libro_rol["titulo"] = "dyd"

# Añadir nuevo elemento
carBmw["nuevo"]= True
lista_compra["precio_total"] = libro_rol["precio"] + boardgame["precio"]
print(carBmw)
print(lista_compra)
print("..................")
# borrar variable, se puede utilizar del o pop de la misma forma
del carBmw["brand"]
carBmw.pop("potencia")
print(carBmw)
print("..................")
# limpiar diccionario
carBmw.clear()
print(carBmw)