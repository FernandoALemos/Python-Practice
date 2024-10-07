# FUNCIONES
# ¿Qué es una función y para qué sirve?, normas de un código limpio
# Estructura de una función, parámetros de entrada y salida
# estructura ->
# def  nombre_función (parámetro 1, parámetro 2):

# Ejemplo de las diferentes combinaciones
itemsAvailableList = ["sartén", "hacha", "ruedas", "té"]
dyd_items = ["hacha", "daga", "laud", "varita", "armadura"]


# no param de entrada, no devuelve nada
#def welcomeMessage():
#    print("Bienvenido a shopping market, cargando información...")
#    print("por favor, introduzca su nombre de usuario: ")


def welcome_adventurous():
    print("¡¡Bienvenido aventurero!!")
    print("Por Favor digame su nombre, es que hubo muchos robos.")


# sí param de entrada, no devuelve nada
#def requestUsername(username):
#    print("nombre de usuario disponible, " + username)

def adventurous_name(fullname):
    print("Genere el nombre de su aventurero, " + fullname)


# sí param de entrada, sí devuelve un valor
#def isAvailable(item):
#    return item in itemsAvailableList
def iem_available(item):
    return item in dyd_items

# main
#welcomeMessage()
welcome_adventurous()
userName = input()
#requestUsername(userName)
adventurous_name(userName)
print("por favor, introduzca los obejetos en lo que quiera empezar: ")
item_buy = input()
print(iem_available(item_buy))
#userBuy = input()
#print(isAvailable(userBuy))
