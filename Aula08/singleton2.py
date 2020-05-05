# Singleton Clássico
class Singleton:
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print("Método __init__ chamado")
        else:
            print("Instância já criada", self.getInstance())
    
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s = Singleton()
s1 = Singleton()
print(s1.getInstance())
print(s.getInstance())
print(s1.getInstance())