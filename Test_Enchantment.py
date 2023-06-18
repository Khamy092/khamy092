# Test file for Enchantment.py

from Enchantment import *
from Enchanter import *
from Materials import *
from Workshop import *


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