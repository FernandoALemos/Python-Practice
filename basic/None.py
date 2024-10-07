# valo que indica la ausencia del mismo

dum_plus = 1+1
var_null = None

def with_out_return():
    return

getting_value_none = with_out_return()

if getting_value_none == None:
    print("El valor de la variable es: "+ str(getting_value_none))
else:
    print("El valor de la  variable es indeterminada.")