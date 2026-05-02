class Servermy: #class for server side operations
    def __init__(self, domainnumber=4, typenumber=1, protocolnum=1, ipnumber="10.0.0.1"):
        self.domainnumber = domainnumber
        self.typenumber = typenumber
        self.protocolnum = protocolnum
        self.ipnumber = ipnumber
        self.available_ports = [5000, 9000]

    def pt_calculator(self, portnumber): #function for calculating round trip time
        x = (portnumber / 1000)
        RoundTripTime = (10000 / ((x ** 2) + (3 * x)))
        return RoundTripTime

    def ServerCont(self, domainnumber, typenumber, protocolnum):
        print("Server: Server take the request.")

        if domainnumber != 4:
            print("Server: Domain number is not true")
            return 0
        elif typenumber != 1:
            print("Server: Type number is not true")
            return 0
        elif protocolnum != 1:
            print("Server: Protocol number is not true")
            return 0
        else:
            print("Server: Server is listening")
            return 1

    def ServerPinger(self, domainnumber, typenumber, protocolnum, ipnumber, portnumber):
        r_value = self.ServerCont(domainnumber, typenumber, protocolnum)

        if r_value == 0:
            return

        print("Server: The IP address is being checked.")

        if ipnumber != self.ipnumber:
            print("Server: Access denied.")
            return

        if portnumber == 3306:
            print("Server: Port 3306 is occupied by MySQL server.")
            print("Server: Access denied.")
            return

        if portnumber not in self.available_ports:
            print("Server: Access denied.")
            return

        RoundTripTime = self.pt_calculator(portnumber)

        if RoundTripTime < 100:
            print("Server: Round Trip Time is=" + str(RoundTripTime) + " The value is acceptable.")
        else:
            print("Server: Round Trip Time is=" + str(RoundTripTime) + " The value is too high.")


class ErrorBackCs(Exception): #custom exception class for client side errors
    pass


class Clientmy: #class for client side operations
    def __init__(self, Clientip="10.0.0.6"):
        self.clientip = Clientip

    def Clientcreat(self, domainnumber, typenumber, protocolnum, Clientip):

        if domainnumber != 4:
            print("Client: Domain number is not true")
            return 0
        elif typenumber != 1:
            print("Client: Type number is not true")
            return 0
        elif protocolnum != 1:
            print("Client: Protocol number is not true")
            return 0
        elif Clientip != "10.0.0.6":
            print("Client: The device is busy")
            return 0
        else:
            print("Client: Client is created")
            print("Client: Client is ready to connection")
            return 1

    def Pingrequest(self):

        try:
            clientport = int(input("Client: Enter Client port number:\n"))

            if clientport != 9000:
                raise ErrorBackCs("Client: Error is occurred.")

            Serverip = input("Client: Enter Server IP: ")
            Destinationport = int(input("Client: Enter Destination Port Number: "))

            return Serverip, Destinationport

        except ErrorBackCs as e:
            print(e)
            return 0


def main():
    server = Servermy()
    client = Clientmy()

    domainnumber = int(input("Enter domain number:\n"))
    typenumber = int(input("Enter type number:\n"))
    protocolnum = int(input("Enter protocol number:\n"))
    Clientip = input("Enter Client IP number:\n")

    status_of_client = client.Clientcreat(domainnumber, typenumber, protocolnum, Clientip)

    if status_of_client == 0:
        print("Program closed.")
        return

    values_of_ping = client.Pingrequest()

    if values_of_ping == 0:
        print("Program closed.")
        return

    Serverip, Destinationport = values_of_ping

    server.ServerPinger(
        domainnumber,
        typenumber,
        protocolnum,
        Serverip,
        Destinationport
    )

    print("Program closed.")


main()