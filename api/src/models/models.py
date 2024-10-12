class Coin:
    coin_id = 0

    def __init__(self, name):
        self.name = name
        self.prices = []

        Coin.coin_id += 1

        self.coin_id = Coin.coin_id

    def __str__(self):
        return {"coin_id": self.coin_id, "name": self.name, "prices": self.prices}

