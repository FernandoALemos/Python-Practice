# lists -> ordenado, modificables, permite duplicados
# sets -> desordenados, no modificables, no duplicados, puede contener Bool,str,int,float
# diccionario ->desordenados, modificables, no dulicados
# tuple -> ordenado, no modificables, permite duplicados

setDeLaCompra = { "manzana", "peras", "lentejas"}
print(setDeLaCompra)

set_yerba = {"Chamigo", "Rosamonte", "Playadito", "CBSé", "Nobleza Gaucha"}
print(set_yerba)
print("...................END......................")

# acceso a los datos
for yerba in set_yerba:
  print(yerba)

print("CBSé" in set_yerba)
for itemShopLits in setDeLaCompra: 
    print(itemShopLits)

print ("manzana"in setDeLaCompra)
print("...................END......................")

# añadir dato
set_yerba.add("Cachamate")
print(set_yerba)

setDeLaCompra.add("naranjas")
print(setDeLaCompra)
print("...................END......................")

# añadir un set, incorpora los datos en el set

setDeLaCompra2 = {"pollo", "ternera"}
setDeLaCompra.update(setDeLaCompra2)
print(setDeLaCompra)

set_yerba2 = {"Mate cocido", "Taragüi"}
set_yerba.update(set_yerba2)
print(set_yerba)

print("...................END......................")

# eliminar un item de la lista .remove, .discard

setDeLaCompra.remove("naranjas")
print(setDeLaCompra)

set_yerba.remove("Mate cocido")
print(set_yerba)

print("...................END......................")

# limpiar lista

setDeLaCompra.clear()
print(setDeLaCompra)
set_yerba.clear()
print(set_yerba)

print("...................END......................")

# union
setDeLaCompra3 = setDeLaCompra.union(setDeLaCompra2)
print(setDeLaCompra3)

set_cafe = {"Bonaffide", "Nesscafe", "Dolca"}
set_union = set_yerba.union(set_cafe)
print(set_union)

print("...................END......................")

# insertion unifica solamente el o los datos duplicados
set1 = {"cosas", 1}
set2 = {"cosas", 2}
set3 = set1.intersection(set2)
print(set3)

set_zapatilla = {"urbana", 1}
set_calzado ={"urbana", "talle 43"}
set_insert = set_zapatilla.intersection(set_calzado)
print(set_insert)

print("...................END......................")

# no dubplicates unifica los datos sin duplicar
set4 = set1.symmetric_difference(set2)
print(set4)

set_diff = set_zapatilla.symmetric_difference(set_calzado)
print(set_diff)