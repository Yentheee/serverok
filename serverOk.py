import sys
import json


def main():
    if len(sys.argv) == 1:

        print("1. Server toevoegen")
        print("2. Server verwijderen")
        print("3. Servers in lijst bekijken")

        keuze = int(input(""))

        match keuze:
            case 1:
                server = input("Welke server wilt u toevoegn: ")
                print("server toevoegend")
            case 2:
                print("server verwijderd")
            case 3:
                print("lijst bekijken")
            case _:
                print("foute invoer")
    else:
        keuze2 = int(sys.argv[1])
        match keuze2:
            case 1:
                server = input("Welke server wilt u toevoegn: ")
                ServerToevoegen(server)
                print("server toegevoegd")
            case 2:
                print("server verwijderd")
            case 3:
                print("lijst bekijken")
            case _:
                print("foute invoer")


def ServerToevoegen(invoer):
    data = {
        "server": invoer
    }
    with open("ingevoerde_data.json", "w") as data_file:
        json.dump(data, data_file)

    print("Gegevens zijn opgeslagen in 'ingevoerde_data.json'.")


if __name__ == '__main__':
    main()
