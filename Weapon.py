# Weapon Module


'''
File: Weapon.py
Description: This class contains all the required methods and attributes for our Weapon object.
Author: Taqi Khaliqdad
StudentID: 110341761
EmailID: khamy092
This is my own work as defined by the University's Academic Misconduct Policy.
'''


class Weapon:

    '''
    This is the constructor for the Weapon class. It initializes the name,
    damage, primaryMaterial, catalystMaterial and enchantment attributes.
    It also contains all the getters and setters for the attributes.
    '''
    def __init__(self, name, damage, primaryMaterial, catalystMaterial, enchantment) -> None:
        self._name = name
        self._damage = damage
        self._primaryMaterial = primaryMaterial
        self._catalystMaterial = catalystMaterial
        self._enchantment = enchantment
        self._enchanted = False


    # getters and setters for the attributes
    
    @property
    def name(self):
        return self._name

    @name.setter    
    def name(self, name):
        self._name = name    

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, damage):
        self._damage = damage

    @property
    def isEnchanted(self):
        return self._enchanted
    
    @isEnchanted.setter
    def isenchanted(self, enchanted):
        self._enchanted = enchanted
    
    @property
    def primaryMaterial(self):
        return self._primaryMaterial

    @primaryMaterial.setter
    def setPrimaryMaterial(self, primaryMaterial):
        self._primaryMaterial = primaryMaterial

    @property
    def catalystMaterial(self):
        return self._catalystMaterial

    @catalystMaterial.setter
    def setCatalystMaterial(self, catalystMaterial):
        self._catalystMaterial = catalystMaterial

    @property
    def enchantment(self):
        return self._enchantment
    
    @enchantment.setter
    def setEnchantment(self, enchantment):
        self._enchantment = enchantment

    
    def calculateDamage(self):
        pass

    def attack(self):
        pass