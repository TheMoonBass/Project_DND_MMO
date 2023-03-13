class Monster:
    def __init__(self, name: str, cr: float, exp: int, hp: int, ac: int, speed: int, stats: dict, abilities: dict, actions: dict, drop_table: dict):
        self.name = name                #The name of the monster
        self.cr = cr                    #The challenge rating of the monster
        self.exp = exp                  #The experience reward for killing the monster
        self.hp = hp                    #The health (Hit Points) of the monster
        self.ac = ac                    #Armor class of the monster
        self.speed = speed              #The amount the monster can move per round of combat
        self.stats = stats              #STR, DEX, CON, INT, WIS, CHA
        self.abilities = abilities      #Any special abilites that the monster can use.
        self.actions = actions          #Attacks that the monster can perform.
        self.drop_table = drop_table    #The drop table for the monster
        return