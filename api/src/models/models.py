class Coin:
    def __init__(self, name):
        self.name = name
        self.prices = []

    def __str__(self):
        return {"name": self.name, "prices": self.prices}