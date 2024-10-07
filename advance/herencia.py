# Herencia clase que hereda propiedades de la clase padre

# clase animal -Padre- pueden estar mas de una calse padre
class Animal:
    # variables
    food = 50  # 0 esta hambriento y 100 esta no hambriento
    # constructor con propiedades

    def __init__(self, name, age, velocity, acuatic):
        self.name = name
        self.age = age
        self.velocity = velocity
        self.acuatic = acuatic

    # métodos
    #si usamos def __nombreFuncion(): es privado
    def __isHungry(self):
        return self.food < 50

    def pasandoHambre(self, food):
        self.food -= food

    def eat(self):
        if self.__isHungry():
            self.food += 10

    def defend(self):
        print(self.name + " se esta defendiendo del enemigo")

print("...................END......................")

class Personaje_mmorpg:
    #variables/constantes
    nivel = 1
    exp = 0
    hp = 65
    mp = 31
    # constructor
    def __init__(self, name_pj, class_pj, raze, gener):
      self.name_pj = name_pj
      self.class_pj = class_pj
      self.raze = raze
      self.gener = gener
  
    # métodos
    def experience(self):
      return self.exp > 20
  
    def level_up(self):
      if self.experience():
        self.nivel += 9
  
    def more_hp(self):
      return self.hp > 65
  
    def more_mp(self):
      return self.mp > 31
  
    def hp_plus_mp_plus(self):
      if self.more_hp() and self.more_mp():
        self.hp += 23
        self.mp += 7

    def battle(self):
      print(self.name_pj + " esta entrando en combate contigo!!")

print("...................END......................")

# Hijos
# caso más simple hereda todas las características sin aportar nada.
class Amorfo(Animal):
    pass

class Npc(Personaje_mmorpg):
  pass
# Mamifero
class Mamifero (Animal): 

    # constructor
    #constructor del padre, llamandolo con super().__init__(params)
    def __init__(self, name, age, velocity, acuatic, milk):
        super().__init__(name, age, velocity, acuatic) 
        self.milk= milk
    # métodos
    def amamantar(self): 
        print ("amamatando")
      
print("...................END......................")

class Nuevo_personaje(Personaje_mmorpg):

    # constructor
    def __init__(self, name_pj, class_pj, raze, gener, gremio):
        super().__init__(name_pj, class_pj, raze, gener)
        self.gremio = gremio
    # métodos
    def guild(self):
        print(self.name_pj + " Felicidades estas en el gremio: " + self.gremio)
    


print("...................END......................")

# main
amorfo = Amorfo("caracol", 1, 5, True)
amorfo.defend()

npc = Npc("Jose", "Guerrero", "Humano", "xxx")
npc.battle()


print("...................END......................")

mamifero = Mamifero("Oso",356,45,True, 80)
print(mamifero.milk)
mamifero.amamantar()

animal= Animal("Perro", 45, 40, True)

print("...................END......................")

new_pj = Nuevo_personaje("Markus", "Magik Night", "Half-Elf", "Masculino", "Cazadores")