import time

class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ["shutdown","running"]

    ### GETTER & SETTER ###
    def get_name(self):
        return self.__name

    def get_power(self):
        return self.__power
    
    def set_power(self, value):
        self.__power = value
    
    def get_current_speed(self):
        return self.__current_speed
    
    def set_current_speed(self, value):
        if (isinstance(value, int) == 0) or (value < 0):
            print("Valeur incorrecte de vitesse !!!")
        else:
            if (self._current_state == self.__states[0]) or (self.get_battery_level == 0):
                print("Robot éteint ou pas assez de batterie pour avancer")
            else:
                self.__current_speed = value

    def get_battery_level(self):
        return self.__battery_level
    
    def set_battery_level(self, value):
        self.__battery_level = value
        if self.__battery_level >= 100:
            self.__battery_level = 100

    def get_current_state(self):
        return self._current_state
    
    def set_current_state(self, value):
        # Rajouter controle
        self._current_state = self.__states[value]

    #########################
    
    # Constructeur par défaut
    def __init__(self, name):
        self.__name = name
        self._current_state = self.__states[0]
    
    # Redefinition du print pour la classe robot
    def __str__(self):
        msg = (f"### Etat du robot ###\n"
               f"Nom : {self.get_name()}\n"
               f"Etat : {self.get_current_state()}\n"
               f"Vitesse actuelle : {self.get_current_speed()}\n"
               f"Niveau de la batterie : {self.get_battery_level()}")
        return msg
    
    # Méthode d'allumage du robot
    def allumage(self):
        # Rajouter controle
        print("Je m'allume !!")
        self.set_power(True)
        self.set_current_state(1)
    
    # Methode d'extinction du robot
    def eteindre(self):
        # Rajouter controle
        print("Je m'éteins")
        self.set_power(False)
        self.set_current_state(0)
    
    # Methode pour recharger la batterie du robot
    def rechargement(self, value):
        if (self.get_battery_level() == 100):
            print("Je suis déjà chargé à bloc chef !")
        else:
            print("Je charge !!!")
            while (self.get_battery_level() < value):
                self.set_battery_level(self.get_battery_level() + 10)
                print(f"Niveau actuel de la batterie : {self.get_battery_level()}")
                time.sleep(1)
            print("Batterie rechargée !!!")
    
    # Methode pour arreter le robot
    def arret(self):
        print("Arret immédiat !!!")
        self.set_current_speed(0)

mon_robot = Robot("Wall-E")
mon_robot.allumage()
mon_robot.set_current_speed(14)
print(mon_robot)
mon_robot.eteindre()
mon_robot.set_current_speed(14)
mon_robot.rechargement(100)
mon_robot.rechargement(100)
print(mon_robot)