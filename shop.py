class Shop:
    def __init__(self, owner: object, listings: list):
        self.owner = owner          # owner => Shop owner
        self.listings = listings    # listings => Items for sale: Each listing will be as follows -- Item (With description and stats): Cost
        return