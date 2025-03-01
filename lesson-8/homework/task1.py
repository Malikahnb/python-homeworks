class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def make_sound(self):
        return f"{self.name} the {self.species} says {self.sound}!"

    def eat(self, food):
        return f"{self.name} is eating {food}."

    def sleep(self):
        return f"{self.name} is sleeping."


class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, "Cow", "Moo")

    def produce_milk(self):
        return f"{self.name} is producing milk."


class Chicken(Animal):
    def __init__(self, name):
        super().__init__(name, "Chicken", "Cluck")

    def lay_egg(self):
        return f"{self.name} has laid an egg!"


class Sheep(Animal):
    def __init__(self, name):
        super().__init__(name, "Sheep", "Baa")

    def shear_wool(self):
        return f"{self.name} is being sheared for wool."


class Horse(Animal):
    def __init__(self, name):
        super().__init__(name, "Horse", "Neigh")

    def herd(self):
        return f"{self.name} herds livestock."


# Example usage
beatrice = Cow("Beatrice")
henry = Chicken("Henry")
shaun = Sheep("Shaun")
mustang = Horse("Mustang")

animals = [beatrice, henry, shaun, mustang]

for animal in animals:
    print(animal.make_sound())
    print(animal.eat("grass"))
    print(animal.sleep())

print(bessie.produce_milk())
print(henry.lay_egg())
print(shaun.shear_wool())
print(mustang.herd())
