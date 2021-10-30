from smartphone import Smartphone
from sockets import EUSocket, USSocket

if __name__ == '__main__':
    smartphone = Smartphone()

    smartphone.charge(USSocket.output_voltage)
    smartphone.charge(EUSocket.output_voltage)
