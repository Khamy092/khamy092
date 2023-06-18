
from Workshop import *
from Enchanter import Enchanter
from Forge import Forge
from Weapon import Weapon
from Materials import *
from Enchantment import *


# Create a workshop, forge, enchanter.
workshop = Workshop(Enchanter(), Forge('Wood','Wood', 'Wood'))

# Create a set of materials and lists for testing.
materials = [Maple(), Oak(), Ash(), Bronze(), Iron(), Steel(),
Ruby(), Sapphire(), Emerald(), Diamond(), Amethyst(), Onyx()]

weaponBlueprints = {
"Sword": [Steel(), Maple()],
"Shield": [Bronze(), Oak()],
"Axe": [Iron(), Ash()],
"Scythe": [Steel(), Ash()],
"Bow": [Oak(), Maple()],
"Wand": [Ash(), Oak()],
"Staff": [Bronze(), Maple()],
"Dagger": [Bronze(), Bronze()]}

enchantmentBlueprints = {
"Holy": [Diamond(), Diamond()],
"Lava": [Ruby(), Onyx()],
"Pyro": [Ruby(), Diamond()],
"Darkness": [Onyx(), Amethyst()],
"Cursed": [Onyx(), Onyx()],
"Hydro": [Sapphire(), Emerald()],
"Venomous": [Emerald(), Amethyst()],
"Earthly": [Emerald(), Emerald()]}

enchantedWeapons = ["Holy Greatsword", "Molten Defender", "Berserker Axe", "Soul Eater",
"Twisted Bow", "Wand of the Deep", "Venemous Battlestaff"]

# Adds a number of materials to use for crafting.
for material in materials:
    if isinstance(material, Wood):
        workshop.addMaterial(material.__class__.__name__, 20)
    elif isinstance(material, Metal):
        workshop.addMaterial(material.__class__.__name__, 10)
    else:
        workshop.addMaterial(material.__class__.__name__, 5)
print("--------------------------------Material Store--------------------------------")
print(workshop.displayMaterials())

# Crafts the following: Sword, Shield, Axe, Scythe, Bow, Wand and Staff weapons.
for weapon, materials in weaponBlueprints.items():
    craftedWeapon = workshop.forge.craft(
        materials[0], materials[1], workshop._materials)
    workshop.addWeapon(craftedWeapon)

# Disassemble the extra weapon.
workshop.removeWeapon(workshop.forge.disassemble(
workshop._weapons[7], workshop._materials))

print("------------------------------------Armoury-----------------------------------")
print(workshop.displayWeapons())


# Crafts the following: Holy, Lava, Pyro, Darkness, Cursed, Hydro and Venomous enchantments.
for enchantment, materials in enchantmentBlueprints.items():
    craftedEnchantment = workshop.enchanter.craft(
        enchantment, materials[0], materials[1], workshop.materials)
    workshop.addEnchantment(craftedEnchantment)

# Disassemble the extra enchantment.
workshop.removeEnchantment(workshop.enchanter.disassemble(
workshop._enchantments[7], workshop._materials))

print("------------------------------------Enchantments------------------------------------")
print(workshop.displayEnchantments())
print("-----------------------------------Material Store-----------------------------------")
print(workshop.displayMaterials())

# Enchant the following weapons: Sword, Shield, Axe, Scythe, Bow, Wand and Staff.
for i in range(len(enchantedWeapons)):
    workshop.enchanter.enchant(
    workshop.weapons[i], enchantedWeapons[i], workshop.enchantments[i])
print("-----------------------------------Enchanted Armoury----------------------------------")
print(workshop.displayWeapons())
