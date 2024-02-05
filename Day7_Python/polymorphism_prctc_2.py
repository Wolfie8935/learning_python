class Wizard():
    def attack(self):
        print("magic attack")

class Archer():
    def attack(self):
        print("shoot arrow")

class Samurai():
    def attack(self):
        print("katana attack")
        
gandalf = Wizard()
hawkeye = Archer()
jack = Samurai()
characters = [hawkeye, gandalf, jack]
for char in characters:
    char.attack()