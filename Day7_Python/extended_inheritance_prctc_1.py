class Father():
    def work(self):
        print("Working in the Public Hospital")

    def laugh(self):
        print("Ha Ha Ha!")

class Mother(Father):
    def work(self):
        print("Working in the Public Prosecutor's Office")
        
class Daughter(Mother):
    pass