from AllClasses import *


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
    
def test_removeEnchantment():
    '''
    This method tests the removeEnchantment method in the Workshop class.
    '''
    workshop = Workshop(Enchanter(), Forge('Sword', 'Iron', 'Fire'))

    # create an enchantment object
    enchantment = Enchantment('Enchantment2', Diamond(), Diamond())
    # calculate the magic damage of the enchantment
    enchantment.calculateMagicDamage()
    # use the enchantment
    enchantment.useEffect()

    # add the enchantment to the workshop
    workshop.addEnchantment(enchantment)

    # remove the enchantment from the workshop
    workshop.removeEnchantment(enchantment)

    # check if the enchantment was removed from the workshop
    assert enchantment not in workshop._enchantments


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
    


def test_displayEnchantments():
    '''
    This method tests the displayEnchantments method in the Workshop class.
    '''
    # creating a workshop object
    workshop = Workshop(Enchanter(), Forge('Sword', 'Iron', 'Fire'))

    # create an enchantment object
    enchantment = Enchantment('Enchantment2', Diamond(), Diamond())
    # calculate the magic damage of the enchantment
    enchantment.calculateMagicDamage()
    # use the enchantment
    enchantment.useEffect()

    # add the enchantment to the workshop
    workshop.addEnchantment(enchantment)

    # display the enchantments in the workshop
    displayed_content = workshop.displayEnchantments()
    # expected content
    expected_content = f'An {enchantment.name} enchantment is stored in the workshop.'

    # check if the enchantment dictionary is added to the workshop
    assert enchantment in workshop._enchantments, "The enchantment is not in the workshop"  

    # check if the enchantment is displayed correctly
    assert displayed_content == expected_content, "The enchantment is not displayed correctly"




def test_enchantWeapon():

    '''
    This method tests the enchantWeapon method in the Workshop class.
    '''
    # creating a workshop object
    workshop = Workshop(Enchanter(), Forge('Sword', 'Iron', 'Fire'))

    # create a weapon object
    weapon = Weapon("SampleWeapon4", Wood, Metal)

    # add the weapon to the workshop
    workshop.addWeapon(weapon)

    # create an enchantment object
    enchantment = Enchantment('Enchantment3', Diamond(), Diamond())
    # calculate the magic damage of the enchantment
    enchantment.calculateMagicDamage()
    # use the enchantment
    enchantment.useEffect()

    # add the enchantment to the workshop
    workshop.addEnchantment(enchantment)

    # enchant the weapon
    workshop.enchanter.enchant(weapon, enchantment.name, enchantment, workshop._enchantments)

    # check if the weapon is enchanted
    assert weapon.enchantment == enchantment, "The weapon is not enchanted"

    # check if the weapon is enchanted correctly
    assert weapon.enchantment.name == enchantment.name, "The weapon is not enchanted correctly"


def test_displayMaterials():
    '''
    This method tests the displayMaterials method in the Workshop class.
    '''
    # creating a workshop object
    workshop = Workshop(Enchanter(), Forge('Sword', 'Iron', 'Fire'))

    # create a material object
    material = Wood(5)
    workshop.addMaterial(material, 5)
    
    # display the materials in the workshop
    displayed_content = workshop.displayMaterials()
    # expected content
    expected_content = f'A {material.__class__.__name__,}: {workshop._materials[material]} remaining.'

    # check if the material dictionary is added to the workshop
    assert material in workshop._materials, "The material is not in the workshop"

    # check if the material is displayed correctly
    assert displayed_content == expected_content, "The material is not displayed correctly"


def test_addMaterial():
    '''
    This method tests the addMaterial method in the Workshop class.
    '''
    # creating a workshop object
    workshop = Workshop(Enchanter(), Forge('Sword', 'Iron', 'Fire'))

    # create a material object
    material = Wood(5)
    workshop.addMaterial(material, 5)

    # check if the material is added to the workshop
    assert material in workshop._materials, "The material is not in the workshop"

    # check if the material is added correctly
    assert workshop._materials[material] == 5, "The material is not added correctly"

def test_removeMaterial():
    '''
    This method tests the removeMaterial method in the Workshop class.
    '''
    # creating a workshop object
    workshop = Workshop(Enchanter(), Forge('Sword', 'Iron', 'Fire'))

    # create a material object
    material = Wood(5)
    workshop.addMaterial(material, 5)

    # remove the material from the workshop
    workshop.removeMaterial(material)

    # check if the material is removed from the workshop
    assert material not in workshop._materials, "The material is not in the workshop"

# Note: We have an instance of the workshop class in each class because want to to isolate the tests for each class.



def test_calculateMagicDamage():
    '''
    This function tests the calculateMagicDamage method in the Enchantment class.
    '''
    # Create an Enchantment object
    enchantment = Enchantment("Holly", Diamond(), Diamond())

    # Call the calculateMagicDamage method to calculate the magic damage
    enchantment.calculateMagicDamage()

    # check if the magic damage is calculated correctly
    assert enchantment.magicDamage == 9.24


def test_useEffect():
    '''
    This function tests the useEffect method in the Enchantment class.
    '''
    # Create an Enchantment object
    enchantment = Enchantment("Holy", Diamond(), Diamond())

    # Call the useEffect method to apply the enchantment to the weapon
    enchantment.useEffect()

    # check if the effect is applied correctly by manually checking the string
    assert enchantment.useEffect() == f'{enchantment.name} enchantment and pulses a blinding beam of light'


# Weapon Test Cases

def test_calculateDamage():
    # test case 1
    weapon1 = Weapon("Weapon1", Ash(), Oak())
    assert weapon1.calculateDamage() == 12.0 #3 * 4

    # test case 2
    weapon2 = Weapon("Weapon2", Ash(), Ash())
    assert weapon2.calculateDamage() == 9.0 #3 * 3

    # test case 3
    weapon3 = Weapon("Weapon3", Oak(), Oak())
    assert weapon3.calculateDamage() == 16.0 #4 * 4


def test_attack():
    
    # test case 1 | wood and wood
    weapon4 = Weapon("Weapon4", Ash(), Oak())
    weapon4.calculateDamage()

    assert weapon4.attack() == "It deals 12 damage."

    # test case 2 | wood and metal

    weapon5 = Weapon("Weapon5", Oak(), Steel())
    weapon5.calculateDamage()

    assert weapon5.attack() == "It deals 72.0 damage."

    # test case 3 | metal and metal

    weapon6 = Weapon("Weapon6", Steel(), Steel())
    weapon6.calculateDamage()
    
    assert weapon6.attack() == "It deals 324.0 damage."


def test_craft():
    '''
    This function tests the craft method in the Enchanter class.
    '''
    # Create an Enchanter object
    workshop = Workshop(Enchanter(), Forge('Wood','Wood', 'Wood'))
    workshop.addMaterial(Ruby(), 5)
    workshop.addMaterial(Onyx(), 5)
    
    # Call the craft method to craft an enchantment
    enchantment = workshop.enchanter.craft("Lava", Ruby(), Onyx(), workshop._materials)
    
    enchantment.calculateMagicDamage()
    enchantment.useEffect()
    workshop.addEnchantment(enchantment)

    # check if the enchantment is crafted correctly by manually checking the string
    assert enchantment.name == "Lava"
    assert enchantment.magicDamage == 8.64
    assert enchantment.effect == "burns the target"
    assert enchantment.primaryMaterial.name == "Ruby"
    assert enchantment.catalystMaterial.name == "Onyx"
