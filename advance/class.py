# ¿Qué es un clase y un objeto?

# Ejemplo básico
class Personaje_ff:
    # variable
    hp = 53
    damage = 27
    # constructor siempre se identifica la funcion constructor con def __init__(self):
    def __init__(self, uname, uage, stat):
      self.uname = uname
      self.uage = uage
      self.stat = stat
    # métodos
    def makingDamage(self, dmg_made):
      self.damage += dmg_made

print("...................END......................")

class Gato: 
    # variable
    life= 100
    damage= 150
    # constructor
    def __init__(self, name, age, velocity): 
        self.name= name
        self.age=age
        self.velocity=velocity
    # métodos 
    def takingDamage(self, dmgRecieve): 
        self.life -= dmgRecieve

print("...................END......................")

# main
# puntero del objeto que apunta a la clase Gato 
gatoObjeto = Gato("Espiga", 3, 50)
print("nombre= "+gatoObjeto.name)
print("edad= "+str(gatoObjeto.age))
print("vida= "+str(gatoObjeto.life))

print("...................END......................")

#todos los armgumentos del objeto deben estar completos (vacios o no)
pj_object = Personaje_ff("Jaffan", 20, "Dexterity")
print("nombre: " + pj_object.uname)
print("edad: " + str(pj_object.uage))
print("atributo maximo: " + pj_object.stat)

print("...................END......................")

# vamos hacer daño al gato, utilizabdo un método del objeto
gatoObjeto.takingDamage(10)
print("vida_actual="+str(gatoObjeto.life))
print("...................END......................")

pj_object.makingDamage(63)
print("daño_hecho: " + str(pj_object.damage))
print("...................END......................")

# modificando una propiedad directamente 
gatoObjeto.age = 11
gatoObjeto.life = 20 

print("edad= " + str(gatoObjeto.age), "vida= " + str(gatoObjeto.life))

print("...................END......................")
pj_object.age = 21
pj_object.hp = 75

print("edad: " + str(pj_object.age), "HP: " + str(pj_object.hp))