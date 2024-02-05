class Wizard():
    def defend(self):
        print("magic shield")

class Archer():
    def defend(self):
        print("duck")

class Samurai():
    def defend(self):
        print("block")
        
def general_defense(character):
    character.defend()