
# Test the Workshop class


from Workshop import *
from Enchanter import *
from Forge import *
from Weapon import *
from Materials import *
from Enchantment import *

# create a workshop object

def test_addWeapon():
    '''
    This method tests the addWeapon method in the Workshop class.
    '''
    
    workshop = Workshop(Enchanter(), Forge('Sword', 'Iron', 'Fire'))

    # create a weapon object
    weapon = Weapon("SampleWeapon", Wood, Metal)
    # add the weapon to the workshop
    workshop.addWeapon(weapon)
    # check if the weapon was added to the workshop
    assert weapon in workshop._weapons

    # checking if the number of weapons in the workshop is greater than 0 after adding a weapon
    assert len(workshop._weapons) > 0, "The weapon is not added to the workshop"

def test_removeWeapon():
    '''
    This method tests the removeWeapon method in the Workshop class.
    '''
    
    workshop = Workshop(Enchanter(), Forge('Sword', 'Iron', 'Fire'))

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
    workshop = Workshop(Enchanter(), Forge('Sword', 'Iron', 'Fire'))

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
    # creating a workshop object
    workshop = Workshop(Enchanter(), Forge('Sword', 'Iron', 'Fire'))

    # create a weapon object
    weapon = Weapon("SampleWeapon3", Wood, Metal)

    # add the weapon to the workshop
    workshop.addWeapon(weapon)

    # display the weapons in the workshop
    displayed_content = workshop.displayWeapons()
    # expected content
    expected_content = f'A {weapon.name} is not enchanted. {weapon.attack()}'

    # check if the weapon dictionary is added to the workshop
    assert weapon in workshop._weapons, "The weapon is not in the workshop"  

    # check if the weapon is displayed correctly
    assert displayed_content == expected_content, "The weapon is not displayed correctly"
    
# Note: We have an instance of the workshop class in each class because want to to isolate the tests for each class.