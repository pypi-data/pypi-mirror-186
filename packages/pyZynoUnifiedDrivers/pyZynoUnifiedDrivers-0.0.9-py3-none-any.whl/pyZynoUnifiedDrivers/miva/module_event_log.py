'''Event Log Monitor Module'''
# import re
# from os import path
import sys
import time
import json
import serial
#
# from miva.module_miva import Miva
# from module_utils import scan_serial_ports
from pyZynoUnifiedDrivers.miva.module_utils import EVENT_LOG_NUMBER_OF_EVENTS
from pyZynoUnifiedDrivers.miva.module_utils import get_line_number
from pyZynoUnifiedDrivers.miva.module_utils import _OK_KEY, _SHORT_PRESS, _RUN_KEY
from pyZynoUnifiedDrivers.miva.module_infusion import InfusionStatus

# Time Out (seconds)
_TIMEOUT = 1

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


class EventLogMonitor:
    '''Event Log Monitor Class'''

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

    def start(self, miva, infusion=None):
        '''start'''
        #
        self.miva = miva
        self._is_on = True
        self._is_paused = False
        if infusion is not None:
            self.infusion = infusion
        # print('start event log monitor...')
        try:
            event_log_index = miva.read_event_log_indices()
            previous_head = int(event_log_index['head'], 16)
        except serial.serialutil.SerialException:
            # Stop event log monitor
            self.stop()
            print('Error: pump failed to respond')
            print('Stop event log monitor...')
            return
        while self._is_on:
            try:
                if self._is_paused:
                    time.sleep(_TIMEOUT)
                    continue
                event_log_index = miva.read_event_log_indices()
                head = int(event_log_index['head'], 16)
                total_length = head - previous_head if head >= previous_head else \
                                head + EVENT_LOG_NUMBER_OF_EVENTS - previous_head
                if total_length > 0:
                    event_logs = miva.read_range_event_log(previous_head, head)
                    print('--')
                    print('total_length = [{}]'.format(total_length))
                    print('--')
                    event_logs_json = json.dumps(event_logs, indent=4)
                    print(event_logs_json)
                    print('Total Event Log Printed: [{}]'.format(len(event_logs)))
                    print('--')
                    previous_head = head
                    # check event logs for certain events
                    for each_event_log in event_logs:
                        if each_event_log.get('event_type') is not None:
                            if each_event_log['event_type'] == 'UNATTENDED_ALARM':
                                # Send [OK] key command
                                result = miva.press_key(_OK_KEY, _SHORT_PRESS)
                                if result:
                                    print('key: Ok/Enter (short)')
                            if each_event_log['event_type'] == 'RUN_INFUSION':
                                self.timestamp_infusion_start = time.time()
                                print("Infusion start at [{}]".format(time.strftime('%H:%M:%S', \
                                        time.localtime())))
                                self.local_time_infusion_start = time.localtime()
                                # Run infusion
                                if infusion is not None and infusion.protocol is not None:
                                    if infusion.status == InfusionStatus.STOPPED:
                                        infusion.run_infusion()
                                    elif infusion.status == InfusionStatus.PAUSED:
                                        infusion.pause()
                                    elif infusion.status == InfusionStatus.PAUSED_AUTO_BOLUS:
                                        infusion.pause()
                                    elif infusion.status == InfusionStatus.PAUSED_DEMAND_BOLUS:
                                        infusion.pause()
                                    elif infusion.status == InfusionStatus.PAUSED_LOADING_DOSE:
                                        infusion.pause()
                                    elif infusion.status == InfusionStatus.PAUSED_CLINICIAN_DOSE:
                                        infusion.pause()
                            if each_event_log['event_type'] == 'INFUSION_PAUSED':
                                timestamp_infusion_pause = time.time()
                                local_time_start = self.local_time_infusion_start
                                print("Infusion start at [{}]"\
                                        .format(time.strftime('%H:%M:%S', local_time_start)))
                                print("Infusion pause at [{}]"\
                                        .format(time.strftime('%H:%M:%S', time.localtime())))
                                timestamp_duration = timestamp_infusion_pause \
                                        -self.timestamp_infusion_start
                                duration = time.strftime('%H:%M:%S', \
                                        time.gmtime(timestamp_duration))
                                print('Infusion duration: [{}]'.format(duration))
                                # Pause infusion
                                if infusion is not None:
                                    print()
                                    print('line {0}: infusion.pause() [{1}]'\
                                            .format(get_line_number(), \
                                            time.strftime('%H:%M:%S', time.localtime())))
                                    infusion.pause()
                            if each_event_log['event_type'] == 'INFUSION_COMPLETED':
                                if infusion is not None:
                                    infusion.reset()
                                timestamp_infusion_complete = time.time()
                                local_time_start = self.local_time_infusion_start
                                print("line {0}: Infusion start at [{1}]"\
                                      .format(get_line_number(), \
                                              time.strftime('%H:%M:%S', local_time_start)))
                                print("line {0}: Infusion complete at [{1}]"\
                                      .format(get_line_number(), \
                                              time.strftime('%H:%M:%S', time.localtime())))
                                timestamp_duration = timestamp_infusion_complete \
                                        -self.timestamp_infusion_start
                                duration = time.strftime('%H:%M:%S', \
                                                         time.gmtime(timestamp_duration))
                                print('line {0}: Infusion duration: [{1}]'\
                                      .format(get_line_number(), duration))
                                #
                                # Send [RUN] key [SHORT] command to confirm infusion complete
                                result = miva.press_key(_RUN_KEY, _SHORT_PRESS)
                                if result:
                                    print('key: Run/Stop (short)')
                            if each_event_log['event_type'] == 'DELAY_END' and \
                                    each_event_log['sub_type'] == 'NORMAL_END':
                                if infusion is not None:
                                    infusion.trigger_delay_end()
                            if each_event_log['event_type'] == 'INFUSION_LIMIT_REACHED' and \
                                    each_event_log['sub_type'] == 'MAX_PER_HOUR':
                                if infusion is not None:
                                    infusion.trigger_mph()
                            if each_event_log['event_type'] == 'INFUSION_LIMIT_REACHED' and \
                                    each_event_log['sub_type'] == 'MAX_PER_INTERVAL':
                                if infusion is not None:
                                    infusion.trigger_mpi()
                            if each_event_log['event_type'] == 'INFUSION_LIMIT_REACHED' and \
                                    each_event_log['sub_type'] == 'CLEARED':
                                if infusion is not None:
                                    infusion.trigger_mpi_mph_clear()
                            if each_event_log['event_type'] == 'BOLUS_GRANTED' and \
                                    each_event_log['sub_type'] == 'AUTO_BOLUS':
                                if infusion is not None:
                                    infusion.trigger_ab()
                            if each_event_log['event_type'] == 'BOLUS_GRANTED' and \
                                    each_event_log['sub_type'] == 'EXTRA_DOSE':
                                if infusion is not None: 
                                    infusion.trigger_db()
                            if each_event_log['event_type'] == 'BOLUS_GRANTED' and \
                                    each_event_log['sub_type'] == 'CLINICIAN_DOSE':
                                if infusion is not None:
                                    infusion.trigger_cd()
                time.sleep(_TIMEOUT)
            except (serial.serialutil.SerialException, ValueError):
                # Stop event log monitor
                self.stop()
                print('Error: pump failed to respond')
                print('Stop event log monitor...')
                break
            except (OSError, TypeError, NameError):
                print()
                print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))
                self.pause()
                raise

        print('Event log monitor stopped at [{}]'\
                .format(time.strftime('%H:%M:%S', time.localtime())))
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
            
# def main(argv):
#     '''main function'''
#     try:
#         current_file = path.basename(__file__)
#         if len(argv) == 1:
#             # Print the name of current script in Python
#             print('Empty argument list. ', end='')
#             print('To start, type <{}> followed by the com port. '.format(current_file), end='')
#             print('Ex: \'{} COM1\''.format(current_file))
#             serial_port_list = scan_serial_ports()
#             print('\tAvailable Serial Ports:')
#             print('\t\t\t\t', end='')
#             for each_serial_port in serial_port_list:
#                 print('{} '.format(each_serial_port), end='')
#         else:
#             serial_port = argv[1].upper()
#             if re.match(r'com\d+', serial_port.lower().rstrip(' \t\r\n\0')):
#                 miva = Miva(serial_port)
#                 event_log_monitor = EventLogMonitor()
#                 event_log_monitor.start(miva)
#             else:
#                 print('Error: invalid port \'{}\' '.format(serial_port), end='')
#                 print('To start, type \'{}\' followed by the com port. '\
#                         .format(current_file), end='')
#                 print('Ex: \'{} COM1\''.format(current_file))
#     except KeyboardInterrupt:
#         pass
#     except serial.serialutil.SerialException:
#         print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))

#
# if __name__ == "__main__":
#     main(sys.argv)
