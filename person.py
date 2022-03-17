class Person:
    def __init__(self, position: str):
        self.__position = position

    def __str__(self):
        return f"{self.__position}"