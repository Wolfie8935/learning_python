class Character:
    def __init__(self,arrows_amount):
        self.arrows_amount = arrows_amount
    def throw_arrow(self):
        self.arrows_amount -= 1
        