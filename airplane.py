class Airplane:
    def __init__(self, model: str, team: list, passenger: int, weight: float):
        self.__model = model
        self.__team = team
        self.__passenger = passenger
        self.__weight = weight

    def __str__(self):
        return f"{self.__model}," \
               f"{self.__team[0]}, " \
               f"{self.__team[1]}," \
               f"{self.__team[2]}," \
               f"{self.__team[3]}, " \
               f"{self.__passenger}, " \
               f"{self.__weight}"