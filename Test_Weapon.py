
# Weapon Test Cases

from Weapon import *
from Materials import *
from Workshop import *

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
    