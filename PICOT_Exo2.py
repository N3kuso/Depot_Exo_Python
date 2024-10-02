import time

# Classe Robot
class Robot():
    # Constructeur par défaut
    def __init__(self, name="<unnamed>"):
        self.__name = name
        self.__battery_level = 0

    # Redefinition de la methode print
    def affichage(self):
        msg = (f"Nom : {self.get_name()}\n"
               f"Niveau de la batterie : {self.get_battery_level()}\n")
        print(msg)
    

    # Methode pour charger le robot
    def charge(self):
        if (self.get_battery_level() >= 100):
            print("Je suis déja à bloc")
        else:
            time1 = time.time()
            while ((time.time() - time1) < 10) and (self.get_battery_level() <= 100):
                print("Temps écoules : " + str(time.time() - time1))
                self.set_battery_level(self.get_battery_level() + 10)
                print(f"Niveau de charge de la batterie : {self.get_battery_level()}")
                time.sleep(1)

    ### GETTER & SETTER ###
    def get_name(self):
        return self.__name
    
    def get_battery_level(self):
        return self.__battery_level
    
    def set_battery_level(self, value):
        if self.get_battery_level() >= 100:
            self.__battery_level = 100
        else:
            self.__battery_level = value
    
    ########################

# Classe Humain
class Human():
    # Constructeur par défaut
    def __init__(self, sexe="<undefined>"):
        self.__sexe = sexe
        self.__stomac = []

    # Redefinition de la methode print
    def affichage(self):
        msg = (f"Sexe : {self.get_sexe()}") #f"Etat de l'estomac : {self.__stomac}")
        print(msg)

    # Methode qui permet de manger des aliments
    def eat(self, aliment):
        if (isinstance(aliment, str)):
            print(f"Je mange {aliment}")
            self.set_stomac(aliment)
        elif (isinstance(aliment, list)):
            for food in aliment:
                print(f"Je mange {food}")
                self.set_stomac(food)
        else:
            print("C'est mort je mange pas ça")
    
    # Methode qui permet de digérer
    def digest(self):
        if len(self.__stomac) == 0:
            print("Comment tu veux que je digere avec le ventre vide ??")
        else:
            for food in self.__stomac:
                print(f"Je digere {food}")
                time.sleep(1)
            self.__stomac = []

    
    ### GETTER & SETTER ###
    def get_sexe(self):
        return self.__sexe
    

    def set_stomac(self, new_aliment):
        self.__stomac.append(new_aliment)

# Classe Cyborg
class Cyborg(Robot, Human):
    # Constructeur par défaut
    def __init__(self, name, sexe):
        Robot.__init__(self, name)

        Human.__init__(self, sexe)

    def status(self):
        Robot.affichage(self)
        Human.affichage(self)

# Main

cyborg = Cyborg("Deus Ex Machina", "M")

print(cyborg.get_name(), "sexe", cyborg.get_sexe())
cyborg.digest()
print("Charging battery...")
#cyborg.charge()
cyborg.status()
cyborg.eat("Banana")
cyborg.digest()
cyborg.eat(["coca", "chips"])
cyborg.digest()
