# función rápida y anonima

# estructura -> lambda parámetro1, param2 : sentencia 

# ejemplo 1 
res = lambda firstParam , secParam : firstParam * secParam

#ejemplo 2, los concatena, aplicar espacio en los textos a concatenar
resultado = lambda first_shoe, sec_shoe :  first_shoe + sec_shoe
def resultado(first_shoe, sec_shoe):
    return first_shoe + sec_shoe
print(resultado("botas", "urbanas"))

# def res (firstParam , secParam):
#     return firstParam * secParam
print(res(2, "-las cosas de la vida-"))


# ejemplo 3 lambda dentro de una función 
def funclambda (text): 
    return lambda param : param + text

res2 = funclambda("cola")
print(res2("colita igual viene la "))

#ejemplo 4, el parametro puede ser cualquier cosa
def lambda_funtion(pepito):
    return lambda conjunto: conjunto + pepito

resultado_2 = lambda_funtion("parte del conjunto.")
print(resultado_2("El saco, la camisa, los pantalones y los zapatos son "))