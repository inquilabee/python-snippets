# Supplier
class Socket(object):
    output_voltage = None


class EUSocket(Socket):
    output_voltage = 230


class USSocket(Socket):
    output_voltage = 120
