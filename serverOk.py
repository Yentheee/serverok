import sys
import json
from ping3 import ping


def main():
    if len(sys.argv) == 1:

        print("1. Server toevoegen")
        print("2. Server verwijderen")
        print("3. Servers in lijst bekijken")

        keuze = int(input(""))

        match keuze:
            case 1:
                servernaam = input("Welke server wilt u toevoegn (naam): ")
                ServerToevoegen(servernaam)
                print("server toegevoegd")
            case 2:
                server = input("welke server wilt u verwijderen: ")
                ServerVerwijderen(server)
                print("server verwijderd")
            case 3:
                print("lijst bekijken")
            case _:
                print("foute invoer")
    else:
        keuze2 = int(sys.argv[1])
        match keuze2:
            case 1:
                servernaam = input("Welke server wilt u toevoegn (naam): ")
                serverok = myping(servernaam)
                ServerToevoegen(servernaam, serverok)
                print("server toegevoegd")
            case 2:
                server = input("welke server wilt u verwijderen: ")
                ServerVerwijderen(server)
                print("server verwijderd")
            case 3:
                print("lijst bekijken")
            case _:
                print("foute invoer")


def ServerToevoegen(naam, serverok):
    with open("ingevoerde_data.json", "r") as bestand:
        data = json.load(bestand)

    with open("serverok.json", "r") as bestand:
        serverdata = json.load(bestand)

    data["server"].append(naam)

    serverdata["server"].append(naam)
    serverdata["serverok"].append(serverok)

    with open("ingevoerde_data.json", "w") as data_file:
        representation = json.dumps(data)
        data_file.write(representation)

    with open("serverok.json", "w") as data_file:
        representation2 = json.dumps(serverdata)
        data_file.write(representation2)


def ServerVerwijderen(server):
    with open("ingevoerde_data.json", "r") as bestand:
        data = json.load(bestand)

    if "server" in data:
        if server in data["server"]:
            data["server"].remove(server)

    with open("ingevoerde_data.json", "w") as data_file:
        representation = json.dumps(data)
        data_file.write(representation)

    with open("serverok.json", "r") as bestand:
        server_data = json.load(bestand)

    if "server" in server_data:
        if server in server_data["server"]:
            positie = server_data["server"].index(server)
            server_data["server"].remove(server)
            if positie < len(server_data["serverok"]):
                del server_data["serverok"][positie]

    with open("serverok.json", "w") as data_file:
        representation = json.dumps(server_data)
        data_file.write(representation)


def lijst_weergeven():
    

def myping(host):
    resp = ping(host)

    if resp == False:
        return False
    else:
        return True


if __name__ == '__main__':
    data_list = []
    serverok_list = []
    main()
