class Player():
    def __init__(self):
        self.gems = {"b": 10, "w": 10, "g": 10, "r": 10, "y": 10,}
        self.discount = {"b": 0, "w": 0, "g": 0, "r": 0, "y": 0,}
        self.cards = []

    def can_purchase(self, card):
        for key,value in card.gems.items():
            if self.gems[key] + self.discount[key] < value:
                return False
            else:
                return True
    
    def purchase(self, card):
        condition = self.can_purchase(card)
        if condition:
            for key in card.gems:
                self.gems[key] = (self.gems[key] + self.discount[key]) -card.gems[key]
            self.cards.append(card)
            self.discount[card.color] += 1
        return condition

        

class Card():
    def __init__(self, color):
        self.color = color
        self.gems = {"b": 2, "w": 0, "g": 0, "r": 2, "y": 0,}




player = Player()

card = Card("r")

player.purchase(card)