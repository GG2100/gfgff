class Animal:
    def __init__(self, name = "None", sound = "None"):
        self.name = name
        self.sound = sound
    def make_sound(self):
        print(f"name - {self.name}\nsound - {self.sound}")
class Dogs(Animal):
    def __init__(self, name="None", sound="Woof wof!"):
        super().__init__(name)
        self.sound = sound
    def make_sound(self):
        super().make_sound()

class Cats(Animal):
    def __init__(self, name="None", sound="Meow"):
        super().__init__(name)
        self.sound = sound
    def make_sound(self):
        super().make_sound()


f=Animal()
ff=Dogs("Бетті")
ff.make_sound()
fd=Cats("Барсік")
fd.make_sound()

#Бетті, Барсік
