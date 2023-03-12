import json

class Player:
    def __init__(self, name: str, classes: dict, gold: int, stats: dict, skills: dict, actions: dict, saving_throw: dict, ac: int, speed: int,  profs: dict,  initiative: int, prof_bonus: int, defs: dict, conds: list, inv: dict):
        self.gold = gold                    # gold => Amount of gold
        self.stats = stats                  # stats => Container for stats: str, dex, con, int, wis, cha
        self.skills = skills                # skills => Container for skills: each skill will be its own dict
        self.name = name                    # name => Players name
        self.classes = classes              # classes => Dictionary of player classes: Each class has its own level, xp, hp (max, current), class proficiencies, spells
        self.saving_throw = saving_throw    # saving_throw => Container for saving throw stats: 
        self.ac = ac                        # ac => Armor class
        self.speed = speed                  # speed => Amount of movement per turn
        self.profs = profs                  # profs => Containter for proficiencies: Weapons, Armor, Tools, and Languages the player can use
        self.actions = actions              # actions => Container for actions: Attacks
        self.initiative = initiative        # initiative => Attack priority in battle: Where you go in attack order
        self.prof_bonus = prof_bonus        # prof_bonus => Amount when player has profiency in something
        self.defs = defs                    # defs => Defences: What the player is resistance or immune to
        self.conds = conds                  # conds => Conditions: Debuffs/Buffs
        self.inv = inv                      # inv => Player inventory: Dictionary containing armor and weapon slots as well as main inventory (20 item slots)
        return

    