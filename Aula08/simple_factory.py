from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass

class Dog(Animal):
    def __init__(self):
        print('cachorro')

    def do_say(self):
        print('Au Au')

class Cat(Animal):
    def __init__(self):
        print('gato')

    def do_say(self):
        print('miau')

class ForestFactory:
    def make_sound(self, object_type):
        return eval(object_type)().do_say()
'''    
ff = ForestFactory()
animal = input("Digite Dog ou Cat")
ff.make_sound(animal)
'''
