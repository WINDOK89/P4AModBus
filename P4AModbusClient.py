from pymodbus.client.sync import ModbusTcpClient as MBC
from P4ADataConverter import int_to_floating_bin
import time


if __name__=="__main__":

    """some stuff to know"""
    #one address is a 16bits register (2 register)
    # if 32 bits double value, the addressing for value 1 is x  and addressing for value 2 is x +2 because we need 32 bits
    # we can handle the data this way
    # per example, we ascii code a word and put each letter in a register, the reading must be programme
    # when reading holding register, the value is a 0 to 65536 integer representing the 16 bits value.

    """connect"""
    client=MBC("10.32.22.73", port=5020)
    client.connect()

    """write and read holding register"""
    for i in range(254):
        client.write_register(i,45)
    answer=client.read_holding_registers(2) #the second parameter is the number of register to be read
    print(answer.registers[0])

    """read input register"""
    # answer=client.read_input_registers(0)
    # print(answer.registers[0])

    """write and read output coil"""
    # client.write_coil(3,True) #3 is the address, True is the first bit value for this address
    # answer=client.read_coils(3, 1) #1 is the numner of bits to read and goes by 8,16,24,32,40,...?
    # print(answer)
    # print(answer.getBit(0))

    """read discrete inputs"""
    # answer=client.read_discrete_inputs(3,1)
    # print(answer)
    # print(answer.getBit(0))

    """readwrite register"""
    #answer=client.readwrite_registers(read_address=3, read_count=1, write_address=1, write_registers=233) #read register 3 and write register 1 with 233, writing is done first
    #print(answer.registers[0])

    """closing connection"""
    client.close()