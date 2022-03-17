from airport import Airport
from airplane import Airplane
from person import Person


class Aviacompany:
    def __init__(self, personals: list, airplanes: list, airports: list):
        self.__personals = personals
        self.__airplanes = airplanes
        self.__airports = airports

    def add_plane(self, plane: Airplane) -> None:
        self.__airplanes.append(plane)

    def add_personal(self, personal: Person) -> None:
        self.__personals.append(personal)

    def add_airport(self, airport: Airport) -> None:
        self.__airports.append(airport)

    def send_plane(self, plane, to_port: Airport):

        airplane = self.__airplanes.pop(plane)

        to_port.take_plane(airplane)

    def show_company(self):
        for i in self.__personals:
            print(i)

        for i in self.__airplanes:
            print(i)
            if i is list:
                for j in i:
                    print(j)

        for i in self.__airports:
            print(i)

    def get_plane(self):
        for i, plane in enumerate(self.__airplanes):
            print(i + 1, plane)

    def __str__(self):
        return f"{self.__personals}, {self.__airplanes}, {self.__airports}"
