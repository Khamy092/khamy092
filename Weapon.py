# Weapon Module


'''
File: Weapon.py
Description: This class contains all the required methods and attributes for our Weapon object.
Author: Taqi Khaliqdad
StudentID: 110341761
EmailID: khamy092
This is my own work as defined by the University's Academic Misconduct Policy.
'''

from Materials import *

class Weapon:

    '''
    This is the constructor for the Weapon class. It initializes the name,
    damage, primaryMaterial, catalystMaterial and enchantment attributes.
    It also contains all the getters and setters for the attributes.
    '''
    def __init__(self, name, primaryMaterial, catalystMaterial, damage=0,  enchantment=None):
        self._name = name
        self._damage = float(damage)
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
    def isEnchanted(self, enchanted):
        self._enchanted = bool(enchanted)
    
    @property
    def primaryMaterial(self):
        return self._primaryMaterial

    @primaryMaterial.setter
    def primaryMaterial(self, primaryMaterial):
        self._primaryMaterial = primaryMaterial

    @property
    def catalystMaterial(self):
        return self._catalystMaterial

    @catalystMaterial.setter
    def catalystMaterial(self, catalystMaterial):
        self._catalystMaterial = catalystMaterial

    @property
    def enchantment(self):
        return self._enchantment
    
    @enchantment.setter
    def enchantment(self, enchantment):
        self._enchantment = enchantment

    
    def calculateDamage(self):

        """
        This method calculates the damage of the weapon based on the materials used to create it.
        """

        # if the weapon is made of two peices of wood
        if isinstance(self._primaryMaterial, Wood) and isinstance(self._catalystMaterial, Wood):
            try:
                self._damage = self._primaryMaterial.strength * self._catalystMaterial.strength
                return self._damage
            except TypeError as e:
                return e
        
        # if the weapon is made of two peices of metal
        elif isinstance(self._primaryMaterial, Metal) and isinstance(self._catalystMaterial, Metal):
            try:
                self._damage = (self._primaryMaterial.strength * self.primaryMaterial.purity) * (self._catalystMaterial.strength * self._catalystMaterial.purity)
                return self._damage
            except TypeError as e:
                return e

        
        # if the weapon is made of a peice of metal and a peice of wood
        elif isinstance(self._primaryMaterial, Metal) and isinstance(self._catalystMaterial, Wood) or isinstance(self._primaryMaterial, Wood) and isinstance(self._catalystMaterial, Metal):
            try:
                self._damage = self._primaryMaterial.strength * (self._catalystMaterial.strength * self._catalystMaterial.purity)
                return self._damage
            
            except TypeError as e:
                return e

    def attack(self):
            
            """
            This method returns a string that describes the attack of the weapon.
            """

            # rounding the damage to two decimal places
            damageRounded = round(self._damage, 2)
            
            return f'It deals {damageRounded} damage.'