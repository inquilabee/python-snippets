# Client
class Smartphone(object):
    max_input_voltage = 5

    @classmethod
    def outcome(cls, input_voltage):
        if input_voltage > cls.max_input_voltage:
            print("Input voltage: {}V -- BURNING!!!".format(input_voltage))
        else:
            print("Input voltage: {}V -- Charging...".format(input_voltage))

    def charge(self, input_voltage):
        """Charge the phone with the given input voltage."""
        self.outcome(input_voltage)
