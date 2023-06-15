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

class Enchanter(Crafter):

    
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

    def craft(self):
        pass

    def disassemble(self):
        pass

    def enchant(self):
        pass
    