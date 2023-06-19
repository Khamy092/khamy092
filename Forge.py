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
from Workshop import Workshop as Workshop
from Enchanter import Enchanter as Enchanter



class Forge(Crafter):
    def __init__(self, name, primaryMaterial, catalystMaterial):
        Weapon.__init__(self, name, primaryMaterial, catalystMaterial)


    def craft(self, name, primaryMaterial, catalystMaterial):
        '''
        This method is used to create a weapon. It takes in the name, primary material and catalyst material as parameters.
        It then creates a weapon object and adds it to the weapons list in the Workshop class.
        It also removes the materials from the materials dictionary to reflect the change in the inventory.
        '''
        workshop = Workshop(Enchanter(), Forge('name', 'primaryMaterial', 'catalystMaterial'))
        # create a weapon object
        craftedWeapon = Weapon(name, primaryMaterial, catalystMaterial, workshopMaterials)
        # add the weapon to the weapons list
        workshop.addWeapon(craftedWeapon)
        workshopMaterials = workshop._materials
        # remove the materials from the materials dictionary
        workshopMaterials[craftedWeapon.primaryMaterial.__class__.__name__] -= 1
        workshopMaterials[craftedWeapon.catalystMaterial.__class__.__name__] -= 1

    def disassemble(self, weapon, workshopMaterials):
        '''
        This method is used to delete a weapon. It takes in the weapon to be deleted as a parameter.
        It then removes the weapon from the weapons list in the Workshop class.
        It also adds the materials from the materials dictionary to reflect the change in the inventory.
        '''
        workshop = Workshop()
        # remove the weapon from the weapons list
        workshop.removeWeapon(weapon)
        
        # add the materials from the materials dictionary
        workshopMaterials = workshop._materials

        workshopMaterials[weapon.primaryMaterial.__class__.__name__] += 1
        workshopMaterials[weapon.catalystMaterial.__class__.__name__] += 1
    