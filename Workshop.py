# Workshop Module

'''
File: Workshop.py
Description: This class is the main class in the system. It uses other classess to create, modify and delete weapons. It also
adds and deletes materials. It also has a method to display all the weapons in the system.
Author: Taqi Khaliqdad
StudentID: 110341761
EmailID: khamy092
This is my own work as defined by the University's Academic Misconduct Policy.
'''
from Materials import *
from Weapon import *

class Workshop:

    '''
    This is the constructor for the Workshop class. It initializes the Enchanter and Forge objects.
    It also initializes the weapons, materials and enchantments lists as well as the materials and enchantments dictionaries.
    The workshop class is the main class in the system. It uses other classess to create, modify and delete weapons. It also adds and deletes materials.
    Workshop is also responsible for taking care of the inventory of the weapons, materials and enchantments.
    '''
    def __init__(self, enchanter, forge):
        
        self.enchanter = enchanter
        self.forge = forge
        self._weapons = []
        self._materials = set()
        self._enchantments = {}

    # Getters and setters for the weapons, materials and enchantments lists and dictionaries.

    def displayWeapons(self):
        for weapon in self._weapons:
            if weapon is Weapon.isEnchanted:
                print(weapon.getName() + " (Enchanted)")
            
            

    def displayEnchantments(self):
        pass

    def displayMaterials(self):
        pass

    def addWeapon(self):
        pass

    def removeWeapon(self):
        pass

    def addEnchantment(self):
        pass

    def removeEnchantment(self):
        pass

    def addMaterial(self):
        pass

    def removeMaterial(self):
        pass
