'''Status Monitor Module'''
import sys
import re
import time
from os import path
import serial
import traceback
from pyZynoUnifiedDrivers.miva.module_miva import Miva
from pyZynoUnifiedDrivers.miva.module_utils import scan_serial_ports
# Time Out (seconds)
_TIMEOUT = 0.05

# Bolus infusion rate (mL/hr)
_BOLUS_RATE = 250

# class PumpEvent(Enum):
    # '''Pump Event'''
    # NONE = 0
    # RUN_INFUSION = 1
    # INFUSION_PAUSED = 2
    # INFUSION_COMPLETED = 3
    # INFUSION_LIMIT_REACHED = 4
    # AUTHENTICATION = 5
    # BOLUS_GRANTED = 6
    # BOLUS_DENIED = 7
    # DOSE_CANCEL = 8
    # OCCLUSION = 9
    # DELAYED_END = 10
    # PUMP_LIMIT_REACHED_ALARM = 11
    # CLEAR_SHIFT_TOTAL = 12
    # BATTERY = 13
    # OPEN_CASSETTE = 14
    # TIMESTAMP = 15
    # POWER_ON = 16
    # POWER_OFF = 17
    # FIRMWARE_ERROR = 18
    # SYSTEM_ERROR = 19
    # BATTERY_FAILURE = 20
    # DEBUG = 21
    # UNATTENDED = 22


class StatusMonitor:
    '''Status Monitor Class'''

    def __init__(self):
        '''__init__'''
        self._is_on = False
        self._is_paused = True
        self.event_log_index_head = '0000'
        self.timestamp_infusion_start = time.time()
        self.local_time_infusion_start = time.localtime()
        #
        self.miva = None
        #
        self.infusion = None

    def start(self, pump):
        '''start'''
        #
        print('Status monitor started at [{}]'\
              .format(time.strftime('%H:%M:%S', time.localtime())))
        print('==')
        #
        self.miva = pump.miva
        miva = self.miva
        self._is_on = True
        self._is_paused = False
        while self._is_on:
            try:
                if self._is_paused:
                    time.sleep(_TIMEOUT)
                    continue
                #
#                 occlusion_sensor = miva.get_occlusion_sensor()
                pump.sensor = miva.get_all_sensor()
#                 pump.sensor['up'] = occlusion_sensor['up']
#                 pump.sensor['down'] = occlusion_sensor['down']
                if pump.sensor == {}:
                    # Stop status monitor
                    self.stop()
                    print('pump.sensor == {}')
                    print('Error: pump failed to respond')
                    print('Stop status monitor...')
                    break
                time.sleep(_TIMEOUT)
            except (serial.serialutil.SerialException, ValueError):
                # Stop status monitor
                self.stop()
                print('Error: pump failed to respond')
                print('Stop status monitor...')
                break
            except (OSError, TypeError, NameError):
                print()
                print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))
                self.pause()
                raise
            except:
                # Stop status monitor
                self.stop()
                print('Error: pump failed to respond')
                print('Stop status monitor...')
                print()
                print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))
                traceback.print_exc()
                break

        print('Status monitor stopped at [{}]'\
              .format(time.strftime('%H:%M:%S', time.localtime())))
        print('==')
        # Stop event log monitor
        self.stop()

    def stop(self):
        '''stop'''
        # print('\nStop event log monitor...')
        self._is_paused = True
        self._is_on = False

    def is_on(self):
        '''is on'''
        return self._is_on

    def is_paused(self):
        ''''is paused'''
        is_paused = True
        if self._is_on:
            is_paused = self._is_paused
        else:
            print('Abort: Event log monitor is [OFF]')
            is_paused = None
        return is_paused

    def pause(self):
        ''''pause'''
        if self._is_on:
            self._is_paused = True
        else:
            print('Pause ELM Aborted: Event log monitor is [OFF]')

    def resume(self):
        ''''resume'''
        if self._is_on:
            self._is_paused = False
        else:
            print('Resume ELM Aborted:: Event log monitor is [OFF]')

            
def main(argv):
    '''main function'''
    try:
        current_file = path.basename(__file__)
        if len(argv) == 1:
            # Print the name of current script in Python
            print('Empty argument list. ', end='')
            print('To start, type <{}> followed by the com port. '.format(current_file), end='')
            print('Ex: \'{} COM1\''.format(current_file))
            serial_port_list = scan_serial_ports()
            print('\tAvailable Serial Ports:')
            print('\t\t\t\t', end='')
            for each_serial_port in serial_port_list:
                print('{} '.format(each_serial_port), end='')
        else:
            serial_port = argv[1].upper()
            if re.match(r'com\d+', serial_port.lower().rstrip(' \t\r\n\0')):
                miva = Miva(serial_port)
                status_monitor = StatusMonitor()
                status_monitor.start(miva)
            else:
                print('Error: invalid port \'{}\' '.format(serial_port), end='')
                print('To start, type \'{}\' followed by the com port. '\
                        .format(current_file), end='')
                print('Ex: \'{} COM1\''.format(current_file))
    except KeyboardInterrupt:
        pass
    except serial.serialutil.SerialException:
        print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))
        traceback.print_exc()


if __name__ == "__main__":
    main(sys.argv)
