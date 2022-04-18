class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        pass

animals = [
    Animal('lion'),
    Animal('tiger')
]

def animal_sound(animals: list):
    for animal in animals:
        if animal.name == 'lion':
            print('roar')

        elif animal.name == 'tiger':
            print('ngrrr')

animal_sound(animals)

#to make it conform OC principles

class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def get_name(self) -> str:
        pass

    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        return 'roar'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())

animal_sound(animals)