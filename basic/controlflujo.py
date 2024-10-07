# ¿En que se basan las sentencias de control de flujo?
# print ('¿Quieres acabar con el mundo?\n')
# .-Sentencias if
#  if condicionante:
#      sentencias
# .-Sentencias else
# .-Ejemplo donde se muestre un ejemplo y combinación con operadores lógicos
list_items = ["Trinity Force", "Night Harvester", "Void Staff", "Sorcerer's Shoes", "kraken Slayer", "Eclipse", "Redemption"]
print("Por ingrese el item para verificar si esta en la lista: ")
item = input()
if item in list_items:
  print("Este item esta en la lista")
else:
  print("No esta en la lista")

input_user = input()
if input_user == "ok":
  print("Okey polilla!..")
else:
  print("Muy mal polilla")

# inputUser = input()
# if inputUser == 'yes' or inputUser == 'y':
#     print('Lanzando misil...')
# elif inputUser == 'no' or inputUser == 'n':
#     print('Cancelando el lanzamiento')

# .-for loops , "\n" salto de linea
listaCompra = ["manzanas", "peras", "platanos"]
for frutaDeLaLista in listaCompra:
    print(frutaDeLaLista + "\n")

for items in list_items:
  print(items + "\n") #muestra cada elemento de la lista

# .-while loops
count = 1
while count <=5: 
    print(count)
    count += 1 #suma 1, hasta llegar a 5
print("se ha acabado")

# .-switch, interruptor con varias salidas(Entrada->Multi salidas)
diaElegido= int(input())

if diaElegido == 1:
	print("lunes")
elif diaElegido == 2:
	print("martes")
elif diaElegido == 3:
	print("miércoles")
elif diaElegido == 4:
	print("jueves")
elif diaElegido == 5:
	print("viernes")
elif diaElegido == 6:
	print("sábado")
elif diaElegido == 7:
	print("domingo")
else:
	print('no existe')

zapatos = ["deportivo", "urbano", "trabajo", "botines", "basket", "traje"]
print("Por favor ingrese el tipo de zapato que desea ver: ")
tipo_zapato = input()

if tipo_zapato in zapatos:
    print(tipo_zapato in zapatos)
else:
    print("El tipo de zapato que desea ver no esta en nuestro catalogo!! ")