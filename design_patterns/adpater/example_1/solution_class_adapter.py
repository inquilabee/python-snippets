from smartphone import Smartphone
from sockets import Socket, EUSocket, USSocket


class CannotTransformVoltage(Exception):
    """Exception raised by the SmartphoneAdapter.

    This exception represents the fact that an adapter can not provide the
    right voltage to the Smartphone if the voltage of the Socket is wrong."""
    pass


class SmartphoneAdapter(Smartphone, Socket):

    @classmethod
    def transform_voltage(cls, input_voltage):
        if input_voltage == cls.output_voltage:
            return cls.max_input_voltage
        else:
            raise CannotTransformVoltage(
                f"Can't transform {input_voltage}-{cls.max_input_voltage}V. "
                f"This adapter transforms {cls.output_voltage}-{cls.max_input_voltage}V."
            )

    @classmethod
    def charge(cls, input_voltage):
        try:
            voltage = cls.transform_voltage(input_voltage)
            cls.outcome(voltage)
        except CannotTransformVoltage as e:
            print(e)


class SmartphoneEUAdapter(SmartphoneAdapter, EUSocket):
    """System (smartphone + adapter) for a European Socket.

    Note: SmartphoneAdapter already inherited from Smartphone and Socket,
    but by re-inheriting from EUSocket we redefine all the stuff inherited from Socket.
    """
    pass


class SmartphoneUSAdapter(SmartphoneAdapter, USSocket):
    """System (smartphone + adapter) for an American Socket."""
    pass


if __name__ == '__main__':
    smartphone = SmartphoneEUAdapter()

    smartphone.charge(EUSocket.output_voltage)
    smartphone.charge(USSocket.output_voltage)

    smartphone = SmartphoneUSAdapter()

    smartphone.charge(EUSocket.output_voltage)
    smartphone.charge(USSocket.output_voltage)
