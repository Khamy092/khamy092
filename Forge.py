# Forge Module (Inherits from Crafter)


'''
File: Forge.py
Description: This class inherits from the Crafter class. It contains the forge method that is used to create weapons. It also contains
the disassemble method that is used to delete weapons.
Author: Taqi Khaliqdad
StudentID: 110341761
EmailID: khamy092
This is my own work as defined by the University's Academic Misconduct Policy.
'''
from Weapon import *
from Crafter import Crafter
from Workshop import Workshop

class Forge(Crafter):
    def __init__(self, name, primaryMaterial, catalystMaterial):
        super().__init__()
        Weapon.__init__(self, name, primaryMaterial, catalystMaterial)

    def craft(self, name, primaryMaterial, catalystMaterial):
        '''
        This method is used to create a weapon. It takes in the name, primary material and catalyst material as parameters.
        It then creates a weapon object and adds it to the weapons list in the Workshop class.
        It also removes the materials from the materials dictionary to reflect the change in the inventory.
        '''
        
        # create a weapon object
        craftedWeapon = Weapon(name, primaryMaterial, catalystMaterial, Workshop.materials)
        # add the weapon to the weapons list
        Workshop.addWeapon(craftedWeapon)
        # remove the materials from the materials dictionary
        materials = Workshop.materials
        materials[primaryMaterial] -= 1
        materials[catalystMaterial] -= 1

    def disassemble(self, weapon):
        '''
        This method is used to delete a weapon. It takes in the weapon to be deleted as a parameter.
        It then removes the weapon from the weapons list in the Workshop class.
        It also adds the materials from the materials dictionary to reflect the change in the inventory.
        '''
        
        # remove the weapon from the weapons list
        Workshop.removeWeapon(weapon)
        
        # add the materials from the materials dictionary
        materials = Workshop.materials
        materials[weapon.primaryMaterial] += 1
        materials[weapon.catalystMaterial] += 1
    