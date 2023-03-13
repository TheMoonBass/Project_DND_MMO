class Weapon:
    def __init__(self, name: str, desc: str, used_stat: str, type: str, rarity: str, num_dmg_dice: int, size_dmg_dice: int, properties: dict, abilities: dict):
        self.name = name                        #The name of the item
        self.desc = desc                        #Item description
        self.used_stat = used_stat              #THe stat that the item scales off of. Ex: Greatsword = STR
        self.type = type                        #The type of weapon (simple, martial, casting focus, etc.)
        self.rarity = rarity                    #The rarity of the weapon (common, uncommon, rare, very rare, legendary)
        self.num_dmg_dice = num_dmg_dice        #The number of dice rolled for damage when attacking with the weapon
        self.size_dmg_dice = size_dmg_dice      #The size of dice rolled for damage when attacking with the weapon (d4, d6, d8, etc.)
        self.properties = properties            #Any notable properties that the weapon has. Ex: Heavy - takes two hands to weild
        self.abilities = abilities              #Any special abilites given to the player weilding the weapon. Ex: Ability to cast a certain spell a number of times
        return