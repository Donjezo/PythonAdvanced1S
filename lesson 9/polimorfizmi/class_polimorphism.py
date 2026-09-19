class Dog:
    def __init__(self,name):
        self.name=name

    def sound(self):
        print(f"{self.name} makes the sound woof")


class Cat:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes the sound majuuu")


class Bird:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes the sound ciu ciu")

dog = Dog("haski")
cat= Cat("haiii")
bird = Bird("twiti")

for animal in (dog,cat,bird):
    animal.sound()