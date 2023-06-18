
# Enchantment module

'''
File: Enchantment.py
Description: This class contains all the required attributes and methods for our Enchantment object. It can calculate the damage of the enchantment used, and
contains the useEffect method which is used to apply the enchantment to the weapon.
Author: Taqi Khaliqdad
StudentID: 110341761
EmailID: khamy092
This is my own work as defined by the University's Academic Misconduct Policy.
'''
 
from Enchanter import Enchanter

class Enchantment:

    """
    This class contains all the required attributes and methods for our Enchantment object.
    It can calculate the damage of the enchantment used, and
    contains the useEffect method which is used to apply the enchantment to the weapon.
    """

   

    def __init__(self, name, primaryMaterial, catalystMaterial):
        self._name = name
        self._magicDamage = 0
        self._effect = ""
        self._primaryMaterial = primaryMaterial
        self._catalystMaterial = catalystMaterial

    # Getters and Setters
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def magicDamage(self):
        return self._magicDamage
    
    @magicDamage.setter
    def magicDamage(self, magicDamage):
        self._magicDamage = magicDamage

    @property
    def effect(self):
        return self._effect
    
    @effect.setter
    def effect(self, effect):
        self._effect = effect

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

    def calculateMagicDamage(self):
        '''
        This method calculates the damage of the enchantment using a specific formula.
        '''
        self.magicDamage = (self._primaryMaterial.strength * self._primaryMaterial.magicPower) + (self._catalystMaterial.strength * self._catalystMaterial.magicPower)
        self.magicDamage = round(self.magicDamage, 2)
        return self.magicDamage

    def useEffect(self):
        '''
        This method applies the effect of the enchantment.
        '''

        enchanter = Enchanter()

        # check if enchantment name is in recipes
        if self.name in enchanter.recipes:
            self.effect = enchanter.recipes[self.name]
            return f'{self.name} enchantment and {self.effect}'