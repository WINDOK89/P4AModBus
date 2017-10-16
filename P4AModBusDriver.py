from pymodbus.client.sync import ModbusTcpClient as MBC
from P4ADataConverter import int_to_floating_bin
import time

class P4AModBusDriver():

    def __init__(self, server, port=502, Startup=True):
        self.client=MBC(server,port)
        if Startup:
            self.client.connect()

    def close(self):
        self.client.close()

    def get_ieee754_float(self, address):
        return int_to_floating_bin(self.client.read_input_registers(address).registers[0])

    def get_integer(self, address):
        return self.client.read_input_registers(address).registers[0]

    def write_output(self, address, value):
        self.client.write_register(address,value)



if __name__=="__main__":

    a=P4AModBusDriver("169.254.1.1")
    print(a.get_ieee754_float(23))
    print(a.get_ieee754_float(17))
    print(a.get_ieee754_float(73))

    print(a.get_integer(400))
    print(a.get_integer(401))
    print(a.get_integer(402))
    a.write_output(600,0)
    a.close()

    # client=MBC("169.254.1.1", port=502)
    #
    # client.connect()
    # answer=client.read_input_registers(73)
    # print(int_to_floating_bin(answer.registers[0],NBit=16))
    #
    # answer = client.read_input_registers(400)
    # print(answer.registers[0])
    #
    # answer = client.read_input_registers(599)
    # print(answer.registers[0])
    #
    # print(client.write_register(600,65000))
    # #print(client.write_register(599,0))
    # time.sleep(2)
    #
    # client.close()