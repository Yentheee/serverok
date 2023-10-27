print("1. Server toevoegen")
print("2. Server verwijderen")
print("3. Servers in lijst bekijken")

keuze = int(input(""))

match keuze:
    case 1:
        server = input("Welke server wilt u toevoegn: ")
        ServerToevoegen(server)
        print("server toevoegend")
    case 2:
        print("server verwijderd")
    case 3:
        print("lijst bekijken")
    case _:
        print("foute invoer")

def ServerToevoegen(invoer):


