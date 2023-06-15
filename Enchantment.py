
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


class Enchantment:
    def __init__(self, name, magicDamage, effect, primaryMaterial, catalystMaterial):
        self._name = name
        self._magicDamage = magicDamage
        self._effect = effect
        self._primaryMaterial = primaryMaterial
        self._catalystMaterial = catalystMaterial


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

    def calculateDamage(self):
        '''
        This method calculates the damage of the enchantment.
        '''
        damage = self.primaryMaterial.strength * self.primaryMaterial.MagicPower + self.catalystMaterial.strength * self.catalystMaterial.MagicPower
        return damage

    def useEffect(self):
        '''
        This method applies the effect of the enchantment.
        '''
        return f'The {self.name} enchantment {self.effect}'
