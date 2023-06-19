
from Materials import *
from abc import ABC, abstractmethod

class Crafter(ABC):

    ''' 
    Crafter is a superclass for the Forge and Enchanter classes. It contains the craft and
    disassemble methods that are used in both the subclasses. This class is an abstract class and cannot be instantiated.'''

    def __init__(self) -> None:
        pass

    # abstract methods
    @abstractmethod
    def craft(self):
        pass
    
    @abstractmethod
    def disassemble(self):
        pass


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
             
            if weapon.isEnchanted == True:
                return f'A {weapon.name} is embued with a {weapon.useEffect()}. {weapon.attack()}'
            
            elif weapon.isEnchanted == False:
                return f'A {weapon.name} is not enchanted. {weapon.attack()}'

            
            
    # display all the enchantments in the workshop
    def displayEnchantments(self):
        for enchantment in self._enchantments:
            return f'An {enchantment.name} enchantment is stored in the workshop.'

    # display all the materials in the workshop
    def displayMaterials(self):
        for material in self._materials:
            return f'A {material.__class__.__name__,}: {self._materials[material]} remaining.'

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
        self._enchantments[enchantment] = enchantment
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

    
    # All tests are done and passed.


class Weapon:

    '''
    This is the constructor for the Weapon class. It initializes the name,
    damage, primaryMaterial, catalystMaterial and enchantment attributes.
    It also contains all the getters and setters for the attributes.
    '''
    def __init__(self, name, primaryMaterial, catalystMaterial, damage=0,  enchantment=None):
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
    

# all tests for the Weapon class done


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
        craftedWeapon = Weapon(name, primaryMaterial, catalystMaterial, workshop._materials)
        # add the weapon to the weapons list
        workshop.addWeapon(craftedWeapon)
        workshopMaterials = workshop._materials
        # remove the materials from the materials dictionary
        workshopMaterials[craftedWeapon.primaryMaterial.__class__.__name__] -= 1
        workshopMaterials[craftedWeapon.catalystMaterial.__class__.__name__] -= 1

    def disassemble(self, weapon):
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
        workshop_materials[primaryMaterial] -= 1
        workshop_materials[catalystMaterial] -= 1

        return CreatedEnchantment
    
    # disassemble method: used to disassemble enchantments
    def disassemble(self, enchantment, workshop_materials, workshop_enchantments): 
        
        """
        This method is used to disassemble enchantments. It takes in an enchantment object and the materials dictionary.
        It then disassembles the enchantment object and adds the materials from the enchantment back into the materials dictionary.
        """
        
        # add materials back into workshop materials dictionary
        workshop_materials[enchantment.primaryMaterial] += 1
        workshop_materials[enchantment.catalystMaterial] += 1

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