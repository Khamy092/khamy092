
# Test the Workshop class


from Workshop import *
from Enchanter import *
from Forge import *
from Weapon import *
from Materials import *
from Enchantment import *

# create a workshop object
workshop = Workshop(Enchanter(), Forge('Sword', 'Iron', 'Fire'))

def test_addWeapon():
    '''
    This method tests the addWeapon method in the Workshop class.
    '''
    # create a weapon object
    weapon = Weapon("SampleWeapon", Wood, Metal)
    # add the weapon to the workshop
    workshop.addWeapon(weapon)
    # check if the weapon was added to the workshop
    assert weapon in workshop._weapons

def test_removeWeapon():
    '''
    This method tests the removeWeapon method in the Workshop class.
    '''
    # create a weapon object
    weapon = Weapon("SampleWeapon2", Wood, Metal)
    # add the weapon to the workshop
    workshop.addWeapon(weapon)
    # remove the weapon from the workshop
    workshop.removeWeapon(weapon)
    # check if the weapon was removed from the workshop
    assert weapon not in workshop._weapons


def test_addEnchantment():
    '''
    This method tests the addEnchantment method in the Workshop class.
    '''
    # create an enchantment object
    enchantment = Enchantment('Enchantment1', Diamond(), Diamond())
    # calculate the magic damage of the enchantment
    enchantment.calculateMagicDamage()
    # use the enchantment
    enchantment.useEffect()

    # add the enchantment to the workshop
    workshop.addEnchantment(enchantment)
    # check if the enchantment was added to the workshop
    assert enchantment in workshop._enchantments
    

def test_displayWeapons():
    '''
    This method tests the displayWeapons method in the Workshop class.
    '''
    # create a weapon object
    weapon = Weapon("SampleWeapon3", Wood, Metal)
    # add the weapon to the workshop
    workshop.addWeapon(weapon)

    # display the weapons in the workshop

    workshop.displayWeapons()
    exceptectedOutput = f'A {weapon.name()} is not enchanted. {weapon.attack()}'

    # check if the weapon was displayed
    assert workshop.displayWeapons() == exceptectedOutput
