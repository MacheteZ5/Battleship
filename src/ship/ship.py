class Ship():
    def __init__(self, ship_registry: str ,size : int):
        self.__ship_registry = ship_registry
        self.__size = size
        self.__life = size
        self.__isAlive = True

    @property
    def ship_registry(self) -> str:
        return self.__ship_registry
    
    @property
    def size(self) -> int:
        return self.__size

    @property
    def life(self) -> int:
        return self.__life

    @property
    def isAlive(self) -> bool:
        return self.__isAlive

    def receiveAttack(self):
        self.__life -= 1
        self.__isAlive = False if (self.__life == 0) else True    