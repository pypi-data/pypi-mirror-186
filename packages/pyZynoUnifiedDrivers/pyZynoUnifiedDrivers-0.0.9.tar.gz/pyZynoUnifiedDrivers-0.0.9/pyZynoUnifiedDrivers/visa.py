'''
Zyno Medical Virtual Instrument Software Architecture (VSIA) python library
Created on May 13, 2022

@author: Yancen Li
'''
import time
import sys
import platform
import serial
from pyZynoUnifiedDrivers.miva.module_miva import Miva
from pyZynoUnifiedDrivers.miva.module_utils import scan_serial_ports

#
_BAUD_RATE = 9600
_BYTE_SIZE = 8
_STOPBITS = 1
_PARITY = serial.PARITY_NONE
_FLOW_CONTROL = 0
_TIMEOUT = 0.025
_WRITE_TIMEOUT = 0.1


class ResourceManager:
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def list_resources(self):
        '''Scan Serial Port'''
        ports = []
        if platform.system() == 'Linux':
            ports = ['/dev/ttyUSB%s' % (i) for i in range(0, 256)]
        else:
            ports = scan_serial_ports()
        result = []
        for port in ports:
            try:
                ser = serial.Serial(port)
                ser.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        result = tuple(result)
        return result

    def open_resource(self, serial_port):
        '''
        Open Resource
        '''
        return Miva(serial_port)

    def get_pump_serial_port(self):
        com_port = ''
        serial_port_list = scan_serial_ports()
        for each_serial_port in serial_port_list:
            miva = Miva(each_serial_port)
            time.sleep(0.5)
            serial_number = miva.get_pump_sn()
            if serial_number != '':
                com_port = each_serial_port
                miva.close()
                break
            else:
                miva.close()
        return com_port


def main(argv):
    '''main function'''
    rm = ResourceManager()
    serial_port = rm.get_pump_serial_port()
    if serial_port != '':
        miva = rm.open_resource(serial_port)
        # Test [query] Function
        pump_sn = miva.query(':SERIAL?')
        print(pump_sn)
        print('len(pump_sn) = {}'.format(len(pump_sn)))
        # Test [*IDN?] query
        pump_identifier = miva.query('*IDN?')
        print(pump_identifier)
        # Test [close] function of miva class
        miva.close()
    # Test [list_resources] Function
    resources = rm.list_resources()
    print(resources)


if __name__ == "__main__":
    main(sys.argv)
