# Padrao Singleton Monostate

class Borg:
    __shared_state = {}
    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass

b = Borg()
b1 = Borg()
b.x = 4

print("Objeto Borg b: ", b)
print("Objeto Borg b1: ", b1)
print("Estado de objetos de b: ", b.__dict__)
print("Estado de objetos de b1: ", b1.__dict__)