from airplane import Airplane


class Airport:
    def __init__(self, name: str, personals: list, airplanes: list, terminal: int, plane_way: int):
        self.__name = name
        self.__personals = personals
        self.__airplanes = airplanes
        self.__terminal = terminal
        self.__plane_way = plane_way

    def take_plane(self, plane: Airplane):
        self.__airplanes.append(plane)

    def get_name(self):
        return self.__name

    def get_personal(self):
        for person in self.__personals:
            print(person)

    def get_airplane(self):
        for plane in self.__airplanes:
            print(plane)

    def get_terminal(self):
        return self.__terminal

    def get_plane_way(self):
        return self.__plane_way

    def __str__(self):
        return f"{Airport.get_name(self)}," \
               f"{Airport.get_personal(self)}," \
               f"{Airport.get_airplane(self)}," \
               f"{Airport.get_terminal(self)}," \
               f"{Airport.get_plane_way(self)}"
