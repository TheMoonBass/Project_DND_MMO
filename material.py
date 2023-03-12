class Material:
    def __init__(self, name: str, desc: str, rarity: str, sell_price: int, buy_price: int, lvl: int):
        self.name = name                                #Material name
        self.desc = desc                                #The material description
        self.rarity = rarity                            #The rarity of the item (common, uncommon, rare, very rare, legendary)
        self.sell_price = sell_price                    #The price an item can be sold to a shop for
        self.buy_price = buy_price                      #The price an item can be bought for from a shop
        self.lvl = lvl                                  #The item level (Should be equal to the level of the monster it would be obtained from, the zone it came from if gathered, or the quest it came from if it was a quest reward)
        return
