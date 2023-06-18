# Test file for Enchanter.py


from Workshop import *
from Enchanter import Enchanter
from Forge import Forge

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
