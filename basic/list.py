# Lists

# 1º parte, conceptos básicos
# - explicación 
# - índice, valor + ejemplo (el indice inicial es 0)
listaCompra = ["manzana", "peras","platanos", 1, False, 1.0, True, "bizcochos","pipas"]
list_items = ["Trinity Force", "Night Harvester", "Void Staff", "Sorcerer's Shoes", "kraken Slayer", "Eclipse", "Redemption"]

# - Crear listas vacías. 
empty_list = []
print(listaCompra)
print(list_items)

# - lista con diferentes objetos 
listaConOtraLista = ["string", 0, listaCompra]
list_spells = ["smite", "teleport", "ignite", "flash", list_items, "flash"]


# 2º parte operadores que nos permiten manipular los datos de una lista. 
# - get, editar , eliminar , añadir
# get, coger un valor de la lista 
print(listaCompra[1])
print(listaConOtraLista[2][2])
print(list_items[1], list_items[2])
print(list_spells[0], list_spells[4][4], list_spells[3])


# editar
listaCompra[7] = "pepas"
list_items[0] = "Black Cleaver"

#eliminar nombre_lista.remove("lo que deseo remover")
#.pop() tambien es para borrar puede borrar la lista
#.clear() borra todos los elementos de la lista sin borrar a la misma lista
listaCompra.remove("platanos")
#añadir nombre_lista.insert
# añadir en la posicion en la que estaba el que removi ó ubicarlo en la posicion deseada
# inserta un nuevo elemento en la ubicacion deseada
listaCompra.insert(2, "platanos de canarias")
print(listaCompra)
# añadir pero en la ultima posicion
list_spells.append("exhaust")
print(list_spells)

# tamaño de la lista 
print(len(listaCompra))
print(len(list_items))

# index busca la ubicacion, dentro de la lista
print(listaCompra.index("platanos de canarias"))
print(list_spells.index(list_items))

#max y min no se pueden mezclar str con int, viceversa.
list2 = [1,2,3,1,1,1]
# max 
print(max(list2))
# min
print(min(list2))
# count para ver cuantas veces se repite algo dentro de una lista
print(list2.count(1))
print(list_spells.count("flash"))

# reverse altera la lista, voltea el orden de dicha lista
listaCompra.reverse()
print(listaCompra)
list_spells.reverse()
print(list_spells)
list_items.reverse()
print(list_items)

# - operaciones matemáticas sobre la lista 
print(list2 * 3)
print(list_items * 2)

# - operador in ya visto en bucles for busca si esta dentro de la lista
#devolviendo true o false
print("manzana" in listaCompra)
print("exhaust" in list_spells)