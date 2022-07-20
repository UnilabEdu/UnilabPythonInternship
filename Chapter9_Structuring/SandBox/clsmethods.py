import datetime


class Animal:
    animal_type = "Animal"

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def which_class(cls):
        return f"This is class {cls.animal_type}"


class Dog(Animal):
    animal_type = "Dog"


class Cat(Dog, Animal):
    animal_type = "Cat"


class Computer:
    def turn_on(self):
        pass

    @staticmethod
    def print_date():
        print(datetime.datetime.now())


if __name__ == "__main__":
    list_of_classes = [Animal, Dog, Cat]

    for _class in list_of_classes:
        print(_class.which_class())
