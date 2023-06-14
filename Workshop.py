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
from Enchantment import *
from Enchanter import *
from Forge import *


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
        self._materials = {}
        self._enchantments = {}

    # display all the weapons in the workshop
    def displayWeapons(self):
        for weapon in self._weapons:
            if weapon is Weapon.isEnchanted:
                print(weapon.getName() + " (Enchanted)")

            
            
    # display all the enchantments in the workshop
    def displayEnchantments(self):
        for enchantment in self._enchantments:
            print(f'An {enchantment.getEnchantmentName()} enchantment is stored in the workshop.')

    # display all the materials in the workshop
    def displayMaterials(self):
        for material in self._materials:
            print(f'A {material.__class__.__name__,}: {self._materials[material]} remaining.')

    # add a weapon to the workshop
    def addWeapon(self, Weapon):
        self._weapons.append(Weapon)
        return self._weapons

    # remove a weapon from the workshop
    def removeWeapon(self, weapon):
        self._weapons.remove(weapon)
        return self._weapons

    # add an enchantment to the workshop
    def addEnchantment(self, enchantment):
        self._enchantments.append(enchantment)
        return self._enchantments
    
    # remove an enchantment from the workshop
    def removeEnchantment(self, enchantment):
        del self._enchantments[enchantment]
        return self._enchantments

    # add a material to the workshop
    def addMaterial(self, material, quantity):
        self._materials[material] = quantity
        return self._materials

    # remove a material from the workshop
    def removeMaterial(self, material):

        # remove the material from the dictionary
        del self._materials[material]
        return self._materials
