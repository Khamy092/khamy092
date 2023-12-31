# Enchanter class (Inherits from Crafter)


'''
File: Workshop.py
Description: This class inherits from the Crafter class. It contains the craft and disassemble methods that are used to create and disassemble enchantments.
Author: Taqi Khaliqdad
StudentID: 110341761
EmailID: khamy092
This is my own work as defined by the University's Academic Misconduct Policy.
'''

from Crafter import Crafter
from Workshop import *
from Enchantment import *

class Enchanter(Crafter):

    """
    This class inherits from the Crafter class. It contains the craft and disassemble methods that are used to create
    and disassemble enchantments. It also contains the enchant method that is used to apply enchantments to weapons.
    """
    
    def __init__(self):

        # recipes of enchantments
        self.recipes = {
        "Holy": "pulses a blinding beam of light",
        "Lava": "melts the armour off an enemy",
        "Pyro": "applies a devastating burning effect",
        "Darkness": "binds the enemy in dark vines",
        "Cursed": "causes the enemy to become crazed",
        "Hydro": "envelops the enemy in a suffocating bubble",
        "Venomous": "afflicts a deadly, fast-acting toxin"
        }

    # craft method: used to create enchantments
    def craft(self, enchantment, primaryMaterial, catalystMaterial, workshop_materials):

        # create enchantment
        CreatedEnchantment = Enchantment(enchantment, 0, enchantment.effect , primaryMaterial, catalystMaterial)

        # check if enchantment name is in recipes
        if enchantment in self.recipes.keys():
            # getting the enchantment's effect from the recipes dictionary
            enchantment.effect = self.recipes[enchantment]
        
        else:
            # if enchantment name is not in recipes, then it is not a valid enchantment
            print("Invalid enchantment name")
            return
        
        # remove materials from workshop
        workshop_materials[self._primaryMaterial.__class__.__name__] -= 1
        workshop_materials[self._catalystMaterial.__class__.__name__] -= 1

        return CreatedEnchantment
    
    # disassemble method: used to disassemble enchantments
    def disassemble(self, enchantment, workshop_materials, workshop_enchantments): 
        
        """
        This method is used to disassemble enchantments. It takes in an enchantment object and the materials dictionary.
        It then disassembles the enchantment object and adds the materials from the enchantment back into the materials dictionary.
        """
        
        # add materials back into workshop materials dictionary
        workshop_materials[self._primaryMaterial.__class__.__name__] += 1
        workshop_materials[self._catalystMaterial.__class__.__name__] += 1
        

        # delete enchantment object from workshop enchantments dictionary
        del workshop_enchantments[enchantment]


    # enchant method: used to apply enchantments to weapons
    def enchant(self, weapon, enchantmentName, enchantment, workshop_enchantments):
        
        # check if enchantment name is in recipes
        if enchantmentName in self.recipes:
            # getting the enchantment's effect from the recipes dictionary
            enchantment.effect = self.recipes[enchantmentName]

        # check if enchantment is in workshop enchantments dictionary
        if enchantment in workshop_enchantments:

            # apply enchantment to weapon
            weapon.enchantment = enchantment

            # set weapon's isEnchanted attribute to True
            weapon.isEnchanted = True
            
            # add enchantment's magic damage to weapon's damage
            weapon.damage *= enchantment.magicDamage

            # remove enchantment from workshop enchantments dictionary
            del workshop_enchantments[enchantment]