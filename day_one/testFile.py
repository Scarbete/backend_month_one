

class Animal:
    name = ''
    age = 0
    color = 'none'

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def make_sound(self):
        print(f'{self.name} is sounded')


class Cat(Animal):
    second_color = 'none'

    def __init__(self, name, age, color, second_color):
        super().__init__(name, age, color)
        self.second_color = second_color

    def make_cound(self):
        print(f'{self.name}: meeeow!')


class Dog(Animal):

    def __init__(self, name, age, color):
        super().__init__(name, age, color)

    def make_cound(self):
        print(f'{self.name}: bark!')


animal_class = Animal('bird', 1, 'white')

animal_class.make_sound()

cat = Cat('Kami', 2, 'gray', 'white')

dog = Dog('Bobik', 12, 'black')

cat.make_sound()

dog.make_sound()
