import sys
import json
import platform
import subprocess


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
                print("server verwijderd")
            case 3:
                print("lijst bekijken")
            case _:
                print("foute invoer")


def ServerToevoegen(naam, serverok):
    data = {
        "naam": naam
    }
    with open("ingevoerde_data.json", "a") as data_file:
        representation = json.dumps(data)
        data_file.write(representation + "\n")

    dataserver = {
        "naam": naam,
        "serverok": serverok
    }
    with open("serverok.json", "a") as data_file:
        representation2 = json.dumps(dataserver)
        data_file.write(representation2 + ",\n")
    print("Gegevens zijn opgeslagen in 'severok.json'.")


def myping(host):
    parameter = "-n" if platform.system().lower() == "windows" else "-c"

    command = ["ping", parameter, "1", host]
    response = subprocess.call(command)

    if response == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
