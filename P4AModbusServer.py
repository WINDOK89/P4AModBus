from pymodbus.server.sync import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext,ModbusServerContext
import logging

if __name__=="__main__":

    logging.basicConfig()
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)

    identify=ModbusDeviceIdentification()
    identify.VendorName='P4A'
    identify.ProductCode='P4AMBS'
    identify.VendorUrl='http://performanceforassets.com'
    identify.ProductName='P4AModbusServer'
    identify.MajorMinorRevision='1.0'

    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [0]*0xff),
        co=ModbusSequentialDataBlock(0, [0]*0xff),
        hr=ModbusSequentialDataBlock(0, [0]*0xff),   #holding register, seems to be 16 bits by default
        ir=ModbusSequentialDataBlock(0, [0]*0xff))
    context = ModbusServerContext(slaves=store, single=True)
    StartTcpServer(context,identity=identify, address=("localhost",5020)) #put lan ip if you want outside computer to access it