class Town:
    def __init__(self, name: str, shops: dict, has_blacksmith: bool):
        self.name = name                        # name => Name of the town
        self.shops = shops                      # shops => The shops in the town: Each shop will be a dictionary
        self.has_blacksmith = has_blacksmith    # has_blacksmith => Boolean value for if there is a blacksmith in the town
        return