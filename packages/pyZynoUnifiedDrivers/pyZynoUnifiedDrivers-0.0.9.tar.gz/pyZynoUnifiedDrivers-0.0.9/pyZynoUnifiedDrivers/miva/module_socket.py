'''Socket Module'''
import re
import json
import sys
import time
import datetime
# from threading import Thread
from os import path  # , system
import socket
import copy
from socketserver import BaseRequestHandler, TCPServer
from pyZynoUnifiedDrivers.miva.module_library import get_parameter_list, get_parameter
from pyZynoUnifiedDrivers.miva.module_infusion import InfusionStatus
from pyZynoUnifiedDrivers.miva.module_utils import json_to_file
from pyZynoUnifiedDrivers.miva.module_utils import _UP_KEY, _DOWN_KEY, _INFO_KEY, _OK_KEY, _POWER_KEY
from pyZynoUnifiedDrivers.miva.module_utils import _RUN_KEY, _BOLUS_KEY, _SHORT_PRESS, _LONG_PRESS, _MID_PRESS

_TIMEOUT = 0.025

SOCKET_BUFFER_SIZE = 4096


class SocketRequestHandler(BaseRequestHandler):
    """
    The request handler class for our server.
 
    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
 
    def handle(self):
        try:
            while (self.server.is_on()):
                # self.request is the TCP socket connected to the client
                self.data = self.request.recv(SOCKET_BUFFER_SIZE)
                if self.data == b'':
                    # break if client closes the socket
                    break            
                elif self.data == b'\r\n':
                    # ignore [\r\n]
                    continue
                else:
                    print('{} wrote: '.format(self.client_address[0]))
                    print(self.data)
                    # just send back the same data, but upper-cased
                    # self.request.sendall(self.data + b'\r\n')
                    # self.request.sendall(b'server status: ' + str(self.server.is_on()).encode() + b'\r\n')
                    if self.server.is_on():
                        cmd = self.data.decode()
                        cmd = cmd.strip(' \t\r\n\0')
                        msg = process_command(self.server, cmd)
                    else:
                        msg = 'server status: Off'
                    self.request.sendall(msg.encode() + b'\r\n')
        except (ConnectionResetError, OSError):
            print()
            print('{0}: {1}\n'.format(sys.exc_info()[0], sys.exc_info()[1]))
        finally: 
            self.request.close()


class SocketServer(TCPServer): 

    def __init__(self, server_address, RequestHandlerClass, miva=None, library=None, infusion=None, infusion_monitor=None, event_log_monitor=None):
        '''__init__'''
        TCPServer.__init__(self, server_address, RequestHandlerClass)
        self._is_on = False
        self.tcp_server = None
        self.HOST, self.PORT = server_address
        self.miva = miva
        self.library = library
        self.infusion = infusion
        self.infusion_monitor = infusion_monitor
        self.event_log_monitor = event_log_monitor

    def start(self):
        '''start'''
        try:
            # print("Socket server started at [{}]"\
            # .format(time.strftime('%H:%M:%S', time.localtime())))
            self.set_on()
            self.serve_forever()
            print("Socket server stopped at [{}]"\
                    .format(time.strftime('%H:%M:%S', time.localtime())))
        except KeyboardInterrupt:
            print('Exiting: [Ctrl + C] is pressed')
            pass        
        except OSError:
            print('Exiting: [OSError] is captured')
            pass
        finally:
            self.stop()
        
    def stop(self):
        '''stop'''
        self.shutdown()
        self._is_on = False
        # print("Socket server stopped at [{}]"\
        # .format(time.strftime('%H:%M:%S', time.localtime())))
    
    def set_on(self):
        '''stop'''
        self._is_on = True        

    def is_on(self):
        '''is on'''
        return self._is_on
    
    def status(self):
        if self._is_on:
            print("Socket Server: [On]")
            print("\t{0:5}: {1}".format('IP', self.HOST))
            print("\t{0:5}: {1}".format('Port', str(self.PORT)))
        else:
            print("Socket Server: [Off]")


def process_command(socket_server, cmd):
    return_msg = ''
    miva = socket_server.miva
    library = socket_server.library
    infusion = socket_server.infusion
    protocol = infusion.protocol
    infusion_monitor = socket_server.infusion_monitor
    event_log_monitor = socket_server.event_log_monitor
    if miva is None:
        return return_msg
    #
    # Pause [Event Log Monitor]
    if event_log_monitor.is_on():
        if not event_log_monitor.is_paused():
            event_log_monitor.pause()
    #
    # Disable [Event Log Monitor] Output
    infusion_monitor.disable_output()
    #
    cmd_original = cmd.strip(' \t\r\n\0')
    cmd = cmd.lower().strip(' \t\r\n\0')
    if re.match(r'\*idn\?', cmd):
        # Identifies Instrument Type and Software Version.
        # *IDN?
        make = 'Zyno Medical'
        platform = miva.read_platform()
        model = 'Nimbus' + ' ' + platform
        serial_number = miva.get_pump_sn()
        software_version = miva.get_firmware_version()
        if serial_number != '':
            return_msg = make + ',' + model + ',' + serial_number + ',' + software_version
            print(return_msg)
        else:
            print('Error: get serial number failed')
    # ==============================================
    elif re.match(r'(:)(even(t)?)(:)(\d+)(\?)', cmd):
        # Read Last [N] Event Log
        # :EVENt:<N>?
        # [r'] means this string is a regular expression
        # (:even(t)?)   : must contain [event:] or [even:] ([t] is optional)
        # (:)          : must contain [:]
        # (\d+)        : must contain 1 or more digit
        # (\?)         : must contain a question mark [?]
        re_match_result = re.match(r'(:)(even(t)?)(:)(\d+)(\?)', cmd)
        # the number of event log to print
        num_to_print = int(re_match_result[5])
        #
        event_logs = miva.read_multiple_event_log(num_to_print)
        event_logs_json = json.dumps(event_logs)
        print(json.dumps(event_logs, indent=4))
        print('     Event logs read: [{}]'.format(len(event_logs)))
        #
        return_msg = event_logs_json
    elif re.match(r'(:)(even(t)?)(:)(ind(ex)?)((:)(head|tail))?(\?)', cmd):
        # Read Event Log Indices
        # :EVENt:INDex[:{HEAD | TAIL }]?
        # (head|tail) : matches either [head] or [tail]
        event_log_index = miva.read_event_log_indices()
        event_log_index_tail = event_log_index['tail']
        event_log_index_head = event_log_index['head']
        if event_log_index_tail != '' and event_log_index_head != '':
            print('Event log tail = {}'.format(event_log_index_tail))
            print('Event log head = {}'.format(event_log_index_head))
        else:
            print('Error: get event log index failed')
        #
        re_match_result = re.match(r'(:)(even(t)?)(:)(ind(ex)?)((:)(head|tail))?(\?)', cmd)
        if re_match_result[9] is not None:
            return_msg = event_log_index[re_match_result[9]]
        else:
            return_msg = json.dumps(event_log_index)
    elif re.match(r'(:)(ser(ial)?)(\?)', cmd):
        # Read Pump Serial Number
        # :SERial?
        serial_number = miva.get_pump_sn()
        if serial_number != '':
            print('S/N: {}'.format(serial_number))
            return_msg = serial_number
        else:
            print('Error: get serial number failed')
    elif re.match(r'(:)(ser(ial)?)(\s)([a-z0-9]{8,8})', cmd):
        # Write Pump Serial Number
        # :SERial <serial_number>
        print('Enter NEW S/N: ', end='')
        re_match_result = re.match(r'(:)(ser(ial)?)(\s)([a-z0-9]{8,8})', cmd)
        serial_number = re_match_result[5].lower()
        if len(serial_number) == 8 and re.findall(r"[a-z0-9]{8,8}", serial_number) != []:
            status = miva.set_pump_sn(serial_number.upper())
            if status:
                # print('New S/N: {}'.format(serial_number))
                print("Write pump serial number  -  Done!")
            else:
                print('Error: set serial number failed')
        else:
            print('Error: invalid serial number \'{}\' '.format(serial_number), end='')
            print('Enter \'SN\' followed by 6-digit pump serial number ', end='')
            print('(ex: \'SN800009\')')
    elif re.match(r'(:)(mot(or)?)(:)(cal(ibrate)?)(:)(fact(or)?)(\?)', cmd):
        # Read [Motor Calibration Factor]
        # :CALibrate:FACTor?
        motor_calibration_factor = miva.get_motor_calibration_factor()
        if motor_calibration_factor is not None:
            print('Motor calibration factor: {}'.format(motor_calibration_factor))
            return_msg = str(motor_calibration_factor)
        else:
            print('Error: get [motor calibration factor] failed')
    elif re.match(r'(:)(sens(or)?)((:)(up|down))?((:)(ref(erence)?))(\?)', cmd):
        # Read Occlusion Sensor Reference Value
        # :SENSor[:{UP | DOWN}]:REFerence?
        re_match_result = re.match(r'(:)(sens(or)?)((:)(up|down))?((:)(ref(erence)?))(\?)', cmd)
        occlusion_thresholds = miva.get_occlusion_thresholds()
        if occlusion_thresholds != {}:
            print('Up stream threshold: {}'.format(occlusion_thresholds['up']))
            print('Dn stream threshold: {}'.format(occlusion_thresholds['down']))
        else:
            print('Error: get [occlusion thresholds] failed')
        #
        if re_match_result[6] is not None:
            return_msg = str(occlusion_thresholds[re_match_result[6]])
        else:
            return_msg = json.dumps(occlusion_thresholds)
    elif re.match(r'(:)(sens(or)?)((:)(up|down))?((:)(ref(erence)?))(\s)(\d+)((\s)(\d+))?', cmd):
        # Write Occlusion Sensor Reference Value
        # :SENSor[:{UP | DOWN}]:REFerence <up_number> [<down_number>]
        re_match_result = re.match(r'(:)(sens(or)?)((:)(up|down))?((:)(ref(erence)?))(\s)(\d+)((\s)(\d+))?', cmd)
        occlusion_thresholds = miva.get_occlusion_thresholds()
        if re_match_result[6] is not None and re_match_result[15] is None:
            # matched {UP | DOWN} and didn't match the second number
            # Write only one sensor reference
            occlusion_thresholds[re_match_result[6]] = int(re_match_result[12]) if 0 <= int(re_match_result[12]) <= 65535 else 65535
        elif re_match_result[6] is None and re_match_result[15] is not None:
            # Didn't match {UP | DOWN} and matched the second number
            # Write both sensor references
            occlusion_thresholds['up'] = int(re_match_result[12]) if 0 <= int(re_match_result[12]) <= 65535 else 65535
            occlusion_thresholds['down'] = int(re_match_result[15]) if 0 <= int(re_match_result[15]) <= 65535 else 65535
        # Write the sensor reference values back
        occlusion_thresholds = miva.set_occlusion_thresholds(occlusion_thresholds)
        if occlusion_thresholds != {}:
            print('Up threshold is set to: {}'.format(occlusion_thresholds['up']))
            print('Dn threshold is set to: {}'.format(occlusion_thresholds['down']))
        else:
            print('Error: set [occlusion thresholds] failed')
    elif re.match(r'(:)(vinf)(:)(tot(al)?)(\?)', cmd):
        # Read [Total Volume Infused]
        # :VINF:TOTal?
        # total_volume_infused = miva.get_total_volume_infused()
        product_life_volume = miva.get_product_life_volume()
        if product_life_volume is not None:
            # print('Total volume infused: {} mL'.format(total_volume_infused))
            print('Total volume infused: {:.2f} mL'.format(product_life_volume['volume']))
            return_msg = '{:.2f}'.format(product_life_volume['volume'])
        else:
            print('Error: get [Total Volume Infused] failed')
    elif re.match(r'(:)(batt(ery)?)(:)(volt(age)?)(\?)', cmd):
        # Read [Battery Voltage]
        # :BATTery:VOLTage?
        battery_voltage = miva.get_battery_voltage()
        if battery_voltage is not None:
            print('Battery voltage: {:.2f} V'.format(battery_voltage))
            return_msg = '{:.2f}'.format(battery_voltage)            
        else:
            print('Error: get [Battery Voltage] failed')
    elif re.match(r'(:)(mot(or)?)(:)(rot(ation)?)(:)(tot(al)?)(\?)', cmd):
        # Read [Motor Total Rotation]
        # :MOTor:ROTation:TOTal?
        product_life_volume = miva.get_product_life_volume()
        if product_life_volume != {}:
            print('Motor total rotation: {}'.format(product_life_volume['rotation']))
            return_msg = str(product_life_volume['rotation'])
        else:
            print('Error: get [Calibration Factor and Total Rotation] failed')
    elif re.match(r'(:)(pump)(:)(on)(:)(time)(\?)', cmd):
        # Read [Total Pump ON Time] (in seconds)
        # :PUMP:ON:TIME?
        total_pump_on_time = miva.get_total_pump_on_time()
        if total_pump_on_time != '':
            day = str(int(total_pump_on_time / 3600 / 24)).zfill(2)
            hour = str(int(total_pump_on_time / 3600 % 24)).zfill(2)
            minute = str(int(total_pump_on_time % 3600 / 60)).zfill(2)
            second = str(int(total_pump_on_time % 3600 % 60)).zfill(2)
            print('{0} day {1} hr {2} min {3} sec'.format(day, hour, minute, second))
            print("Read pump total ON time - Done!")
            return_msg = str(total_pump_on_time)
        else:
            print('Error: get [Battery Voltage] failed')
    elif re.match(r'(:)(batt(ery)?)(:)(cal(ibrate)?)(:)(fact(or)?)(\?)', cmd):
        # Read Battery Calibration Factor
        # :BATTery:CALibrate:FACTor?
        battery_calibration_and_voltage = miva.get_battery_calibration_and_voltage()
        if battery_calibration_and_voltage != {}:
            print('Battery calibration factor = {}'\
                    .format(battery_calibration_and_voltage['calibration']))
            print('Battery voltage = {:.2f} V'\
                    .format(battery_calibration_and_voltage['voltage']))
            return_msg = str(battery_calibration_and_voltage['calibration'])
        else:
            print('Error: get [Battery Voltage] failed')
    elif re.match(r'(:)(base)(:)(year)(\?)', cmd):
        # Read [Base Year] (2000)
        # :BASE:YEAR?
        base_year = miva.get_base_year()
        if base_year != '':
            print('Base year = {}'.format(base_year))
            return_msg = str(base_year)
        else:
            print('Error: get [Base Year] failed')
    elif re.match(r'(:)(sens(or)?)((:)(up|down))?(\?)', cmd):
        # Read Occlusion Sensor Value
        # :SENSor[:{UP | DOWN}]?
        re_match_result = re.match(r'(:)(sens(or)?)((:)(up|down))?(\?)', cmd)
        occlusion_sensor = miva.get_occlusion_sensor()
        if occlusion_sensor != {}:
            print('Up stream: {}'.format(occlusion_sensor['up']))
            print('Dn stream: {}'.format(occlusion_sensor['down']))
        else:
            print('Error: get [occlusion thresholds] failed')
        #
        if re_match_result[6] is not None:
            return_msg = str(occlusion_sensor[re_match_result[6]])
        else:
            return_msg = json.dumps(occlusion_sensor)
    elif re.match(r'(:)(lib(rary)?)((:)(name|ver(sion)?))?(\?)', cmd):
        # Read [Library Name and Version]
        re_match_result = re.match(r'(:)(lib(rary)?)((:)(name|ver(sion)?))?(\?)', cmd)
        library_name_version = miva.get_library_name_version()
        if library_name_version != '':
            print('Library name: [{}]'.format(library_name_version['name']))
            print('Library version: [{}]'.format(library_name_version['version']))
        else:
            print('Error: get [Library Name and Version] failed')
        #
        if re_match_result[6] is not None:
            if re_match_result[6] == 'name':
                return_msg = str(library_name_version['name'])
            else:
                return_msg = str(library_name_version['version'])
        else:
            return_msg = json.dumps(library_name_version)
    elif re.match(r'(:)(firm(ware)?)(:)(ver(sion)?)(\?)', cmd):
        # Read [Firmware Version]
        software_version = miva.get_firmware_version()
        if software_version != '':
            print('Firmware version: [{}]'.format(software_version))
            return_msg = software_version
        else:
            print('Error: get [Software Version] failed')
    # ==============================================
    elif re.match(r'(:)(key)(:)(info)((:)(shor(t)?|long))?', cmd):
        # Send [INFO] key command [Short | Long] Press
        re_match_result = re.match(r'(:)(key)(:)(info)((:)(shor(t)?|long))?', cmd)
        if re_match_result[7] is not None:
            if re_match_result[7] == 'long':
                return_text = miva.press_key(_INFO_KEY, _LONG_PRESS)
            else:
                return_text = miva.press_key(_INFO_KEY, _SHORT_PRESS)
        else:
            return_text = miva.press_key(_INFO_KEY, _SHORT_PRESS)
        if len(return_text) == 4 and return_text[0:2] == 'KE':
            print('key: Info ({})'.format(re_match_result[7]))
    elif re.match(r'(:)(key)(:)(run|stop)', cmd):
        # Send [RUN | STOP] key command [Short | Long] Press
        re_match_result = re.match(r'(:)(key)(:)(run|stop)((:)(short|long))?', cmd)
        if re_match_result[4] == 'run':
            return_text = miva.press_key(_RUN_KEY, _MID_PRESS)
        elif re_match_result[4] == 'stop':
            return_text = miva.press_key(_RUN_KEY, _MID_PRESS)
        if len(return_text) == 4 and return_text[0:2] == 'KE':
            print('key: {}'.format(re_match_result[4].upper()))
    elif re.match(r'(:)(key)(:)(ok|ent(er)?)', cmd):
        # Send [OK | ENTER] key command [Short] Press
        return_text = miva.press_key(_OK_KEY, _SHORT_PRESS)
        if len(return_text) == 4 and return_text[0:2] == 'KE':
            print('key: Ok/Enter (short)')
    elif re.match(r'(:)(key)(:)(up)', cmd):
        # Send [UP] key command [Short] Press
        return_text = miva.press_key(_UP_KEY, _SHORT_PRESS)
        if len(return_text) == 4 and return_text[0:2] == 'KE':
            print('key: Up (short)')
    elif re.match(r'(:)(key)(:)(down)', cmd):
        # Send [DOWN] key command [Short] Press
        return_text = miva.press_key(_DOWN_KEY, _SHORT_PRESS)
        if len(return_text) == 4 and return_text[0:2] == 'KE':
            print('key: Down (short)')
    elif re.match(r'(:)(key)(:)(bol(us)?)', cmd):
        # Send [BOLUS] key command [Short] Press
        return_text = miva.press_key(_BOLUS_KEY, _SHORT_PRESS)
        if len(return_text) == 4 and return_text[0:2] == 'KE':
            print('key: Bolus (short)')
    elif re.match(r'(:)(key)(:)(power)', cmd):
        # Send [ON/OFF] key command [Long] Press
        return_text = miva.press_key(_POWER_KEY, _LONG_PRESS)
        if len(return_text) == 4 and return_text[0:2] == 'KE':
            print('key: On/Off (long)')
    # ==============================================
    elif re.match(r'(:)(pin)(:)(\d{3})', cmd):
        # Input PIN number
        pin_number = re.match(r'(:)(pin)(:)(\d{3})', cmd)[4]
        print('Input PIN number [{}]...'.format(pin_number))
        time.sleep(_TIMEOUT * 10)
        #
        miva.input_digits(pin_number)
    elif re.match(r'(:)(cloc(k)?)(\?)', cmd):
        # Read Pump Time
        pump_time_str = miva.read_pump_time()
        if len(pump_time_str) == 10:
            # print(pump_time_str)
            day = str(int(pump_time_str[0:2], 16)).zfill(2)
            month = str(int(pump_time_str[2:4], 16)).zfill(2)
            year = str(int(pump_time_str[4:6], 16) + 2000).zfill(2)
            hour = str(int(pump_time_str[6:8], 16)).zfill(2)
            minute = str(int(pump_time_str[8:10], 16)).zfill(2)
            second = str(int(pump_time_str[10:12], 16)).zfill(2)
            print('{0}-{1}-{2} {3}:{4}:{5}'.format(year, month, day, hour, minute, second))
            print("Read pump time - Done!")
            return_msg = '{0}-{1}-{2} {3}:{4}:{5}'.format(year, month, day, hour, minute, second)
        elif len(pump_time_str) == 8:
            # The pump time is in relative format
            # [pump_time_str] is in format 'F0 00 00 00', So the first 'F' need to be removed.
            pump_life = int('0' + pump_time_str[1:], 16)
            active_since = datetime.datetime.now() - datetime.timedelta(seconds=pump_life)
            active_since_str = active_since.strftime("%Y-%m-%d %H:%M:%S")
            pump_life_delta = datetime.timedelta(seconds=pump_life)
            print('{0} (0x{1} - {2} sec - {3})'.format(active_since_str, \
                                                       pump_time_str, \
                                                       pump_life, \
                                                       pump_life_delta))
            print("Read pump time - Done!")
        else:
            print('Error: read pump time failed')
    elif re.match(r'(:)(cloc(k)?)(:)(sync(hronize)?)', cmd):
        # Synchronize Pump Time with PC time
        status = miva.write_pump_time()
        if status:
            current_date_time = datetime.datetime.now()
            current_date = datetime.date(current_date_time.year, \
                    current_date_time.month, current_date_time.day)
            current_time = datetime.time(current_date_time.hour, \
                    current_date_time.minute, current_date_time.second)
            print('{0} {1}'.format(current_date, current_time))
            print("Write pump time - Done!")
        else:
            print('Error: write pump time failed')
    elif re.match(r'(\*rst)', cmd):
        # Reset Pump Total VINF and Total ON Time
        print("Reset pump ...")
        status = miva.reset_pump()
        if status:
            print("Reset service total volume infused - Done!")
            print("Reset service total ON time - Done!")
        else:
            print('Error: reset pump failed')
    elif re.match(r'(:)(raw)(:)(.+)', cmd):
        # Send Raw Command (the command that pump recognize directly)
        re_match_result = re.match(r'(:)(raw)(:)(.+)', cmd)
        sent_text = re_match_result[4].upper().strip(' \t\r\n\0')
        print('Command to send: {}'.format(sent_text))
        return_msg = miva.query(sent_text)
        print(return_msg)
    elif re.match(r'(:)(plat(form)?)(\?)', cmd):
        # Read Platform (H and K pump only)
        platform = miva.read_platform()
        if platform != '':
            print('pump platform: [{}]'.format(platform))
            return_msg = platform
        else:
            print('Error: read pump platform failed')
    elif re.match(r'(:)(plat(form)?)(\s)(h|k)', cmd):
        # Write Platform (H and K pump only)
        re_match_result = re.match(r'(:)(plat(form)?)(\s)(h|k)', cmd)
        platform = re_match_result[5]
        status = miva.write_platform(platform)
        if status:
            print("Write pump platform - Done!")
        else:
            print('Error: write pump platform failed')
    # ==============================================
    elif re.match(r'(:)(sim(ulator)?)(:)(lib(rary)?)(:)(load)(\s)(.+)', cmd):
        # Load Library (to the pump simulator)
        re_match_result = re.match(r'(:)(sim(ulator)?)(:)(lib(rary)?)(:)(load)(\s)(.+)', cmd)
        lib_path = re_match_result[10]
        if path.exists(lib_path):
            library.load(lib_path)
            miva.pump_config["library_path"] = lib_path
            json_to_file(miva.pump_config, miva.pump_config_path)
            print("library: ")
            # Title
            print("    {0:5s}    |    {1:5s}    |    {2:15s}    "
                    .format('id', 'ver.', 'name'))
            print("----{0:5s}----|----{1:5s}----|----{2:15s}----"\
                    .format('-----', '-----', '---------------'))
            # Content
            print("    {0:5s}    |    {1:5s}    |    {2:15s}"\
                    .format(str(library.get_id()), \
                            str(library.get_version()), \
                            library.get_name()))
    elif re.match(r'(:)(sim(ulator)?)(:)(lib(rary)?)(:)(load)(\?)', cmd):
        # Query Library Name (from the pump simulator)
        print("library: ")
        # Title
        print("    {0:5s}    |    {1:5s}    |    {2:15s}    "
                .format('id', 'ver.', 'name'))
        print("----{0:5s}----|----{1:5s}----|----{2:15s}----"\
                .format('-----', '-----', '---------------'))
        # Content
        print("    {0:5s}    |    {1:5s}    |    {2:15s}"\
                .format(str(library.get_id()), \
                        str(library.get_version()), \
                        library.get_name()))
        lib_info = {'id':library.get_id(), \
                    'version':library.get_version(), \
                    'name':library.get_name()
                    }
        return_msg = json.dumps(lib_info)
    elif re.match(r'(:)(sim(ulator)?)(:)(prot(ocol)?)(:)(list)(\?)', cmd):
        # Query Protocol List (from the pump simulator)
        protocol_list = []
        protocols = library.get_protocols()
        for each_protocol in protocols:
            protocol_info = {'id':str(each_protocol['id']),
                             'name': str(each_protocol['content']['name']),
                             'deliveryMode': str(each_protocol['content']['deliveryMode'])}
            protocol_list.append(protocol_info)
        return_msg = json.dumps(protocol_list)
        print(json.dumps(protocol_list, indent=4))
        print('Total [{}] protocols extracted'.format(len(protocols)))
    elif re.match(r'(:)(sim(ulator)?)(:)(prot(ocol)?)(:)(sel(ect)?)(\s)(.+)', cmd):
        # Select Protocol (on the pump simulator and on the pump)
        re_match_result = re.match(r'(:)(sim(ulator)?)(:)(prot(ocol)?)(:)(sel(ect)?)(\s)(.+)', \
                                   cmd_original, re.IGNORECASE)
        protocol_name = re_match_result[11]
        # print('protocol name = {}'.format(protocol_name))
        # MUST BE DEEP COPY
        protocol = copy.deepcopy(library.get_protocol(protocol_name))
        if protocol is not None:
            # Quit the current infusion task on the simulator
            if 'PAUSED' in infusion.status.name:
                infusion_monitor.set_command('quit')
            elif 'RUNNING' in infusion.status.name:
                print('Abort: infusion is running...')
                return return_msg
            # select protocol on the pump
            miva.select_protocol(library, protocol)
            # set protocol on the simulator
            infusion.set_protocol(protocol)
            # save selected protocol
            miva.pump_config["protocol_selected"] = protocol_name
            json_to_file(miva.pump_config, miva.pump_config_path)
    elif re.match(r'(:)(sim(ulator)?)(:)(prot(ocol)?)(:)(sel(ect)?)(\?)', cmd):
        # Query the Selected Protocol (on the pump simulator and on the pump)
        protocol_name = protocol['content']['name']
        protocol_id = protocol['id']
        protocol_info = {'id':protocol_id, 'name':protocol_name} 
        return_msg = json.dumps(protocol_info)
    elif re.match(r'(:)(sim(ulator)?)(:)(prot(ocol)?)(:)(para(meter)?)(:)(list)(\?)', cmd):
        # Print Parameter List
        parameter_list = get_parameter_list(library, protocol)
        return_msg = ' '.join(parameter_list)
        print('==')
        print('Infusion Parameter List = {}'.format(parameter_list))
    elif re.match(r'(:)(sim(ulator)?)(:)(prot(ocol)?)(:)(para(meter)?)(:)(.+)(\s)(\d+)((.)(\d+))?', cmd):
        # Change Parameter Value (on the pump simulator and on the pump)
        re_match_result = re.match(r'(:)(sim(ulator)?)(:)(prot(ocol)?)(:)(para(meter)?)(:)(.+)(\s)(\d+)((.)(\d+))?', \
                                   cmd_original, re.IGNORECASE)
        parameter_name = re_match_result[11]
        parameter_value = re_match_result[13]
        parameter_list = get_parameter_list(library, protocol)
        if parameter_name not in parameter_list \
                and parameter_name not in ['drugAmount', 'diluteVolume']:
            print('    Invalid parameter name: {}'.format(parameter_name))
            return return_msg
        if parameter_name in ['drug', 'label']:
            print('    Abort: [{}] is NOT editable'.format(parameter_name))
            return return_msg
        if parameter_name == 'concentration':
            if protocol['content']['drug']['content']['concentrationImmutable']:
                print('    Abort: concentration is NOT editable')
            else:
                print('    Abort: concentration is NOT editable'.format(parameter_name))
                print('           type \'drugAmount\' or \'diluteVolume\' instead')
            return return_msg
        # get parameter original, maximum, minimum values and unit
        parameter = get_parameter(protocol, parameter_name, infusion)
        original_value = float(parameter['value'])
        max_value = float(parameter['max'])
        min_value = float(parameter['min'])
        upper_limit = max_value
        lower_limit = min_value
        unit = parameter['unit']
        # get NEW value
        if parameter['name'] == 'weight':
            upper_limit = float(parameter['upper_limit'])
            lower_limit = float(parameter['lower_limit'])
            print('{0} = {1:.2f} {2} (max: {3:.2f} {2}; min: {4:.2f} {2})'\
                    .format(parameter_name, original_value, \
                            unit, upper_limit, lower_limit))
        elif parameter['name'] == 'diluteVolume':
            print('{0} = {1:.0f} {2} (max: {3:.0f} {2}; min: {4:.0f} {2})'\
                    .format(parameter_name, original_value, \
                            unit, max_value, min_value))
        else:
            print('{0} = {1:.2f} {2} (max: {3:.2f} {2}; min: {4:.2f} {2})'\
                    .format(parameter_name, original_value, \
                            unit, max_value, min_value))
        if parameter['name'] == 'diluteVolume':
            new_value_str = parameter_value
            new_value_str = int(float(new_value_str))
            new_value_str = str(new_value_str)
        else: 
            new_value_str = parameter_value
        # check if it is a number
        if new_value_str.replace('.', '', 1).isdigit():
            if float(new_value_str) > max_value:
                print('Out of range: {0} will be set to {1:.2f} {2}'.format(parameter_name, max_value, unit))
                new_value = max_value
            elif float(new_value_str) < min_value:
                print('Out of range: {0} will be set to {1:.2f} {2}'.format(parameter_name, min_value, unit))
                new_value = min_value
            else:
                new_value = float(new_value_str)
        elif new_value_str.lower().strip(' \t\r\n\0') == 'max':
            if parameter['name'] == 'weight':
                new_value = upper_limit
            else:
                new_value = max_value
        elif new_value_str.lower().strip(' \t\r\n\0') == 'min':
            if parameter['name'] == 'weight':
                new_value = lower_limit
            else:
                new_value = min_value
        else:
            print('invalid input: {}'.format(new_value_str))
            return return_msg
        if new_value == original_value:
            print('Abort: two values are equal')
            return return_msg
        # select [Parameter] on the pump
        result = miva.select_parameter(library, protocol, parameter_name)
        if result:
            print('==')
            print('Set [{0}] to [{1:.2f}] {2}...'.format(parameter_name, new_value, unit))
            time.sleep(_TIMEOUT * 10)
            # Set [Parameter] Value on the Pump
            miva.set_parameter_value(new_value, parameter)
            # Update [Parameter] value
            if parameter_name == 'weight':
                infusion.patient_weight = new_value
            elif parameter_name in ['drugAmount', 'diluteVolume']:
                protocol['content']['drug']['content'][parameter_name]['value'] = new_value
            else:
                protocol['content']['program'][parameter_name]['value'] = new_value
            #
            infusion.set_protocol(protocol)
        # Return to top of the [Parameter] list
        miva.return_top(library, protocol, parameter_name)
        # Display infusion parameters
        infusion.print_parameters()
    elif re.match(r'(:)(sim(ulator)?)(:)(prot(ocol)?)(:)(para(meter)?)(:)((?!list).+)(\?)', cmd):
        # Query Parameter Value (from the pump simulator)
        re_match_result = re.match(r'(:)(sim(ulator)?)(:)(prot(ocol)?)(:)(para(meter)?)(:)((?!list).+)(\?)', \
                                   cmd_original, re.IGNORECASE)
        parameter_name = re_match_result[11]
        parameter_list = get_parameter_list(library, protocol)
        if parameter_name not in parameter_list \
                and parameter_name not in ['drugAmount', 'diluteVolume']:
            print('    Invalid parameter name: {}'.format(parameter_name))
            return return_msg
        if parameter_name == 'drug':
            drug_info = protocol['content']['drug']['content']
            return_msg = json.dumps(drug_info)
            return return_msg
        if parameter_name == 'label':
            label_set = library.get_protocol_label_set(protocol['content']['name'])
            return_msg = json.dumps(label_set)
            return return_msg
        if parameter_name == 'concentration':
            if protocol['content']['drug']['content']['concentrationImmutable']:
                print('    Abort: concentration is NOT editable')
            else:
                print('    Abort: concentration is NOT editable'.format(parameter_name))
                print('           type \'drugAmount\' or \'diluteVolume\' instead')
            return return_msg
        # get parameter original, maximum, minimum values and unit
        parameter = get_parameter(protocol, parameter_name, infusion)
        return_msg = json.dumps(parameter)
        print(json.dumps(parameter, indent=4))
    elif re.match(r'(:)(sim(ulator)?)(:)(inf(usion)?)(:)(run)', cmd):
        # Run Infusion (on the pump)
        if library.get_library() is not None:
            if protocol is not None:
                # protocl_name = protocol['content']['name']
                infusion.set_protocol(protocol)
                print("Protocol: ")
                print()
                # Title
                print("    {0:5s}    |    {1:15s}    |    {2:20s}"\
                        .format('id', 'name', 'mode'))
                print("----{0:5s}----|----{1:15s}----|----{2:20s}"\
                        .format('-----', '---------------', '--------------------'))
                # Content
                print("    {:5s}    |".format(str(protocol['id'])), end='')
                print("    {:15s}    |".format(protocol['content']['name']), end='')
                print("    {:20s}".format(protocol['content']['deliveryMode']))
                print()
                #
                print("Extracted Parameters:")
                print()
                if protocol['content']['deliveryMode'] == 'continuousInfusion':
                    infusion.print_cont_parameters()
                if protocol['content']['deliveryMode'] == 'bolusInfusion':
                    infusion.print_bolus_parameters()
                if protocol['content']['deliveryMode'] == 'intermittentInfusion':
                    infusion.print_int_parameters()
                #
                start_yes_no = 'y'
                if start_yes_no.lower().find('y') != -1 or start_yes_no == '':
                    print('infusion start...')
                    # Run Protocol on the Pump
                    miva.run_protocol(library, protocol)
                    # infusion.run_infusion()
                    if infusion.status in [InfusionStatus.PAUSED_AUTO_BOLUS, \
                                           InfusionStatus.PAUSED_DEMAND_BOLUS, \
                                           InfusionStatus.PAUSED_LOADING_DOSE, \
                                           InfusionStatus.PAUSED_CLINICIAN_DOSE]:
                        infusion_monitor.output_enabled = False
                        #
                        resume_dose = 'y'
                        if resume_dose == 'y':
                            print('==')
                            print('resume dose...')
                            time.sleep(_TIMEOUT * 10)
                            # Press [Ok] Key
                            return_text = miva.press_key(_OK_KEY, _SHORT_PRESS)
                            if len(return_text) == 4 and return_text[0:2] == 'KE':
                                print('key: Ok/Enter (short)')
                            time.sleep(_TIMEOUT * 10)
                        else:
                            infusion.status = InfusionStatus.PAUSED
                            basal_rate = infusion.get_rate(infusion.protocol)
                            infusion.motor.set_rate(basal_rate)
                            print('==')
                            print('cancel dose...')
                            time.sleep(_TIMEOUT * 10)
                            # Press [Down] Key
                            return_text = miva.press_key(_DOWN_KEY, _SHORT_PRESS)
                            if len(return_text) == 4 and return_text[0:2] == 'KE':
                                print('key: Down (short)')
                            time.sleep(_TIMEOUT * 10) 
                            # Press [Ok] Key
                            return_text = miva.press_key(_OK_KEY, _SHORT_PRESS)
                            if len(return_text) == 4 and return_text[0:2] == 'KE':
                                print('key: Ok/Enter (short)')
                            time.sleep(_TIMEOUT * 10)
                        infusion_monitor.output_enabled = True
                            
                else:
                    print('infusion aborted...')
            else:
                print('Empty Protocol: Use <SP> command to select protocol first.')
        else:
            print('Empty Library: Use <LL> command to load library first.')
    elif re.match(r'(:)(sim(ulator)?)(:)(inf(usion)?)(:)(stop)', cmd):
        # Stop Infusion (on the pump)
        return_text = miva.trigger_stop_infusion()
        if return_text:
            print('Trigger Stop Infusion')
    elif re.match(r'(:)(sim(ulator)?)(:)(inf(usion)?)(:)(cli(nician)?)(:)(run)', cmd):
        # Run [Clinician Dose] on the Pump
        clinician_code = library.get_access_code('clinician')
        switches = protocol['content']['program']['switches']
        if switches.get('clinicianDose') and switches['clinicianDose']:
            # Get the platform of the pump
            platform = miva.read_platform()
            if platform in ['H', 'K']:
                if infusion.status in [InfusionStatus.RUNNING_AUTO_BOLUS, \
                                       InfusionStatus.RUNNING_DEMAND_BOLUS, \
                                       InfusionStatus.RUNNING_LOADING_DOSE]:
                    print('clinician dose NOT granted: infusion status = {}'\
                          .format(infusion.status.name))
                    print()
                else:
                    miva.run_clinician_dose(clinician_code)
            elif platform == 'C':
                if infusion.status in [InfusionStatus.PAUSED_MPH_REACHED, \
                                       InfusionStatus.PAUSED_MPI_REACHED] \
                        and infusion.previous_status in [InfusionStatus.RUNNING_AUTO_BOLUS, \
                                                         InfusionStatus.RUNNING_DEMAND_BOLUS, \
                                                         InfusionStatus.RUNNING_LOADING_DOSE]:
                    print('clinician dose NOT granted: previous infusion status = {}'\
                          .format(infusion.previous_status.name))
                    print()
                elif infusion.status in [InfusionStatus.RUNNING_AUTO_BOLUS, \
                                       InfusionStatus.RUNNING_DEMAND_BOLUS, \
                                       InfusionStatus.RUNNING_LOADING_DOSE]:
                    print('clinician dose NOT granted: infusion status = {}'\
                          .format(infusion.status.name))
                    print()
                else:
                    miva.run_clinician_dose(clinician_code)
    elif re.match(r'(:)(sim(ulator)?)(:)(inf(usion)?)(:)(stat(us)?)(\?)', cmd):
        # Check Infusion Status
        infusion_monitor.set_command('status')
        return_msg = infusion.status.name
    elif re.match(r'(:)(sim(ulator)?)(:)(inf(usion)?)(:)(para(meter)?)(\?)', cmd):
        # Query Infusion Runtime Parameters
        return_msg = json.dumps(socket_server.infusion.get_runtime_parameters())
        print(json.dumps(socket_server.infusion.get_runtime_parameters(), indent=4))
    if re.match(r'(:)(sim(ulator)?)(:)(inf(usion)?)(:)(quit|pause|parameters)', cmd):
        # Run [Infusion Monitor] Command
        re_match_result = re.match(r'(:)(sim(ulator)?)(:)(inf(usion)?)(:)(quit|pause|parameters)', cmd)
        infusion_monitor.set_command(re_match_result[8])
    # ==============================================
    # Resume [Event Log Monitor]
    if event_log_monitor.is_on():
        event_log_monitor.resume()
    # ==============================================
    # Enable [Event Log Monitor] Output
    infusion_monitor.enable_output()
                    
    return return_msg


def main():
    '''main function'''
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print("IP address: {0}".format(local_ip))
    
        # HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
        HOST = local_ip
        PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
        # Create the server, binding to localhost on port 9999
#         with socketserver.TCPServer((HOST, PORT), SocketRequestHandler) as tcp_server:
#             #######################################
#             # create a [request_handler] thread   #
#             #######################################
#             request_handler_thread = Thread(target=tcp_server.serve_forever, args=())
#             request_handler_thread.daemon = True
#             request_handler_thread.start()
#             request_handler_thread.join()
        with SocketServer((HOST, PORT), SocketRequestHandler,) as socket_server:
            socket_server.start()
    except KeyboardInterrupt:
        print('Exiting: [Ctrl + C] is pressed')
        pass


if __name__ == "__main__":
    main()
