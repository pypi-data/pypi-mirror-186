'''nimbus CAPS pump simulator'''
import sys
# import time
from os import path
from threading import Thread 
# from threading import Lock
from pyZynoUnifiedDrivers.miva.module_infusion import Infusion, InfusionStatus, InfusionMonitor
from pyZynoUnifiedDrivers.miva.module_library import Library
from pyZynoUnifiedDrivers.miva.module_utils import load_json_file, json_to_file
from pyZynoUnifiedDrivers.miva.module_utils import PUMP_CONFIG_FILE_PATH
# from module_sendrx import SendRx

# refresh interval (second)
_REFRESH_TIMER = 0.1


class Pump:
    '''pump class'''

    def __init__(self):
        self.sensor = {'up': 0, \
                       'down':0, \
                       'system':0, \
                       'battery_voltage':0, \
                       'motor_running':0}
        self.status_monitor = None
        self.miva = None
        self.connected = False
        self.com_port = ''
        self.serial_number = ''
        self.firmware_version = ''
        self.library_path = ''
        self.library = Library()
        self.infusion = Infusion()
        self.infusion_monitor = InfusionMonitor()
        self.protocol = None
        self.protocol_name = ''
        self.rx_path = ''
        self.infusion.set_status(InfusionStatus.IDLE)
        # Pump configuration file path
        self.pump_config_path = PUMP_CONFIG_FILE_PATH
        # Pump config data structure
        self.pump_config = {"library_path": "", \
							"protocol_selected": "", \
                            "rx_path": "",
                            }

        if path.exists(self.pump_config_path):
            self.pump_config = load_json_file(self.pump_config_path)
            lib_path = self.pump_config["library_path"]
            protocol_name = self.pump_config["protocol_selected"]
            rx_path = self.pump_config["rx_path"]
            if path.exists(lib_path):
                self.library.load(lib_path)
                protocol = self.library.get_protocol(protocol_name)
                if protocol is not None:
                    self.infusion.set_protocol(protocol)
                    self.protocol = protocol
                    self.protocol_name = protocol_name
                if path.exists(rx_path):
                    self.rx_path = rx_path
    
    def start(self):
        '''start console'''
        library = self.library
        infusion = self.infusion
        protocol = self.protocol
        try:
            print('start infusion monitor...')
            print('==')
            self.run_infusion_monitor()
            cmd = ''
            while cmd not in ['exit']:
                cmd = input('>')
                cmd = cmd.lower().strip(' \t\r\n\0')

                if cmd.lower() in ['help', '?']:
                    print(' LL - Load Library')
                    print(' SP - Select Protocol')
                    print(' RP - Run Protocol')

                if cmd.lower() in ['ll', 'load library']:
                    if library.get_library() is not None:
                        print("currently loaded library: ")
                        # Title
                        print("    {0:5s}    |    {1:15s}    ".format('id', 'name'))
                        print("----{0:5s}----|----{1:15s}----".format('-----', '---------------'))
                        # Content
                        print("    {0:5s}    |    {1:15s}"\
                                .format(str(library.get_id()), library.get_name()))
                        lib_path = input('Enter NEW library path: ')
                    else:
                        lib_path = input('    Enter library path: ')
                    if path.exists(lib_path):
                        library.load(lib_path)
                        print("library: ")
                        # Title
                        print("    {0:5s}    |    {1:15s}    ".format('id', 'name'))
                        print("----{0:5s}----|----{1:15s}----".format('-----', '---------------'))
                        # Content
                        print("    {0:5s}    |    {1:15s}"\
                                .format(str(library.get_id()), library.get_name()))
                        #
                        # print("library id = {}   |   ".format(library.get_id()), end='')
                        # print("library name = {}".format(library.get_name()))
                        #
                        self.pump_config["library_path"] = lib_path
                        json_to_file(self.pump_config, self.pump_config_path)
                    else:
                        if lib_path == '':
                            pass
                        else:
                            print('    Invalid library path: \'{}\''.format(lib_path))

                if cmd.lower() in ['sp', 'select protocol']:
                    if library.get_library() is not None:
                        protocols = library.get_protocols()
                        print("library: ")
                        # Title
                        print("    {0:5s}    |    {1:15s}    ".format('id', 'name'))
                        print("----{0:5s}----|----{1:15s}----".format('-----', '---------------'))
                        # Content
                        print("    {:5s}    |    ".format(str(library.get_id())), end='')
                        print("{:15s}".format(library.get_name()))
                        #
                        print("protocol: ")
                        # Title
                        print("    {0:5s}    |    {1:15s}    |    {2:20s}"\
                                .format('id', 'name', 'mode'))
                        print("----{0:5s}----|----{1:15s}----|----{2:20s}"\
                                .format('-----', '---------------', '--------------------'))
                        # Content
                        for each_protocol in protocols:
                            print("    {:5s}    |    ".format(str(each_protocol['id'])), end='')
                            print("{:15s}    |    ".format(each_protocol['content']['name']), end='')
                            print("{:20s}".format(each_protocol['content']['deliveryMode']))
                        print("Total [{}] protocols extracted".format(len(protocols)))
                        #
                        protocol_name = self.protocol_name
                        protocol = library.get_protocol(protocol_name)
                        if protocol is not None:
                            self.infusion.set_protocol(protocol)
                            self.protocol = protocol
                            print("currently selected protocol: ")
                            # Title
                            print("    {0:5s}    |    {1:15s}    |    {2:20s}"\
                                    .format('id', 'name', 'mode'))
                            print("----{0:5s}----|----{1:15s}----|----{2:20s}"\
                                    .format('-----', '---------------', '--------------------'))
                            # Content
                            print("    {0:5s}    |".format(str(protocol['id'])), end='')
                            print("    {0:15s}    |".format(protocol['content']['name']), end='')
                            print("    {0:20s}".format(protocol['content']['deliveryMode']))
                            #
                            print("Extracted Parameters:")
                            if protocol['content']['deliveryMode'] == 'continuousInfusion':
                                infusion.print_cont_parameters()
                            if protocol['content']['deliveryMode'] == 'bolusInfusion':
                                infusion.print_bolus_parameters()
                            if protocol['content']['deliveryMode'] == 'intermittentInfusion':
                                infusion.print_int_parameters()
                            protocol_name = input('Enter NEW protocol name / id: ')
                        else:
                            protocol_name = input('    Enter protocol name / id: ')
                        #
                        if library.get_protocol(protocol_name) is not None:
                            protocol = library.get_protocol(protocol_name)
                            infusion.set_protocol(protocol)
                            print("protocol: ")
                            # Title
                            print("    {0:5s}    |    {1:15s}    |    {2:20s}"\
                                    .format('id', 'name', 'mode'))
                            print("----{0:5s}----|----{1:15s}----|----{2:20s}"\
                                    .format('-----', '---------------', '--------------------'))
                            # Content
                            print("    {0:5s}    |".format(str(protocol['id'])), end='')
                            print("    {0:15s}    |".format(protocol['content']['name']), end='')
                            print("    {0:20s}".format(protocol['content']['deliveryMode']))
                            #
                            print("Extracted Parameters:")
                            if protocol['content']['deliveryMode'] == 'continuousInfusion':
                                infusion.print_cont_parameters()
                            if protocol['content']['deliveryMode'] == 'bolusInfusion':
                                infusion.print_bolus_parameters()
                            if protocol['content']['deliveryMode'] == 'intermittentInfusion':
                                infusion.print_int_parameters()
                            #
                            self.pump_config["protocol_selected"] = protocol_name
                            json_to_file(self.pump_config, self.pump_config_path)
                        else:
                            # invalid protocol name
                            if protocol_name != '':
                                print('    Invalid Protocol: \'{}\''.format(protocol_name))
                    else:
                        # No library loaded
                        print('empty libarary: use <ll> command to load libarary first')
                if cmd.lower() in ['rp', 'run protocol', 'run']:
                    if library.get_library() is not None:
                        if protocol is not None:
                            protocl_name = protocol['content']['name']
                            infusion.set_protocol(protocol)
                            print("protocol: ")
                            # Title
                            print("    {0:5s}    |    {1:15s}    |    {2:20s}"\
                                    .format('id', 'name', 'mode'))
                            print("----{0:5s}----|----{1:15s}----|----{2:20s}"\
                                    .format('-----', '---------------', '--------------------'))
                            # Content
                            print("    {:5s}    |".format(str(protocol['id'])), end='')
                            print("    {:15s}    |".format(protocol['content']['name']), end='')
                            print("    {:20s}".format(protocol['content']['deliveryMode']))
                            #
                            print("Extracted Parameters:")
                            if protocol['content']['deliveryMode'] == 'continuousInfusion':
                                infusion.print_cont_parameters()
                            if protocol['content']['deliveryMode'] == 'bolusInfusion':
                                infusion.print_bolus_parameters()
                            if protocol['content']['deliveryMode'] == 'intermittentInfusion':
                                infusion.print_int_parameters()
                            start_yes_no = input("run protocol - [{}]? (y/n): "\
                                    .format(protocl_name))
                            if start_yes_no.lower().find('y') != -1 or start_yes_no == '':
                                print('infusion start...')
                                self.run_infusion()
                                # time.sleep(_REFRESH_TIMER * 10)
                                # print('infusion stop...')
                            else:
                                print('infusion aborted...')
                        else:
                            print('Empty Protocol: Use <SP> command to select protocol first.')
                    else:
                        print('Empty Libarary: Use <LL> command to load libarary first.')
                #
                if cmd in ['quit', 'status', 'db', 'bolus', 'cd', 'clinician dose', 'stop', 'run', 'pause']:
                    self.infusion_monitor.set_command(cmd)
            # Reset Infusion
            self.infusion.reset()
            # Stop infusion monitor
            self.infusion_monitor.stop()
        except KeyboardInterrupt:
            print()
            print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))
        except AttributeError:
            print()
            print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))
        except EOFError:
            # press Ctrl + C
            pass
        except OSError:
            print()
            print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))
        # Reset Infusion
        self.infusion.reset()
        # Stop infusion monitor
        self.infusion_monitor.stop()

    def run_infusion(self):
        '''Run Infusion'''
        ##############################
        # create a [infusion] thread #
        ##############################
        infusion_thread = Thread(target=self.infusion.run, args=())
        infusion_thread.start()

    def run_infusion_monitor(self):
        '''Run Infusion Monitor'''
        ######################################
        # create a [infusion monitor] thread #
        ######################################
        infusion_monitor_thread = Thread(target=self.infusion_monitor.start, \
                args=([self.infusion]))
        infusion_monitor_thread.start()


def main():
    '''main function'''
    try:
        print('Pump turn on ...')
        pump = Pump()
        pump.start()
        print('Pump turn off ...')
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
    
