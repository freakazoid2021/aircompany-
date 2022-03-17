# practices
from aviacompany import Aviacompany
from airport import Airport
from airplane import Airplane
from person import Person

if __name__ == '__main__':
    # team
    pilot1 = Person("First Pilot")
    pilot2 = Person("Second Pilot")
    shturman = Person("Shturman")
    stuardes = Person("Stuardes")

    team = [pilot1, pilot2, shturman, stuardes]

    # plane
    an_2 = Airplane("An-2", team, 10, 250.5)
    an_24 = Airplane("An-24", team, 50, 550.5)
    tu_134 = Airplane("TU-134", team, 120, 1050.5)

    planes = [an_2, an_24, tu_134]

    # airports
    director = Person("Director")
    registration = Person("Registration")

    grodno = Airport("Grodno", [director, registration], [an_2], 3, 2)

    minsk = Airport("Minsk", [director, registration], [an_24], 4, 3)

    # aviacompany
    salesman = Person("Salesman")
    cleaner = Person("Cleaner")
    belavia = Aviacompany([salesman, director, cleaner, *team], planes, [grodno, minsk])

    belavia.show_company()

    belavia.get_plane()
    plane = int(input("which plane: "))

    where = input("where: ")

    belavia.send_plane(plane - 1, minsk if where == "Minsk" else grodno)

    belavia.get_plane()
    print(grodno)
    print(minsk)
