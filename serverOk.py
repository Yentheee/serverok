import sys
import json
from ping3 import ping
from jinja2 import Template

def serverData():
    with open("serverok.json", "r") as data_file:
        data = json.load(data_file)
    return data


def ingevoerdeData():
    with open("ingevoerde_data.json", "r") as data_file:
        data = json.load(data_file)
    return data

def generate_html_page(server_status):
    # Lees het HTML-templatebestand
    with open('template.html', 'r') as template_file:
        template = Template(template_file.read())
    
    # Vervang de placeholder in het template door de serverstatusgegevens
    rendered_html = template.render(server_status=server_status)
    
    # Sla de gegenereerde HTML op in een bestand
    with open('server_status.html', 'w') as html_file:
        html_file.write(rendered_html)

def ServerToevoegen(naam, serverok):
    data = ingevoerdeData()

    serverdata = serverData()

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
    data = ingevoerdeData()

    if "server" in data:
        if server in data["server"]:
            data["server"].remove(server)

    with open("ingevoerde_data.json", "w") as data_file:
        representation = json.dumps(data)
        data_file.write(representation)

    server_data = serverData()

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
    server_data = serverData()

    if "server" in server_data and "serverok" in server_data:
        servers = server_data["server"]
        serverok = server_data["serverok"]

        for server, ok in zip(servers, serverok):
            print(f"Server: {server}, OK: {ok}")
    else:
        print("Geen gegevens beschikbaar in het bestand.")


def myping(host):
    resp = ping(host)

    if resp == False:
        return False
    else:
        return True



def main():
    if len(sys.argv) == 1:

        print("1. Server toevoegen")
        print("2. Server verwijderen")
        print("3. Servers in lijst bekijken")

        keuze = int(input(""))

        match keuze:
            case 1:
                servernaam = input("Welke server wilt u toevoegn (naam): ")
                serverok = myping(servernaam)
                ServerToevoegen(servernaam, serverok)
                print("server toegevoegd")
                server_status = serverData()
                generate_html_page(server_status)
                print("Serverstatuspagina gegenereerd")
            case 2:
                server = input("welke server wilt u verwijderen: ")
                ServerVerwijderen(server)
                print("server verwijderd")
                server_status = serverData()
                generate_html_page(server_status)
                print("Serverstatuspagina gegenereerd")
            case 3:
                lijst_weergeven()
                print("lijst bekijken")
                server_status = serverData()
                generate_html_page(server_status)
                print("Serverstatuspagina gegenereerd")
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

if __name__ == '__main__':
    data = serverData()
    main()

