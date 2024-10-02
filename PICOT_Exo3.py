from abc import ABCMeta, abstractmethod
# Classe abstraite Vehicule
class Vehicule(metaclass=ABCMeta):
    @abstractmethod
    def description():
        pass

# Classe abstraite UnmannedVehicule
class UnmannedVehicule(Vehicule):
    """ 
        An autonomous vehicle have to do his mission automatically.
        This mission can be configured by an operator.
    """
    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def start_mission(self):
        print(f"{self.__name} : Starting Mission")

    @abstractmethod
    def description(self):
        print(f"Mon nom est {self.__name}")

# Classe abstraite AerialVehicule
class AerialVehicule(Vehicule):
    """ A vehicle made for aerial areas."""
    def __init__(self):
        self.__weight = 130
        self.__max_height = 120

    @abstractmethod
    def fly(self):
        pass
    
    @abstractmethod
    def description(self):
        print(f"Je pèse {self.__weight} kg")
        print(f"Je peux voler jusqu'à {self.__max_height} m")

# Classe abstraite GroundVehicule
class GroundVehicule(Vehicule):
    """ A vehicle made for ground fields."""
    def __init__(self):
        self.__weight = 50
        self.__max_speed = 70

    @abstractmethod
    def ride(self):
        pass
    
    @abstractmethod
    def description(self):
        print(f"Je pèse {self.__weight} kg")
        print(f"Je peux rouler à {self.__max_speed} km/h ")

# Classe abstraite UnderseaVehicule
class UnderseaVehicule(metaclass=ABCMeta):
    """ A vehicle made for underwater sea."""
    def __init__(self):
        self.__weight = 150
        self.__max_depth = 300

    @abstractmethod
    def dive(self):
        pass
    
    @abstractmethod
    def description(self):
        print(f"Je pèse {self.__weight} kg")
        print(f"Je peux plonger à {self.__max_depth} m ")
 
# Classe UAV
class UAV(UnmannedVehicule, AerialVehicule):
    """Unmanned Aerial Vehicule"""
    def __init__(self, name):
        UnmannedVehicule.__init__(self, name)
        AerialVehicule.__init__(self)

    def fly(self):
        print("I believe I can flyyyyyyyy !!!!")

    def start_mission(self):
        super().start_mission()
        self.fly()

    def description(self):
        UnmannedVehicule.description(self)
        AerialVehicule.description(self)
        print("Je suis un UAV")

# Classe UUV
class UUV(UnmannedVehicule, UnderseaVehicule):
    """Unmanned Undersea Vehicule"""
    def __init__(self, name):
        UnmannedVehicule.__init__(self, name)
        UnderseaVehicule.__init__(self)
    
    def dive(self):
        print("BlBlBlBlBLBL")

    def start_mission(self):
        super().start_mission()
        self.dive()
    
    def description(self):
        UnmannedVehicule.description(self)
        UnderseaVehicule.description(self)
        print("Je suis un UUV")

# Classe UGV
class UGV(UnmannedVehicule, GroundVehicule):
    """Unmanned Ground Vehicule"""
    def __init__(self, name):
        UnmannedVehicule.__init__(self, name)
        GroundVehicule.__init__(self)
    
    def ride(self):
        print("Vroom Vroom Vroom")
    
    def start_mission(self):
        super().start_mission()
        self.ride()

    def description(self):
        UnmannedVehicule.description(self)
        GroundVehicule.description(self)
        print("Je suis un UGV")

##################################################
###                 MAIN                       ###
##################################################

ground_robot = UGV("Char Leclerc")
aerial_robot = UAV("A-10 Thunderbolt")
undersea_robot = UUV("Emeraude")

ground_robot.description()
ground_robot.start_mission()
print()
aerial_robot.description()
aerial_robot.start_mission()
print()
undersea_robot.description()
undersea_robot.start_mission()
print()