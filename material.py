class Material:
    def __init__(self, name: str, desc: str, rarity: str, shop_sell_price: int, lvl: int):
        self.name = name                                #Material name
        self.desc = desc                                #The material description
        self.rarity = rarity                            #The rarity of the item (common, uncommon, rare, very rare, legendary)
        self.shop_sell_price = shop_sell_price          #The price the item is available from a shop within the world. If the item is unavailable from a shop, this should be 0
        self.lvl = lvl                                  #The item level (Should be equal to the level of the monster it would be obtained from, the zone it came from if gathered, or the quest it came from if it was a quest reward)

