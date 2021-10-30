from smartphone import Smartphone
from sockets import EUSocket, USSocket


class EUAdapter(object):
    """EUAdapter encapsulates client (Smartphone) and supplier (EUSocket)."""
    input_voltage = EUSocket.output_voltage
    output_voltage = Smartphone.max_input_voltage


class USAdapter(object):
    """USAdapter encapsulates client (Smartphone) and supplier (USSocket)."""

    input_voltage = USSocket.output_voltage
    output_voltage = Smartphone.max_input_voltage


if __name__ == '__main__':
    smartphone = Smartphone()

    smartphone.charge(EUAdapter.output_voltage)
    smartphone.charge(USAdapter.output_voltage)
