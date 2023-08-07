'''Module MIVA'''
import binascii
import re
import json
import struct
import time
import datetime
import copy
import sys
import socket
import ssl
import platform
import traceback
from threading import Thread
from threading import Lock
from os import path, system, makedirs
import serial
from Cryptodome.Cipher import AES
from pyZynoUnifiedDrivers.miva.module_infusion import Infusion, InfusionStatus, InfusionMonitor
from pyZynoUnifiedDrivers.miva.module_library import Library, get_parameter_list, encrypt_library, parse_library_hex
from pyZynoUnifiedDrivers.miva.module_library import get_parameter
from pyZynoUnifiedDrivers.miva.module_sendrx import SendRx, parse_rx_hex, encrypt_rx
from pyZynoUnifiedDrivers.miva.module_utils import re_serial_port, re_ip_address, create_pump_config_file
from pyZynoUnifiedDrivers.miva.module_utils import scan_serial_ports, hex_to_float, float_to_hex
from pyZynoUnifiedDrivers.miva.module_utils import EVENT_LOG_NUMBER_OF_EVENTS, EVENT_LOGS_PER_INFUSION_DATA_LOG
from pyZynoUnifiedDrivers.miva.module_utils import re_scpi_common_cmd, re_scpi_get_cmd, re_scpi_set_cmd, re_query_event_list
from pyZynoUnifiedDrivers.miva.module_utils import crc32c, crc_checksum, isfloat, int_to_time_str, file_to_list
from pyZynoUnifiedDrivers.miva.module_utils import json_to_file, list_to_file, bitmap_to_image, apply_screenshot_masks
from pyZynoUnifiedDrivers.miva.module_utils import load_json_file, hex_to_bitmap, compare_file_equal, re_get_key_list
from pyZynoUnifiedDrivers.miva.module_utils import re_search_for_event, re_query_event_timestamp
from pyZynoUnifiedDrivers.miva.module_utils import re_read_event_log, re_read_event_log_hex, re_query_help_file
from pyZynoUnifiedDrivers.miva.module_utils import re_get_screenshot, re_compare_screenshot, re_clear_key_list
from pyZynoUnifiedDrivers.miva.module_utils import re_checksum, re_query_lockout, re_query_screenshot_line
from pyZynoUnifiedDrivers.miva.module_utils import _UP_KEY, _DOWN_KEY, _INFO_KEY, _OK_KEY, _POWER_KEY
from pyZynoUnifiedDrivers.miva.module_utils import _RUN_KEY, _BOLUS_KEY, _STOP_KEY, _SHORT_PRESS, _LONG_PRESS
from pyZynoUnifiedDrivers.miva.module_utils import VISA_RESOURCE_CONFIG_FILE_PATH, PUMP_CONFIG_FILE_PATH
from pyZynoUnifiedDrivers.miva.module_utils import download_mfg_32_bit, download_miva_8_bit, download_miva_32_bit 
from pyZynoUnifiedDrivers.miva.module_test import Test
from pyZynoUnifiedDrivers.miva.module_socket_server_ssl import SocketServerSSL, SocketRequestHandlerSSL
from pyZynoUnifiedDrivers.miva.module_socket_server_ssl import SERVER_CERTIFICATE_PATH, PRIVATE_KEY_PATH, SOCKET_BUFFER_SIZE
from pyZynoUnifiedDrivers.miva.module_script import Script
from pyZynoUnifiedDrivers.miva.module_event_log import EventLogMonitor

# from module_utils import byte_fill
# from miva.module_event_log import EventLogMonitor

CLIENT_CERTIFICATE_PATH = './miva/client_trust_store/certificate.crt'
 
#
_BAUD_RATE = 9600
_BYTE_SIZE = 8
_STOPBITS = 1
_PARITY = serial.PARITY_NONE
_FLOW_CONTROL = 0
_TIMEOUT = 0.025
_WRITE_TIMEOUT = 0.1
_ENCRYPTION_KEY = b'\x01\x23\x45\x67\x89\xAB\xCD\xEF' + \
                  b'\x01\x23\x45\x67\x89\xAB\xCD\xEF' + \
                  b'\x01\x23\x45\x67\x89\xAB\xCD\xEF' + \
                  b'\x01\x23\x45\x67\x89\xAB\xCD\xEF'


class Key:
    '''Key Definition'''
    
    # Define Key Pressing
    NONE_KEY = '0'
    UP_KEY = '1'
    DOWN_KEY = '2'
    INFO_KEY = '3'
    OK_KEY = '4'
    POWER_KEY = '5'
    RUN_KEY = '6'
    BOLUS_KEY = '7'
    SHORT_PRESS = '0'
    LONG_PRESS = '1'


def build_message(command, checksum_symbol='+'):
    '''Build Message to Be Sent to Pump Based on Command
        @param command R/W+Index+Parameters
        @return message that can be recognized by pump
    '''
    frame_start = 0x02
    frame_end = 0x03
    crc = crc_checksum(command, checksum_symbol).upper()
    #
    message = []
    #
    message.append(frame_start)
    #
    for each_char in command:
        message.append(ord(each_char))
    #
    for each_char in crc:
        message.append(ord(each_char))
    #
    message.append(frame_end)
    #
    return message


def get_infusion_data_frame(event_log_hex):
    '''get infusion data frame
        -- DATA_LOG_BEGIN 1
        16 x 16 bytes protocol data in between
        -- DATA_LOG_END 2    
    '''
    infusion_data_frame_id = int(event_log_hex[10:12], 16)
    switcher = {
        1: 'INFUSION_DATA_BEGIN',
        2: 'INFUSION_DATA_END'
    }
    return switcher.get(infusion_data_frame_id, "Unknown Status ({})".format(infusion_data_frame_id))


def get_battery_status(event_log_hex):
    '''get battery status'''
    battery_status_id = int(event_log_hex[10:14], 16)
    switcher = {
        # 0: 'BATTERY_NO_UPDATE',
        1: 'BATTERY_MEDIUM',
        2: 'BATTERY_LOW',
        4: 'BATTERY_DEPLETED',
        8: 'BATTERY_RESET',
        16: 'BATTERY_AC',
        32: 'BATTERY_HIGH',
        64: 'BATTERY_NEW',
        128: 'BATTERY_OVER_UPPER_LIMIT',
        256: 'BATTERY_EMPTY',
        512: 'BATTERY_UNDER_LOWER_LIMIT'
    }
    # get() method of dictionary data type returns  
    # value of passed argument if it is present  
    # in dictionary otherwise second argument will 
    # be assigned as default value of passed argument
    battery_status_list = []
    if battery_status_id == 0:
        battery_status_list = ['BATTERY_NO_UPDATE']
    else:
        for i in range(len(switcher)):
            battery_status = switcher.get(battery_status_id & (2 ** i), "Unknown Status")
            if battery_status != "Unknown Status":
                battery_status_list.append(battery_status + ' (b\'' + '{0:b}'.format(battery_status_id & (2 ** i)).zfill(8) + '\')')
        if battery_status_list == []:
            battery_status_list = ['Unknown Status (b\'' + '{0:b}'.format(event_log_hex[10:14]).zfill(8) + '\')']
    if len(battery_status_list) == 1:
        battery_status_list = battery_status_list[0]
    return battery_status_list


def get_battery_state(event_log_hex):
    '''get battery state'''
    battery_state_id = int(event_log_hex[10:14], 16)
    switcher = {
        # 0: 'BATTERY_NO_UPDATE',
        1:'BATTERY_HIGH',
        2:'BATTERY_MEDIUM',
        3:'BATTERY_LOW',
        4:'BATTERY_CRITICAL',
        5:'BATTERY_AC',
        # ifdef MIVA
        6:'BATTERY_NEW',
        7:'BATTERY_DEPLETED',
        8:'BATTERY_EMPTY'        
    }
    # get() method of dictionary data type returns  
    # value of passed argument if it is present  
    # in dictionary otherwise second argument will 
    # be assigned as default value of passed argument
    battery_state = switcher.get(battery_state_id, "Unknown Status")
    return battery_state


def get_send_library_crc(library_bytes):
    library_block_begin_index = 64
    library_block_end_index = 1152
    block_size = 64
    # The library Block range is : [64:1152]
    # The library Block size should be [1152 - 64 = 1088]
    # Calculate the Digital Signature (Checksum)
    library_hex = library_bytes.hex().upper()
    crc = 0x0
    total_blocks = library_block_end_index - library_block_begin_index
    for i in range(total_blocks):
        # Check to see if the whole block is all [FF]
        # If the whole block is all FF then don't calculate the checksum for the block
        # And do not send the block to the pump in order to save time
        all_empty_bytes = True
        for each_byte in library_bytes[i * block_size:(i + 1) * block_size]:
            if each_byte != 0xFF:
                all_empty_bytes = False
                break
        if (not all_empty_bytes):
            crc = crc32c(crc, library_hex[i * block_size * 2: (i + 1) * block_size * 2])
    return crc


def get_infusion_pause_vinf(event_log_hex):
    ''' get VINF when infusion paused (ml)'''
    pause_vinf_hex = event_log_hex[14:22]
    pause_vinf_float = hex_to_float(pause_vinf_hex)
    return float('{0:.2f}'.format(pause_vinf_float))

    
def get_infusion_limit_type(event_log_hex):
    ''' get infusion limit reached type'''
    limit_reached_type = int(event_log_hex[10:14], 16);
    switcher = {
        1: 'MAX_PER_HR',
        2: 'MAX_PER_INTERVAL',
        4: 'CLEARED'
    }
    return switcher.get(limit_reached_type, "Unknown Type ({})".format(limit_reached_type))


def get_authentication_code(event_log_hex):
    '''get authentication code'''
    authentication_code = int(event_log_hex[10:14], 16);
    return authentication_code


def get_bolus_type(event_log_hex):
    '''get bolus type'''
    bolus_type_id = int(event_log_hex[10:12], 16);
    switcher = {
        1: 'AUTO_BOLUS',
        2: 'EXTRA_DOSE',
        8: 'CLINICIAN_DOSE'
    }
    return switcher.get(bolus_type_id, "Unknown Type ({})".format(bolus_type_id))


def get_bolus_attempted_number(event_log_hex):
    '''get bolus attempted number'''
    number_of_bolus_attempted = int(event_log_hex[12:14], 16);
    return number_of_bolus_attempted


def get_occlusion_type(event_log_hex):
    '''get occlusion type'''
    occlusion_type_id = int(event_log_hex[10:14], 16);
    switcher = {
        1: 'UPSTREAM_OCCLUSION',
        2: 'DOWNSTREAM_OCCLUSION',
        4: 'OCCLUSION_CLEARED'
    }
    return switcher.get(occlusion_type_id, "Unknown Type ({})".format(occlusion_type_id))


def get_delay_end_type(event_log_hex):
    '''get delay end type'''
    delay_end_type_id = int(event_log_hex[10:14], 16);
    switcher = {
        1: 'NORMAL_END',
        2: 'SKIPPED'        
    }
    return switcher.get(delay_end_type_id, "Unknown Type ({})".format(delay_end_type_id))


def get_pump_limit_type(event_log_hex):
    '''get limit type'''
    limit_type = int(event_log_hex[10:14], 16);
    switcher = {
        1: 'PRODUCT_LIFE_REACHED_SEEK_REPLACEMENT_PUMP',
        2: 'SERVICE_LIFE_REACHED_DUE_FOR_SERVICE'        
    }
    return switcher.get(limit_type, "Unknown Type ({})".format(limit_type))


def get_eventlog_battery_voltage(event_log_hex):
    '''get battery voltage (V)'''
    battery_voltage_hex = event_log_hex[14:22]
    battery_voltage_float = hex_to_float(battery_voltage_hex)
    return float('{0:.2f}'.format(battery_voltage_float))


def get_eventlog_battery_vinf(event_log_hex):
    '''get battery VINF (mL)'''
    battery_vinf_hex = event_log_hex[22:30]
    battery_vinf_float = hex_to_float(battery_vinf_hex)
    return float('{0:.1f}'.format(battery_vinf_float))


def get_firmware_error_type(event_log_hex):
    '''get firmware error type'''
    firmware_error_type_id = int(event_log_hex[10:14], 16);
    switcher = {
        1: 'FLASH_CRC_ERROR',
        2: 'CORRUPTED_LIB'        
    }
    return switcher.get(firmware_error_type_id, "Unknown Type ({})".format(firmware_error_type_id))


def get_firmware_error_file(event_log_hex):
    '''get firmware error file'''
    firmware_error_file_id = int(event_log_hex[14:16], 16);
    
    switcher = {
        1: 'infusion_info.c',
        2: 'infusion_task_manage.c',
        3: 'navigation.c',
        4: 'main.c',
        5: 'post.c',
        6: 'protocol_data.c',
        7: 'uart_manager.c',
        8: 'uart_command.c',
        9: 'pump_info.c'
    }
    return switcher.get(firmware_error_file_id, "Unknown File ({})".format(firmware_error_file_id))


def get_firmware_error_line(event_log_hex):
    '''get firmware error line number

       It is the line number of the code line in the file 
       that cause the firmware error.
    '''
    firmware_error_line_hex = event_log_hex[16:20]
    firmware_error_line_int = int(firmware_error_line_hex, 16)
    return firmware_error_line_int


def get_system_error_type(event_log_hex):
    '''get system error type'''
    system_error_type_id = int(event_log_hex[10:14], 16);
    
    switcher = {
                    1: 'UPSTREAM_PRESSURE_SENSOR_ERROR',
                    2: 'SLOW_MOTOR_ERROR',
                    4: 'DOWNSTREAM_PRESSURE_SENSOR_ERROR',
                    8: 'MOTOR_CONTROLLER_FAILURE',
                    16: 'VINF_LIMIT_REACHED',
                    32: 'MOTOR_RUNNING_WRONG_STATE_ERROR',
                    64: 'MOTOR_DRIVER_FAILURE',
                    128: 'TIMER_INTERRUPT_FAILURE',
                    256: 'POST_FAILURE',
                    512: 'FAST_MOTOR_ERROR',
                    1024: 'UPSTREAM_SENSOR_FAILURE',
                    2048: 'DOWNSTREAM_SENSOR_FAILURE',
                    4096: 'MOTOR_SENSOR_FAILURE',
                    8192: 'PRIMARY_AUDIO_FAILURE',
                    16384: 'SUPER_CAPACITOR_FAILURE',
                    32768: 'EXTERNAL_WATCHDOG_FAILURE'
                }
    # get() method of dictionary data type returns  
    # value of passed argument if it is present  
    # in dictionary otherwise second argument will 
    # be assigned as default value of passed argument
    # return switcher.get(system_error_type_id, "Unknown Error ({})".format(system_error_type_id))
    system_error_type_list = []
    if system_error_type_id == 0:
        system_error_type_list = ['Unknown Error']
    else:
        for i in range(len(switcher)):
            system_error_type = switcher.get(system_error_type_id & (2 ** i), "Unknown Error")
            if system_error_type != "Unknown Error":
                system_error_type_list.append(system_error_type + ' (b\'' + '{0:b}'.format(system_error_type_id & (2 ** i)).zfill(8) + '\')')
        if system_error_type_list == []:
            system_error_type_list = ['Unknown Error (b\'' + '{0:b}'.format(system_error_type_id).zfill(8) + '\')']
    return system_error_type_list


def get_battery_failure_type(event_log_hex):
    '''get battery failure type'''
    battery_failure_type_id = int(event_log_hex[10:14], 16);
    
    switcher = {
        1: 'BATTERY_OVERHEATED',
        2: 'BATTERY_EMPTY'
    }
    return switcher.get(battery_failure_type_id, "Unknown Type ({})".format(battery_failure_type_id))


def get_debug_info(event_log_hex):
    '''get debug info'''
    debug_info_hex = event_log_hex[10:14]
    debug_info_int = int(debug_info_hex, 16)
    return debug_info_int

    
def get_timer_count(event_log_hex):
    '''get timer count'''
    timer_count_hex = event_log_hex[14:22]
    timer_count_int = int(timer_count_hex, 16)
    return timer_count_int


def get_dose_finish_type(event_log_hex):
    '''get dose finish type'''
    dose_type_id = int(event_log_hex[10:14], 16);
    
    switcher = {
        1: 'EXTRA_DOSE_FINISH',
        2: 'STARTING_DOSE_FINISH'
    }
    return switcher.get(dose_type_id, "Unknown Type ({})".format(dose_type_id))


def get_cancel_dose_type(event_log_hex):
    '''get cancel dose type'''
    dose_type_id = int(event_log_hex[10:13], 16);
    
    switcher = {
        1: 'STARTING_DOSE',
        2: 'EXTRA_DOSE',
        4: 'DOSE_TYPE_UNKNOWN'
    }
    return switcher.get(dose_type_id, "Unknown Type ({})".format(dose_type_id))


def get_system_error2_type(event_log_hex):
    '''get system error2 type'''
    system_error2_type_id = int(event_log_hex[10:14], 16);
    
    switcher = {
                    1: 'BATTERY_OVER_UPPER_LIMIT',
                    2: 'BATTERY_UNDER_LOWER_LIMIT',
                    4: 'PROTECTION_CPU_FAILURE',
                    8: 'BACKUP_AUDIO_FAILURE',
                   16: 'BACKUP_VDD_LOSS',
                   32: 'PRESSURE_SENSOR_STUCK',
                   64: 'LCD_FAILURE',
                  128: 'BACKUP_BATTERY_FAILURE',
                  256: 'BIST_FAILURE',
                  512: 'MOTOR_ROTATE_FAST'
                }
    system_error2_type_list = []
    if system_error2_type_id == 0:
        system_error2_type_list = ['Unknown Error']
    else:
        for i in range(len(switcher)):
            system_error2_type = switcher.get(system_error2_type_id & (2 ** i), "Unknown Error")
            if system_error2_type != "Unknown Error":
                system_error2_type_list.append(system_error2_type + ' (b\'' + '{0:b}'.format(system_error2_type_id & (2 ** i)).zfill(8) + '\')')
        if system_error2_type_list == []:
            system_error2_type_list = ['Unknown Error (b\'' + '{0:b}'.format(system_error2_type_id).zfill(8) + '\')']
    return system_error2_type_list


def get_pump_hard_limit_reached_type(event_log_hex):
    '''get pump hard limit reached type'''
    limit_type = int(event_log_hex[10:14], 16);
    switcher = {
        4: 'PRODUCT_LIFE_REACHED_REPLACE_PUMP'
    }
    return switcher.get(limit_type, "Unknown Type ({})".format(limit_type))


def get_battery_check_status_type(event_log_hex):
    '''get battery check status type'''
    status_type = int(event_log_hex[10:14], 16);
    switcher = {
        1: 'BATTERY_EMPTY_POST_CHECK',
        2: 'BATTERY_DEPLETED_MOTOR_CHECK',
        3: 'BATTERY_EMPTY_MOTOR_CHECK'               
    }
    return switcher.get(status_type, "Unknown Type ({})".format(status_type))


def get_event_log_sub_type(event_log_hex):
    '''Get Event Log Sub-Type'''
    event_log_sub_type = 'UNKOWN_TYPE'
    event_log_type = get_event_log_type(event_log_hex)
    if event_log_type == 'INFUSION_DATA':
        # INFUSION_DATA 0
        event_log_sub_type = get_infusion_data_frame(event_log_hex)
    elif event_log_type == 'RUN_INFUSION':
        # RUN_INFUSION 1
        pass    
    elif event_log_type == 'INFUSION_PAUSED':
        # INFUSION_PAUSED 2
        pass    
    elif event_log_type == 'CASSETTE_EMPTY_ALARM':
        # CASSETTE_EMPTY_ALARM 3
        pass
    elif event_log_type == 'INFUSION_LIMIT_REACHED':
        # INFUSION_LIMIT_REACHED 4
        event_log_sub_type = get_infusion_limit_type(event_log_hex)
    elif event_log_type == 'AUTHENTICATION':
        # AUTHENTICATION 5
        pass
    elif event_log_type == 'DOSE_GRANTED':
        # DOSE_GRANTED 6
        bolus_type = get_bolus_type(event_log_hex)
        event_log_sub_type = bolus_type
    elif event_log_type == 'EXTRA_DOSE_DENIED':
        # EXTRA_DOSE_DENIED 7
        pass
    elif event_log_type == 'DOSE_CANCEL':
        # DOSE_CANCEL 8
        cancel_dose_type = get_cancel_dose_type(event_log_hex)
        event_log_sub_type = cancel_dose_type
    elif event_log_type == 'OCCLUSION_ALARM':
        # OCCLUSION_ALARM 9
        occlusion_type = get_occlusion_type(event_log_hex)
        event_log_sub_type = occlusion_type
    elif event_log_type == 'DELAY_END':
        # DELAY_END 10
        delay_end_type = get_delay_end_type(event_log_hex)
        event_log_sub_type = delay_end_type
    elif event_log_type == 'PUMP_LIMIT_REACHED_ALARM':
        # PUMP_LIMIT_REACHED_ALARM 11
        limit_type = get_pump_limit_type(event_log_hex)
        event_log_sub_type = limit_type
    elif event_log_type == 'CLEAR_SHIFT_TOTAL':
        # CLEAR_SHIFT_TOTAL 12
        pass
    elif event_log_type == 'BATTERY':
        # BATTERY 13
        battery_status = get_battery_status(event_log_hex)
        event_log_sub_type = battery_status
    elif event_log_type == 'CASSETTE_DETACHED_ALARM':
        # CASSETTE_DETACHED_ALARM 14
        pass
    elif event_log_type == 'TIME_STAMP':
        # TIME_STAMP 15
        pass
    elif event_log_type == 'POWER_OFF':
        # POWER_OFF 16
        pass    
    elif event_log_type == 'FIRMWARE_ERROR_ALARM':
        # FIRMWARE_ERROR_ALARM 17
        firmware_error_type = get_firmware_error_type(event_log_hex)
        event_log_sub_type = firmware_error_type
    elif event_log_type == 'SYSTEM_ERROR_ALARM':
        # SYSTEM_ERROR_ALARM 18
        event_log_sub_type = get_system_error_type(event_log_hex)
    elif event_log_type == 'BATTERY_FAILURE':
        # BATTERY_FAILURE 19
        event_log_sub_type = get_battery_failure_type(event_log_hex)
    elif event_log_type == 'DEBUG':
        # DEBUG 20
        pass
    elif event_log_type == 'UNATTENDED_ALARM':
        # UNATTENDED_ALARM 21
        pass
    elif event_log_type == 'SETTING_CHANGE':
        # SETTING_CHANGE 22
        pass
    elif event_log_type == 'DOSE_FINISH':
        # DOSE_FINISH 23
        finish_dose_type = get_dose_finish_type(event_log_hex)
        event_log_sub_type = finish_dose_type
    elif event_log_type == 'POWER_ON':
        # POWER_ON 24
        battery_state = get_battery_state(event_log_hex)
        event_log_sub_type = battery_state
    elif event_log_type == 'STARTING_DOSE_SKIP':
        # STARTING_DOSE_SKIP 25
        pass
    elif event_log_type == 'SYSTEM_ERROR2_ALARM':
        # SYSTEM_ERROR2_ALARM 26
        system_error2_type = get_system_error2_type(event_log_hex)
        event_log_sub_type = system_error2_type
    elif event_log_type == 'PUMP_HARD_LIMIT_REACHED_ALARM':
        # PUMP_HARD_LIMIT_REACHED_ALARM 27
        limit_type = get_pump_hard_limit_reached_type(event_log_hex)
        event_log_sub_type = limit_type
    elif event_log_type == 'BATTERY_DEPLETED_ALARM':
        # BATTERY_DEPLETED_ALARM 28
        pass
    elif event_log_type == 'PROGRAMMING_INCOMPLETE_ALARM':
        # PROGRAMMING_INCOMPLETE_ALARM 29
        pass
    elif event_log_type == 'BATTERY_LOW_ALARM':
        # BATTERY_LOW_ALARM 30
        pass
    elif event_log_type == 'BATTERY_CHECK_STATUS':
        # BATTERY_CHECK_STATUS 31 
        event_log_sub_type = get_battery_check_status_type(event_log_hex)
    return event_log_sub_type


def get_event_log_type(event_log_hex):
    '''get event log status'''
    
    # event_log_hex[0:2] - event log id
    event_log_type_id = int(event_log_hex[0:2], 16)
    
    switcher = { 
        0: 'INFUSION_DATA',
        1: 'RUN_INFUSION',
        2: 'INFUSION_PAUSED',
        # 'INFUSION_COMPLETED'
        3: 'CASSETTE_EMPTY_ALARM',
        4: 'INFUSION_LIMIT_REACHED',
        5: 'AUTHENTICATION',
        6: 'DOSE_GRANTED',
        7: 'EXTRA_DOSE_DENIED',
        8: 'DOSE_CANCEL',
        9: 'OCCLUSION_ALARM',
       10: 'DELAY_END',
       11: 'PUMP_LIMIT_REACHED_ALARM',
       12: 'CLEAR_SHIFT_TOTAL',
       13: 'BATTERY',
       14: 'CASSETTE_DETACHED_ALARM',
       15: 'TIME_STAMP',
       # 'POWER_ON',
       16: 'POWER_OFF',
       17: 'FIRMWARE_ERROR_ALARM',
       18: 'SYSTEM_ERROR_ALARM',
       19: 'BATTERY_FAILURE',
       20: 'DEBUG',
       21: 'UNATTENDED_ALARM',
       22: 'SETTING_CHANGE',
       23: 'DOSE_FINISH',
       24: 'POWER_ON',
       25: 'STARTING_DOSE_SKIP',
       26: 'SYSTEM_ERROR2_ALARM',
       27: 'PUMP_HARD_LIMIT_REACHED_ALARM',
       28: 'BATTERY_DEPLETED_ALARM',
       29: 'PROGRAMMING_INCOMPLETE_ALARM',
       30: 'BATTERY_LOW_ALARM',
       31: 'BATTERY_CHECK_STATUS'
    } 
  
    # get() method of dictionary data type returns  
    # value of passed argument if it is present  
    # in dictionary otherwise second argument will 
    # be assigned as default value of passed argument 
    return switcher.get(event_log_type_id, "Unknown Type ({})".format(event_log_type_id)) 

  
def get_time_stamp(event_log_hex, relative_time=True):
    '''get time stamp
       input:
           event_log_hex - 16-bytes
       return:
           time stamp ("YYYY-MM-DD HH:MM:SS")
       Hex Bitmap (high - low):
            year: 6-byte
           month: 4-byte
             day: 5-byte
            hour: 5-byte
          minute: 6-byte
          second: 6-byte
    '''
    # event_log_hex[2:10] - time_stamp
    time_stamp_hex = event_log_hex[2:10]
    
    time_stamp = {'year': '1',
                  'month': '1',
                  'day': '1',
                  'hour': '1',
                  'minute': '1',
                  'second': '1'
                  }
    if relative_time:
        # The pump time is in relative format
        time_stamp_hex_little = event_log_hex[2:10].upper()
        time_stamp_int_little = int(time_stamp_hex_little, 16)
        time_stamp_int_big = struct.unpack("<I", struct.pack(">I", time_stamp_int_little))[0]
        time_stamp_hex_big = hex(time_stamp_int_big)[2:].upper().zfill(8)
        # print("time_stamp_hex_little    = 0x{0}".format(time_stamp_hex_little))
        # print('time_stamp_hex_big = 0x{0}'.format(time_stamp_hex_big))
        # [time_stamp_hex_big] is in format 'F0 00 00 00', So the first 'F' need to be removed.
        time_stamp_int = 0
        if time_stamp_hex_big[0] == '0':
            time_stamp_int = int(time_stamp_hex_big, 16)
        time_stamp_int = int('0' + time_stamp_hex_big[1:], 16)
        return time_stamp_int
    else:
        time_stamp_int = int(time_stamp_hex, 16)
        year = int((time_stamp_int & 0xFC000000) >> 26) + 2000
        time_stamp['year'] = str(year)
                    
        month = int((time_stamp_int & 0x3C00000) >> 22)
        month = str(month)
        while len(month) < 2:
            month = '0' + month
        time_stamp['month'] = month
        
        days = int((time_stamp_int & 0x3E0000) >> 17)
        days = str(days)
        while len(days) < 2:
            days = '0' + days
        time_stamp['day'] = days
        
        hours = int((time_stamp_int & 0x1F000) >> 12)
        hours = str(hours)
        while len(hours) < 2:
            hours = '0' + hours
        time_stamp['hour'] = hours
    
        minutes = int((time_stamp_int & 0xFC0) >> 6)
        minutes = str(minutes)
        while len(minutes) < 2:
            minutes = '0' + minutes
        time_stamp['minute'] = minutes
        
        seconds = time_stamp_int & 0x3F
        seconds = str(seconds)
        while len(seconds) < 2:
            seconds = '0' + seconds
        time_stamp['second'] = seconds
    return time_stamp


def parse_multiple_event_log(event_log_hex_list):
    # Parse Multiple Event Logs
    event_logs = []
    num_to_print = len(event_log_hex_list)
    print('Parsing [{}] event log...'.format(num_to_print))
    event_log_index = 0
    while len(event_logs) < num_to_print:
        if event_log_index >= num_to_print:
            break
        if event_log_hex_list[event_log_index] == "".join(['F'] * 32):
            # Ignore All 'F' lines
            event_log_index += 1
            continue
        # Rotation buffer. Pointer need to be reset when hit 0
        event_log_hex = event_log_hex_list[event_log_index]
        each_event_log = parse_event_log(event_log_hex, pump_time_offset=0)
        # print(each_event_log)
        event_logs.append(each_event_log)
        if len(event_logs) < num_to_print \
                and each_event_log['event_type'] == 'INFUSION_DATA' \
                and each_event_log['infusion_data_frame'] == 'INFUSION_DATA_BEGIN':
            print('event_type = INFUSION_DATA', end='\r')
            print('infusion_data_frame = INFUSION_DATA_BEGIN', end='\r')
            # Break, if index out of range
            if (event_log_index + 2 + 1) >= num_to_print:
                break
            # Try out the correct infusion data log size
            tentative_event_log_hex = event_log_hex_list[event_log_index + 2 + 1]
            tentative_event_log = parse_event_log(tentative_event_log_hex, pump_time_offset=0)
            # print(tentative_event_log)
            if tentative_event_log['infusion_data_frame'] == 'INFUSION_DATA_END':
                infusion_data_log_size = 2
            else:
                infusion_data_log_size = 16
            # Break, if index out of range
            if (event_log_index + infusion_data_log_size + 1) >= num_to_print:
                break
            #
            infusion_data_hex = ''
            for i in range(event_log_index + 1, event_log_index + infusion_data_log_size + 1):
                infusion_data_hex += event_log_hex_list[i]
            # print('infusion data hex = {}'.format(infusion_data_hex))
            infusion_data = parse_infusion_data_log(infusion_data_hex)
            event_logs.append(infusion_data)
            event_log_index += infusion_data_log_size
        elif each_event_log['event_type'] == 'INFUSION_DATA' and \
                each_event_log['infusion_data_frame'] == 'INFUSION_DATA_END':
            print('event_type = INFUSION_DATA', end='\r')
            print('infusion_data_frame = INFUSION_DATA_END', end='\r')
        event_log_index += 1
    return event_logs 


def parse_event_log(event_log_hex, pump_time_offset=-1):
    '''Parse Event Log
        Input:
            event_log_hex -- 32 bytes hex (16 bytes data)
            pump_time_offset -- the pump time counter value
                if it is [-1], it'll use the old way to parse the time stamp,
                otherwise, it'll use the new way to parse the time stamp. 
        Output:
            event_log_json -- event log json string
        
    '''
    event_log = {}
    event_log_type = get_event_log_type(event_log_hex)
    event_log['event_type'] = event_log_type
    if event_log_type == 'SYSTEM_ERROR2_ALARM':
        event_log['event_type'] = 'SYSTEM_ERROR_ALARM'
    if pump_time_offset == -1:
        # The pump time is in normal format
        time_stamp = get_time_stamp(event_log_hex, relative_time=False)
        time_stamp_string = time_stamp['year'] + '-' + \
                            time_stamp['month'] + '-' + \
                            time_stamp['day'] + ' ' + \
                            time_stamp['hour'] + ':' + \
                            time_stamp['minute'] + ':' + \
                            time_stamp['second']
        # print("{0:7s} = {1}".format('time', time_stamp_string))
        event_log['time'] = time_stamp_string
    else:
        # The pump time is in relative format
        time_stamp_int = get_time_stamp(event_log_hex)
        time_stamp_hex_big = hex(time_stamp_int).upper()[2:]
        if pump_time_offset >= time_stamp_int and pump_time_offset != 0:
            # [pump_time_offset] is supposed to be always greater than [time_stamp_int]
            relative_time_diff = pump_time_offset - time_stamp_int
            relative_time_diff_delta = datetime.timedelta(seconds=relative_time_diff)
            current_time = datetime.datetime.now()
            time_of_event_occur = current_time - relative_time_diff_delta
            event_log['time'] = time_of_event_occur.strftime("%Y-%m-%d %H:%M:%S") \
                                +' (0x' + time_stamp_hex_big + ' - ' + str(time_stamp_int) + ' sec)'
            if -time.timezone >= 0:
                event_log['time'] = time_of_event_occur.strftime("%Y-%m-%dT%H:%M:%S") \
                                +'+' + int_to_time_str(abs(time.timezone), 'hh:mm')\
                                +' (0x' + time_stamp_hex_big + ' - ' + str(time_stamp_int) + ' sec)'
            elif -time.timezone == 0:
                event_log['time'] = time_of_event_occur.strftime("%Y-%m-%dT%H:%M:%SZ") \
                                +' (0x' + time_stamp_hex_big + ' - ' + str(time_stamp_int) + ' sec)'
            elif -time.timezone < 0:
                event_log['time'] = time_of_event_occur.strftime("%Y-%m-%dT%H:%M:%S") \
                                +'-' + int_to_time_str(abs(time.timezone), 'hh:mm')\
                                +' (0x' + time_stamp_hex_big + ' - ' + str(time_stamp_int) + ' sec)'
        else:
            event_log['time'] = '0x' + time_stamp_hex_big + ' (' + str(time_stamp_int) + ' sec)'
    if event_log_type == 'INFUSION_DATA':
        # INFUSION_DATA 0
        infusion_data_frame = get_infusion_data_frame(event_log_hex)
        event_log['infusion_data_frame'] = infusion_data_frame
    if event_log_type == 'RUN_INFUSION':
        # RUN_INFUSION 1
        pass
    if event_log_type == 'INFUSION_PAUSED':
        # INFUSION_PAUSED 2
        pause_vinf = get_infusion_pause_vinf(event_log_hex)
        event_log['vinf (mL)'] = pause_vinf
    if event_log_type == 'CASSETTE_EMPTY_ALARM':
        # CASSETTE_EMPTY_ALARM 3
        pass
    if event_log_type == 'INFUSION_LIMIT_REACHED':
        # INFUSION_LIMIT_REACHED 4
        event_log['sub_type'] = get_event_log_sub_type(event_log_hex)
    if event_log_type == 'AUTHENTICATION':
        # AUTHENTICATION 5
        auth_code = get_authentication_code(event_log_hex)
        event_log['auth code'] = auth_code
    if event_log_type == 'DOSE_GRANTED':
        # DOSE_GRANTED 6
        event_log['sub_type'] = get_event_log_sub_type(event_log_hex)
    if event_log_type == 'EXTRA_DOSE_DENIED':
        # EXTRA_DOSE_DENIED 7
        number_of_bolus_attempted = get_bolus_attempted_number(event_log_hex)
        event_log['attempted_no.'] = number_of_bolus_attempted
    if event_log_type == 'DOSE_CANCEL':
        # DOSE_CANCEL 8
        event_log['sub_type'] = get_event_log_sub_type(event_log_hex)
        pass
    if event_log_type == 'OCCLUSION_ALARM':
        # OCCLUSION_ALARM 9
        event_log['sub_type'] = get_event_log_sub_type(event_log_hex)
    if event_log_type == 'DELAY_END':
        # DELAY_END 10
        event_log['sub_type'] = get_event_log_sub_type(event_log_hex)
    if event_log_type == 'PUMP_LIMIT_REACHED_ALARM':
        # PUMP_LIMIT_REACHED_ALARM 11
        event_log['sub_type'] = get_event_log_sub_type(event_log_hex)
        life_time = get_pump_life_time(event_log_hex)
        event_log['life_time (sec)'] = life_time
        life_volume = get_pump_life_volume(event_log_hex)
        event_log['life_volume (mL)'] = life_volume
    if event_log_type == 'CLEAR_SHIFT_TOTAL':
        # CLEAR_SHIFT_TOTAL 12
        pass
    if event_log_type == 'BATTERY':
        # BATTERY 13
        battery_status = get_battery_status(event_log_hex)
        # print('{0:7s} = {1}'.format('battery_status', battery_status))
        event_log['battery_status'] = battery_status
        #
        battery_voltage = get_eventlog_battery_voltage(event_log_hex)
        # print('{0:7s} = {1}'.format('battery_voltage (V)', battery_voltage))
        event_log['battery_voltage (V)'] = battery_voltage
        #
        battery_vinf = get_eventlog_battery_vinf(event_log_hex)
        # print('{0:7s} = {1}'.format('battery_vinf (mL)', battery_vinf))
        event_log['battery_vinf (mL)'] = battery_vinf
    if event_log_type == 'CASSETTE_DETACHED_ALARM':
        # CASSETTE_DETACHED_ALARM 14
        pass
    if event_log_type == 'TIME_STAMP':
        # TIME_STAMP 15
        pass
    if event_log_type == 'POWER_OFF':
        # POWER_OFF 16
        battery_voltage = get_eventlog_battery_voltage(event_log_hex)
        event_log['battery_voltage (V)'] = battery_voltage
        #
        battery_vinf = get_eventlog_battery_vinf(event_log_hex)
        # print('{0:7s} = {1}'.format('battery_vinf (mL)', battery_vinf))
        event_log['battery_vinf (mL)'] = battery_vinf
    if event_log_type == 'FIRMWARE_ERROR_ALARM':
        # FIRMWARE_ERROR_ALARM 17
        event_log['sub_type'] = get_event_log_sub_type(event_log_hex)
        firmware_error_file = get_firmware_error_file(event_log_hex)
        event_log['file_name'] = firmware_error_file
        firmware_error_line = get_firmware_error_line(event_log_hex)
        event_log['line_#'] = firmware_error_line
    if event_log_type == 'SYSTEM_ERROR_ALARM':
        # SYSTEM_ERROR_ALARM 18
        event_log['sub_type'] = get_event_log_sub_type(event_log_hex)
    if event_log_type == 'BATTERY_FAILURE':
        # BATTERY_FAILURE 19
        battery_failure_type = get_battery_failure_type(event_log_hex)
        event_log['battery_status'] = battery_failure_type
        #
        battery_voltage = get_eventlog_battery_voltage(event_log_hex)
        # print('{0:7s} = {1}'.format('battery_voltage (V)', battery_voltage))
        event_log['battery_voltage (V)'] = battery_voltage
        #
        battery_vinf = get_eventlog_battery_vinf(event_log_hex)
        # print('{0:7s} = {1}'.format('battery_vinf (mL)', battery_vinf))
        event_log['battery_vinf (mL)'] = battery_vinf
    if event_log_type == 'DEBUG':
        # DEBUG 20
        debug_info = get_debug_info(event_log_hex)
        event_log['debug info'] = debug_info
        debug_message_hex = event_log_hex
        event_log['message hex'] = debug_message_hex
        timer_count = get_timer_count(event_log_hex)
        event_log['timer count'] = timer_count
    if event_log_type == 'UNATTENDED_ALARM':
        # UNATTENDED_ALARM 21
        pass
    if event_log_type == 'SETTING_CHANGE':
        # SETTING_CHANGE 22
        event_log['protocol_name'] = get_protocol_name_from_index(event_log_hex)
        event_log['node_type'] = get_node_type(event_log_hex) 
        event_log['is_guards_equal_to_value'] = is_guards_equal_to_value(event_log_hex)
        event_log['parameter_index'] = get_parameter_index(event_log_hex)
        event_log['old_value'] = get_value_before_change(event_log_hex)
        event_log['new_value'] = get_value_after_change(event_log_hex)
    if event_log_type == 'DOSE_FINISH':
        # DOSE_FINISH 23
        event_log['sub_type'] = get_event_log_sub_type(event_log_hex)
        pass
    if event_log_type == 'POWER_ON':
        # POWER_ON 24
        battery_state = get_battery_state(event_log_hex)
        # print('{0:7s} = {1}'.format('battery_status', battery_status))
        event_log['battery_status'] = battery_state
        #
        event_log['battery_voltage (V)'] = get_eventlog_battery_voltage(event_log_hex)
        #
        battery_vinf = get_eventlog_battery_vinf(event_log_hex)
        # print('{0:7s} = {1}'.format('battery_vinf (mL)', battery_vinf))
        event_log['battery_vinf (mL)'] = battery_vinf
        pass
    if event_log_type == 'STARTING_DOSE_SKIP':
        # STARTING_DOSE_SKIP 25
        pass
    if event_log_type == 'SYSTEM_ERROR2_ALARM':
        # SYSTEM_ERROR2_ALARM 26
        event_log['sub_type'] = get_event_log_sub_type(event_log_hex)
    if event_log_type == 'PUMP_HARD_LIMIT_REACHED_ALARM':
        # PUMP_HARD_LIMIT_REACHED_ALARM 27
        event_log['sub_type'] = get_event_log_sub_type(event_log_hex)
        life_time = get_pump_life_time(event_log_hex)
        event_log['life_time (sec)'] = life_time
        life_volume = get_pump_life_volume(event_log_hex)
        event_log['life_volume (mL)'] = life_volume
    if event_log_type == 'BATTERY_DEPLETED_ALARM':
        # BATTERY_DEPLETED_ALARM 28
        pass
    if event_log_type == 'PROGRAMMING_INCOMPLETE_ALARM':
        # PROGRAMMING_INCOMPLETE_ALARM 29
        pass
    if event_log_type == 'BATTERY_LOW_ALARM':
        # BATTERY_LOW_ALARM 30
        pass
    if event_log_type == 'BATTERY_CHECK_STATUS':
        # BATTERY_CHECK_STATUS 31
        event_log['sub_type'] = get_event_log_sub_type(event_log_hex)
    return event_log


def get_protocol_name_from_index(event_log_hex):
    '''Get Protocol Name From Index'''
    protocol_index_hex = event_log_hex[10:11]
    protocol_index = int(protocol_index_hex, 16)
    if protocol_index == 0:
        return 'Daily 1'
    elif protocol_index == 1:
        return 'Nightly'
    elif protocol_index == 2:
        return 'Daily 2'


def get_node_type(event_log_hex):
    '''Get Node Type'''
    node_type = int(event_log_hex[11:12], 16) & 0x7
    if node_type == 0:
        return 'Value'
    elif node_type == 1:
        return 'Upper Limit'
    elif node_type == 2:
        return 'Lower Limit'


def is_guards_equal_to_value(event_log_hex):
    '''Is Guards Equal to Value'''
    is_guards_equal = int(event_log_hex[11:12], 16) & 0x8
    if is_guards_equal == 8:
        return 'Yes'
    elif is_guards_equal == 0:
        return 'No'


def get_parameter_index(event_log_hex):
    '''Get Parameter Index'''
    parameter_index = int(event_log_hex[12:14], 16)
    if parameter_index == 0:
        return 'STARTING_DOSE'
    elif parameter_index == 1:
        return 'RATE'
    elif parameter_index == 2:
        return 'EXTRA_DOSE_VOL'
    elif parameter_index == 3:
        return 'EXTRA_DOSE_LCK'
    elif parameter_index == 4:
        return 'VTBI'
    elif parameter_index == 6:
        return 'NEAR_END'
    elif parameter_index == 8:
        return 'STDOS_LCK'
    elif parameter_index == 9:
        return 'VISIBILITY'


def get_value_before_change(event_log_hex):
    '''Get Value before Change'''
    parameter_index = int(event_log_hex[12:14], 16)
    if parameter_index == 3 or parameter_index == 8:
        return int(event_log_hex[14:22], 16)
    elif parameter_index == 9:
        if int(event_log_hex[14:22], 16) == 0:
            return "VISIBLE"
        else:
            return "INVISIBLE"
    else:
        return hex_to_float(event_log_hex[14:22])


def get_value_after_change(event_log_hex):
    '''Get Value after Change'''
    parameter_index = int(event_log_hex[12:14], 16)
    if parameter_index == 3 or parameter_index == 8:
        return int(event_log_hex[22:30], 16)
    elif parameter_index == 9:
        if int(event_log_hex[22:30], 16) == 0:
            return "VISIBLE"
        else:
            return "INVISIBLE"
    else:
        return hex_to_float(event_log_hex[22:30])


def get_pump_life_time(event_log_hex):
    '''Get Pump Life Time'''
    life_time = int(event_log_hex[14:22], 16)
    return life_time


def get_pump_life_volume(event_log_hex):
    '''Get Pump Life Volume'''
    life_volume = hex_to_float(event_log_hex[22:30])
    life_volume = float("{:.1f}".format(life_volume))
    return life_volume

   
def get_protocol_name(protocol_hex):
    '''Get Protocol Name'''
    protocol_name_hex = protocol_hex[198:218]
    protocol_bytes = bytes.fromhex(protocol_name_hex)
    # trim / remove trailing null spaces from a string
    protocol_name = protocol_bytes.decode("ASCII").rstrip(' \t\r\n\0')
    return protocol_name


def get_protocol_drug_name(protocol_hex):
    '''Get Protocol Name'''
    protocol_drug_name_hex = protocol_hex[218:238]
    protocol_drug_name_bytes = bytes.fromhex(protocol_drug_name_hex)
    # trim / remove trailing null spaces from a string
    protocol_drug_name = protocol_drug_name_bytes.decode("ASCII").rstrip(' \t\r\n\0')
    if len(protocol_drug_name) == 0:
        protocol_drug_name = None
    return protocol_drug_name


def get_protocol_infusion_mode(protocol_hex):
    '''Get Infusion Mode'''
    infusion_mode_id = int(protocol_hex[186:188], 16)
    switcher = {
        0: 'continuous',
        1: 'bolus',
        2: 'intermittent'        
    }
    return switcher.get(infusion_mode_id, "Unknown Mode")

    
def get_protocol_rate_unit(protocol_hex):
    '''Get Rate Unit'''
    rate_unit = int(protocol_hex[194:196], 16)
    switcher = {
        0: 'mL/hr',
        1: 'mg/min',
        2: 'mg/kg/min',
        3: 'mcg/min',
        4: 'mcg/kg/min'
    }
    return switcher.get(rate_unit, "Unknown Unit")


def get_protocol_drug_unit(protocol_hex):
    '''Get Drug Concentration Unit'''
    drug_unit = int(protocol_hex[196:198], 16)
    switcher = {
        0: 'mg',
        1: 'mcg'
    }
    return switcher.get(drug_unit, "Unknown Unit")


def get_protocol_switches(protocol_hex):
    '''Get Switches'''
    switches_int = int(protocol_hex[160:168], 16)
    # print('switches_int = {}'.format(switches_int))
    switches = {}
    infusion_mode = get_protocol_infusion_mode(protocol_hex)
    if infusion_mode == 'continuous':
        # Continuous Mode Bit Map:
        # Rate 0
        switches['rate'] = ((switches_int >> 0) & 1) == 1
        # Vtbi 1
        switches['vtbi'] = ((switches_int >> 1) & 1) == 1
        # Loading Dose 2
        switches['loading_dose'] = ((switches_int >> 2) & 1) == 1
        # Time 3
        switches['time'] = ((switches_int >> 3) & 1) == 1
        # Delay Start 4
        switches['delay_start'] = ((switches_int >> 4) & 1) == 1
        # KVO Rate 5
        switches['kvo_rate'] = ((switches_int >> 5) & 1) == 1
        # Delay KVO Rate 6
        switches['delay_kvo_rate'] = ((switches_int >> 6) & 1) == 1
        # Concentration 7
        switches['concentration'] = ((switches_int >> 7) & 1) == 1
        # Weight 10
        switches['weight'] = ((switches_int >> 10) & 1) == 1
        # Drug Amount 22
        switches['drug_amount'] = ((switches_int >> 22) & 1) == 1
        # Dilute Volume
        switches['dilute_volume'] = False
        # Flow Rate Calibration Factor
        # switches['flow_rate_calibration_factor'] = False

    elif infusion_mode == 'bolus':
        # Bolus Mode Bit Map:
        # Basal Rate 0
        switches['basal_rate'] = ((switches_int >> 0) & 1) == 1
        # VTBI 1
        switches['vtbi'] = ((switches_int >> 1) & 1) == 1
        # Loading Dose 2
        switches['loading_dose'] = ((switches_int >> 2) & 1) == 1
        # Time 3
        switches['time'] = ((switches_int >> 3) & 1) == 1
        # Delay Start 4
        switches['delay_start'] = ((switches_int >> 4) & 1) == 1
        # Auto Bolus 5
        switches['auto_bolus'] = ((switches_int >> 5) & 1) == 1
        # Bolus Interval 6
        switches['bolus_interval'] = ((switches_int >> 6) & 1) == 1
        # Demand Bolus 7
        switches['demand_bolus'] = ((switches_int >> 7) & 1) == 1
        # Lockout Time 8
        switches['lockout_time'] = ((switches_int >> 8) & 1) == 1
        # KVO Rate 10
        switches['kvo_rate'] = ((switches_int >> 9) & 1) == 1
        # Delay KVO Rate 10
        switches['delay_kvo_rate'] = ((switches_int >> 10) & 1) == 1
        # Max Per Hour 11
        switches['max_per_hour'] = ((switches_int >> 11) & 1) == 1
        # Max Per Interval 12
        switches['max_per_interval'] = ((switches_int >> 12) & 1) == 1
        # Clinician Dose 13
        switches['clinician_dose'] = ((switches_int >> 13) & 1) == 1
        # Concentration 14
        switches['concentration'] = ((switches_int >> 14) & 1) == 1
        # Drug Amount 15
        switches['drug_amount'] = ((switches_int >> 15) & 1) == 1
        # Dilute Volume 16
        switches['dilute_volume'] = ((switches_int >> 16) & 1) == 1
        # Weight 17
        switches['weight'] = ((switches_int >> 17) & 1) == 1
        # Flow Rate Calibration Factor
        # switches['flow_rate_calibration_factor'] = False

    elif infusion_mode == 'intermittent':
        # Intermittent Mode Bit Map:
        # Dose Rate 0
        switches['dose_rate'] = ((switches_int >> 0) & 1) == 1
        # Dose VTBI 1
        switches['dose_vtbi'] = ((switches_int >> 1) & 1) == 1
        # Loading Dose 2
        switches['loading_dose'] = ((switches_int >> 2) & 1) == 1
        # Total Time 3
        switches['total_time'] = ((switches_int >> 3) & 1) == 1
        # Interval Time 4
        switches['interval_time'] = ((switches_int >> 4) & 1) == 1
        # Delay Start 5
        switches['delay_start'] = ((switches_int >> 5) & 1) == 1
        # Intermittent KVO Rate 6
        switches['intermittent_kvo_rate'] = ((switches_int >> 6) & 1) == 1
        # KVO Rate 7
        switches['kvo_rate'] = ((switches_int >> 7) & 1) == 1
        # Delay KVO Rate 8
        switches['delay_kvo_rate'] = ((switches_int >> 8) & 1) == 1        
        # Max Amount Per Hour 9
        switches['max_per_hour'] = ((switches_int >> 9) & 1) == 1        
        # Max Amount Per Interval 10
        switches['max_per_interval'] = ((switches_int >> 10) & 1) == 1
        # Concentration 11
        switches['concentration'] = ((switches_int >> 11) & 1) == 1
        # Drug Amount 12
        switches['drug_amount'] = ((switches_int >> 12) & 1) == 1
        # Dilute Volume 13
        switches['dilute_volume'] = ((switches_int >> 13) & 1) == 1
        # Weight 14
        switches['weight'] = ((switches_int >> 14) & 1) == 1
        # Flow Rate Calibration Factor
        # switches['flow_rate_calibration_factor'] = False

    return switches


def get_protocol_drug_components(protocol_hex):
    '''Get Drug Components'''
    drug_components_hex = protocol_hex[238:448]
    # print('drug_components_hex = {}'.format(drug_components_hex))
    drug_components_bytes = bytes.fromhex(drug_components_hex)
    # print('drug components = {}'.format(drug_components_bytes.decode("ASCII").rstrip(' \t\r\n\0')))
    drug_components = []
    DRUG_COMPONENT_LENGTH = 35
    DRUG_COMPONENT_NAME_LENGTH = 20
    # DRUG_COMPONENT_CONCENTRATION_LENGTH = 15
    for drug_component_index in range(3):
        name_start_index = drug_component_index * DRUG_COMPONENT_LENGTH
        name_end_index = drug_component_index * DRUG_COMPONENT_LENGTH + DRUG_COMPONENT_NAME_LENGTH
        name_bytes = drug_components_bytes[name_start_index:name_end_index]
        # print('name_bytes = {}'.format(name_bytes))
        # trim / remove trailing null spaces from a string
        name = name_bytes.decode("ASCII").rstrip(' \t\r\n\0')
        # print('name = {}'.format(name))
        #
        concentration_start_index = drug_component_index * DRUG_COMPONENT_LENGTH + \
                                    DRUG_COMPONENT_NAME_LENGTH
        concentration_end_index = (drug_component_index + 1) * DRUG_COMPONENT_LENGTH
        concentration_bytes = drug_components_bytes[concentration_start_index:concentration_end_index]
        # print('concentration_bytes = {}'.format(concentration_bytes))
        # trim / remove trailing null spaces from a string
        concentration = concentration_bytes.decode("ASCII").rstrip(' \t\r\n\0')
        # print('concentration = {}'.format(concentration))
        # [each_drug] is a local variable
        each_drug = {}
        each_drug['name'] = name
        each_drug['concentration'] = concentration
        if each_drug['name'] != '':
            drug_components.append(each_drug)
    # print('drug_components = {}'.format(drug_components))
    if len(drug_components) == 0:
        drug_components = None
    return drug_components

    
def get_protocol_union(protocol_hex):
    '''Get Protocol Union'''
    protocol_union_hex = protocol_hex[0:160]
    protocol_union_bytes = bytes.fromhex(protocol_union_hex)
    swithes = get_protocol_switches(protocol_hex)
    protocol_union = {}
    infusion_mode = get_protocol_infusion_mode(protocol_hex)
    if infusion_mode == 'continuous':
        # 0:4 Rate 4-byte Float
        protocol_union['rate'] = None
        if swithes['rate']:
            protocol_union['rate'] = struct.unpack('!f', protocol_union_bytes[0:4])[0]
            protocol_union['rate_hex'] = protocol_union_hex[0:8]
        # 4:8 VTBI 4-byte Float
        protocol_union['vtbi'] = None
        if swithes['vtbi']:
            protocol_union['vtbi'] = struct.unpack('!f', protocol_union_bytes[4:8])[0]
        # 8:12 Loading Dose 4-byte Float
        protocol_union['loading_dose'] = None
        if swithes['loading_dose']:
            protocol_union['loading_dose'] = struct.unpack('!f', protocol_union_bytes[8:12])[0]
        # 12:16 Time 4-byte int (minute)
        protocol_union['time'] = None
        if swithes['time']:
            protocol_union['time'] = int(int.from_bytes(protocol_union_bytes[12:16], 'big') / 60)
        # 16:20 Delay Start 4-byte
        protocol_union['delay_start'] = None
        if swithes['delay_start']:
            protocol_union['delay_start'] = int(int.from_bytes(protocol_union_bytes[16:20], 'big') / 60)
        # 20:24 KVO Rate 4-byte
        protocol_union['kvo_rate'] = None
        if swithes['kvo_rate']:
            protocol_union['kvo_rate'] = struct.unpack('!f', protocol_union_bytes[20:24])[0]
        # 24:28 Delay KVO Rate 4-byte
        protocol_union['delay_kvo_rate'] = None
        if swithes['delay_kvo_rate']:
            protocol_union['delay_kvo_rate'] = struct.unpack('!f', protocol_union_bytes[24:28])[0]
        # 28:32 Concentration 4-byte
        protocol_union['concentration'] = None
        if swithes['concentration']:
            protocol_union['concentration'] = struct.unpack('!f', protocol_union_bytes[28:32])[0]
        # 32:36 Drug Amount 4-byte
        protocol_union['drug_amount'] = None
        if swithes['drug_amount']:
            protocol_union['drug_amount'] = struct.unpack('!f', protocol_union_bytes[32:36])[0]
        # 36:40 Solvent Volume 4-byte
        protocol_union['dilute_volume'] = None
        if swithes['dilute_volume']:
            protocol_union['dilute_volume'] = struct.unpack('!f', protocol_union_bytes[36:40])[0]
        # 40:44 Weight 4-byte
        protocol_union['weight'] = None
        if swithes['weight']:
            protocol_union['weight'] = struct.unpack('!f', protocol_union_bytes[40:44])[0]

    if infusion_mode == 'bolus':
        # 0:4 Basal Rate 4-byte Float
        protocol_union['basal_rate'] = None
        if swithes['basal_rate']:
            protocol_union['basal_rate'] = struct.unpack('!f', protocol_union_bytes[0:4])[0]
        # 4:8 VTBI 4-byte Float
        protocol_union['vtbi'] = None
        if swithes['vtbi']:
            protocol_union['vtbi'] = struct.unpack('!f', protocol_union_bytes[4:8])[0]
        # 8:12 Loading Dose 4-byte Float
        protocol_union['loading_dose'] = None
        if swithes['loading_dose']:
            protocol_union['loading_dose'] = struct.unpack('!f', protocol_union_bytes[8:12])[0]
        # 12:16 Time 4-byte Integer (minute)
        protocol_union['time'] = None
        if swithes['time']:
            protocol_union['time'] = int(int.from_bytes(protocol_union_bytes[12:16], 'big') / 60)
        # 16:20 Delay Start 4-byte Integer
        protocol_union['delay_start'] = None
        if swithes['delay_start']:
            protocol_union['delay_start'] = int(int.from_bytes(protocol_union_bytes[16:20], 'big') / 60)
        # 20:24 Auto Bolus 4-byte Float
        protocol_union['auto_bolus'] = None
        if swithes['auto_bolus']:
            protocol_union['auto_bolus'] = struct.unpack('!f', protocol_union_bytes[20:24])[0]
        # 24:28 Auto Bolus Interval 4-byte Integer (minute)
        protocol_union['bolus_interval'] = None
        if swithes['bolus_interval']:
            protocol_union['bolus_interval'] = int(int.from_bytes(protocol_union_bytes[24:28], 'big') / 60)
        # 28:32 Demand Bolus 4-byte Float
        protocol_union['demand_bolus'] = None
        if swithes['demand_bolus']:
            protocol_union['demand_bolus'] = struct.unpack('!f', protocol_union_bytes[28:32])[0]
        # 32:36 Demand Bolus Lockout Time 4-byte Integer (minute)
        protocol_union['lockout_time'] = None
        if swithes['lockout_time']:
            protocol_union['lockout_time'] = int(int.from_bytes(protocol_union_bytes[32:36], 'big') / 60)
        # 36:40 KVO Rate 4-byte Float
        protocol_union['kvo_rate'] = None
        if swithes['kvo_rate']:
            protocol_union['kvo_rate'] = struct.unpack('!f', protocol_union_bytes[36:40])[0]
        # 40:44 Delay KVO Rate 4-byte Float        
        protocol_union['delay_kvo_rate'] = None
        if swithes['delay_kvo_rate']:
            protocol_union['delay_kvo_rate'] = struct.unpack('!f', protocol_union_bytes[40:44])[0]
        # 44:48 Max Per Hour 4-byte Float
        protocol_union['max_per_hour'] = None
        if swithes['max_per_hour']:
            protocol_union['max_per_hour'] = struct.unpack('!f', protocol_union_bytes[44:48])[0]
        # 48:52 Max Per Interval 4-byte Float
        protocol_union['max_per_interval'] = None
        if swithes['max_per_interval']:
            protocol_union['max_per_interval'] = struct.unpack('!f', protocol_union_bytes[48:52])[0]
        # 52:56 Clinician Dose 4-byte Float
        protocol_union['clinician_dose'] = None
        if swithes['clinician_dose']:
            protocol_union['clinician_dose'] = struct.unpack('!f', protocol_union_bytes[52:56])[0]
        # 56:60 Concentration 4-byte Float
        protocol_union['concentration'] = None
        if swithes['concentration']:
            protocol_union['concentration'] = struct.unpack('!f', protocol_union_bytes[56:60])[0]
        # 60:64 Drug Amount 4-byte Float
        protocol_union['drug_amount'] = None
        if swithes['drug_amount']:
            protocol_union['drug_amount'] = struct.unpack('!f', protocol_union_bytes[60:64])[0]
        # 64:68 Solvent Volume 4-byte Float
        protocol_union['dilute_volume'] = None
        if swithes['dilute_volume']:
            protocol_union['dilute_volume'] = struct.unpack('!f', protocol_union_bytes[64:68])[0]
        # 68:72 Weight 4-byte Float
        protocol_union['weight'] = None
        if swithes['weight']:
            protocol_union['weight'] = struct.unpack('!f', protocol_union_bytes[68:72])[0]

    if infusion_mode == 'intermittent':
        # 0:4 Dose Rate 4-Byte Float
        protocol_union['dose_rate'] = None
        if swithes['dose_rate']:
            protocol_union['dose_rate'] = struct.unpack('!f', protocol_union_bytes[0:4])[0]
        # 4:8 Dose VTBI 4-Byte Float
        protocol_union['dose_vtbi'] = None
        if swithes['dose_vtbi']:
            protocol_union['dose_vtbi'] = struct.unpack('!f', protocol_union_bytes[4:8])[0]
        # 8:12 Loading Dose 4-Byte Float
        protocol_union['loading_dose'] = None
        if swithes['loading_dose']:
            protocol_union['loading_dose'] = struct.unpack('!f', protocol_union_bytes[8:12])[0]
        # 12:16 Total Time 4-Byte Integer (Minute)
        protocol_union['total_time'] = None
        if swithes['total_time']:
            protocol_union['total_time'] = int(int.from_bytes(protocol_union_bytes[12:16], 'big') / 60)
        # 16:20 Interval Time 4-Byte Integer (Minute)
        protocol_union['interval_time'] = None
        if swithes['interval_time']:
            protocol_union['interval_time'] = int(int.from_bytes(protocol_union_bytes[16:20], 'big') / 60)
        # 20:24 Delay Start 4-Byte Integer (Minute)
        protocol_union['delay_start'] = None
        if swithes['delay_start']:
            protocol_union['delay_start'] = int(int.from_bytes(protocol_union_bytes[20:24], 'big') / 60)
        # 24:28 Intermittent KVO Rate 4-Byte Float
        protocol_union['intermittent_kvo_rate'] = None
        if swithes['intermittent_kvo_rate']:
            protocol_union['intermittent_kvo_rate'] = struct.unpack('!f', protocol_union_bytes[24:28])[0]
        # 28:32 KVO Rate 4-Byte Float
        protocol_union['kvo_rate'] = None
        if swithes['kvo_rate']:
            protocol_union['kvo_rate'] = struct.unpack('!f', protocol_union_bytes[28:32])[0]
        # 32:36 Delay KVO Rate 4-Byte Float
        protocol_union['delay_kvo_rate'] = None
        if swithes['delay_kvo_rate']:
            protocol_union['delay_kvo_rate'] = struct.unpack('!f', protocol_union_bytes[32:36])[0]
        # 36:40 Max Per Hour 4-Byte Float
        protocol_union['max_per_hour'] = None
        if swithes['max_per_hour']:
            protocol_union['max_per_hour'] = struct.unpack('!f', protocol_union_bytes[36:40])[0]
        # 40:44 Max Per Interval 4-Byte Float
        protocol_union['max_per_interval'] = None
        if swithes['max_per_interval']:
            protocol_union['max_per_interval'] = struct.unpack('!f', protocol_union_bytes[40:44])[0]
        # 44:48 Concentration 4-Byte Float
        protocol_union['concentration'] = None
        if swithes['concentration']:
            protocol_union['concentration'] = struct.unpack('!f', protocol_union_bytes[44:48])[0]
        # 48:52 Drug Amount  4-Byte Float
        protocol_union['drug_amount'] = None
        if swithes['drug_amount']:
            protocol_union['drug_amount'] = struct.unpack('!f', protocol_union_bytes[48:52])[0]
        # 52:56 Solvent Volume 4-Byte Float
        protocol_union['dilute_volume'] = None
        if swithes['dilute_volume']:
            protocol_union['dilute_volume'] = struct.unpack('!f', protocol_union_bytes[52:56])[0]
        # 56:60 Weight 4-Byte Float
        protocol_union['weight'] = None
        if swithes['weight']:
            protocol_union['weight'] = struct.unpack('!f', protocol_union_bytes[56:60])[0]
    return protocol_union


def parse_infusion_data_log(protocol_hex):
    '''parse infusion data log'''
    infusion_data = {}
    if len(protocol_hex) == 16 * 32:
        # ['protocol'] 0:160
        infusion_data['protocol'] = get_protocol_union(protocol_hex)
        # ['switches'] 160:168
        infusion_data['switches'] = get_protocol_switches(protocol_hex)
        # ['protocol_crc'] 168:176
        infusion_data['crc'] = protocol_hex[168:176]
        # ['auth_role'] 176:180
        infusion_data['auth_role'] = int(protocol_hex[176:180], 16)
        # ['rate_factor'] 180:184
        infusion_data['rate_factor'] = int(protocol_hex[180:184], 16)
        # ['concentration_modifiable'] 184:186
        infusion_data['concentration_modifiable'] = int(protocol_hex[184:186], 16) == int(1)
        # ['infusion_mode'] 186:188
        infusion_data['infusion_mode'] = get_protocol_infusion_mode(protocol_hex)
        # ['id'] 188:190
        infusion_data['id'] = int(protocol_hex[188:190], 16)
        # ['label_pool_id] 190:192
        infusion_data['label_pool_id'] = int(protocol_hex[190:192], 16)
        # ['label_id'] 192:194
        infusion_data['label_id'] = int(protocol_hex[192:194], 16)
        # ['rate_unit'] 194:196
        infusion_data['rate_unit'] = get_protocol_rate_unit(protocol_hex)
        # ['concentration_unit'] 196:198
        infusion_data['concentration_unit'] = get_protocol_drug_unit(protocol_hex)
        # ['name'] 198:218
        infusion_data['name'] = get_protocol_name(protocol_hex)
        # ['drug_name'] 218:238
        infusion_data['drug_name'] = get_protocol_drug_name(protocol_hex)
        # ['drug_components'] 238:448
        # infusion_data['drug_components'] = get_protocol_drug_components(protocol_hex)
        infusion_data['drug_components'] = None
        # ['protocol_index'] 448:450
        infusion_data['protocol_index'] = int(protocol_hex[448:450], 16)
        # ['view_index'] 450:452
        infusion_data['view_index'] = int(protocol_hex[450:452], 16)
        # ['label_index'] 452:454
        infusion_data['label_index'] = int(protocol_hex[452:454], 16)
    elif len(protocol_hex) == 2 * 32:
        switcher = {
            2: 'Daily 1',
            3: 'Nightly',
            4: 'Daily 2'
        }
        protocol_bytes = bytes.fromhex(protocol_hex)
        name_id = int(int.from_bytes(protocol_bytes[0:4], 'big'))
        infusion_data['name'] = switcher.get(name_id, 'Unknown_Name')
        infusion_data['cont_dose_rate'] = struct.unpack('!f', protocol_bytes[4:8])[0]
        # infusion_data['rate_hex'] = protocol_hex[0:8]
        infusion_data['vtbi'] = float('{0:.2f}'.format(struct.unpack('!f', protocol_bytes[8:12])[0]))
        infusion_data['starting_dose'] = struct.unpack('!f', protocol_bytes[12:16])[0]
        infusion_data['extra_dose'] = struct.unpack('!f', protocol_bytes[16:20])[0]
        infusion_data['extra_dose_lockout'] = int(int.from_bytes(protocol_bytes[20:24], 'big'))
        # infusion_data['db_lockout_hex'] = protocol_hex[32:40]
    else:
        infusion_data = {'content': 'empty'}
    return infusion_data


def get_send_rx_error_messge(error_code):
    '''get error message'''
    switcher = { 
        0: 'No_Error',
        1: 'SEND_RX_ERROR_UNEXPECTED_INITIALIZATION_INPUT',
        2: 'SEND_RX_ERROR_SERIAL_NUMBER',
        3: 'SEND_RX_ERROR_LIBRARY_BUILDER_LIBRARY_AUTHENTICATION',
        4: 'SEND_RX_ERROR_LIBRARY_BUILDER_PROTOCOL_CRC',
        5: 'SEND_RX_ERROR_STATE',
        6: 'SEND_RX_ERROR_DATA_INTEGRITY',
        7: 'SEND_RX_ERROR_ENCRYPTION_AUTHORIZATION',
        8: 'Unknown_Error',
    }
    # get() method of dictionary data type returns  
    # value of passed argument if it is present  
    # in dictionary otherwise second argument will 
    # be assigned as default value of passed argument 
    return switcher.get(error_code, "Unknown_Error")


def parse_key_list(key_list_str):
    '''
    parse the key list
    input:
        key_list_str - A string of key press each key press is 2-digit.
                       The first digit is the key type
                       The second digit is the key duration
    '''
    short_press_switcher = {
        _UP_KEY: 'up',
        _DOWN_KEY: 'down',
        _INFO_KEY: 'back',
        _OK_KEY: 'ok',
        _POWER_KEY: '#',
        _RUN_KEY: 'mute',
        _BOLUS_KEY: 'bolus'
    }
    long_press_switcher = {
        _UP_KEY: '#',
        _DOWN_KEY: '#',
        _INFO_KEY: 'info',
        _OK_KEY: '#',
        _POWER_KEY: '#',
        _RUN_KEY: 'run',
        _BOLUS_KEY: '#',
        _STOP_KEY: 'stop'
    }

    key_list = []
    current_key = ''
    for i in range(int(len(key_list_str) / 2)):
        key_type = key_list_str[2 * i]
        # print('key_type = {}'.format(key_type))
        key_duration = key_list_str[2 * i + 1]
        # print('key_duration = {}'.format(key_duration))
        if key_duration == _SHORT_PRESS:
            current_key = short_press_switcher.get(key_type, "Unknown Key ({})".format(key_list_str[2 * i:2 * i + 2]))
        elif key_duration == _LONG_PRESS:
            current_key = long_press_switcher.get(key_type, "Unknown Key ({})".format(key_list_str[2 * i:2 * i + 2]))
        if current_key != '':
            # print('current_key = {}'.format(current_key))
            key_list.append(current_key)
    return key_list


class Miva:
    '''Serial Communication class'''
    _CONSTANT = 0

    def __init__(self, visa_resource):
        self.library = Library()
        self.infusion = Infusion()
        self.event_log_monitor = EventLogMonitor()
        self.infusion_monitor = InfusionMonitor()
        self.protocol = None
        self.protocol_name = ''
        self.rx_path = ''
        # Create a mutex
        self.lock = Lock()
        # Serial configuration file path
        self.visa_resource_config_path = VISA_RESOURCE_CONFIG_FILE_PATH
        self.visa_resource_config = {}
        self.serial = None
        self.ip_address = None
        visa_resource = visa_resource.lower()
        if re.match(re_serial_port, visa_resource):
            s_port = visa_resource
            # Visa Resource Config data structure
            self.visa_resource_config['serial_port'] = s_port
            self.visa_resource_config['baud_rate'] = _BAUD_RATE
            self.visa_resource_config['byte_size'] = _BYTE_SIZE
            self.visa_resource_config['stop_bits'] = _STOPBITS
            self.visa_resource_config['parity'] = _PARITY
            self.visa_resource_config['flow_control'] = _FLOW_CONTROL
            self.visa_resource_config['timeout'] = _TIMEOUT
            self.visa_resource_config['write_timeout'] = _WRITE_TIMEOUT

            # self.serial = None
            # create a serial object
            print('Initializing Serial Port [{}] Connection...'.format(s_port))
            print('==')
            self.serial = serial.Serial(s_port, self.visa_resource_config['baud_rate'], \
                                        timeout=_TIMEOUT, \
                                        write_timeout=_WRITE_TIMEOUT)
            self.serial.bytesize = self.visa_resource_config['byte_size']
            self.serial.stopbits = self.visa_resource_config['stop_bits']
            self.serial.parity = self.visa_resource_config['parity']
            self.serial.xonxoff = self.visa_resource_config['flow_control']
            self.serial.rtscts = self.visa_resource_config['flow_control']
            self.serial.timeout = self.visa_resource_config['timeout']
            self.serial.write_timeout = self.visa_resource_config['write_timeout']
            print('Serial Port [{}] Connected'.format(s_port))
            print('==')
        elif re.match(re_ip_address, visa_resource): 
            self.ip_address = visa_resource
            self.socket_port = 443
            self.socket_timeout = 10 + 15
            self.socket_client = True
            # Visa Resource Config data structure
            self.visa_resource_config['ip_address'] = self.ip_address
            self.visa_resource_config['socket_port'] = self.socket_port
            self.visa_resource_config['socket_timeout'] = self.socket_timeout
        # Pump config data structure
        self.pump_config = {}
        if path.exists(PUMP_CONFIG_FILE_PATH):
            self.pump_config = load_json_file(PUMP_CONFIG_FILE_PATH)
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
        else:
            self.pump_config = create_pump_config_file(PUMP_CONFIG_FILE_PATH)
        # Pump configuration file path
        self.pump_config_path = PUMP_CONFIG_FILE_PATH
        # pump type is in ['caps', 'h', 'k']
        self.pump_type = None
        # pump time offset
        self.pump_time_offset = -1
        #
        self.socket_server = None
        # load test script
        self.script = Script()
        # load test 
        self.test = Test()
        self.test_protocol = None
        self.test_protocol_name = ''
        #
        self.checksum_symbol = '+'
    
    def run_event_log_monitor(self):
        ''' Run Event Log Monitor'''
        if self.event_log_monitor.is_on():
            print('Abort: Event log monitor already running.')
        else:
            #######################################
            # create a [event_log monitor] thread #
            #######################################
            event_log_monitor_thread = Thread(target=self.event_log_monitor.start, \
                    args=([self, self.infusion]))
            event_log_monitor_thread.start()

    def stop_event_log_monitor(self):
        ''' Stop Event Log Monitor'''
        if not self.event_log_monitor.is_on():
            print('Abort: Event log monitor is NOT running.')
        else:
            self.event_log_monitor.stop()

    def check_event_log_monitor_status(self):
        ''' Check Event Log Monitor Status'''
        status = False
        if self.event_log_monitor.is_on():
            status = True
        return status
    
    def run_infusion_monitor(self):
        ''' Run Infusion Monitor'''
        if self.infusion == None:
            print('Abort: Infusion is NOT set yet.')
            print('==')
            return
        if self.infusion_monitor.is_on():
            print('Abort: Infusion monitor already running.')
        else:
            ######################################
            # create a [infusion monitor] thread #
            ######################################
            infusion_monitor_thread = Thread(target=self.infusion_monitor.start, \
                    args=([self.infusion]))
            infusion_monitor_thread.start()
        
    def stop_infusion_monitor(self):
        ''' Stop Infusion Monitor'''
        if not self.infusion_monitor.is_on():
            print('Abort: infusion monitor is NOT running.')
        else:
            self.infusion_monitor.stop()
    
    def check_infusion_monitor_status(self):
        ''' Check Infusion Monitor Status'''
        status = False
        if self.infusion_monitor.is_on():
            status = True
        return status
    
    def run_socket_server(self):
        if self.socket_server is not None:
            if self.socket_server.is_on():
                print('Abort: Socket server already running.')
            else:
                self.socket_server.set_on() 
        else:
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            # print("IP address: {0}".format(local_ip))
            
            # HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
            HOST = local_ip
            PORT = 443  # Port to listen on (non-privileged ports are > 1023)
            self.socket_server = SocketServerSSL((HOST, PORT),
                                    SocketRequestHandlerSSL,
                                    certfile=SERVER_CERTIFICATE_PATH,
                                    keyfile=PRIVATE_KEY_PATH,
                                    miva=self)
            ######################################
            # create a [socket server] thread #
            ######################################
            socket_server_thread = Thread(target=self.socket_server.start, args=())
            socket_server_thread.daemon = True
            socket_server_thread.start()
    
    def stop_socket_server(self):
        ''' Stop Socket Server'''
        if self.socket_server is None:
            print('Abort: socket server is NOT running.')
            return
        if not self.socket_server.is_on():
            print('Abort: socket server is NOT running.')
        else:
            self.socket_server.stop()
            self.socket_server = None

    def check_socket_server_status(self):
        ''' Check Socket Server Status'''
        status = False
        if self.socket_server is None:
            return status
        if self.socket_server.is_on():
            status = True
        return status
    
    def read_single_event_log(self, index):
        '''read event log with index
            index - event log index number (data type: integer)
        '''
        # Event log index construction
        # Each page 4096 bytes, each event 16 bytes, 256 events, totally 169 pages long.
        # use [index mod (256 * 169)] to determine the real index value.
        index = int(index)
        event_log_index = hex(index % EVENT_LOG_NUMBER_OF_EVENTS)[2:].upper()
        if len(event_log_index) > 8:
            event_log_index = event_log_index[len(event_log_index) - 8:]
        elif len(event_log_index) < 8:
            while len(event_log_index) < 8:
                event_log_index = '0' + event_log_index
        return_text = self.query('RE' + event_log_index)
        print('return = {}'.format(return_text), end='\r')
        # print(len(return_text))
        if len(return_text) != 42 or return_text[0:2] != 'RE':
            return_text = ''
        return return_text
    
    def query(self, sent_text):
        '''query'''
        return_text = ''
        try:
            ############################################################################
            # #                         CRITICAL SECTION START                         ##
            #                                                                          #
    
            # Acquire Mutex
            self.lock.acquire()
            # print("lock.acquire")
            
            if self.serial != None:
                sent_message = build_message(sent_text, self.checksum_symbol)
                self.serial.write(sent_message)
                self.serial.flush()
                time.sleep(_TIMEOUT)
                if re.match(r':screen(shot)?\?', sent_text.lower()):
                    time.sleep(_TIMEOUT * 2)
                if sent_text[0:2] in ['W1', 'WN', 'WX']:
                    # Wait some time otherwise the return text will be empty
                    time.sleep(_TIMEOUT * 2)
                # trim / remove trailing NULL(0x00) spaces from a string
                return_text = self.serial.readline()
                # print('len(return_text) = {}'.format(len(return_text)))
                # print('return_text = {}'.format(return_text))
                # Check if it is raw binary data or ASCII data
                if re.match(r':screen(shot)?\?', sent_text.lower()):
                    # [:screen?] or [:screenshot?]
                    # process binary data bytes
                    # Remove STX(0x02) and ETX(0x03) and 2-byte CRC
                    return_text = return_text[1:1025]
                    # print('len(return_text) = {}'.format(len(return_text)))
                    return_text = return_text.hex().upper()
                elif re.match(re_query_screenshot_line, sent_text.lower()):
                    # [:screen:line:<line_number>?] or [:screenshot:line:<line_number>?]
                    # process binary data bytes
                    # Remove STX(0x02) and ETX(0x03) and 2-byte CRC
                    return_text = return_text[1:129]
                    # print('len(return_text) = {}'.format(len(return_text)))
                    return_text = return_text.hex().upper()
                else:
                    # Process ASCII data
                    return_text = return_text.decode(errors='ignore').rstrip(' \t\r\n\0')
                    # print('#1801 return_text = {}'.format(return_text))
                    # STX(0x02) + pay_load + 2-byte CRC + ETX(0x03)
                    # remove STX(0x02) and ETX(0x03)
                    return_text = re.sub(r'[\x00-\x1F]+', '', return_text)
                    # remove 2-byte CRC
                    return_text = return_text[:len(return_text) - 2].upper()
                # time.sleep(_TIMEOUT)
            elif self.ip_address != None:
                socket.setdefaulttimeout(self.socket_timeout)
                # create a socket object
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
                    ssl_soc = ssl.wrap_socket(soc,
                                              ca_certs=CLIENT_CERTIFICATE_PATH,
                                              cert_reqs=ssl.CERT_REQUIRED,
                                              ssl_version=ssl.PROTOCOL_TLSv1)
                    ssl_soc.connect((self.ip_address, self.socket_port))
                    sent_message = sent_text.strip(' \t\r\n\0')           
                    # print('sent_message = {}'.format(sent_message))
                    ssl_soc.sendall(sent_message.encode())
                    return_text = ssl_soc.recv(SOCKET_BUFFER_SIZE).split(b"\r\n")
                    ssl_soc.close()
                    return_text = return_text[0].decode().rstrip(' \t\r\n\0')
    
            # Release Mutex
            self.lock.release()
            # print("lock.release")
            #                                                                          #
            # #                         CRITICAL SECTION END                           ##
            ############################################################################
            return return_text
        except UnicodeDecodeError:
            print()
            print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))
            traceback.print_exc()
            self.lock.release()
            return ''
        except socket.timeout:
            # print()
            # print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))
            # traceback.print_exc()
            self.lock.release()
            return ''
        except ConnectionRefusedError:
            self.lock.release()
            # print("lock.release")
            raise
        except:
            self.lock.release()
            # print("lock.release")
            raise
    
    def write(self, sent_text):
        '''write'''
        return_text = ''
        try:
            ############################################################################
            # #                         CRITICAL SECTION START                         ##
            #                                                                          #
    
            # Acquire Mutex
            self.lock.acquire()
            # print("lock.acquire")
            
            if self.serial != None:
                sent_message = build_message(sent_text, self.checksum_symbol)
                self.serial.write(sent_message)
                self.serial.flush()
                time.sleep(_TIMEOUT)
                if sent_text[0:2] == 'W1':
                    time.sleep(_TIMEOUT * 2)
                # trim / remove trailing NULL(0x00) spaces from a string
                return_text = self.serial.readline()
                # print('len(return_text) = {}'.format(len(return_text)))
                # print('return_text = {}'.format(return_text))
                return_text = return_text.decode(errors='ignore').rstrip(' \t\r\n\0')
                # print('#1801 return_text = {}'.format(return_text))
                # STX(0x02) + pay_load + 2-byte CRC + ETX(0x03)
                # remove STX(0x02) and ETX(0x03)
                return_text = re.sub(r'[\x00-\x1F]+', '', return_text)
                # remove 2-byte CRC
                return_text = return_text[:len(return_text) - 2].upper()
                # time.sleep(_TIMEOUT)
            elif self.ip_address != None:
                socket.setdefaulttimeout(self.socket_timeout)
                # create a socket object
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
                    ssl_soc = ssl.wrap_socket(soc,
                                              ca_certs=CLIENT_CERTIFICATE_PATH,
                                              cert_reqs=ssl.CERT_REQUIRED,
                                              ssl_version=ssl.PROTOCOL_TLSv1)
                    ssl_soc.connect((self.ip_address, self.socket_port))
                    sent_message = sent_text.strip(' \t\r\n\0')           
                    # print('sent_message = {}'.format(sent_message))
                    ssl_soc.sendall(sent_message.encode())
                    return_text = ssl_soc.recv(SOCKET_BUFFER_SIZE).split(b"\r\n")
                    ssl_soc.close()
                    return_text = return_text[0].decode().rstrip(' \t\r\n\0')
            # Release Mutex
            self.lock.release()
            # print("lock.release")
            #                                                                          #
            # #                         CRITICAL SECTION END                           ##
            ############################################################################
            return return_text
        except:
            self.lock.release()
            # print("lock.release")
            raise
    
    def read(self):
        '''read'''
        return_text = ''
        try:
            ############################################################################
            # #                         CRITICAL SECTION START                         ##
            #                                                                          #
    
            # Acquire Mutex
            self.lock.acquire()
            # print("lock.acquire")
            read_limit = 10
            if self.serial != None:
                while return_text == '' and read_limit > 0:
                    # trim / remove trailing NULL(0x00) spaces from a string
                    return_text = self.serial.read_all().decode().rstrip(' \t\r\n\0')
                    read_limit = read_limit - 1
                # the first is STX(0x02) the last 3 are 2-byte CRC and ETX(0x03)
                return_text = re.sub(r'[\x00-\x1F]+', '', return_text)
                return_text = return_text[0:len(return_text) - 2].upper()
            elif self.ip_address != None:
                socket.setdefaulttimeout(self.socket_timeout)
                # create a socket object
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
                    ssl_soc = ssl.wrap_socket(soc,
                                            ca_certs=CLIENT_CERTIFICATE_PATH,
                                            cert_reqs=ssl.CERT_REQUIRED,
                                            ssl_version=ssl.PROTOCOL_TLSv1)
                    ssl_soc.connect((self.ip_address, self.socket_port))
                    while return_text == '' and read_limit > 0:
                        return_text = ssl_soc.recv(SOCKET_BUFFER_SIZE).split(b"\r\n")
                        read_limit = read_limit - 1
                    ssl_soc.close()
            return_text = re.match(r'.*((S9)([A-F0-9]{9}))', return_text)
            if return_text is not None:
                return_text = return_text[1]
            else:
                return_text = ''
            time.sleep(_TIMEOUT)
            # Release Mutex
            self.lock.release()
            # print("lock.release")
            #                                                                          #
            # #                         CRITICAL SECTION END                           ##
            ############################################################################
            return return_text
        except:
            self.lock.release()
            # print("lock.release")
            raise
    
    def read_line(self):
        '''Read Line'''
        return_text = ''
        try:
            ############################################################################
            # #                         CRITICAL SECTION START                         ##
            #                                                                          #
    
            # Acquire Mutex
            self.lock.acquire()
            # print("lock.acquire")
            while return_text == '':
                # trim / remove trailing NULL(0x00) spaces from a string
#                 return_text = self.serial.readall().decode().rstrip(' \t\r\n\0')
                return_text = self.serial.readline()
                # the first is STX(0x02) the last 3 are 2-byte CRC and ETX(0x03)
#                 return_text = re.sub(r'[\x00-\x1F]+', '', return_text)
#                 return_text = return_text[0:len(return_text) - 2].upper()
                time.sleep(_TIMEOUT)
            # Release Mutex
            self.lock.release()
            # print("lock.release")
            #                                                                          #
            # #                         CRITICAL SECTION END                           ##
            ############################################################################
            return return_text
        except:
            self.lock.release()
            # print("lock.release")
            raise
            
    def close(self):
        '''close serial port'''
        if self.serial != None:
            self.serial.close()
        
    def read_infusion_data_log(self, index, event_logs_size=EVENT_LOGS_PER_INFUSION_DATA_LOG):
        '''read infusion data log
            the infusion data log is build with [event_logs_size] event log
            each event log
        '''
        index_offset = 0
        infusion_data_log_data_hex = ''
        while index_offset < event_logs_size:
            return_text = self.read_single_event_log(index + index_offset)
            if len(return_text) == 42 and return_text[0:2] == 'RE':
                hex_event_log = return_text[10:42]
                infusion_data_log_data_hex += hex_event_log
            index_offset += 1
        if len(infusion_data_log_data_hex) != event_logs_size * 32:
            infusion_data_log_data_hex = ''
        return infusion_data_log_data_hex

    def search_event(self, event_type=''):
        '''search through the event logs for a specific event type
            return - event log hex'''
        return_event_log_hex = ''
        event_log_index = self.read_event_log_indices()        
        event_log_index_head = int(event_log_index['head'], 16)
        event_log_index_tail = int(event_log_index['tail'], 16)
        if event_log_index_tail > event_log_index_head: 
            event_log_index_head += EVENT_LOG_NUMBER_OF_EVENTS       
        #
        num_to_search = event_log_index_head - event_log_index_tail + 1
        event_logs = []
        
        if num_to_search == 0:
            print('Abort: NO event log is to be printed')
        else:
            # Update [self.pump_time_offset]
            self.read_pump_time()
            while len(event_logs) < num_to_search:
                if event_log_index_tail > event_log_index_head:
                    break
                # Rotation buffer. Pointer need to be reset when hit 0
                if event_log_index_head < 0:
                    event_log_index_head += EVENT_LOG_NUMBER_OF_EVENTS
                single_event_log = self.read_single_event_log(event_log_index_head)
                if len(single_event_log) == 42 and single_event_log[0:2] == 'RE':
                    event_log_hex = single_event_log[10:42]
                    # Get Event Log Type
                    event_log_type = get_event_log_type(event_log_hex)
                    event_log_sub_type = get_event_log_sub_type(event_log_hex)
                    if len(event_logs) < num_to_search:
                        if event_log_type != 'INFUSION_DATA':
                            event_logs.insert(0, event_log_hex)
                            if event_type in [event_log_type, event_log_sub_type]:
                                return_event_log_hex = event_log_hex
                                
                                break
                        elif event_log_type == 'INFUSION_DATA':
                            # INFUSION_DATA 0
                            if event_log_sub_type == 'INFUSION_DATA_BEGIN':
                                event_logs.insert(0, event_log_hex)
                                if event_type == event_log_sub_type:
                                    return_event_log_hex = event_log_hex
                                    break
                            elif event_log_sub_type == 'INFUSION_DATA_END':
                                event_logs.insert(0, event_log_hex)
                                if event_type == event_log_sub_type:
                                    return_event_log_hex = event_log_hex
                                    break
                                # Try out the correct infusion data log size
                                tentative_return_text = self.read_single_event_log(event_log_index_head - 2 - 1)
                                if len(tentative_return_text) == 42 and tentative_return_text[0:2] == 'RE':
                                    tentative_event_log_hex = tentative_return_text[10:42]
                                    tentative_event_log = parse_event_log(tentative_event_log_hex, self.pump_time_offset)
                                    if tentative_event_log['infusion_data_frame'] == 'INFUSION_DATA_BEGIN':
                                        infusion_data_log_size = 2
                                    else:
                                        infusion_data_log_size = 16
                                #
                                event_log_index_head -= infusion_data_log_size
                                infusion_data_hex = self.read_infusion_data_log(event_log_index_head, infusion_data_log_size)
                                event_logs.insert(0, infusion_data_hex)
                                if event_type == 'INFUSION_DATA':
                                    return_event_log_hex = infusion_data_hex
                                    break
                else:
                    print("Reading [Event Log] Failed")
                #
                event_log_index_head -= 1
            print()
        return return_event_log_hex
        
    def read_multiple_event_log(self, num_to_print=-1):
        '''Reda Multiple Event Log'''
        event_log_index = self.read_event_log_indices()        
        event_log_index_head = int(event_log_index['head'], 16)
        event_log_index_tail = int(event_log_index['tail'], 16)
        if event_log_index_tail > event_log_index_head: 
            event_log_index_head += EVENT_LOG_NUMBER_OF_EVENTS       
        #
        if num_to_print < 0:
            print('Querying [ALL] event log...')
            num_to_print = event_log_index_head - event_log_index_tail + 1
        else:
            print('Querying [{}] event log...'.format(num_to_print))
        event_logs = []
        if num_to_print == 0:
            print('Abort: NO event log is to be printed')
        else:
            # Update [self.pump_time_offset]
            self.read_pump_time()
            while len(event_logs) < num_to_print:
                if event_log_index_tail > event_log_index_head:
                    break
                # Rotation buffer. Pointer need to be reset when hit 0
                if event_log_index_head < 0:
                    event_log_index_head += EVENT_LOG_NUMBER_OF_EVENTS
                return_text = self.read_single_event_log(event_log_index_head)
                if len(return_text) == 42 and return_text[0:2] == 'RE':
                    event_log_hex = return_text[10:42]
                    each_event_log = parse_event_log(event_log_hex, self.pump_time_offset)
                    event_logs.insert(0, each_event_log)
                    if len(event_logs) < num_to_print and \
                            each_event_log['event_type'] == 'INFUSION_DATA' and \
                            each_event_log['infusion_data_frame'] == 'INFUSION_DATA_END':
                        print('event_type = INFUSION_DATA', end='\r')
                        print('infusion_data_frame = INFUSION_DATA_END', end='\r')
                        # Try out the correct infusion data log size
                        tentative_return_text = self.read_single_event_log(event_log_index_head - 2 - 1)
                        if len(tentative_return_text) == 42 and tentative_return_text[0:2] == 'RE':
                            tentative_event_log_hex = tentative_return_text[10:42]
                            tentative_event_log = parse_event_log(tentative_event_log_hex, self.pump_time_offset)
                            if tentative_event_log['infusion_data_frame'] == 'INFUSION_DATA_BEGIN':
                                infusion_data_log_size = 2
                            else:
                                infusion_data_log_size = 16
                        #
                        event_log_index_head -= infusion_data_log_size
                        infusion_data_hex = self.read_infusion_data_log(event_log_index_head, infusion_data_log_size)
                        # print('infusion data hex = {}'.format(infusion_data_hex))
                        infusion_data = parse_infusion_data_log(infusion_data_hex)
                        event_logs.insert(0, infusion_data)
                    elif each_event_log['event_type'] == 'INFUSION_DATA' and \
                            each_event_log['infusion_data_frame'] == 'INFUSION_DATA_BEGIN':
                        print('event_type = INFUSION_DATA', end='\r')
                        print('infusion_data_frame = INFUSION_DATA_BEGIN', end='\r')
                else:
                    print("Reading [Event Log] Failed at [{0}]".format(event_log_index_head))
                event_log_index_head -= 1
        return event_logs

    def read_range_event_log(self, start_index, end_index):
        number_to_print = int((EVENT_LOG_NUMBER_OF_EVENTS + end_index - start_index) \
                                % EVENT_LOG_NUMBER_OF_EVENTS)
        event_logs = []
        offset = 1
        print()
        print('start_index = {}'.format(start_index))
        print('end_index = {}'.format(end_index))
        print('number_to_print = {}'.format(number_to_print))
        # Update the [pump_time_offset] 
        self.read_pump_time()
        while offset <= number_to_print:
            index = (start_index + offset) % EVENT_LOG_NUMBER_OF_EVENTS
            return_text = self.read_single_event_log(index)
            if len(return_text) == 42 and return_text[0:2] == 'RE':
                event_log_hex = return_text[10:42]
                each_event_log = parse_event_log(event_log_hex, self.pump_time_offset)
                event_logs.append(each_event_log)
                if len(event_logs) < number_to_print and \
                        each_event_log['event_type'] == 'INFUSION_DATA' and \
                        each_event_log['infusion_data_frame'] == 'INFUSION_DATA_BEGIN':
                    # Try out the correct infusion data log size
                    tentative_return_text = self.read_single_event_log(index + 2 + 1)
                    if len(tentative_return_text) == 42 and tentative_return_text[0:2] == 'RE':
                        tentative_event_log_hex = tentative_return_text[10:42]
                        tentative_event_log = parse_event_log(tentative_event_log_hex, self.pump_time_offset)
                        if tentative_event_log['infusion_data_frame'] == 'INFUSION_DATA_END':
                            infusion_data_log_size = 2
                        else:
                            infusion_data_log_size = 16
                    #
                    print('event_type = {}'.format(each_event_log['event_type']))
                    print('infusion_data_frame = {}'.format(each_event_log['infusion_data_frame']))
                    #
                    infusion_data_hex = self.read_infusion_data_log(start_index + offset + 1, infusion_data_log_size)
                    # print('infusion data hex = {}'.format(infusion_data_hex))
                    infusion_data = parse_infusion_data_log(infusion_data_hex)
                    event_logs.append(infusion_data)
                    offset += infusion_data_log_size
                elif each_event_log['event_type'] == 'INFUSION_DATA' and \
                        each_event_log['infusion_data_frame'] == 'INFUSION_DATA_END':
                    print('event_type = {}'.format(each_event_log['event_type']))
                    print('infusion_data_frame = {}'.format(each_event_log['infusion_data_frame']))
            else:
                print("Reading [Event Log] Failed")
            offset += 1
        return event_logs 

    def read_event_log_indices(self):
        '''Read event log index'''
        # the event log start with Tail and end with Head
        # whenever a new log is generated, the Head index increases by 1
        event_log_index = {'tail': '',
                           'head': ''}
        return_text = self.query('RI')
        # print('return_text = {}'.format(return_text))
        # print('len(return_text) = {}'.format(len(return_text)))
        # return_text includes the command 'RI'
        if len(return_text) == 18 and return_text[0:2] == 'RI':
            event_log_index['tail'] = return_text[2:10]
            event_log_index['head'] = return_text[10:18]
        return event_log_index
        
    def get_pump_sn(self):
        '''Get pump serial number'''
        serial_number = ''
        
        return_text = self.query('RN')
#         print(return_text)
#         print(len(return_text))
        return_text = re.match(r'.*((RN)([A-Z0-9]{8}))', return_text)
        if return_text is not None:
            return_text = return_text[1]
        else:
            return_text = ''
        if len(return_text) == 10 and return_text[0:2] == 'RN':
            serial_number = return_text[2:10]
        return serial_number

    def set_pump_sn(self, serial_number):
        '''Set pump serial number'''
        return_text = self.query('WN' + serial_number)
        # print(len(return_text))
        status = len(return_text) == 2 and return_text[0:2] == 'WN'
        return status
    
    def disable_s9_command (self):
        '''Disable S9 command output'''
        return_text = self.query('W0' + '0')
        # print(return_text)
        # print('len(return_text) = {}'.format(len(return_text)))
        status = len(return_text) == 2 and return_text[0:2] == 'W0'
        return status
    
    def enable_s9_command (self):
        '''Enable S9 command output'''
        return_text = self.query('W0' + '1')
        # print(return_text)
        # print('len(return_text) = {}'.format(len(return_text)))
        status = len(return_text) == 2 and return_text[0:2] == 'W0'
        return status
    
    def get_motor_calibration_factor(self):
        '''Get motor calibration factor'''
        motor_calibration_factor = None
        return_text = self.query('R1')
        print(return_text)
        # print(len(return_text))
        if len(return_text) == 6 and return_text[0:2] == 'R1':
            motor_calibration_factor = int(return_text[2:], 16)
        return motor_calibration_factor
    
    def set_motor_calibration_factor(self, calibration_factor=None):
        '''Set motor calibration factor'''
        if calibration_factor is None:
            calibration_factor = input('Enter motor calibration factor (range: 1-65535, default: 4600): ')
            calibration_factor = calibration_factor.strip(' \t\r\n\0')
            if calibration_factor.isdigit() and int(calibration_factor) > 0 and int(calibration_factor) < 65536:
                calibration_factor_hex = hex(int(calibration_factor))[2:].zfill(4).upper()
                w1_command = 'W1' + calibration_factor_hex
                # print('w1_command = {}'.format(w1_command))
                return_text = self.query(w1_command)
                # print(return_text)
            else:
                calibration_factor = None
                print('Aborted: set [motor calibration factor]')
        else:
            # convert integer to hex string
            calibration_factor_hex = hex(int(calibration_factor))[2:].zfill(4).upper()
            w1_command = 'W1' + calibration_factor_hex
            print('w1_command = {}'.format(w1_command))
            return_text = self.query(w1_command)
            print(return_text)
            print('len(return_text) = '.format(len(return_text)))
        return calibration_factor
    
    def get_occlusion_thresholds(self):
        '''Get upstream and downstream thresholds of the occlusion sensor'''
        occlusion_thresholds = {}
        return_text = self.query('R2')
        print(return_text)
        # print(len(return_text))
        return_text = re.match(r'.*((R2)([A-F0-9]{8}))', return_text)
        if return_text is not None:
            return_text = return_text[1]
        else:
            return_text = ''
        if len(return_text) == 10 and return_text[0:2] == 'R2':
            occlusion_thresholds['up'] = int(return_text[2:6], 16)
            occlusion_thresholds['down'] = int(return_text[6:10], 16)
        return occlusion_thresholds

    def set_occlusion_thresholds(self, occlusion_thresholds=None):
        '''Set upstream and downstream thresholds of the occlusion sensor'''
        if occlusion_thresholds is None:
            occlusion_thresholds = {}
            print('Set [Occlusion Thresholds]')
            input('Please remove cassette from the pump first, then hit [ENTER]...')
            message = input('The cassette is removed? (y/n):')
            if message.lower().strip(' \t\r\n\0') not in ['abort', 'n', 'no', '']:
                return_text = self.query('RD')
#                 print(return_text)
                w2_command = return_text.replace("RD", "W2")
#                 print('w2_command = {}'.format(w2_command))
#                 time.sleep(_TIMEOUT * 10)
#                 w2_command = 'W2' + '00FF' + '00FF'
                return_text = self.query(w2_command)
#                 print(return_text)
#                 print('len(return_text) = '.format(len(return_text)))
#                 if len(return_text) == 10 and return_text[0:2] == 'W2':
#                     occlusion_thresholds['up'] = int(return_text[2:6], 16)
#                     occlusion_thresholds['down'] = int(return_text[6:10], 16)
                occlusion_thresholds['up'] = int(w2_command[2:6], 16)
                occlusion_thresholds['down'] = int(w2_command[6:10], 16)
            else:
                print('Aborted: set [occlusion thresholds]')
        else:
            # convert integer to hex string
            up_str = hex(occlusion_thresholds['up'])[2:].zfill(4).upper()
            down_str = hex(occlusion_thresholds['down'])[2:].zfill(4).upper()
            w2_command = 'W2' + up_str + down_str
            print('w2_command = {}'.format(w2_command))
            return_text = self.query(w2_command)
            print(return_text)
            print('len(return_text) = '.format(len(return_text)))
            if len(return_text) == 10 and return_text[0:2] == 'W2':
                occlusion_thresholds['up'] = int(return_text[2:6], 16)
                occlusion_thresholds['down'] = int(return_text[6:10], 16)
        return occlusion_thresholds

    def parse_occlusion_calibration_factors(self, rx_text):
        '''Parse the occlusion calibration factors from \
            the return text of the [RX] command
        '''
        occlusion_calibration_factors = {'up':{},
                                         'down':{},
                                         '0_6':{},
                                         '1_4':{}}
        up_k_hex = rx_text[2:10]
        up_k_float = hex_to_float(up_k_hex)
        up_k_float = round(up_k_float, 4)
        up_b_hex = rx_text[10:18]
        up_b_float = hex_to_float(up_b_hex)
        up_b_float = round(up_b_float, 4)
        down_k_hex = rx_text[18:26]
        down_k_float = hex_to_float(down_k_hex)
        down_k_float = round(down_k_float, 4)
        down_b_hex = rx_text[26:34]
        down_b_float = hex_to_float(down_b_hex)
        down_b_float = round(down_b_float, 4)
        # K, B to displacement conversion
        up_0_6_float = (1200 - up_b_float) / up_k_float
        up_1_4_float = up_0_6_float - (1200 - 550) / up_k_float
        down_0_6_float = (1200 - down_b_float) / down_k_float
        down_1_4_float = down_0_6_float - (1200 - 550) / down_k_float
        # Round to integer
        up_0_6_float = round(up_0_6_float, 0)
        up_0_6 = int(up_0_6_float)
        down_0_6_float = round(down_0_6_float, 0)
        down_0_6 = int(down_0_6_float)
        up_1_4_float = round(up_1_4_float, 0)
        up_1_4 = int(up_1_4_float)
        down_1_4_float = round(down_1_4_float, 0)
        down_1_4 = int(down_1_4_float)
        
        occlusion_calibration_factors['up']['k'] = up_k_float
        occlusion_calibration_factors['up']['b'] = up_b_float
        occlusion_calibration_factors['down']['k'] = down_k_float
        occlusion_calibration_factors['down']['b'] = down_b_float
        
        occlusion_calibration_factors['0_6']['up'] = up_0_6
        occlusion_calibration_factors['0_6']['down'] = down_0_6
        occlusion_calibration_factors['1_4']['up'] = up_1_4
        occlusion_calibration_factors['1_4']['down'] = down_1_4
        
        return occlusion_calibration_factors

    def write_calibration_factors(self, calibration_factors):
        return_text = ''
        if not isfloat(calibration_factors['0_6']['up'])\
                or not isfloat(calibration_factors['0_6']['down'])\
                or not isfloat(calibration_factors['1_4']['up'])\
                or not isfloat(calibration_factors['1_4']['down']):
            return_text = 'Invalid Parameters'
            return return_text 
        target_0_6 = 1200
        target_1_4 = 550
        up_0_6 = float(calibration_factors['0_6']['up'])
        down_0_6 = float(calibration_factors['0_6']['down'])
        up_1_4 = float(calibration_factors['1_4']['up'])
        down_1_4 = float(calibration_factors['1_4']['down'])
        # Round to integer
        up_0_6 = round(up_0_6, 0)
        up_0_6 = int(up_0_6)
        down_0_6 = round(down_0_6, 0)
        down_0_6 = int(down_0_6)
        up_1_4 = round(up_1_4, 0)
        up_1_4 = int(up_1_4)
        down_1_4 = round(down_1_4, 0)
        down_1_4 = int(down_1_4)
        
        print('up_0_6 = {}'.format(up_0_6))
        print('down_0_6 = {}'.format(down_0_6))
        print('up_1_4 = {}'.format(up_1_4))
        print('down_1_4 = {}'.format(down_1_4))
        # Calculate Upstream K and B
        up_k = (target_0_6 - target_1_4) / (up_0_6 - up_1_4)
        up_b = target_0_6 - up_k * up_0_6
        up_k = round(up_k, 4)
        up_b = round(up_b, 4)        
        # Calculate K and B
        down_k = (target_0_6 - target_1_4) / (down_0_6 - down_1_4)
        down_b = target_0_6 - down_k * down_0_6
        down_k = round(down_k, 4)
        down_b = round(down_b, 4)
        up_k_hex = float_to_hex(up_k)
        up_b_hex = float_to_hex(up_b)
        down_k_hex = float_to_hex(down_k)
        down_b_hex = float_to_hex(down_b)
        wx_cmd = 'WX' + up_k_hex + up_b_hex + down_k_hex + down_b_hex
        return_text = self.query(wx_cmd)
        return return_text
        
    def set_occlusion_calibration_factors(self):
        '''Set upstream and downstream occlusion calibration factors of the occlusion sensor'''
        return_text = ''
        rx_text = self.query('RX')
        rx_text = self.parse_occlusion_calibration_factors(rx_text)
        
        target_0_6 = 1200
        target_1_4 = 550
        enter_k_b = input('Enter K, B values? (y/n):')
        if enter_k_b.lower().strip(' \t\r\n\0') in ['yes', 'y', '']:
            # Ask User to Enter K and B
            up_k = input('Up K: ')
            if isfloat(up_k):
                up_k = float(up_k)
            else:
                up_k = round(rx_text['up']['k'], 4)
                print('Aborted: set [Up K]')
            up_b = input('Up B: ')
            if isfloat(up_b):
                up_b = float(up_b)
            else:
                up_b = round(rx_text['up']['b'], 4)
                print('Aborted: set [Up B]')
            down_k = input('Down K: ')
            if isfloat(down_k):
                down_k = float(down_k)
            else:
                down_k = round(rx_text['down']['k'], 4)
                print('Aborted: set [Down K]')
            down_b = input('Down B: ')
            if isfloat(down_b):
                down_b = float(down_b)
            else:
                down_b = round(rx_text['down']['b'], 4)
                print('Aborted: set [Down B]')
        else:
            # Ask User to Enter sensor displacement
            up_0_6 = input('Upstream 0.6 mm displacement: ')
            if isfloat(up_0_6):
                up_0_6 = float(up_0_6)
            else:
                print('Aborted: Invalid parameter')
                return return_text
            up_1_4 = input('Upstream 1.4 mm displacement: ')
            if isfloat(up_1_4):
                up_1_4 = float(up_1_4)
            else:
                print('Aborted: Invalid parameter')
                return return_text
            # Calculate Upstream K and B
            up_k = (target_0_6 - target_1_4) / (up_0_6 - up_1_4)
            up_b = target_0_6 - up_k * up_0_6
            up_k = round(up_k, 4)
            up_b = round(up_b, 4)
            down_0_6 = input('Downstream 0.6 mm displacement: ')
            if isfloat(down_0_6):
                down_0_6 = float(down_0_6)
            else:
                print('Aborted: Invalid parameter')
                return return_text
            down_1_4 = input('Downstream 1.4 mm displacement: ')
            if isfloat(down_1_4):
                down_1_4 = float(down_1_4)
            else:
                print('Aborted: Invalid parameter')
                return return_text
            # Calculate K and B
            down_k = (target_0_6 - target_1_4) / (down_0_6 - down_1_4)
            down_b = target_0_6 - down_k * down_0_6
            down_k = round(down_k, 4)
            down_b = round(down_b, 4)
            # Previous K, B
            pre_up_k = rx_text['up']['k']
            pre_up_b = rx_text['up']['b']
            pre_down_k = rx_text['down']['k']
            pre_down_b = rx_text['down']['b']
            # Incremental Calibration 
            up_k = up_k * pre_up_k
            up_b = up_b + pre_up_b
            down_k = down_k * pre_down_k
            down_b = down_b + pre_down_b
        
        # Ask User to Confirm
        result = input('Set K, B to: {}, {}, {}, {}? (y/n): '.format(up_k, up_b, down_k, down_b))
        if result.lower().strip(' \t\r\n\0') in ['yes', 'y', '']:
            up_k_hex = float_to_hex(up_k)
            up_b_hex = float_to_hex(up_b)
            down_k_hex = float_to_hex(down_k)
            down_b_hex = float_to_hex(down_b)
            wx_cmd = 'WX' + up_k_hex + up_b_hex + down_k_hex + down_b_hex
            return_text = self.query(wx_cmd)
        else:
            print('Aborted: set [Occlusion Calibration Factors]')
        return return_text

    def get_total_volume_infused(self):
        '''Get total volume infused'''
        total_volume_infused = None
        return_text = self.query('R3')
        # print(len(return_text))
        if len(return_text) == 6 and return_text[0:2] == 'R3':
            total_volume_infused = int(return_text[2:], 16) / 10
            total_volume_infused = round(total_volume_infused, 1)
        return total_volume_infused
        
    def get_battery_voltage(self):
        '''Get Battery Voltage'''
        battery_voltage = None
        return_text = self.query('R7')
        # print(len(return_text))
        if len(return_text) == 6 and return_text[0:2] == 'R7':
            # For MIVA            
            battery_voltage = int(return_text[2:], 16) / 100
        return battery_voltage

    def get_product_life_volume(self):
        '''Get Product Life Volume'''
        product_life_volume = {}
        return_text = self.query('R8')
        # print('return_text = {}'.format(return_text))
        # print(len(return_text))
        if len(return_text) == 12 and return_text[0:2] == 'R8':
            # the last 2-bytes(return_text[12:14]) are checksum bytes
            calibration_factor = int(return_text[2:6], 16)
            #
            total_rotation = int(return_text[6:12], 16)
            # 
            calibration_multiplier = 0.000005
            rmpk = calibration_factor * calibration_multiplier
            total_volume = total_rotation * rmpk 
            #
            product_life_volume['calibration'] = calibration_factor
            product_life_volume['rotation'] = total_rotation
            product_life_volume['volume'] = total_volume
        return product_life_volume
    
    def get_total_pump_on_time(self):
        '''Get total pump ON time (seconds, type = integer)'''
        return_text = self.query('R9')
        # print('return_text = {}'.format(return_text))
        # print(len(return_text))
        if len(return_text) == 10 and return_text[0:2] == 'R9':
            total_pump_on_time = int(return_text[2:10], 16)
        return total_pump_on_time

    def get_battery_calibration_and_voltage(self):
        '''Get Battery Calibration and Voltage'''
        calibration_and_voltage = {}
        return_text = self.query('RA')
        # print('return_text = {}'.format(return_text))
        # print(len(return_text))
        if len(return_text) == 10 and return_text[0:2] == 'RA':
            calibration = int(return_text[2:6], 16) / 1000
            #
            voltage = int(return_text[6:10], 16) / 100
            #
            calibration_and_voltage['calibration'] = calibration
            calibration_and_voltage['voltage'] = voltage
        return calibration_and_voltage
    
    def set_battery_calib(self, calib_factor):
        '''Set Battery Calibration Factor
           calib_factor - Calibration Factor. A float number around 1 (ex. 1.026 or 0.985)
        '''
        calib_factor = int(calib_factor * 1000)
        calib_factor_hex = hex(calib_factor)[2:].zfill(4).upper()
        return_text = self.query('WA' + calib_factor_hex)
        # print('sent_text = {}'.format('WA' + calib_factor_hex))
        print('return_text = {}'.format(return_text))
        print(len(return_text))
        status = len(return_text) == 6 and return_text[0:2] == 'WA'
        return status
    
    def get_base_year(self):
        '''Get Base Year'''
        base_year = None
        return_text = self.query('RB')
        # print('return_text = {}'.format(return_text))
        # print(len(return_text))
        if len(return_text) == 6 and return_text[0:2] == 'RB':
            # the last 2-bytes(return_text[2:6]) are checksum bytes
            base_year = int(return_text[2:6], 16)
        return base_year

    def get_library_name_version(self):
        '''Get Library Version'''
        library_name_version = {}
        return_text = self.query('RL')
        # print('return_text = {}'.format(return_text))
        # print(len(return_text))
        if len(return_text) == 22 and return_text[0:2] == 'RL':
            name_version = return_text[2:22].rstrip(' \t\r\n\0')
            library_name_version['name'] = name_version.split()[0].rstrip(' \t\r\n\0')
            library_name_version['version'] = name_version.split()[1].rstrip(' \t\r\n\0')
        return library_name_version

    def get_firmware_version(self):
        '''Get Software Version'''
        software_version = ''
        return_text = self.query('RS')
        # print(return_text)
        # print(len(return_text))
        return_text = re.match(r'.*((RS)([A-Za-z0-9\.\-]+))', return_text)
        if return_text is not None:
            return_text = return_text[1]
        else:
            return_text = ''
        if return_text[0:2] == 'RS':
            software_version = return_text[2:].rstrip(' \t\r\n\0')
        return software_version

    def send_command(self, cmd):
        '''Send [cmd] command to the pump'''
        return_text = ''
        cmd = cmd.upper().rstrip(' \t\r\n\0')
        if cmd in ['INFO']:
            # Send [INFO Key] command
            return_text = self.press_key(Key.INFO_KEY, Key.LONG_PRESS)
            if len(return_text) == 4 and return_text[0:2] == 'KE':
                print('key: Info (long)')
        elif cmd in ['BACK']:
            # Send [INFO] key command (Short)
            return_text = self.press_key(Key.INFO_KEY, Key.SHORT_PRESS)
            if len(return_text) == 4 and return_text[0:2] == 'KE':
                print('key: Back (short)')
        elif cmd in ['RUN']:
            # Send [RUN] key command
            return_status = self.trigger_run_infusion()
            if return_status:
                print('key: Run (long)')
        elif cmd in ['STOP']:
            # Send [STOP] key command
            return_status = self.trigger_stop_infusion()
            if return_status:
                print('key: Stop (long)')
        elif cmd in ['OK', 'ENTER']:
            # Send [OK] key command
            return_text = self.press_key(Key.OK_KEY, Key.SHORT_PRESS)
            if len(return_text) == 4 and return_text[0:2] == 'KE':
                print('key: Ok/Enter (short)')
        elif cmd in ['UP']:
            # Send [UP] key command
            return_text = self.press_key(Key.UP_KEY, Key.SHORT_PRESS)
            if len(return_text) == 4 and return_text[0:2] == 'KE':
                print('key: Up (short)')
        elif cmd in ['DOWN']:
            # Send [DOWN] key command
            return_text = self.press_key(Key.DOWN_KEY, Key.SHORT_PRESS)
            if len(return_text) == 4 and return_text[0:2] == 'KE':
                print('key: Down (short)')
        elif cmd in ['POWER OFF', 'POWEROFF', 'SHUT DOWN', 'SHUTDOWN', 'SHUT OFF', 'SHUTOFF', 'POWER']:
            # Send [POWER] key command
            return_text = self.trigger_power_off()
            if return_text:
                print('key: On/Off (long)')
        elif cmd in ['BOLUS']:
            # Send [BOLUS] key command
            return_text = self.press_key(Key.BOLUS_KEY, Key.SHORT_PRESS)
            if len(return_text) == 4 and return_text[0:2] == 'KE':
                print('key: Bolus (short)')
        elif cmd in ['MUTE']:
            # Send [RUN/STOP] key command
            return_text = self.press_key(Key.RUN_KEY, Key.SHORT_PRESS)
            if len(return_text) == 4 and return_text[0:2] == 'KE':
                print('key: Run/Stop (short)')
        elif re.match(r'(:)(infu(sion)?)(:)(mode)(\?)', cmd.lower()):
            # Query Infusion Mode 
            # Command -- ':INFUsion:MODE?'
            return_text = self.get_infusion_mode()
            # print(':infu:mode? == {}'.format(return_text))
        elif re.match(r'(:)(infu(sion)?)(:)(time)(\?)', cmd.lower()):
            # Query Infusion Time in Seconds? 
            # Command -- ':INFUsion:TIME?'
            return_text = self.get_infusion_time()
            # print(':infu:time? == {0} sec'.format(return_text))
            # print('type(return_text) == {0}'.format(type(return_text)))
        elif re.match(r'(:)(infu(sion)?)(:)(rate)(:)(unit)(\?)', cmd.lower()):
            # Query Infusion Rate Unit? 
            # Command -- ':INFUsion:RATE:UNIT?'
            return_text = self.get_infusion_rate_unit()
            # print(':infu:rate:unit? == {0}'.format(return_text))
        elif re.match(r'(:)(infu(sion)?)(:)(vinf)(\?)', cmd.lower()):
            # Query Infusion Volume Infused (VINF)? 
            # Command -- ':INFUsion:VINF?'
            return_text = self.get_infusion_vinf()
            # print(':infu:vinf? == {0} mL'.format(return_text))
        elif re.match(r'(:)(infu(sion)?)(:)(vtbi)(\?)', cmd.lower()):
            # Query Infusion Volume To Be Infused (VTBI)? 
            # Command -- ':INFUsion:VTBI?'
            return_text = self.get_infusion_vtbi()
            # print(':infu:vtbi? == {0} mL'.format(return_text))
        elif re.match(r'(:)(infu(sion)?)(:)(bol(us)?)(:)(run(ning)?)(\?)', cmd.lower()):
            # Query Is BOLUS Running?
            # Command -- ':INFUsion:BOLus:RUNning?'
            return_text = self.is_bolus_running()
            # print(':infu:bolus:run? == {0}'.format(return_text))
        elif re.match(r'(:)(infu(sion)?)(:)(bol(us)?)(:)(rate)(\?)', cmd.lower()):
            # Query BOLUS Rate?
            # Command -- ':INFUsion:BOLus:RATE?'
            return_text = self.get_bolus_rate()
            # print(':infu:bolus:rate? == {0}'.format(return_text))
        elif re.match(r'(:)(infu(sion)?)(:)(bol(us)?)(:)(vinf)(\?)', cmd.lower()):
            # Query BOLUS Volume Infused (VINF)? 
            # Command -- ':INFUsion:BOLus:VINF?'
            return_text = self.get_bolus_vinf()
            # print(':infu:bolus:vinf? == {0} mL'.format(return_text))
        elif re.match(r'(:)(infu(sion)?)(:)(bol(us)?)(:)(vtbi)(\?)', cmd.lower()):
            # Query BOLUS Volume To Be Infused (VTBI)? 
            # Command -- ':INFUsion:BOLus:VTBI?'
            return_text = self.get_bolus_vtbi()
            # print(':infu:bolus:vtbi? == {0} mL'.format(return_text))
        elif re.match(r'(:)(prot(ocol)?)(:)(rate)(:)(unit)(\?)', cmd.lower()):
            # Query Protocol Rate Unit? 
            # Command -- ':PROTocol:RATE:UNIT?'
            return_text = self.get_protocol_rate_unit()
            # print(':prot:rate:unit? == {0}'.format(return_text))
        elif re.match(r'(:)(prot(ocol)?)(:)(vtbi)(\?)', cmd.lower()):
            # Query Protocol Volume To Be Infused (VTBI)? 
            # Command -- ':PROTocol:VTBI?'
            return_text = self.get_protocol_vtbi()
            # print(':prot:vtbi? == {0:.2f}'.format(return_text))
        elif re.match(r'(:)(prot(ocol)?)(:)(time)(\?)', cmd.lower()):
            # Query Protocol Time in Seconds? 
            # Command -- ':PROTocol:TIME?'
            return_text = self.get_protocol_time()
            print(':prot:time? == {0} sec'.format(return_text))
        elif re.match(r'(:)(prot(ocol)?)(:)(time)(:)(unit)(\?)', cmd.lower()):
            # Query Protocol Time Unit? 
            # Command -- ':PROTocol:TIME:UNIT?'
            return_text = self.get_protocol_time_unit()
            # print(':prot:time:unit? == {0}'.format(return_text))
        elif re.match(r'(:)(prot(ocol)?)(:)(bol(us)?)(:)(rate)(\?)', cmd.lower()):
            # Query Protocol BOLUS Rate?
            # Command -- ':PROTocol:BOLus:RATE?'
            return_text = self.get_protocol_bolus_rate()
            # print(':prot:bolus:rate? == {0}'.format(return_text))
        elif re.match(r'(:)(prot(ocol)?)(:)(auto)(:)(bol(us)?)(:)(vtbi)(\?)', cmd.lower()):
            # Query Protocol Auto BOLUS Volume To Be Infused (VTBI)? 
            # Command -- ':PROTocol:AUTO:BOLus:VTBI?'
            return_text = self.get_protocol_auto_bolus_vtbi()
            if type(return_text) == float:
                print(':prot:auto:bolus:vtbi? == {0:.2f}'.format(return_text))
            else:
                print(':prot:auto:bolus:vtbi? == {0}'.format(return_text))
        elif re.match(r'(:)(prot(ocol)?)(:)(dem(and)?)(:)(bol(us)?)(:)(vtbi)(\?)', cmd.lower()):
            # Query Protocol Demand BOLUS Volume To Be Infused (VTBI)? 
            # Command -- ':PROTocol:DEMand:BOLus:VTBI?'
            return_text = self.get_protocol_demand_bolus_vtbi()
            if type(return_text) == float:
                print(':prot:demand:bolus:vtbi? == {0:.2f}'.format(return_text))
            else:
                print(':prot:demand:bolus:vtbi? == {0}'.format(return_text))
        elif re.match(r'(:)(power)', cmd.lower()):
            # Send [POWER] key command
            return_status = self.trigger_power_off()
            if return_status:
                print('key: On/Off (long)')
        elif re.match(re_query_event_timestamp, cmd.lower()):
            # Query time stamp of certain event in the event log
            # Command -- ':TIMEstamp:{event_type}?'
            re_match_result = re.match(re_query_event_timestamp, cmd.lower())
            event_type = re_match_result[5]
            event_type = event_type.upper()
            print('search for [{}]'.format(event_type))
            event_log_hex = self.search_event(event_type)
            time_stamp_int = None
            if len(event_log_hex) == 32:
                time_stamp_int = get_time_stamp(event_log_hex)
            # print()
            # print(time_stamp_int)            
            return_text = time_stamp_int
        elif re.match(re_search_for_event, cmd.lower()):
            # Search for certain event in the event log
            # Command -- ':EVENTlog:{event_type}?'
            re_match_result = re.match(re_search_for_event, cmd.lower())
            event_type = re_match_result[5]
            event_type = event_type.upper()
            print('Search for [{}]'.format(event_type))
            event_log_hex = self.search_event(event_type)
            event_log = {}
            if len(event_log_hex) == 32:
                event_log = parse_event_log(event_log_hex, self.pump_time_offset)
            elif len(event_log_hex) == 16 * 32:
                event_log = parse_infusion_data_log(event_log_hex)
            elif len(event_log_hex) == 2 * 32:
                event_log = parse_infusion_data_log(event_log_hex)
            # print()
            # print('{0} == {1}'.format(cmd, event_log_json))
            return_text = event_log
        elif re.match(re_query_event_list, cmd.lower()):
            # Query Event Log List
            # Command -- ':EVENTlog:{number_to_query}?'
            re_match_result = re.match(re_query_event_list, cmd.lower())
            num_to_query = int(re_match_result[5])
            return_text = self.get_eventlog_list(num_to_query)
            print(':event:{0}? == {1}'.format(num_to_query, return_text))
        elif re.match(re_get_key_list, cmd.lower()):
            # Get key press list from the pump 
            # Command -- ':KEY:LIST?'
            re_match_result = re.match(re_get_key_list, cmd.lower())
            sent_text = ':KEY:LIST?'
            return_text = self.query(sent_text)
            raw_key_lsit = []
            for i in range(int(len(return_text) / 2)):
                raw_key_lsit.append(return_text[2 * i:2 * i + 2])
            print('len = {}'.format(len(raw_key_lsit)))
            print('{}'.format(raw_key_lsit))
            key_list = parse_key_list(return_text)
            return_text = key_list
            print('{0} == {1}'.format(cmd.upper(), return_text))
        elif re.match(re_scpi_common_cmd, cmd.lower()):
            # SCPI common commands, such as:
            # *idn?
            return_text = self.query(cmd.upper())
            # print('type(return_text) == {}'.format(type(return_text)))
            # print('len(return_text) == {}'.format(len(return_text)))
            if return_text == 'TRUE':
                # Check for True
                return_text = True
            elif return_text == 'FALSE':
                # Check for False
                return_text = False
        elif re.match(re_scpi_get_cmd, cmd.lower()):
            # SCPI get commands, such as:
            # :protocol:rate?
            # :key:list?
            # :screen?
            return_text = self.query(cmd.upper())
            # print('type(return_text) == {}'.format(type(return_text)))
            # print('len(return_text) == {}'.format(len(return_text)))
            if return_text.isdigit() and not re.match(r':screen(shot)?:line:[0-8]\?', cmd.lower()):
                # Check for Integer
                return_text = int(return_text)            
            elif isfloat(return_text) and not re.match(r':screen(shot)?:line:[0-8]\?', cmd.lower()):
                # Check for Float
                return_text = float(return_text)
            elif return_text == 'TRUE':
                # Check for True
                return_text = True
            elif return_text == 'FALSE':
                # Check for False
                return_text = False
            elif re.match(r':serv(ice)?:time\?', cmd.lower()):
                # Total Infusion Run Time
                return_text = int(return_text, 16)
            elif re.match(r':total:time\?', cmd.lower()):
                # Total Pump On Time
                return_text = int(return_text, 16)
        elif re.match(re_scpi_set_cmd, cmd.lower()):
            # SCPI set commands, such as:
            # :protocol:rate 20.0
            # :key:list:clear
            return_text = self.query(cmd.upper())
            print(cmd.upper())
        return return_text

    def press_key(self, key_type, key_duration):
        '''Simulate [key_type] key [duration] press'''        
        key_command = "KE" + key_type + key_duration
        print('{0:6s} : {1}'.format('sent', key_command))
        return_text = self.query(key_command)
        # print('{0:6s} : {1}'.format('return', return_text))
        # if len(return_text) == 4 and return_text[0:2] == 'KE':
            # print('[KE] command succeed')
        # else:
            # print('[KE] command failed!')
        return return_text

    def send_rx_initialize(self, rx):
        '''Send Rx Initialization [LI] command'''
        result = True
        error_code = ''

        # get pump serial number (8-digit ASCII string) Ex.: SN800008
        pump_sn = rx.get_pump_sn().zfill(8)
        print('{0:11s} = {1}'.format('pump sn', pump_sn))
        # convert ASCII string to Hex string (16-digit Hex string) Ex.: 534E383030303038
        pump_sn_hex = binascii.hexlify(pump_sn.encode()).decode()
        print('{0:11s} = {1}'.format('pump sn hex', pump_sn_hex))
        # library CRC (8-digit Hex string) Ex.: 6B6B8B66
        library_crc = rx.get_library_crc().zfill(8)
        print('{0:11s} = {1}'.format('lib crc', library_crc))
        # library number (integer) Ex.: 318
        library_number = rx.get_library_number()
        print('{0:11s} = {1}'.format('lib num', library_number))
        # convert integer to hex string (8 digit hex string) Ex.: 0000013E
        library_number_hex = hex(library_number)[2:].zfill(8)
        print('{0:11s} = {1}'.format('lib num hex', library_number_hex))
        # build [LI] command Ex.: LI534E3830303030386B6B8B660000013E
        li_command = 'LI' + pump_sn_hex + library_crc + library_number_hex
        print("{0:6s} : {1}".format('sent', li_command))
        return_text = self.query(li_command)
        print('{0:6s} : {1}'.format('return', return_text))
        # print(len(return_text))
        if len(return_text) == 3 and return_text[0:2] == 'LI':
            error_code = return_text[2:3]
        if error_code != '0':
            print('[LI] command error: {}'.format(error_code))
            result = False
        else:
            print('[LI] command succeed')
        return result

    def send_rx_confirm(self, rx):
        '''Send Rx Confirmation [LC] command'''
        result = True
        error_code = ''
        pump_sn = rx.get_pump_sn().zfill(8)
        send_rx_hex = rx.get_rx_hex()
        # Calculate the SendRx CRC (4 bytes integer)
        send_rx_crc = crc32c(0, send_rx_hex)
        message_bytes = pump_sn.encode() + send_rx_crc.to_bytes(4, 'big') + b'0000'
        # If AES is enabled (CAPS) pumps
        cipher = AES.new(_ENCRYPTION_KEY, AES.MODE_ECB)
        encrypted_data = cipher.encrypt(message_bytes).hex().upper()
        # build [LC] command
        # lc_command = 'LC' + 'aa3632d2c477926ee186bb2994121f88'
        # lc_command = 'LC' + 'db991d410b14b983981ea045bd9e0494'
        lc_command = 'LC' + encrypted_data        
        print("{0:6s} : {1}".format('sent', lc_command))
        return_text = self.query(lc_command)
        print('{0:6s} : {1}'.format('return', return_text))
        # print(len(return_text))
        if len(return_text) == 3 and return_text[0:2] == 'LC':
            # the last 2-bytes(return_text[3:5]) are checksum bytes
            error_code = return_text[2:3]
        if error_code != '0':
            error_messge = get_send_rx_error_messge(error_code)
            print('[LC] command error: [{0}] {1}'.format(error_code, error_messge))
            result = False
        else:
            print('[LC] command succeed')
        return result

    def send_rx_protocol(self, rx):
        '''Send Rx Protocol [LS] command'''
        result = True
        print('buidling sendrx hex from protocol: [{}]'.format(rx.protocol['content']['name']))
        send_rx_hex = rx.get_rx_hex()
        print(send_rx_hex.lower())
        send_rx_hex_len = len(send_rx_hex)
        block_size = 128
        for i in range(int(send_rx_hex_len / block_size)):
            index = hex(i)[2:].zfill(8).upper()
            # build [LS] command
            ls_command = 'LS' + index + send_rx_hex[i * block_size: (i + 1) * block_size]
            print("{0:6s} : {1}".format('sent', ls_command))
            return_text = self.query(ls_command)
            print('{0:6s} : {1}'.format('return', return_text))
            # print(len(return_text))
            if len(return_text) == 10 and return_text[0:2] == 'LS':
                print('[LS] command succeed')
            else:
                print('[LS] command error:')
                result = False
        return result

    def send_rx(self, rx_path):
        '''Write SendRx consist of sending three commands:
           [LI] Command: Rx Initialization
           [LS] Command: Rx Protocol
           [LC] Command: Rx Confirmation
        '''
        try:
            result = True
            # Send [INFO Key] command
            # to bring the pump to the [STANDBY] State
            self.press_key(_INFO_KEY, _SHORT_PRESS)
            time.sleep(_TIMEOUT * 10)
            self.press_key(_INFO_KEY, _SHORT_PRESS)
            time.sleep(_TIMEOUT * 10)
            
            rx = SendRx()
            rx.load(rx_path)
            
            if self.infusion.patient_weight is not None:
                rx.weight = self.infusion.patient_weight

            # Send [LI] command
            result = self.send_rx_initialize(rx)

            # Send [LS] command
            result = self.send_rx_protocol(rx)

            # Send [LC] command
            result = self.send_rx_confirm(rx)

            return result
        except KeyError:
            pass
        except (OSError, serial.SerialException):
            raise

    def save_rx(self, rx):
        # Build Rx Path        
        protocol_name = rx['sendRxProtocol']['content']['name'].strip(' \t\r\n\0')
        protocol_id = str(rx['sendRxProtocol']['id'])
        time_stamp = str(int(time.time() * 1000))
        # replace '\' or '/' or ' ' character to '' or '_' in the [protocol_name]
        protocol_name = protocol_name.replace('\\', '')
        protocol_name = protocol_name.replace('/', '')
        protocol_name = protocol_name.replace(' ', '_')
        #
        rx_path = 'Rx-[' + protocol_name + ']-[' + protocol_id + ']@' + time_stamp + '.json'
        #
        # convert Python Dict to JSON:
        rx_json = json.dumps(rx, indent=4)
        # Save to json file
        file = open(rx_path, "w")
        file.write(rx_json)
        file.close()
        return rx_path

    def generate_rx(self, protocol):
        print('Generating Rx...')
        print()        
        library = self.library
        protocol_name = protocol['content']['name']        
        # Create an Rx
        rx = {"serialNumber": "", \
              "libraryCrc": "", \
              "libraryNumber": "", \
              "protocolIndex": "", \
              "viewIndex": "", \
              "labelIndex": "", \
              "sendRxProtocol": ""
              }
        # Get Pump Serial Number
        pump_serial_number = self.get_pump_sn()
        if pump_serial_number != '':
            print('    S/N: {}'.format(pump_serial_number))
            rx['serialNumber'] = pump_serial_number
        else: 
            print('Error: get serial number failed')
        # Get Library CRC
        rx['libraryCrc'] = library.get_library_crc()
        print('    Library CRC: {}'.format(rx['libraryCrc']))
        # Get Library Number
        rx['libraryNumber'] = library.get_library_id()
        print('    Library Number: {}'.format(rx['libraryNumber']))
        # Get Protocol Index
        rx['protocolIndex'] = str(library.get_protocol_index(protocol_name))
        print('    Protocol Index: {}'.format(rx['protocolIndex']))
        # Get View Index
        rx['viewIndex'] = library.get_protocol_view_index(protocol_name)
        print('    View Index: {}'.format(rx['viewIndex']))
        # Get Label Index
        rx['labelIndex'] = library.get_protocol_label_set_index(protocol_name)
        print('    Label Index: {}'.format(rx['labelIndex']))
        # Get SendRx Protocol
        rx['sendRxProtocol'] = protocol
        # Save Rx
        rx_path = self.save_rx(rx)
        print()
        print('Rx is saved as [{}]'.format(rx_path))
        return rx_path

    def send_library_begin(self):
        '''Send Library Begin [LB] Command'''
        result = True
        return_text = self.query('LB')
        print('{0:6s} : {1}'.format('return', return_text))
        if len(return_text) == 2 and return_text[0:2] == 'LB':
            print('[LB] command succeed')
        else:
            print('[LB] command failed!')
            result = False
        return result

    def send_library_erase(self):
        '''Send Library Erase [LE] Command'''
        result = True
        library_block_begin_index = 64
        library_block_end_index = 1152
        # library_buffer_size = (block_end_index - block_begin_index) * block_size
        # (1152-64) * 64 = 69632 Bytes
        # library_buffer_size = 69632

        # each block is 64 bytes        
        blocks_per_page = 64

        # The library [Block] range is : [64:1152]
        # The library [Page] range is : [1:18] totally 17 pages
        # This step is necessary for writing the library
        library_page_begin_index = int(library_block_begin_index / blocks_per_page)
        library_page_end_index = int(library_block_end_index / blocks_per_page)
        for page_index in range(library_page_begin_index, library_page_end_index):
            page_index = hex(page_index)[2:].zfill(8).upper()
            le_command = 'LE' + page_index
            print(le_command)
            return_text = self.query(le_command)
            print('{0:6s} : {1}'.format('return', return_text))
            if len(return_text) == 10 and return_text[0:2] == 'LE':
                print('[LE] command succeed')
            else:
                print('[LE] command failed!')
                result = False
        return result

    def send_library_write(self, library):
        '''Send Library write [LW] Command'''
        result = True
        library_block_begin_index = 64
        library_block_end_index = 1152
        block_size = 64
        #
        library_bytes = library.get_library_bytes()
        library_hex = library_bytes.hex().upper()
        # The library Block range is : [64:1152]
        # The library Block size should be [1152 - 64 = 1088]
        total_blocks = library_block_end_index - library_block_begin_index
        for i in range(total_blocks):
            # Check to see if the whole block is all [FF]
            # If the whole block is all FF then don't calculate the checksum for the block
            # And do not send the block to the pump in order to save time
            all_empty_bytes = True
            for each_byte in library_bytes[i * block_size:(i + 1) * block_size]:
                if each_byte != 0xFF:
                    all_empty_bytes = False
                    break
            if (not all_empty_bytes):
                # Block Index construction
                block_index = hex(i + library_block_begin_index)[2:].zfill(8).upper()
                # Write library block command construction
                lw_command = "LW" + block_index + \
                                library_hex[block_size * 2 * i: block_size * 2 * (i + 1)]
                print('{0:6s} : {1}'.format('sent', lw_command))
                return_text = self.query(lw_command)
                print('{0:6s} : {1}'.format('return', return_text[:len(return_text) - 2]))
                if len(return_text) == 10 and return_text[0:2] == 'LW':
                    print('[LW] command succeed')
                else:
                    print('[LW] command failed!')
                    result = False
        return result

    def send_library_authorize(self, library):
        '''Send Library Authorize [LA] Commnad'''
        result = True
        pump_sn = self.get_pump_sn().zfill(8)
        library_bytes = library.get_library_bytes()
        # Calculate the [Send Library CRC] (4 bytes integer)
        library_crc = get_send_library_crc(library_bytes)
        print("calculated crc is", library_crc)
        message_bytes = pump_sn.encode() + library_crc.to_bytes(4, 'big') + b'0000'
        cipher = AES.new(_ENCRYPTION_KEY, AES.MODE_ECB)
        # If AES is enabled (CAPS pumps)
        encrypted_data = cipher.encrypt(message_bytes).hex().upper()
        # If AES is NOT enabled (v6.1 pumps)
        # encrypted_data = library_crc.to_bytes(4, 'big')
        # encrypted_data = hex(library_crc)[2:].zfill(8).upper()
        print(encrypted_data)
        # build [LA] command   
        # la_command = 'LA' + 'C81CE4255C2FA5B92B03D76DF43CB1E1'
        la_command = 'LA' + encrypted_data
        print("{0:6s} : {1}".format('sent', la_command))
        return_text = self.query(la_command)
        print('{0:6s} : {1}'.format('return', return_text[:len(return_text)]))
        if len(return_text) == 2 and return_text[0:2] == 'LA':
            print('[LA] command succeed')
        else:
            result = False
            print('[LA] command failed!')
        return result
        
    def send_library_reset(self):
        '''Send Library Reset [LR] Commnad'''
        result = True
        return_text = self.query('LR')
        print('{0:6s} : {1}'.format('return', return_text[:len(return_text) - 2]))
        if len(return_text) == 2 and return_text[0:2] == 'LR':
            print('[LR] command succeed')
        else:
            print('[LR] command failed!')
            result = False
        return result

    def send_library(self, library_path):
        '''Send Library consist of sending three commands:
           [LB] Command: Library Begin
           [LE] Command: Library Erase
           [LW] Command: Library Write
           [LA] Command: Library Authorize
           [LR] Command: Library Reset
        '''        
        self.library = Library()
        library = self.library
        library.load(library_path)
        # Send [LB] command
        result = self.send_library_begin()
        # Send [LE] command
        result = result and self.send_library_erase()
        # Send [LW] command
        result = result and self.send_library_write(library)
        # Send [LA] command
        result = result and self.send_library_authorize(library)
        # Send [LR] command
        result = result and self.send_library_reset()
        if result:
            time.sleep(3)
            return_text = self.press_key(_POWER_KEY, _LONG_PRESS)
            if len(return_text) == 4 and return_text[0:2] == 'KE':
                print('key: On/Off (long)')
            
        return result
    
    def input_digits(self, digits_str):
        '''Input Number (on the pump)'''
        # print('Input Digits [{}]...'.format(digits_str))
        # time.sleep(_TIMEOUT * 2)
        # Input Digits
        for index in range(len(digits_str)):
            digit = int(digits_str[index])
            if digit > 5:
                while digit < 10:
                    self.press_key(_DOWN_KEY, _SHORT_PRESS)
                    print('key: Down (short)')
                    time.sleep(_TIMEOUT * 2)
                    digit += 1
            else: 
                while digit > 0:
                    self.press_key(_UP_KEY, _SHORT_PRESS)
                    print('key: Up (short)')
                    time.sleep(_TIMEOUT * 2)
                    digit -= 1
            self.press_key(_OK_KEY, _SHORT_PRESS)
            print('key: Ok (short)')
            time.sleep(_TIMEOUT * 2)
        
    def write_aes_encrypt_key(self, old_key, new_key):
        '''Write AES Encryption Key [WK] command'''
        # Combine old key and new key into the command
        if len(old_key) != 64  or len(new_key) != 64:
            return ""
        old_key_bytes = bytes.fromhex(old_key)
        new_key_bytes = bytes.fromhex(new_key)
        message = old_key_bytes
        message += new_key_bytes
        # Encrypt the command and prepare to send
        cipher = AES.new(old_key_bytes, AES.MODE_ECB)
        encrypted_text = cipher.encrypt(message).hex()
        return_text = self.query('WK' + encrypted_text)
        print(return_text)
        return return_text

    def read_pump_time(self):
        '''Read Pump Time'''
        pump_time = ''
        return_text = self.query('RC')
        # print(return_text)
        # print(len(return_text))
        if len(return_text) == 14 and return_text[0:2] == 'RC':
            # Normal time stamp, need to be interpreted
            pump_time = return_text[2:14]
        elif len(return_text) == 10 and return_text[0:2] == 'RC':
            # Relative time since firmware download (4-byte integer represented in 8-byte Hex)
            pump_time = return_text[2:10]
            # [pump_time] is in format 'F0 00 00 00', So the first 'F' need to be removed.
            self.pump_time_offset = int('0' + pump_time[1:], 16)
        return pump_time
        
    def get_occlusion_sensor(self):
        '''Read Pump Occlusion Sensor Values'''
        occlusion_sensor = {}
        return_text = self.query('RD')
        # print(return_text)
        # print(len(return_text))
        if len(return_text) == 10 and return_text[0:2] == 'RD':
            up_stream = int(return_text[2:6], 16)
            down_stream = int(return_text[6:10], 16)
            occlusion_sensor['up'] = up_stream
            occlusion_sensor['down'] = down_stream
        return occlusion_sensor
    
    def get_all_sensor(self):
        '''Read Pump Motor Sensor Values'''
        sensor = {}
        return_text = self.query('S9')
        print(return_text)
        # print(len(return_text))
        return_text = re.match(r'.*((S9)([A-F0-9]{9}))', return_text)
        if return_text is not None:
            return_text = return_text[1]
        else:
            return_text = ''
        if len(return_text) == 11 and return_text[0:2] == 'S9':
            hall_effect_sensor = int(bin(int(return_text[2], 16) & 0x8)[2]) 
            motor_running = int(bin(int(return_text[2], 16) & 0x4)[2])
            up_stream = int(return_text[2:5], 16) & 0x3FF
            down_stream = int(return_text[6:8], 16)
            battery_voltage = int(return_text[8:11], 16) / 100
            sensor['up'] = up_stream
            sensor['down'] = down_stream
            sensor['system'] = hall_effect_sensor
            sensor['motor_running'] = motor_running
            sensor['battery_voltage'] = battery_voltage
        return sensor
    
    def write_pump_time(self, time_stamp=None):
        '''Write Pump Time
        input: 
            time_stamp - [YYYY-MM-DD hh:mm:ss]
        output:
            status - [True | False]
            
        '''
        status = False
        if time_stamp == None:
            current_datetime = datetime.datetime.now()
            day = hex(current_datetime.day)[2:].zfill(2)
            month = hex(current_datetime.month)[2:].zfill(2)
            year = hex(current_datetime.year - 2000)[2:].zfill(2)
            hour = hex(current_datetime.hour)[2:].zfill(2)
            minute = hex(current_datetime.minute)[2:].zfill(2)
            second = hex(current_datetime.second)[2:].zfill(2)
            wc_command = 'WC' + day + month + year + hour + minute + second
            return_text = self.query(wc_command)
            # print(return_text)
            # print(len(return_text))
            status = (len(return_text) == 2 and return_text[0:2] == 'WC')
        else:
            day = hex(int(time_stamp[8:10]))[2:].zfill(2)
            month = hex(int(time_stamp[5:7]))[2:].zfill(2)
            year = hex(int(time_stamp[:4]) - 2000)[2:].zfill(2)
            hour = hex(int(time_stamp[11:13]))[2:].zfill(2)
            minute = hex(int(time_stamp[14:16]))[2:].zfill(2)
            second = hex(int(time_stamp[17:19]))[2:].zfill(2)
            wc_command = 'WC' + day + month + year + hour + minute + second
            return_text = self.query(wc_command)
            # print(return_text)
            # print(len(return_text))
            status = (len(return_text) == 2 and return_text[0:2] == 'WC')
        return status

    def reset_pump(self):
        '''Reset Pump Service Total VINF and Total Infusion Time
            need to restart the pump and verify from the info menu
        '''
        return_text = self.query('WR')
        # print(return_text)
        # print(len(return_text))
        status = (len(return_text) == 2 and return_text[0:2] == 'WR')
        return status

    def read_platform(self):
        '''read pump platform ('H' or 'K')'''
        platform = 'C'
        return_text = self.query('RM')
        if len(return_text) == 4 and return_text[0:2] == 'RM':
            if return_text[2:] == '00':
                platform = 'H'
            elif return_text[2:] == '01':
                platform = 'K'
        return platform

    def write_platform(self, platform):
        '''write pump platform'''
        status = True
        platform = platform.upper().strip(' \t\r\n\0')
        if platform in ['H', 'K']:
            if platform == 'H':
                sent_text = 'WM00'
            else:
                sent_text = 'WM01'
            return_text = self.query(sent_text)
            if len(return_text) == 4 and return_text[0:2] == 'WM':
                print('Pump platform is set to: {0} ({1})'.format(platform, return_text[2:4]))
        else:
            status = False
            print('Abort: unkown platform: {}'.format(platform))
        return status

    #===================

    def get_infusion_mode(self):
        infusion_mode = ''
        return_text = self.query('Q0')
        if return_text[0:2] == 'Q0':
            infusion_mode = return_text[2:]
        return infusion_mode
    
    # def is_infusion_running(self):
    #     is_infusion_running = False
    #     return_text = self.query('Q1')
    #     if return_text[0:2] == 'Q1':
    #         if return_text[2:] == '1':
    #             is_infusion_running = True
    #     return is_infusion_running

    # def get_infusion_rate(self):
    #     infusion_rate = -1
    #     return_text = self.query('Q2')
    #     if return_text[0:2] == 'Q2':
    #         infusion_rate = int(return_text[2:], 16) / 100
    #     return infusion_rate

    def get_infusion_time(self):
        infusion_time = -1
        return_text = self.query('Q3')
        if return_text[0:2] == 'Q3':
            # print(return_text)
            infusion_time = int(return_text[2:], 16)
        return infusion_time
    
    def get_infusion_rate_unit(self):
        infusion_rate_unit = ''
        return_text = self.query('Q4')
        if return_text[0:2] == 'Q4':
            # print(return_text)
            infusion_rate_unit = return_text[2:]
        return infusion_rate_unit
    
    def get_infusion_vinf(self):
        infusion_vinf = -1
        return_text = self.query('Q5')
        if return_text[0:2] == 'Q5':
            infusion_vinf = int(return_text[2:], 16) / 100
        return infusion_vinf

    def get_infusion_vtbi(self):
        infusion_vtbi = -1
        return_text = self.query('Q6')
        if return_text[0:2] == 'Q6':
            infusion_vtbi = int(return_text[2:], 16) / 100
        return infusion_vtbi

    def is_bolus_running(self):
        is_bolus_running = False
        return_text = self.query('Q7')
        if return_text[0:2] == 'Q7':
            if return_text[2:] == '1':
                is_bolus_running = True
        return is_bolus_running
    
    def get_bolus_rate(self):
        bolus_rate = -1
        return_text = self.query('Q8')
        if return_text[0:2] == 'Q8':
            bolus_rate = int(return_text[2:], 16) / 100
        return bolus_rate
    
    def get_bolus_vinf(self):
        bolus_vinf = -1
        return_text = self.query('Q9')
        if return_text[0:2] == 'Q9':
            bolus_vinf = int(return_text[2:], 16) / 100
        return bolus_vinf
    
    def get_bolus_vtbi(self):
        bolus_vtbi = -1
        return_text = self.query('QA')
        if return_text[0:2] == 'QA':
            bolus_vtbi = int(return_text[2:], 16) / 100
        return bolus_vtbi
        
    def get_protocol_rate_unit(self):
        protocol_rate_unit = ''
        return_text = self.query('QC')
        if return_text[0:2] == 'QC':
            # print(return_text)
            protocol_rate_unit = return_text[2:]
        return protocol_rate_unit
    
    def get_protocol_vtbi(self):
        protocol_vtbi = ''
        return_text = self.query('QD')
        if return_text[0:2] == 'QD':
            # print(return_text)
            protocol_vtbi = int(return_text[2:], 16) / 100
        return protocol_vtbi
    
    def get_protocol_time(self):
        protocol_time = ''
        return_text = self.query('QE')
        if return_text[0:2] == 'QE':
            # print(return_text)
            protocol_time = int(return_text[2:], 16)
        return protocol_time
    
    def get_protocol_time_unit(self):
        protocol_time_unit = ''
        return_text = self.query('QF')
        if return_text[0:2] == 'QF':
            # print(return_text)
            protocol_time_unit = return_text[2:]
        return protocol_time_unit
    
    def get_protocol_bolus_rate(self):
        protocol_bolus_rate = -1
        return_text = self.query('QG')
        if return_text[0:2] == 'QG':
            # print(return_text)
            protocol_bolus_rate = int(return_text[2:], 16) / 100
        return protocol_bolus_rate
    
    def get_protocol_auto_bolus_vtbi(self):
        protocol_auto_bolus_vtbi = ''
        return_text = self.query('QH')
        if return_text[0:2] == 'QH' and return_text[2:] != 'ERROR':
            # print(return_text)
            protocol_auto_bolus_vtbi = int(return_text[2:], 16) / 100
        else:
            print(return_text)
        return protocol_auto_bolus_vtbi
    
    def get_protocol_demand_bolus_vtbi(self):
        protocol_demand_bolus_vtbi = ''
        return_text = self.query('QI')
        if return_text[0:2] == 'QI' and return_text[2:] != 'ERROR':
            # print(return_text)
            protocol_demand_bolus_vtbi = int(return_text[2:], 16) / 100
        else:
            print(return_text)
        return protocol_demand_bolus_vtbi

    def get_eventlog_list(self, num_to_query):
        eventlog_list = []
        eventlogs = self.read_multiple_event_log(num_to_query)
        for each_eventlog in eventlogs:
            if 'event_type' in each_eventlog:
                eventlog_list.append(each_eventlog['event_type'])
                if each_eventlog['event_type'] == 'INFUSION_DATA':
                    eventlog_list.append(each_eventlog['infusion_data_frame'])
                elif each_eventlog['event_type'] == 'OCCLUSION_ALARM':
                    eventlog_list.append(each_eventlog['sub_type'])
        return eventlog_list
    
    def get_screenshot_hex_list(self):
        screenshot_hex_list = []
        screenshot_ready = False
        while not screenshot_ready:
            screenshot_ready = self.send_command(':screenshot:ready?')
            print('screenshot_ready = {}'.format(screenshot_ready))
            if screenshot_ready == '':
                print('screenshot_ready == \'\'')
                return screenshot_hex_list
            if screenshot_ready is None:
                print('screenshot_ready is None')
                return screenshot_hex_list
        for i in range(8):
            sent_text = ':screenshot:line:' + str(i) + '?'
            return_text = self.send_command(sent_text)
            print(return_text)
            screenshot_hex_list.append(return_text)
        return screenshot_hex_list
    
    def get_screenshot_hex(self):
        screenshot_hex = ''
        screenshot_ready = False
        index = 20
        while not screenshot_ready and index > 0:
            index -= 1
            screenshot_ready = self.send_command(':screenshot:ready?')
            print('screenshot_ready = {}'.format(screenshot_ready))
            if screenshot_ready == '':
                print('screenshot_ready == \'\'')
                return screenshot_hex
            if screenshot_ready is None:
                print('screenshot_ready is None')
                return screenshot_hex
            if index == 0 and not screenshot_ready:
                print('screenshot_ready is False')
                return screenshot_hex
        sent_text = ':screenshot?'
        screenshot_hex = self.send_command(sent_text)
        print(screenshot_hex)
        return screenshot_hex

    #===================
    def trigger_power_off(self):
        '''trigger power off'''
        status = False
        sent_text = 'WT00'
        return_text = self.query(sent_text)
        if len(return_text) == 2 and return_text[0:2] == 'WT':
            # print('Trigger Power Off')
            status = True
        return status
    
    def trigger_run_infusion(self):
        '''trigger run infusion'''
        status = False
        sent_text = 'WT01'
        return_text = self.query(sent_text)
        if len(return_text) == 2 and return_text[0:2] == 'WT':
            # print('Trigger Run Infusion succeed')
            status = True
        return status
    
    def trigger_stop_infusion(self):
        '''trigger stop infusion'''
        status = False
        sent_text = 'WT02'
        return_text = self.query(sent_text)
        if len(return_text) == 2 and return_text[0:2] == 'WT':
            # print('Trigger Stop Infusion succeed')
            status = True
        return status
    
    def return_top(self, library, protocol, parameter_name):
        '''Return to the top of the Parameter list (on the pump)'''
        result = False
        parameter_list = get_parameter_list(library, protocol)
        # Go back to top of the list
        if parameter_name in ['drugAmount', 'diluteVolume']:
            parameter_name = 'concentration'
        if parameter_name in parameter_list:
            # Get menu index of Parameter
            parameter_index = parameter_list.index(parameter_name)
            # Select the Parameter
            print('==')
            print('Return to the top of the parameter list...')
            time.sleep(_TIMEOUT * 2)
            while parameter_index > 0:
                # Press [Up] Key
                return_text = self.press_key(_UP_KEY, _SHORT_PRESS)
                if len(return_text) == 4 and return_text[0:2] == 'KE':
                    print('key: Up (short)')
                time.sleep(_TIMEOUT * 2)
                parameter_index -= 1
            result = True
        return result
    
    def run_protocol(self, library, protocol):
        '''Run Protocol (on the Pump)'''
        parameter_list = get_parameter_list(library, protocol)
        print('Infusion Parameter List = {}'.format(parameter_list))
        parameter_list_length = len(parameter_list)
        # Press [Run] Key [SHORT]
        return_text = self.trigger_run_infusion()
        if return_text:
            print('key: Trigger Run Infusion')
        seconds_to_wait = 1.5 * parameter_list_length
        print('Infusion start in [{:2.2f}] seconds... '.format(seconds_to_wait))
        # Wait [Review Parameters] to Finish
        # wait(seconds_to_wait)
        # Start infusion on the pump
        # Press [Ok] Key 
    #     return_text = self.press_key(_OK_KEY, _SHORT_PRESS)
    #     if len(return_text) == 4 and return_text[0:2] == 'KE':
    #         print('key: Ok/Enter (short)')
        time.sleep(_TIMEOUT * 2)
    
    def set_parameter_value(self, new_value, parameter):
        '''Set Parameter Value on the Pump
           parameter include the following information:
            length       - total length of the parameter
            fract_length - length of fractional part of the parameter
            value        - the value of the parameter
            unit         - the unit of the parameter
            name         - the name of the parameter
        '''
        old_value = parameter['value']
        max_value = parameter['max']
        min_value = parameter['min']
        fract_length = parameter['fract_length']
        length = parameter['length']
        # Translate new and old values if the unit is [minute]
        if parameter['unit'] == 'minute':
            new_value_str = str(int(new_value / 60))
            new_value_str = new_value_str + str(int(new_value % 60)).zfill(2)
            new_value = int(new_value_str)
            
            old_value_str = str(int(old_value / 60))
            old_value_str = old_value_str + str(int(old_value % 60)).zfill(2)
            old_value = int(old_value_str)
            
            max_value_str = str(int(max_value / 60))
            max_value_str = max_value_str + str(int(max_value % 60)).zfill(2)
            max_value = int(max_value_str)
            
            min_value_str = str(int(min_value / 60))
            min_value_str = min_value_str + str(int(min_value % 60)).zfill(2)
            min_value = int(min_value_str)
        #
        old_value = str(int(old_value * pow(10, fract_length))).zfill(length)
        max_value = str(int(max_value * pow(10, fract_length))).zfill(length)
        min_value = str(int(min_value * pow(10, fract_length))).zfill(length)
        new_value = str(int(new_value * pow(10, fract_length))).zfill(length)
        print('old_value = {}'.format(old_value))
        print('new_value = {}'.format(new_value))
        #
        if parameter['name'] == 'diluteVolume':
            index = 3
            while index > 0:
                # Press [Ok] Key / Skip over the [Drug Amount]
                self.press_key(_OK_KEY, _SHORT_PRESS)
                print('key: Ok (short)')
                time.sleep(_TIMEOUT * 2)
                index -= 1
        # Set value from [OLD] value to [MIN] value
        print('==')
        print('Set value from [{}] to [{}]'.format(old_value, min_value))
        time.sleep(_TIMEOUT * 2)
        # diff_value = ''
        for index in range(length):
            diff = int(min_value[index]) - int(old_value[index])
            if diff < 0:
                while diff < 0:
                    # Press [Down] Key
                    self.press_key(_DOWN_KEY, _SHORT_PRESS)
                    print('key: Down (short)')
                    time.sleep(_TIMEOUT * 2)
                    diff += 1
            if diff > 0:
                while diff > 0:
                    # Press [Up] Key
                    self.press_key(_UP_KEY, _SHORT_PRESS)
                    print('key: Up (short)')
                    time.sleep(_TIMEOUT * 2)
                    diff -= 1
            # Press [Ok] Key
            self.press_key(_OK_KEY, _SHORT_PRESS)
            print('key: Ok (short)')
            time.sleep(_TIMEOUT * 2)
        #
        if parameter['name'] == 'drugAmount':
            index = 3
            while index > 0:
                # Press [Ok] Key / Skip over the [Dilute Volume]
                self.press_key(_OK_KEY, _SHORT_PRESS)
                print('key: Ok (short)')
                time.sleep(_TIMEOUT * 2)
                index -= 1
        # Press [Ok] Key / Enter the Parameter Agian
        self.press_key(_OK_KEY, _SHORT_PRESS)
        print('key: Ok (short)')
        time.sleep(_TIMEOUT * 2)
        #
        if parameter['name'] == 'diluteVolume':
            index = 3
            while index > 0:
                # Press [Ok] Key / Skip over the [Drug Amount]
                self.press_key(_OK_KEY, _SHORT_PRESS)
                print('key: Ok (short)')
                time.sleep(_TIMEOUT * 2)
                index -= 1
        # Set value from [MIN] value to [MAX] value
        print('==')
        print('Set value from [{}] to [{}]'.format(min_value, max_value))
        time.sleep(_TIMEOUT * 2)
        for index in range(length):
            diff = int(max_value[index]) - int(min_value[index])
            if int(min_value[index]) > 0 and diff >= 0 and index > 0:
                diff = int(min_value[index])
                while diff > 0:
                    # Press [Down] Key
                    self.press_key(_DOWN_KEY, _SHORT_PRESS)
                    print('key: Down (short)')
                    time.sleep(_TIMEOUT * 2)
                    diff -= 1
            # Press [Down] Key
            self.press_key(_DOWN_KEY, _SHORT_PRESS)
            print('key: Down (short)')
            time.sleep(_TIMEOUT * 2)
            # Press [Ok] Key
            self.press_key(_OK_KEY, _SHORT_PRESS)
            print('key: Ok (short)')
            time.sleep(_TIMEOUT * 2)
        #
        if parameter['name'] == 'drugAmount':
            index = 3
            while index > 0:
                # Press [Ok] Key / Skip over the [Dilute Volume]
                self.press_key(_OK_KEY, _SHORT_PRESS)
                print('key: Ok (short)')
                time.sleep(_TIMEOUT * 2)
                index -= 1
        # Press [Ok] Key Enter the Parameter Agian
        self.press_key(_OK_KEY, _SHORT_PRESS)
        print('key: Ok (short)')
        time.sleep(_TIMEOUT * 2)
        #
        if parameter['name'] == 'diluteVolume':
            index = 3
            while index > 0:
                # Press [Ok] Key / Skip over the [Drug Amount]
                self.press_key(_OK_KEY, _SHORT_PRESS)
                print('key: Ok (short)')
                time.sleep(_TIMEOUT * 2)
                index -= 1
        # Set value from [MAX] value to [NEW] value
        print('==')
        print('Set value from [{}] to [{}]'.format(max_value, new_value))
        time.sleep(_TIMEOUT * 2)
        # diff_value = ''
        raise_base = True
        for index in range(length):
            diff = int(new_value[index]) - int(max_value[index])
            if diff < 0:
                while diff < 0:
                    # Press [Down] Key
                    self.press_key(_DOWN_KEY, _SHORT_PRESS)
                    print('key: Down (short)')
                    time.sleep(_TIMEOUT * 2)
                    diff += 1
            if diff > 0:
                if raise_base and int(min_value[index]) > int(max_value[index]):
                    diff = diff - (int(min_value[index]) - int(max_value[index])) + 1
                while diff > 0:
                    # Press [Up] Key
                    self.press_key(_UP_KEY, _SHORT_PRESS)
                    print('key: Up (short)')
                    time.sleep(_TIMEOUT * 2)
                    diff -= 1
            # Press [Ok] Key
            self.press_key(_OK_KEY, _SHORT_PRESS)
            print('key: Ok (short)')
            time.sleep(_TIMEOUT * 2)
            # 
            if int(new_value[index]) > int(min_value[index]):
                raise_base = False
        #
        if parameter['name'] == 'drugAmount':
            index = 3
            while index > 0:
                # Press [Ok] Key / Skip over the [Dilute Volume]
                self.press_key(_OK_KEY, _SHORT_PRESS)
                print('key: Ok (short)')
                time.sleep(_TIMEOUT * 2)
                index -= 1
    
    def select_protocol(self, library, protocol):
        '''Select Protocol (on the pump)'''
        protocol_id = protocol['id']
        node_children = library.library['content']['node']['children']
        protocol_navi_path = library.get_protocol_navi_path(protocol_id, node_children)
        # convert Python Dictionary to JSON:
        # protocol_navi_path_json = json.dumps(protocol_navi_path, indent=4)
        # print(protocol_navi_path_json)
        # Go back to the [Top] menu
        print('==')
        print('Go back to [Top] menu...')
        time.sleep(_TIMEOUT * 2)
        #
        navi_path_len = len(protocol_navi_path)
        while navi_path_len >= 0:
            return_text = self.press_key(_INFO_KEY, _SHORT_PRESS)
            if len(return_text) == 4 and return_text[0:2] == 'KE':
                print('key: Back (short)')
            time.sleep(_TIMEOUT * 2)
            navi_path_len -= 1
        # Reset Battery
        self.reset_battery()
        # Select [New Rx]
        print('==')
        print('Select [New Rx]...')
        time.sleep(_TIMEOUT * 2)
        #
        return_text = self.press_key(_DOWN_KEY, _SHORT_PRESS)
        if len(return_text) == 4 and return_text[0:2] == 'KE':
            print('key: Down (short)')
        time.sleep(_TIMEOUT * 2)
        # Enter [New Rx]
        return_text = self.press_key(_OK_KEY, _SHORT_PRESS)
        if len(return_text) == 4 and return_text[0:2] == 'KE':
            print('key: Ok/Enter (short)')
        time.sleep(_TIMEOUT * 2)
        #
        # Go back to the [Top] menu the 2nd Time
        print('==')
        print('Go back to [Top] menu...')
        time.sleep(_TIMEOUT * 2)
        #
        navi_path_len = len(protocol_navi_path)
        while navi_path_len >= 0:
            return_text = self.press_key(_INFO_KEY, _SHORT_PRESS)
            if len(return_text) == 4 and return_text[0:2] == 'KE':
                print('key: Back (short)')
            time.sleep(_TIMEOUT * 2)
            navi_path_len -= 1
        # Select [New Rx]
        print('==')
        print('Select [New Rx]...')
        time.sleep(_TIMEOUT * 2)
        #
        return_text = self.press_key(_DOWN_KEY, _SHORT_PRESS)
        if len(return_text) == 4 and return_text[0:2] == 'KE':
            print('key: Down (short)')
        time.sleep(_TIMEOUT * 2)
        # Enter [New Rx]
        return_text = self.press_key(_OK_KEY, _SHORT_PRESS)
        if len(return_text) == 4 and return_text[0:2] == 'KE':
            print('key: Ok/Enter (short)')
        time.sleep(_TIMEOUT * 2)
        # Go to the selected protocol
        print('==')
        print('Select [{}]...'.format(protocol['content']['name'].strip(' \t\r\n\0')))
        time.sleep(_TIMEOUT * 2)
        #
        pin_entered = False
        for each_navi_node in protocol_navi_path:
            index = each_navi_node['menu_position']
            while index > 0:
                # Press [Down] Key
                return_text = self.press_key(_DOWN_KEY, _SHORT_PRESS)
                if len(return_text) == 4 and return_text[0:2] == 'KE':
                    print('key: Down (short)')
                time.sleep(_TIMEOUT * 2)
                index -= 1
            # Press [Ok] Key
            return_text = self.press_key(_OK_KEY, _SHORT_PRESS)
            if len(return_text) == 4 and return_text[0:2] == 'KE':
                print('key: Ok/Enter (short)')
            time.sleep(_TIMEOUT * 2)
            # Enter Pin
            if each_navi_node['auth'][0]['pin'] != '' and not pin_entered:
                pin_number = each_navi_node['auth'][0]['pin']
                # Input PIN number
                print('==')
                print('Input PIN number [{}]...'.format(pin_number))
                time.sleep(_TIMEOUT * 2)
                #
                self.input_digits(pin_number)
                pin_entered = True
    
    def run_clinician_dose(self, clinician_code):
        '''Run [Clinician Dose] on the pump
           During the infusion, the user can run the clinician dose if there is no
           bolus is running
           clinician_code: pin number for [clinician] role'''
        # Enter [infusionRoot] Menu in the [defaultNavigationTree]
        print('==')
        print('Enter [Infusion Root Menu]...')
        time.sleep(_TIMEOUT * 2)
        #
        return_text = self.press_key(_INFO_KEY, _SHORT_PRESS)
        if len(return_text) == 4 and return_text[0:2] == 'KE':
            print('key: Back (short)') 
        time.sleep(_TIMEOUT * 2)
        #
        # Get menu index of [Clinician Dose]
        parameter_index = 4
        # Select [Clinician Dose]
        print('==')
        print('Select [Clinician Dose]...')
        time.sleep(_TIMEOUT * 2)
        #
        while parameter_index > 0:
            # Press [Down] Key
            return_text = self.press_key(_DOWN_KEY, _SHORT_PRESS)
            if len(return_text) == 4 and return_text[0:2] == 'KE':
                print('key: Down (short)')
            time.sleep(_TIMEOUT * 2)
            parameter_index -= 1
        # Press [Ok] Key
        return_text = self.press_key(_OK_KEY, _SHORT_PRESS)
        if len(return_text) == 4 and return_text[0:2] == 'KE':
            print('key: Ok/Enter (short)')
        time.sleep(_TIMEOUT * 2)
        # Press [Info] Key (short)
        return_text = self.press_key(_INFO_KEY, _SHORT_PRESS)
        if len(return_text) == 4 and return_text[0:2] == 'KE':
            print('key: Back (short)')
        time.sleep(_TIMEOUT * 2)
        # Press [Info] Key (short)
        return_text = self.press_key(_INFO_KEY, _SHORT_PRESS)
        if len(return_text) == 4 and return_text[0:2] == 'KE':
            print('key: Back (short)')
        time.sleep(_TIMEOUT * 2)
        # Enter [infusionRoot] Menu in the [defaultNavigationTree]
        print('==')
        print('Enter [Infusion Root Menu]...')
        time.sleep(_TIMEOUT * 2)
        #
        return_text = self.press_key(_INFO_KEY, _SHORT_PRESS)
        if len(return_text) == 4 and return_text[0:2] == 'KE':
            print('key: Back (short)') 
        time.sleep(_TIMEOUT * 2)
        #
        # Get menu index of [Clinician Dose]
        parameter_index = 4
        # Select [Clinician Dose]
        print('==')
        print('Select [Clinician Dose]...')
        time.sleep(_TIMEOUT * 2)
        #
        while parameter_index > 0:
            # Press [Down] Key
            return_text = self.press_key(_DOWN_KEY, _SHORT_PRESS)
            if len(return_text) == 4 and return_text[0:2] == 'KE':
                print('key: Down (short)')
            time.sleep(_TIMEOUT * 2)
            parameter_index -= 1
        # Press [Ok] Key
        return_text = self.press_key(_OK_KEY, _SHORT_PRESS)
        if len(return_text) == 4 and return_text[0:2] == 'KE':
            print('key: Ok/Enter (short)')
        time.sleep(_TIMEOUT * 2)
        # Input PIN number [Clinician Code]
        print('==')
        print('Input PIN number [{}]...'.format(clinician_code))
        time.sleep(_TIMEOUT * 2)
        self.input_digits(clinician_code)
        # Select [OK to Confirm]
        print('==')
        print('Select [OK to Confirm]...')
        time.sleep(_TIMEOUT * 2)
        # Press [Down] Key
        return_text = self.press_key(_DOWN_KEY, _SHORT_PRESS)
        if len(return_text) == 4 and return_text[0:2] == 'KE':
            print('key: Down (short)')
        time.sleep(_TIMEOUT * 2)
        # Press [Ok] Key
        return_text = self.press_key(_OK_KEY, _SHORT_PRESS)
        if len(return_text) == 4 and return_text[0:2] == 'KE':
            print('key: Ok/Enter (short)')
        time.sleep(_TIMEOUT * 2)
    
    def select_parameter(self, library, protocol, parameter_name):
        '''Select Parameter (on the pump)'''
        result = False
        parameter_list = get_parameter_list(library, protocol)
        print('==')
        print('Infusion Parameter List = {}'.format(parameter_list))
        if parameter_name in ['drugAmount', 'diluteVolume']:
            parameter_name = 'concentration'
        if parameter_name in parameter_list:
            # Get menu index of Parameter
            parameter_index = parameter_list.index(parameter_name)
            # Select the Parameter
            print('==')
            print('Select [{}]...'.format(parameter_name))
            time.sleep(_TIMEOUT * 2)
            while parameter_index > 0:
                # Press [Down] Key
                return_text = self.press_key(_DOWN_KEY, _SHORT_PRESS)
                if len(return_text) == 4 and return_text[0:2] == 'KE':
                    print('key: Down (short)')
                time.sleep(_TIMEOUT * 2)
                parameter_index -= 1
            # Press [Ok] Key
            return_text = self.press_key(_OK_KEY, _SHORT_PRESS)
            if len(return_text) == 4 and return_text[0:2] == 'KE':
                print('key: Ok/Enter (short)')
            time.sleep(_TIMEOUT * 2)
            result = True
        return result
    
    def reset_battery(self):
        '''Reset Battery (on the pump)'''
        print('==')
        print('Reset Battery...')
        time.sleep(_TIMEOUT * 2)
        #
        return_text = self.press_key(_INFO_KEY, _LONG_PRESS)
        if len(return_text) == 4 and return_text[0:2] == 'KE':
            print('key: Info (long)')
        time.sleep(_TIMEOUT * 2)
        #
        return_text = self.press_key(_DOWN_KEY, _SHORT_PRESS)
        if len(return_text) == 4 and return_text[0:2] == 'KE':
            print('key: Down (short)')
        time.sleep(_TIMEOUT * 2)
        #
        return_text = self.press_key(_OK_KEY, _SHORT_PRESS)
        if len(return_text) == 4 and return_text[0:2] == 'KE':
            print('key: Ok (short)')
        time.sleep(_TIMEOUT * 2)
        #
        return_text = self.press_key(_DOWN_KEY, _SHORT_PRESS)
        if len(return_text) == 4 and return_text[0:2] == 'KE':
            print('key: Down (short)')
        time.sleep(_TIMEOUT * 2)
        #
        return_text = self.press_key(_OK_KEY, _SHORT_PRESS)
        if len(return_text) == 4 and return_text[0:2] == 'KE':
            print('key: Ok (short)')
        time.sleep(_TIMEOUT * 2)
        #
        return_text = self.press_key(_INFO_KEY, _LONG_PRESS)
        if len(return_text) == 4 and return_text[0:2] == 'KE':
            print('key: Info (long)')
        time.sleep(_TIMEOUT * 2)
        
    def start(self):
        '''start console'''
        library = self.library
        infusion = self.infusion
        miva = self
        protocol = self.protocol
        test = self.test
        try:
            # print('start event log monitor...')
            # print('==')
            # self.run_event_log_monitor()
            # print('start infusion monitor...')
            # print('==')
            # self.run_infusion_monitor()
            # print('start socket server...')
            # print('==')
            # self.run_socket_server()            
            #
            cmd = ''
            while cmd not in ['exit']:
                cmd = input('>').lower().strip(' \t\r\n\0')
                #
                # Pause [Event Log Monitor]
                if self.event_log_monitor.is_on():
                    if not self.event_log_monitor.is_paused():
                        self.event_log_monitor.pause()
                #
                # Disable [Infusion Monitor] Output
                self.infusion_monitor.disable_output()
                # Start Processing Commands
                if cmd.upper() in ['HELP', 'MAIN', '?']:
                    # query the help main file
                    help_file_dir = self.pump_config['help_file_path']
                    if help_file_dir != '':
                        if not path.isdir(help_file_dir):
                            makedirs(help_file_dir)   
                    main_help_file_path = help_file_dir + '/help_main.txt'
                    
                    if path.exists(main_help_file_path):
                        main_help_list = file_to_list(main_help_file_path)
                        for each_line in main_help_list:
                            print('\t {}'.format(each_line))
                    else:
                        print('Abort - Help File Unavailable [{}]'.format(main_help_file_path))
                elif re.match(re_query_help_file, cmd.lower()):
                    # query help file for a specific command
                    re_match_result = re.match(re_query_help_file, cmd.lower())
                    # query the help main file
                    help_file_dir = self.pump_config['help_file_path']
                    if help_file_dir != '':
                        if not path.isdir(help_file_dir):
                            makedirs(help_file_dir)
                    command = re_match_result[3].lstrip(' ')
                    command = command.lstrip(':')
                    command = command.replace(":", "_")
                    help_file_path = help_file_dir + '/help_' + command.replace(" ", "_") + '.txt'
                    if path.exists(help_file_path):
                        help_file_list = file_to_list(help_file_path, False, False)
                        for each_line in help_file_list:
                            print('{}'.format(each_line))
                    else:
                        print('Abort - Help File Unavailable [{}]'.format(help_file_path))
                elif cmd.lower() in ['version', 'about']:
                    copyright_symbol = u"\u00A9"
                    print('\t Nimbus MIVA Pump Configuration Tool')
                    print('\t Copyright {} 2021-2022'.format(copyright_symbol))
                    print('\t Zyno Medical LLC')
                    print('\t Ver 1.0.0.12')
                    print('\t Author: yancen.li@zynomed.com')
                # ==============================================
                elif cmd.lower().rstrip(' \t\r\n\0') in ['flash', 'install', 'flash firmware']:
                    print('1. Install MFG 32-bit firmware')
                    print('2. Install MIVA 8-bit firmware')
                    print('3. Install MIVA 32-bit firmware')
                    flash_choice = input('Enter your choice: ').strip(' \t\r\n\0')
                    if flash_choice == '1':
                        download_mfg_32_bit()
                    elif flash_choice == '2':
                        download_miva_8_bit()
                    elif flash_choice == '3':
                        download_miva_32_bit()
                    else:
                        print('Abort - flash firmware')
                # ==============================================
                elif cmd.lower() in ['peh', 'parse event log hex']:
                    # peh - Parse Event Log Hex File
                    event_log_hex_path = input('    Enter event log hex path: ').strip(' \t\r\n\0')
                    if path.exists(event_log_hex_path):
                        event_log_hex_list = file_to_list(event_log_hex_path)
                        event_logs = parse_multiple_event_log(event_log_hex_list)
                        event_logs_json = json.dumps(event_logs, indent=4)
                        print()
                        print(event_logs_json)
                        print('     Event logs parsed: [{}]'.format(len(event_logs)))
                    else:
                        print('Abort - File NOT Exist [{}]'.format(event_log_hex_path))
                elif re.match(re_read_event_log_hex, cmd):
                    # Read Event Log HEX from [0] up to [EVENT_LOG_NUMBER_OF_EVENTS]
                    re_match_result = re.match(re_read_event_log_hex, cmd)
                    if re_match_result[3] is None or re_match_result[6] is None:
                        print('usage: reh <start_index> <stop_index>')
                        print('index range: 0x{0} - {1}\n'.format(hex(0)[2:].zfill(4), \
                                                                hex(EVENT_LOG_NUMBER_OF_EVENTS)))
                        print('       ex. reh 0x0000 0x00AF')
                        print('           reh 0 20\n')
                        continue
                    start_index_str = re_match_result[3]
                    stop_index_str = re_match_result[6]
                    start_index = 0
                    stop_index = 0
                    if re_match_result[4] == '0x':
                        start_index = int(start_index_str[2:], 16)
                    else:
                        start_index = int(start_index_str)
                    if re_match_result[7] == '0x':
                        stop_index = int(stop_index_str[2:], 16)
                    else:
                        stop_index = int(stop_index_str)
                    if not (0 <= start_index <= stop_index <= EVENT_LOG_NUMBER_OF_EVENTS):
                        print('Index out of range (0x{0} - {1})'.format(hex(0)[2:].zfill(4), \
                                                                    hex(EVENT_LOG_NUMBER_OF_EVENTS)))
                        continue
                    event_logs = []
                    for i in range(start_index, stop_index):
                        single_event_log = self.read_single_event_log(i)
                        event_logs.append(single_event_log[10:42])
                        print('{0}    {1}'.format(single_event_log[2:10], single_event_log[10:42]))
                    print('     Event logs hex read: [{}]'.format(len(event_logs)))
                    # the path the event log hex will be saved to
                    # print('re_match_result[10] = {}'.format(re_match_result[10]))
                    # print('re_match_result[12] = {}'.format(re_match_result[12]))
                    if re_match_result[10] == '>' and re_match_result[12] is not None:
                        event_log_path = re_match_result[12]
                        abs_file_path = list_to_file(event_logs, event_log_path)
                        print('     Event logs hex saved: [{}]'.format(abs_file_path))   
                elif re.match(re_read_event_log, cmd):
                    # Read the last N event log
                    re_match_result = re.match(re_read_event_log, cmd)
                    # the number of event log to print
                    num_to_print = 0
                    if re_match_result[3] is None:
                        num_to_print = -1
                    else:
                        num_to_print = int(re_match_result[3])
                    event_logs = self.read_multiple_event_log(num_to_print)
                    event_logs_json = json.dumps(event_logs, indent=4)
                    print()
                    print(event_logs_json)
                    print('     Event logs read: [{}]'.format(len(event_logs)))
                    # the path the event log will be saved to
                    event_log_path = None
                    # print('re_match_result[6] = {}'.format(re_match_result[6]))
                    # print('re_match_result[8] = {}'.format(re_match_result[8]))
                    if re_match_result[6] == '>' and re_match_result[8] is not None:
                        event_log_path = re_match_result[8]
                        abs_file_path = json_to_file(event_logs, event_log_path)
                        print('     Event logs saved: [{}]'.format(abs_file_path))
                elif cmd.upper() in ['RI']:
                    # Read Event Log Indices
                    event_log_index = self.read_event_log_indices()
                    event_log_index_tail = event_log_index['tail']
                    event_log_index_head = event_log_index['head']
                    if event_log_index_tail != '' and event_log_index_head != '':
                        print('Event log tail = {}'.format(event_log_index_tail))
                        print('Event log head = {}'.format(event_log_index_head))
                    else:
                        print('Error: get event log index failed')
                elif cmd.upper() in ['RN']:
                    # Read Pump Serial Number
                    serial_number = self.get_pump_sn()
                    if serial_number != '':
                        print('S/N: {}'.format(serial_number))
                    else:
                        print('Error: get serial number failed')
                elif cmd.upper() in ['WN']:
                    # Write Pump Serial Number
                    print('Enter NEW S/N: ', end='')
                    serial_number = input('').upper()
                    if len(serial_number) == 8 and re.findall(r"[A-Za-z0-9]{8,8}", serial_number) != []:
                        status = self.set_pump_sn(serial_number)
                        if status:
                            # print('New S/N: {}'.format(serial_number))
                            print("Write pump serial number  -  Done!")
                        else:
                            print('Error: set serial number failed')
                    else:
                        print('Error: invalid serial number \'{}\' '.format(serial_number), end='')
                        print('Enter \'SN\' followed by 6-digit pump serial number ', end='')
                        print('(ex: \'SN800009\')')
                elif cmd.upper() in ['R1']:
                    # Read Motor Calibration Factor
                    motor_calibration_factor = self.get_motor_calibration_factor()
                    if motor_calibration_factor is not None:
                        print('Motor calibration factor: {}'.format(motor_calibration_factor))
                    else:
                        print('Error: get [motor calibration factor] failed')
                elif cmd.upper() in ['W1']:
                    # Write Motor Calibration Factor
                    calibration_factor = self.set_motor_calibration_factor()
                    if calibration_factor is not None:
                        print('Motor calibration factor is set to: {}'.format(calibration_factor))
                    else:
                        print('Error: set [calibration factor] failed')
                elif cmd.upper() in ['R2']:
                    # Read Occlusion Sensor Threshold Value
                    occlusion_thresholds = self.get_occlusion_thresholds()
                    if occlusion_thresholds != {}:
                        print('Up threshold: {}'.format(occlusion_thresholds['up']))
                        print('Dn threshold: {}'.format(occlusion_thresholds['down']))
                    else:
                        print('Error: get [occlusion thresholds] failed')
                
                elif cmd.upper() in ['W2']:
                    # Write Occlusion Sensor Threshold Value
                    occlusion_thresholds = self.set_occlusion_thresholds()
                    if occlusion_thresholds != {}:
                        print('Up threshold is set to: {}'.format(occlusion_thresholds['up']))
                        print('Dn threshold is set to: {}'.format(occlusion_thresholds['down']))
                    else:
                        print('Error: set [occlusion thresholds] failed')
                elif cmd.upper().rstrip(' \t\r\n\0') == 'R3':
                    # Read [Total Volume Infused]
                    total_volume_infused = self.get_total_volume_infused()
                    if total_volume_infused is not None:
                        print('Total volume infused: {} mL'.format(total_volume_infused))
                    else:
                        print('Error: get [Total Volume Infused] failed')
                elif cmd.upper().rstrip(' \t\r\n\0') == 'R7':
                    # Read [Battery Voltage]
                    battery_voltage = self.get_battery_voltage()
                    if battery_voltage is not None:
                        print('Battery voltage: {:.2f} V'.format(battery_voltage))
                    else:
                        print('Error: get [Battery Voltage] failed')
                elif cmd.upper().rstrip(' \t\r\n\0') == 'R8':
                    # Read [Motor Calibration Factor] and [Total Rotation]
                    product_life_volume = self.get_product_life_volume()
                    if product_life_volume != {}:
                        print('Motor calibration factor: {}'\
                                .format(product_life_volume['calibration']))
                        print('Motor total rotation: {}'.format(product_life_volume['rotation']))
                        print('Product life volume: {:.2f} mL'\
                                .format(product_life_volume['volume']))
                    else:
                        print('Error: get [Calibration Factor and Total Rotation] failed')
                elif cmd.upper().rstrip(' \t\r\n\0') == 'R9':
                    # Read [Total Pump ON Time]
                    total_pump_on_time = self.get_total_pump_on_time()
                    if total_pump_on_time != '':
                        day = str(int(total_pump_on_time / 3600 / 24)).zfill(2)
                        hour = str(int(total_pump_on_time / 3600 % 24)).zfill(2)
                        minute = str(int(total_pump_on_time % 3600 / 60)).zfill(2)
                        second = str(int(total_pump_on_time % 3600 % 60)).zfill(2)
                        print('{0} day {1} hr {2} min {3} sec'.format(day, hour, minute, second))
                        print("Read pump total ON time - Done!")
                    else:
                        print('Error: get [Battery Voltage] failed')
                elif cmd.upper().rstrip(' \t\r\n\0') == 'RA':
                    # Read Battery Calibration
                    battery_calibration_and_voltage = self.get_battery_calibration_and_voltage()
                    if battery_calibration_and_voltage != {}:
                        print('Battery calibration factor = {:.3f}'\
                                .format(battery_calibration_and_voltage['calibration']))
                        print('Battery voltage = {:.2f} V'\
                                .format(battery_calibration_and_voltage['voltage']))
                    else:
                        print('Error: get [Battery Voltage] failed')
                elif cmd.upper().rstrip(' \t\r\n\0') == 'WA':
                    # Write Battery Calibration Factor
                    calib_factor = input('Enter Battery Calibration Factor: ')
                    if re.match(r'^\d+(.)?(\d+)?$', calib_factor) is None:
                        print('Error: invalid battery calibration factor \'{}\' '.format(calib_factor))
                    else:
                        calib_factor = float(calib_factor)
                        if calib_factor >= 0.9 and calib_factor <= 1.1:
                            status = self.set_battery_calib(calib_factor)
                            if status:
                                print("Set battery calibration factor  -  Done!")
                            else:
                                print('Error: set battery calibration factor failed')
                        else:
                            print('Error: \'{}\' out of range [0.900, 1.100]'.format(calib_factor))
                elif cmd.upper().rstrip(' \t\r\n\0') == 'RB':
                    # Read [Base Year]
                    base_year = self.get_base_year()
                    if base_year != '':
                        print('Base year = {}'.format(base_year))
                    else:
                        print('Error: get [Base Year] failed')
                elif cmd.upper().rstrip(' \t\r\n\0') == 'RD':
                    # Read [Up Down Stream Occlusion Sensor]
                    occlusion_sensor = self.get_occlusion_sensor()
                    if occlusion_sensor != '':
                        print('Read occlusion sensor...')
                        print('Up stream = {}'.format(occlusion_sensor['up']))
                        print('Dn stream = {}'.format(occlusion_sensor['down']))
                    else:
                        print('Error: get [Occlusion Sensor] failed')
                elif cmd.upper().rstrip(' \t\r\n\0') == 'RL':
                    # Read [Library Name and Version]
                    library_name_version = self.get_library_name_version()
                    if library_name_version != '':
                        print('Library name: [{}]'.format(library_name_version['name']))
                        print('Library version: [{}]'.format(library_name_version['version']))
                    else:
                        print('Error: get [Library Version] failed')
                elif cmd.upper().rstrip(' \t\r\n\0') == 'RS':
                    # Read [Firmware Version]
                    software_version = self.get_firmware_version()
                    if software_version != '':
                        print('Firmware version: [{}]'.format(software_version))
                    else:
                        print('Error: get [Software Version] failed')
                elif cmd.upper() in ['RX']:
                    # Read Occlusion Sensor Calibration Factors
                    return_text = self.query('RX')
                    if re.match(r'(RX)([A-F0-9]{32})', return_text):
                        # print(return_text)
                        return_text = self.parse_occlusion_calibration_factors(return_text)
                        print(json.dumps(return_text, indent=4))
                    else:
                        print('Error: get [Occlusion Calibration Factors] failed')
                elif cmd.upper() in ['WX']:
                    # Write Occlusion Sensor Calibration Factors
                    return_text = self.set_occlusion_calibration_factors()
                    if return_text != '':
                        # print(return_text)
                        return_text = self.parse_occlusion_calibration_factors(return_text)
                        print(json.dumps(return_text, indent=4))
                elif cmd.upper().rstrip(' \t\r\n\0') == 'S9':
                    # Enable the [S9] Command Output
                    # self.enable_s9_command()
                    # Read [Firmware Version]
                    all_sensor = self.get_all_sensor()
                    if all_sensor != {}:
                        all_sensor_json = json.dumps(all_sensor, indent=4)
                        print('[{}]'.format(all_sensor_json))
                    else:
                        print('Error: get [All Sensors] failed')
                    # Disable the [S9] Command Output
                    # self.disable_s9_command()
                # ==============================================
                # Generate Rx
                elif cmd.lower().rstrip(' \t\r\n\0') in ['gr', 'generate rx']:
                    print(' GR - Generate RX')
                    if library.get_library() is not None:
                        print("currently loaded library: ")
                        # Title
                        print("    {0:5s}    |    {1:5s}    |    {2:15s}    "\
                                .format('id', 'ver.', 'name'))
                        print("----{0:5s}----|----{1:5s}----|----{2:15s}----"\
                                .format('-----', '-----', '---------------'))
                        # Content
                        print("    {0:5s}    |    {1:5s}    |    {2:15s}"\
                                .format(str(library.get_id()), str(library.get_version()), library.get_name()))
                        lib_path = input('Enter NEW library path: ')
                    else:
                        lib_path = input('    Enter library path: ')

                    if path.exists(lib_path) and lib_path.lower().find('library-[') != -1:
                        library.load(lib_path)
                        print("library: ")
                        # Title
                        print("    {0:5s}    |    {1:5s}    |    {2:15s}    "\
                                .format('id', 'ver.', 'name'))
                        print("----{0:5s}----|----{1:5s}----|----{2:15s}----"\
                                .format('-----', '-----', '---------------'))
                        # Content
                        print("    {0:5s}    |    {1:5s}    |    {2:15s}"\
                                .format(str(library.get_id()), \
                                        str(library.get_version()), \
                                        library.get_name()))
                        #
                        self.library = library
                        #
                        self.pump_config["library_path"] = lib_path
                    else:
                        if lib_path == '':
                            pass
                        else:
                            print('    Invalid library path: \'{}\''.format(lib_path))
                            continue

                    if library.get_library() is not None:
                        protocols = library.get_protocols()
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
                            print("{:15s}    |    "\
                                    .format(each_protocol['content']['name']), end='')
                            print("{:20s}".format(each_protocol['content']['deliveryMode']))
                        print("Total [{}] protocols extracted".format(len(protocols)))
                        #
                        protocol_name = self.protocol_name
                        protocol = library.get_protocol(protocol_name)
                        if protocol is not None:
                            self.infusion.set_protocol(protocol)
                            # self.protocol = protocol
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
                            protocol_name = input('Enter NEW protocol name / id: ')\
                                    .strip(' \t\r\n\0') or protocol_name
                        else:
                            protocol_name = input('    Enter protocol name / id: ')
                        #
                        if library.get_protocol(protocol_name) is not None:
                            self.protocol_name = protocol_name
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
                            print("Infusion parameters:")
                            print()
                            if protocol['content']['deliveryMode'] == 'continuousInfusion':
                                infusion.print_cont_parameters()
                            if protocol['content']['deliveryMode'] == 'bolusInfusion':
                                infusion.print_bolus_parameters()
                            if protocol['content']['deliveryMode'] == 'intermittentInfusion':
                                infusion.print_int_parameters()
                            print()
                            #
                            self.pump_config["protocol_selected"] = protocol_name
                            #
                            rx_path = self.generate_rx(protocol)
                            if path.exists(rx_path):
                                # print('Generate Rx succeed')
                                self.rx_path = rx_path
                                self.pump_config['rx_path'] = rx_path
                                json_to_file(self.pump_config, self.pump_config_path)
                            else:
                                print('Generate Rx failed')
                            #
                        else:
                            # invalid protocol name
                            if protocol_name != '':
                                print('    Invalid Protocol: \'{}\''.format(protocol_name))
                                continue
                    else:
                        # No library loaded
                        # print('Abort: empty libarary')
                        pass
                elif cmd.lower().rstrip(' \t\r\n\0') == 'sr':
                    # Send Rx
                    print(' SR - Send Rx')
                    result = False
                    rx_path = self.rx_path
                    if path.exists(rx_path):
                        y_n = input('    Send - [{}]? (y/n):'\
                                .format(self.rx_path)).strip(' \t\r\n\0') or 'y'
                        if y_n == 'y':
                            result = self.send_rx(rx_path)
                            if result:
                                print('Send Rx succeed')
                            else:
                                print('Send Rx failed')
                            continue
                    rx_path = input('    Enter Rx path: ') or 'hello'
                    if path.exists(rx_path):
                        result = self.send_rx(rx_path)
                        if result:
                            print('Send Rx succeed')
                            self.rx_path = rx_path
                            self.pump_config['rx_path'] = rx_path
                            json_to_file(self.pump_config, self.pump_config_path)
                        else:
                            print('Send Rx failed')
                    else:
                        if rx_path == '':
                            pass
                        else:
                            print('Abort: path NOT exist')
                elif cmd.lower().rstrip(' \t\r\n\0') in ['sl', 'send library']:
                    # Send Library
                    print('Send Library... ')
                    result = False
                    library_path = input('    Enter library path: ')
                    if path.exists(library_path):
                        result = self.send_library(library_path)
                        if result:
                            print('Send library succeed')
                        else:
                            print('Send library failed')
                    else:
                        if library_path == '':
                            pass
                        else:
                            print('Abort: path NOT exist')
                elif cmd.lower().rstrip(' \t\r\n\0') in ['el', 'encrypt library']:
                    # Encrypt Library JSON To Byte Array
                    result = False
                    print(' EL - Encrypt Library JSON To Byte Array')
                    library_path = input('    Enter library path: ')
                    if path.exists(library_path):
                        encrypt_library(library_path)
                    else:
                        if library_path == '':
                            pass
                        else:
                            print('Abort: path NOT exist')
                elif cmd.lower().rstrip(' \t\r\n\0') in ['pl', 'parse library']:
                    # Parse Library Hex
                    result = False
                    print(' PL - Parse Library Hex')
                    library_hex_path = input('    Enter library Hex file path: ')
                    if path.exists(library_hex_path):
                        library_hex = ""
                        # read hex file
                        file = open(library_hex_path, "r")
                        library_hex = file.read()
                        file.close()
                        # parse librar hex
                        parse_library_hex(library_hex)
                    else:
                        if library_hex_path == '':
                            pass
                        else:
                            print('Abort: path NOT exist')
                elif cmd.lower().rstrip(' \t\r\n\0') in ['er', 'encrypt rx']:
                    # Encrypt Rx JSON To Byte Array
                    result = False
                    print(' ER - Encrypt Rx JSON To Byte Array')
                    rx_path = input('    Enter Rx path: ')
                    if path.exists(rx_path):
                        encrypt_rx(rx_path)
                    else:
                        if rx_path == '':
                            pass
                        else:
                            print('Abort: path NOT exist')
                elif cmd.lower().rstrip(' \t\r\n\0') in ['pr', 'parse rx']:
                    # Parse Rx Hex
                    result = False
                    print(' PR - Parse Rx Hex')
                    rx_hex_path = input('    Enter Rx Hex file path: ')
                    if path.exists(rx_hex_path):
                        rx_hex = ""
                        # read hex file
                        file = open(rx_hex_path, "r")
                        rx_hex = file.read()
                        file.close()
                        # parse librar hex
                        parse_rx_hex(rx_hex)
                    else:
                        if rx_hex_path == '':
                            pass
                        else:
                            print('Abort: path NOT exist')
                # ==============================================
                elif cmd.upper().rstrip(' \t\r\n\0') == 'INFO':
                    # Send [INFO Key] command
                    return_text = self.press_key(Key.INFO_KEY, Key.LONG_PRESS)
                    if len(return_text) == 4 and return_text[0:2] == 'KE':
                        print('key: Info (long)')
                elif cmd.upper() in ['BACK']:
                    # Send [INFO] key command (Short)
                    return_text = self.press_key(Key.INFO_KEY, Key.SHORT_PRESS)
                    if len(return_text) == 4 and return_text[0:2] == 'KE':
                        print('key: Back (short)')
                elif cmd.upper().rstrip(' \t\r\n\0') in ['RUN']:
                    # Send [RUN] key command [LONG]
                    return_status = self.trigger_run_infusion()
                    if return_status:
                        print('key: Run/Stop (long)')
                elif cmd.upper() in ['STOP']:
                    # Send [STOP] key command [LONG]
                    return_status = self.trigger_stop_infusion()
                    if return_status:
                        print('key: Run/Stop (long)')
                elif cmd.upper().rstrip(' \t\r\n\0') in ['OK', 'ENTER']:
                    # Send [OK] key command
                    return_text = self.press_key(Key.OK_KEY, Key.SHORT_PRESS)
                    if len(return_text) == 4 and return_text[0:2] == 'KE':
                        print('key: Ok/Enter (short)')
                elif cmd.upper().rstrip(' \t\r\n\0') == 'UP':
                    # Send [UP] key command
                    return_text = self.press_key(Key.UP_KEY, Key.SHORT_PRESS)
                    if len(return_text) == 4 and return_text[0:2] == 'KE':
                        print('key: Up (short)')
                elif cmd.upper().rstrip(' \t\r\n\0') == 'DOWN':
                    # Send [DOWN] key command
                    return_text = self.press_key(Key.DOWN_KEY, Key.SHORT_PRESS)
                    if len(return_text) == 4 and return_text[0:2] == 'KE':
                        print('key: Down (short)')
                elif cmd.upper().rstrip(' \t\r\n\0') in \
                        ['POWER OFF', 'POWEROFF', 'SHUT DOWN', 'SHUTDOWN', \
                            'SHUT OFF', 'SHUTOFF', 'POWER']:
                    # Send [POWER] key command
                    return_status = self.trigger_power_off()
                    if return_status:
                        print('key: On/Off (long)')
                elif cmd.upper().rstrip(' \t\r\n\0') == 'BOLUS':
                    # Send [BOLUS] key command
                    return_text = self.press_key(Key.BOLUS_KEY, Key.SHORT_PRESS)
                    if len(return_text) == 4 and return_text[0:2] == 'KE':
                        print('key: Bolus (short)')
                elif cmd.upper().rstrip(' \t\r\n\0') == 'MUTE':
                    # Send [RUN/STOP] key command
                    return_text = self.press_key(Key.RUN_KEY, Key.SHORT_PRESS)
                    if len(return_text) == 4 and return_text[0:2] == 'KE':
                        print('key: Run/Stop (short)')
                # ==============================================
                elif cmd.lower().rstrip(' \t\r\n\0') in ['enable s9']:
                    # Enable [S9] Command
                    self.enable_s9_command()
                elif cmd.lower().rstrip(' \t\r\n\0') in ['disable s9']:
                    # Disable [S9] Command
                    self.disable_s9_command()
                # ==============================================
                elif cmd.lower().rstrip(' \t\r\n\0') in ['start em', 'run em']:
                    # Run [Event Log Monitor]
                    self.run_event_log_monitor()
                elif cmd.lower().rstrip(' \t\r\n\0') == 'stop em':
                    # Stop [Event Log Monitor]
                    self.stop_event_log_monitor()
                elif cmd.lower().rstrip(' \t\r\n\0') == 'status em':
                    # Check [Event Log Monitor] Status
                    result = self.check_event_log_monitor_status()
                    if result:
                        print('Event log monitor: [On]')
                    else:
                        print('Event log monitor: [Off]')
                # ==============================================
                elif cmd.lower().rstrip(' \t\r\n\0') in ['start im', 'run im']:
                    # Run [Infusion Monitor]
                    self.run_infusion_monitor()
                elif cmd.lower().rstrip(' \t\r\n\0') in ['stop im']:
                    # Stop [Infusion Monitor]
                    self.stop_infusion_monitor()
                elif cmd.lower().rstrip(' \t\r\n\0') == 'status im':
                    # Check [Infusion Monitor] Status
                    result = self.check_infusion_monitor_status()
                    if result:
                        print('Infusion monitor: [On]')
                    else:
                        print('Infusion monitor: [Off]')
                # ==============================================
                elif cmd.lower().rstrip(' \t\r\n\0') in ['start ss', 'run ss']:
                    # Run [Socket Server]
                    self.run_socket_server()
                elif cmd.lower().rstrip(' \t\r\n\0') in ['stop ss']:
                    # Stop [Socket Server]
                    self.stop_socket_server()
                elif cmd.lower().rstrip(' \t\r\n\0') == 'status ss':
                    # Check [Socket Server] Status
                    result = self.check_socket_server_status()
                    if result: 
                        self.socket_server.status()
                    else:
                        print('Socket Server: [Off]')
                # ==============================================
                elif re.match(r'(pin)(\s+)(\d{3})', cmd.lower().rstrip(' \t\r\n\0')):
                    # Input PIN number
                    pin_number = re.match(r'(pin)(\s+)(\d{3})', cmd.lower().rstrip(' \t\r\n\0'))[3]
                    print('Input PIN number [{}]...'.format(pin_number))
                    time.sleep(_TIMEOUT * 10)
                    #
                    self.input_digits(pin_number)
                elif cmd.lower().rstrip(' \t\r\n\0') in ['wk', 'write key']:
                    # Write AES Key (written by Leyang Yu)
                    print('Write AES Key...')
                    old_key = input('Please input current AES key: ')
                    new_key = input('Please input new AES key: ')
                    status = self.write_aes_encrypt_key(old_key, new_key)
                    if len(status) == 0:
                        print('Key length incorrect, please try again.')
                    elif status[2] == '0':
                        print("Key successfully changed to: ", new_key)
                        with open("new_key.key", "w") as text_file:
                            print("{}".format(new_key), file=text_file)
                    elif status[2] == '1':
                        print("Key change failed, please check your old key.")
                elif cmd.lower().rstrip(' \t\r\n\0') in ['rc', 'read clock']:
                    # Read Pump Time
                    pump_time_str = self.read_pump_time()
                    if len(pump_time_str) == 10:
                        # The pump time is in normal format
                        # print(pump_time_str)
                        day = str(int(pump_time_str[0:2], 16)).zfill(2)
                        month = str(int(pump_time_str[2:4], 16)).zfill(2)
                        year = str(int(pump_time_str[4:6], 16) + 2000).zfill(2)
                        hour = str(int(pump_time_str[6:8], 16)).zfill(2)
                        minute = str(int(pump_time_str[8:10], 16)).zfill(2)
                        second = str(int(pump_time_str[10:12], 16)).zfill(2)
                        print('{0}-{1}-{2} {3}:{4}:{5}'.format(year, month, day, hour, minute, second))
                        print("Read pump time - Done!")
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
                        print("Read pump age - Done!")
                    else:
                        print('Error: read pump time failed')
                elif cmd.lower().rstrip(' \t\r\n\0') in ['wc', 'write clock']:
                    # Write Pump Time
                    status = self.write_pump_time()
                    if status:
                        current_date_time = datetime.datetime.now()
                        current_date = datetime.date(current_date_time.year, current_date_time.month, current_date_time.day)
                        current_time = datetime.time(current_date_time.hour, current_date_time.minute, current_date_time.second)
                        print('{0} {1}'.format(current_date, current_time))
                        print("Write pump time - Done!")
                    else:
                        print('Error: write pump time failed')
                elif re.match(r'(wc)(\s+)(\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d)', cmd.lower().rstrip(' \t\r\n\0')):
                    # Write Arbitrary Pump Time in the format of [YYYY-MM-DD HH:MM:SS]
                    re_match_result = re.match(r'(wc)(\s+)(\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d)', cmd.lower().rstrip(' \t\r\n\0'))
                    time_stamp = re_match_result[3]
                    status = self.write_pump_time(time_stamp)
                    if status:
                        print('{}'.format(time_stamp))
                        print("Write pump time - Done!")
                    else:
                        print('Error: write pump time failed')
                elif cmd.lower().rstrip(' \t\r\n\0') in ['wr', 'reset pump']:
                    # Reset Pump Total VINF and Total ON Time
                    print("Reset pump ...")
                    status = self.reset_pump()
                    if status:
                        print("Reset service total volume infused - Done!")
                        print("Reset service total ON time - Done!")
                    else:
                        print('Error: reset pump failed')
                elif cmd.lower().rstrip(' \t\r\n\0') in ['sc', 'send command']:
                    # Send Generic Command
                    print('Enter command to send: ', end='')
                    sent_text = input('').upper()
                    return_text = self.query(sent_text)
                    print(return_text)
                elif cmd.lower().rstrip(' \t\r\n\0') in ['rm', 'read platform']:
                    # Read Platform (H and K pump only)
                    platform = self.read_platform()
                    if platform != '':
                        print('pump platform: [{}]'.format(platform))
                    else:
                        print('Error: read pump platform failed')
                elif cmd.lower().rstrip(' \t\r\n\0') in ['wm', 'write platform']:
                    # Write Platform (H and K pump only)
                    print('Enter Pump Platform (H or K): ', end='')
                    platform = input('').upper()
                    status = self.write_platform(platform)
                    if status:
                        print("Write pump platform - Done!")
                    else:
                        print('Error: write pump platform failed')
                elif cmd.lower().rstrip(' \t\r\n\0') in ['gs', 'generate screenshot']:
                    # Send Generate Screenshot Command
                    print('Enter screenshot bitmap file (.txt|.json): ', end='')
                    screenshot_file_path = input('')
                    if path.exists(screenshot_file_path):
                        if screenshot_file_path[-3:] == 'txt':
                            bitmap = file_to_list(screenshot_file_path)
                            screenshot_image_path = screenshot_file_path[:-3] + 'png'
                            abs_file_path = bitmap_to_image(bitmap, screenshot_image_path)
                            print('     Screenshot image saved: [{}]'.format(abs_file_path))
                        elif screenshot_file_path[-4:] == 'json':
                            screenshot_with_masks = load_json_file(screenshot_file_path)
                            bitmap = screenshot_with_masks['bitmap']
                            masks = screenshot_with_masks['masks']
                            screenshot_image_path = screenshot_file_path[:-4] + 'png'
                            abs_file_path = bitmap_to_image(bitmap, screenshot_image_path, masks)
                            print('     Screenshot image saved: [{}]'.format(abs_file_path))
                        else:
                            print('     Abort - invalid screenshot file: [{}]'.format(screenshot_file_path))
                    else:
                        print('Abort - screenshot file NOT exist: [{}]'.format(screenshot_file_path))
                # ==============================================
                elif cmd.lower().rstrip(' \t\r\n\0') in ['wt00', 'trigger power off']:
                    # Trigger Power Off (Miva pump only)
                    return_text = self.query('WT00')
                    print(return_text)
                elif cmd.lower().rstrip(' \t\r\n\0') in ['wt01', 'trigger run infusion']:
                    # Trigger Run Infusion (Miva pump only)
                    return_text = self.query('WT01')
                    print(return_text)
                elif cmd.lower().rstrip(' \t\r\n\0') in ['wt02', 'trigger stop infusion']:
                    # Trigger Stop Infusion (Miva pump only)
                    return_text = self.query('WT02')
                    print(return_text)
                # ==============================================
                elif re.match(r'(:)(infu(sion)?)(:)(mode)(\?)', cmd):
                    # Query Infusion Mode 
                    # Command -- ':INFU(sion):MODE?'
                    infution_mode = self.get_infusion_mode()
                    print(infution_mode)
                elif re.match(r'(:)(infu(sion)?)(:)(time)(\?)', cmd.lower()):
                    # Query Infusion Time in Seconds? 
                    # Command -- ':INFU(sion):TIME?'
                    infusion_time = self.get_infusion_time()
                    print('{0}'.format(infusion_time))
                    # print('type(infusion_time) == {0}'.format(type(infusion_time)))
                elif re.match(r'(:)(infu(sion)?)(:)(rate)(:)(unit)(\?)', cmd.lower()):
                    # Query Infusion Rate Unit? 
                    # Command -- ':INFUsion:RATE:UNIT?'
                    infusion_rate_unit = '\"' + self.get_infusion_rate_unit() + '\"' 
                    print('{0}'.format(infusion_rate_unit))
                elif re.match(r'(:)(infu(sion)?)(:)(vinf)(\?)', cmd.lower()):
                    # Query Infusion Volume Infused (VINF)? 
                    # Command -- ':INFU(sion):VINF?'
                    infusion_vinf = self.get_infusion_vinf()
                    print('{0}'.format(infusion_vinf))
                elif re.match(r'(:)(infu(sion)?)(:)(vtbi)(\?)', cmd.lower()):
                    # Query Infusion Volume To Be Infused (VTBI)? 
                    # Command -- ':INFU(sion):VTBI?'
                    infusion_vtbi = self.get_infusion_vtbi()
                    print('{0}'.format(infusion_vtbi))
                elif re.match(r'(:)(infu(sion)?)(:)(bol(us)?)(:)(run(ning)?)(\?)', cmd.lower()):
                    # Query Is BOLUS Running?
                    # Command -- ':INFU(sion):BOL(us):RUN(ning)?'
                    bool_bolus_running = self.is_bolus_running()
                    print(bool_bolus_running)
                elif re.match(r'(:)(infu(sion)?)(:)(bol(us)?)(:)(rate)(\?)', cmd.lower()):
                    # Query BOLUS Rate?
                    # Command -- ':INFU(sion):BOL(us):RATE?'
                    bolus_rate = self.get_bolus_rate()
                    print(bolus_rate)
                elif re.match(r'(:)(infu(sion)?)(:)(bol(us)?)(:)(vinf)(\?)', cmd.lower()):
                    # Query BOLUS Volume Infused (VINF)? 
                    # Command -- ':INFU(sion):BOL(us):VINF?'
                    bolus_vinf = self.get_bolus_vinf()
                    print(bolus_vinf)
                elif re.match(r'(:)(infu(sion)?)(:)(bol(us)?)(:)(vtbi)(\?)', cmd.lower()):
                    # Query BOLUS Volume To Be Infused (VTBI)? 
                    # Command -- ':INFU(sion):BOL(us):VTBI?'
                    bolus_vtbi = self.get_bolus_vtbi()
                    print(bolus_vtbi)
                elif re.match(r'(:)(prot(ocol)?)(:)(rate)(:)(unit)(\?)', cmd.lower()):
                    # Query Protocol Rate Unit? 
                    # Command -- ':PROT(ocol):RATE:UNIT?'
                    protocol_rate_unit = self.get_protocol_rate_unit()
                    print('{0}'.format(protocol_rate_unit))
                elif re.match(r'(:)(prot(ocol)?)(:)(vtbi)(\?)', cmd.lower()):
                    # Query Protocol Volume To Be Infused (VTBI)?  
                    # Command -- ':PROT(ocol):VTBI?'
                    protocol_vtbi = self.get_protocol_vtbi()
                    print(protocol_vtbi)
                elif re.match(r'(:)(prot(ocol)?)(:)(time)(\?)', cmd.lower()):
                    # Query Protocol Time in Seconds? 
                    # Command -- ':PROT(ocol):TIME?'
                    protocol_time = self.get_protocol_time()
                    print('{0}'.format(protocol_time))
                elif re.match(r'(:)(prot(ocol)?)(:)(time)(:)(unit)(\?)', cmd.lower()):
                    # Query Protocol Time Unit? 
                    # Command -- ':PROT(ocol):TIME:UNIT?'
                    protocol_time_unit = self.get_protocol_time_unit()
                    print('{0}'.format(protocol_time_unit))
                elif re.match(r'(:)(prot(ocol)?)(:)(bol(us)?)(:)(rate)(\?)', cmd.lower()):
                    # Query Protocol BOLUS Rate?
                    # Command -- ':PROT(ocol):BOL(us):RATE?'
                    protocol_bolus_rate = self.get_protocol_bolus_rate()
                    print(protocol_bolus_rate)
                elif re.match(r'(:)(prot(ocol)?)(:)(auto)(:)(bol(us)?)(:)(vtbi)(\?)', cmd.lower()):
                    # Query Protocol Auto BOLUS Volume To Be Infused (VTBI)?  
                    # Command -- ':PROT(ocol):AUTO:BOL(us):VTBI?'
                    protocol_auto_bolus_vtbi = self.get_protocol_auto_bolus_vtbi()
                    print(protocol_auto_bolus_vtbi)
                elif re.match(r'(:)(prot(ocol)?)(:)(dem(and)?)(:)(bol(us)?)(:)(vtbi)(\?)', cmd.lower()):
                    # Query Protocol Demand BOLUS Volume To Be Infused (VTBI)?  
                    # Command -- ':PROTocol:DEMand:BOLus:VTBI?'
                    protocol_demand_bolus_vtbi = self.get_protocol_demand_bolus_vtbi()
                    print(protocol_demand_bolus_vtbi)
                elif re.match(r'(:)(power)', cmd.lower()):
                    # Send [POWER] key command
                    return_status = self.trigger_power_off()
                    if return_status:
                        print('key: On/Off (long)')
                elif re.match(re_query_event_list, cmd.lower()):
                    # Query Event Log List
                    # Command -- ':EVENTlog:{number_to_query}?'
                    re_match_result = re.match(re_query_event_list, cmd.lower())
                    num_to_query = int(re_match_result[5])
                    eventlog_list = self.get_eventlog_list(num_to_query)
                    print()
                    print(eventlog_list)
                elif re.match(re_get_key_list, cmd.lower()):
                    # Get key press list from the pump 
                    # Command -- ':KEY:LIST?'
                    re_match_result = re.match(re_get_key_list, cmd.lower())
                    sent_text = ':KEY:LIST?'
                    return_text = self.query(sent_text)
                    raw_key_lsit = []
                    for i in range(int(len(return_text) / 2)):
                        raw_key_lsit.append(return_text[2 * i:2 * i + 2])
                    print('len = {}'.format(len(raw_key_lsit)))
                    print('{}'.format(raw_key_lsit))
                    key_list = parse_key_list(return_text)
                    print('{}'.format(key_list))
                    # the path the key list will be saved to
                    # print('re_match_result[8] = {}'.format(re_match_result[8]))
                    # print('re_match_result[10] = {}'.format(re_match_result[10]))
                    if re_match_result[8] == '>' and re_match_result[10] is not None:
                        key_list_path = re_match_result[10]
                        abs_file_path = list_to_file(key_list, key_list_path)
                        print('     Key list saved: [{}]'.format(abs_file_path))
                elif re.match(re_clear_key_list, cmd.lower()):
                    # Get key press list from the pump 
                    # Command -- ':KEY:LIST:CLEAR'
                    re_match_result = re.match(re_get_key_list, cmd.lower())
                    sent_text = ':KEY:LIST:CLEAR'
                    return_text = self.query(sent_text)
                    raw_key_lsit = []
                    for i in range(int(len(return_text) / 2)):
                        raw_key_lsit.append(return_text[2 * i:2 * i + 2])
                    print('len = {}'.format(len(raw_key_lsit)))
                    print('{}'.format(raw_key_lsit))
                    key_list = parse_key_list(return_text)
                    print('{}'.format(key_list))
                elif re.match(re_scpi_common_cmd, cmd.lower()):
                    # SCPI common commands, such as:
                    # *idn?
                    return_msg = self.send_command(cmd)
                    if type(return_msg) in [dict]:
                        return_msg = json.dumps(return_msg)
                    elif type(return_msg) in [str]:
                        return_msg = '\"' + return_msg + '\"'
                    print(return_msg)
                elif re.match(re_scpi_get_cmd, cmd.lower()):
                    # SCPI get commands, such as:
                    # :protocol:rate?
                    # :key:list?
                    # :screen?
                    return_msg = self.send_command(cmd)
                    if type(return_msg) in [dict]:
                        return_msg = json.dumps(return_msg)
                    elif type(return_msg) in [int]:
                        if re.match(re_query_lockout, cmd):
                            # Format an integer to [HH:MM] time string
                            if type(return_msg) in [int]:
                                return_msg = int_to_time_str(return_msg)
                    elif type(return_msg) in [str]:
                        return_msg = '\"' + return_msg + '\"'
                    print(return_msg)
                elif re.match(re_scpi_set_cmd, cmd.lower()):
                    # SCPI set commands, such as:
                    # :protocol:rate 20.0
                    # :key:list:clear
                    return_msg = self.query(cmd.upper())
                    # print(cmd.upper())
                    print(return_msg)
                # ==============================================
                elif re.match(re_get_screenshot, cmd.lower()):
                    # Get screenshot from the pump 
                    # Command -- 'SCREENshot'
                    # r'(screen(shot)?)((\s+)?(>)(\s+)?([a-z0-9_]+\.txt))?$'
                    re_match_result = re.match(re_get_screenshot, cmd.lower())
                    screenshot_hex_list = self.get_screenshot_hex_list()
                    screenshot_bitmap = hex_to_bitmap(screenshot_hex_list)
                    print('{}\u00D7{}'.format(len(screenshot_bitmap), len(screenshot_bitmap[0])))
                    # the path the screenshot hex list will be saved to
                    # print('re_match_result[5] = {}'.format(re_match_result[5]))
                    # print('re_match_result[7] = {}'.format(re_match_result[7]))
                    if re_match_result[5] == '>' and re_match_result[7] is not None:
                        if re_match_result[7][-3:] == 'txt':
                            screenshot_bitmap_path = re_match_result[7]
                            abs_file_path = list_to_file(screenshot_bitmap, screenshot_bitmap_path)
                            print('     Screenshot bitmap saved: [{}]'.format(abs_file_path))
                        elif re_match_result[7][-4:] == 'json':
                            screenshot_with_masks_path = re_match_result[7]
                            screenshot_with_masks = {
                                                    'masks':[{'name':'battery_mask',
                                                              'row':5,
                                                              'column':113,
                                                              'width':13,
                                                              'height':6},
                                                             {'name': 'progress_bar',
                                                              'row': 25,
                                                              'column': 33,
                                                              'width': 63,
                                                              'height': 6}],
                                                    'bitmap':screenshot_bitmap
                                                    }
                            abs_file_path = json_to_file(screenshot_with_masks, screenshot_with_masks_path)
                            print('     Screenshot with masks saved: [{}]'.format(abs_file_path))
                        elif re_match_result[7][-3:] in ['png', 'jpg']:
                            image_file_path = re_match_result[7]
                            abs_file_path = bitmap_to_image(screenshot_bitmap, image_file_path)
                            print('     Screenshot image saved: [{}]'.format(abs_file_path))
                elif re.match(re_compare_screenshot, cmd.lower()):
                    # Compare screenshot from the pump with the bitmaps file
                    # r'(screen(shot)?)(\s+)?(==)(\s+)?(.+\.(txt))?$'
                    re_match_result = re.match(re_compare_screenshot, cmd.lower())
                    screenshot_hex_list = self.get_screenshot_hex_list()
                    screenshot_bitmap = hex_to_bitmap(screenshot_hex_list)
                    print('{}\u00D7{}'.format(len(screenshot_bitmap), len(screenshot_bitmap[0])))
                    # print('type(screenshot_bitmap) = {}'.format(type(screenshot_bitmap)))
                    # print('len(screenshot_bitmap) = {}'.format(len(screenshot_bitmap)))
                    # print('len(screenshot_bitmap[0]) = {}'.format(len(screenshot_bitmap[0])))
                    screenshot_file_path = re_match_result[6]
                    if path.exists(screenshot_file_path):
                        file_equal = False
                        # Get Screenshot Bitmap Reference
                        if screenshot_file_path[-3:] == 'txt':
                            # Save screenshot to .txt
                            realtime_screenshot_file_path = screenshot_file_path[:-4] + '_realtime' + screenshot_file_path[-4:]
                            abs_file_path = list_to_file(screenshot_bitmap, realtime_screenshot_file_path)
                            print('     Screenshot saved: [{}]'.format(abs_file_path))
                            file_equal = compare_file_equal(abs_file_path, screenshot_file_path)
                        elif screenshot_file_path[-4:] == 'json':
                            bitmap_with_mask = load_json_file(screenshot_file_path)
                            bitmap_to_compare = bitmap_with_mask['bitmap']
                            bitmap_masks = bitmap_with_mask['masks']
                            screenshot_bitmap = apply_screenshot_masks(screenshot_bitmap, bitmap_masks)
                            bitmap_to_compare = apply_screenshot_masks(bitmap_to_compare, bitmap_masks)
                            if screenshot_bitmap == bitmap_to_compare:
                                file_equal = True
                        elif screenshot_file_path[-3:] in ['jpg', 'png']:
                            # Save screenshot to .jpg | .png
                            realtime_screenshot_file_path = screenshot_file_path[:-4] + '_realtime' + screenshot_file_path[-4:]
                            abs_file_path = bitmap_to_image(screenshot_bitmap, realtime_screenshot_file_path)
                            print('     Screenshot saved: [{}]'.format(abs_file_path))
                            file_equal = compare_file_equal(abs_file_path, screenshot_file_path)
                        # Compare Screenshot Bitmap Against Reference
                        if file_equal:
                            print('Screenshot compare result: EQUAL')
                        else:
                            if screenshot_file_path[-3:] in ['txt', 'jpg', 'png']:
                                print('Screenshot compare Result: NOT EQUAL')
                            else:
                                not_equal_position = []
                                for i in range(len(screenshot_bitmap)):
                                    for j in range(len(screenshot_bitmap[i])):
                                        if screenshot_bitmap[i][j] != bitmap_to_compare[i][j]:
                                            not_equal_position.append(i)
                                            not_equal_position.append(j)
                                            print('Screenshot compare Result: NOT EQUAL starting from {}'.format(not_equal_position))
                                            break;
                                    if not_equal_position != []:
                                        break
                # ==============================================
                elif re.match(re_checksum, cmd.lower()):
                    # Checksum Configuration
                    # r'^(checksum)((status)|(\s+(good|bad)))$'
                    re_match_result = re.match(re_checksum, cmd.lower())
                    if re_match_result[2] == 'status':
                        if self.checksum_symbol == '+':
                            print('good')
                        else:
                            print('bad')
                    elif re_match_result[2] == 'good':
                        self.checksum_symbol = '+'
                        print('checksum set to [good]')
                    elif re_match_result[2] == 'bad':
                        self.checksum_symbol = '^'
                        print('checksum set to [bad]')
                # ==============================================
                elif cmd.lower().rstrip(' \t\r\n\0') in ['ll', 'load library']:
                    # LL - Load Library (to the pump simulator)
                    if library.get_library() is not None:
                        print("currently loaded library: ")
                        # Title
                        print("    {0:5s}    |    {1:5s}    |    {2:15s}    "\
                                .format('id', 'ver.', 'name'))
                        print("----{0:5s}----|----{1:5s}----|----{2:15s}----"\
                                .format('-----', '-----', '---------------'))
                        # Content
                        print("    {0:5s}    |    {1:5s}    |    {2:15s}"\
                                .format(str(library.get_id()), \
                                        str(library.get_version()), \
                                        library.get_name()))
                        lib_path = input('Enter NEW library path: ')
                    else:
                        lib_path = input('    Enter library path: ')
                    if path.exists(lib_path):
                        library.load(lib_path)
                        print("library: ")
                        # Title
                        print("    {0:5s}    |    {1:5s}    |    {2:15s}    "\
                                .format('id', 'ver.', 'name'))
                        print("----{0:5s}----|----{1:5s}----|----{2:15s}----"\
                                .format('-----', '-----', '---------------'))
                        # Content
                        print("    {0:5s}    |    {1:5s}    |    {2:15s}"\
                                .format(str(library.get_id()), \
                                        str(library.get_version()), \
                                        library.get_name()))
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
                elif cmd.lower().rstrip(' \t\r\n\0') in ['sp', 'select protocol']:
                    # SP - Select Protocol (on the pump simulator and on the pump)
                    if library.get_library() is None:
                        # No library loaded
                        print('empty libarary: use <ll> command to load libarary first')
                        continue
                    #
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
                        print("{:15s}    |    "\
                                .format(each_protocol['content']['name']), end='')
                        print("{:20s}".format(each_protocol['content']['deliveryMode']))
                    print("Total [{}] protocols extracted".format(len(protocols)))
                    #
                    protocol_name = self.protocol_name
                    # MUST BE DEEP COPY
                    protocol = copy.deepcopy(library.get_protocol(protocol_name))
                    infusion.patient_weight = None
                    if protocol is not None:
                        self.infusion.set_protocol(protocol)
                        # self.protocol = protocol
                        print()
                        print("Currently selected protocol: ")
                        print()
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
                        print()
                        print("Extracted Parameters:")
                        print()
                        if protocol['content']['deliveryMode'] == 'continuousInfusion':
                            infusion.print_cont_parameters()
                        if protocol['content']['deliveryMode'] == 'bolusInfusion':
                            infusion.print_bolus_parameters()
                        if protocol['content']['deliveryMode'] == 'intermittentInfusion':
                            infusion.print_int_parameters()
                        print()
                        protocol_name = input('Enter NEW protocol name / id: ') or self.protocol_name
                    else:
                        protocol_name = input('    Enter protocol name / id: ')
                    #
                    if library.get_protocol(protocol_name) is None:
                        print('    Invalid Protocol: \'{}\''.format(protocol_name))
                        continue
                    while self.protocol_name != protocol_name:
                        self.protocol_name = protocol_name
                        infusion.patient_weight = None
                        # MUST BE DEEP COPY
                        protocol = copy.deepcopy(library.get_protocol(protocol_name))
                        infusion.set_protocol(protocol)
                        print()
                        print("Newly selected protocol: ")
                        print()
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
                        print()
                        print("Extracted Parameters:")
                        print()
                        if protocol['content']['deliveryMode'] == 'continuousInfusion':
                            infusion.print_cont_parameters()
                        if protocol['content']['deliveryMode'] == 'bolusInfusion':
                            infusion.print_bolus_parameters()
                        if protocol['content']['deliveryMode'] == 'intermittentInfusion':
                            infusion.print_int_parameters()
                        print()    
                        protocol_name = input('Enter NEW protocol name / id: ') or self.protocol_name
                        if library.get_protocol(protocol_name) is None:
                            break

                    if library.get_protocol(protocol_name) is None:
                        print('    Invalid Protocol: \'{}\''.format(protocol_name))
                        continue
                    #
                    self.pump_config["protocol_selected"] = protocol_name
                    json_to_file(self.pump_config, self.pump_config_path)
                    # #
                    # patient_weight = infusion.patient_weight
                    # Select Protocol on Pump
                    self.select_protocol(library, protocol)
                    # # Select [Weight] Parameter on Pump
                    # result = self.select_parameter(library, protocol, 'weight')
                    # # Set [Weight] Parameter Value on Pump
                    # if result:
                        # print('==')
                        # print('Set [Weight] to [{:.1f}] Kg...'.format(patient_weight))
                        # time.sleep(_TIMEOUT * 10)
                        # parameter_weight = {}
                        # parameter_weight['length'] = 4
                        # parameter_weight['fract_length'] = 1
                        # parameter_weight['value'] = 0
                        # parameter_weight['name'] = 'weight'
                        # parameter_weight['max'] = 999.9
                        # parameter_weight['min'] = 1.0
                        # parameter_weight['unit'] = 'kg'
                        # self.set_parameter_value(patient_weight, parameter_weight)
                    # # Return to top of the parameter list
                    # self.return_top(library, protocol, 'weight')
                    # Ask the user if he want to chagne the infusion parameters
                    change_parameters = input('Change existing parameters? (y/n): ') or 'y'
                    if change_parameters != 'y':
                        continue
                    # display infusion parameters with the default values
                    print("Extracted Parameters:")
                    if protocol['content']['deliveryMode'] == 'continuousInfusion':
                        infusion.print_cont_parameters()
                    if protocol['content']['deliveryMode'] == 'bolusInfusion':
                        infusion.print_bolus_parameters()
                    if protocol['content']['deliveryMode'] == 'intermittentInfusion':
                        infusion.print_int_parameters()
                    parameter_name = ''
                    while parameter_name not in ['quit', 'done']:
                        parameter_name = input('Enter parameter name to change (to finish, type \'done\' ): ')
                        parameter_list = get_parameter_list(library, protocol)
                        if parameter_name not in parameter_list \
                                and parameter_name not in ['drugAmount', 'diluteVolume']:
                            print('    Invalid parameter name: {}'.format(parameter_name))
                            continue
                        if parameter_name in ['drug', 'label']:
                            print('    Abort: [{}] is NOT editable'.format(parameter_name))
                            continue
                        if parameter_name == 'concentration':
                            if protocol['content']['drug']['content']['concentrationImmutable']:
                                print('    Abort: concentration is NOT editable')
                                continue
                            else:
                                print('    Abort: concentration is NOT editable'.format(parameter_name))
                                print('           type \'drugAmount\' or \'diluteVolume\' instead')
                                continue
                            
                        # get parameter original, max, min values and unit
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
                            new_value_str = input('Input NEW value of [{0}] ({1:.0f} {2}):'\
                                    .format(parameter_name, original_value, unit)) or str(original_value)
                            new_value_str = int(float(new_value_str))
                            new_value_str = str(new_value_str)
                        else: 
                            new_value_str = input('Input NEW value of [{0}] ({1:.2f} {2}):'\
                                    .format(parameter_name, original_value, unit)) or str(original_value)
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
                            continue
                        if new_value == original_value:
                            print('Abort: two values are equal')
                            continue
                        # select [Parameter] on the pump
                        result = self.select_parameter(library, protocol, parameter_name)
                        if result:
                            print('==')
                            print('Set [{0}] to [{1:.2f}] {2}...'.format(parameter_name, new_value, unit))
                            time.sleep(_TIMEOUT * 10)
                            # Set [Parameter] Value on Pump
                            self.set_parameter_value(new_value, parameter)
                            # Update [Parameter] value
                            if parameter_name == 'weight':
                                infusion.patient_weight = new_value
                            elif parameter_name in ['drugAmount', 'diluteVolume']:
                                protocol['content']['drug']['content'][parameter_name]['value'] = new_value
                            else:
                                protocol['content']['program'][parameter_name]['value'] = new_value
                            #
                        # Return to top of the [Parameter] list
                        self.return_top(library, protocol, parameter_name)
                        # Display infusion parameters
                        print("==")
                        print("Extracted Parameters:")
                        if protocol['content']['deliveryMode'] == 'continuousInfusion':
                            infusion.print_cont_parameters()
                        if protocol['content']['deliveryMode'] == 'bolusInfusion':
                            infusion.print_bolus_parameters()
                        if protocol['content']['deliveryMode'] == 'intermittentInfusion':
                            infusion.print_int_parameters()
                        #
                        # if patient_weight != infusion.patient_weight:
                            # patient_weight = infusion.patient_weight
                            # # Select [Weight] Parameter on Pump
                            # result = self.select_parameter(library, protocol, 'weight')
                            # # Set [Weight] Parameter Value on Pump
                            # if result:
                                # print('==')
                                # print('Set [Weight] to [{:.1f}] Kg...'.format(patient_weight))
                                # time.sleep(_TIMEOUT * 10)
                                # parameter_weight = {}
                                # parameter_weight['length'] = 4
                                # parameter_weight['fract_length'] = 1
                                # parameter_weight['value'] = 0
                                # parameter_weight['name'] = 'weight'
                                # parameter_weight['max'] = 999.9
                                # parameter_weight['min'] = 1.0
                                # parameter_weight['unit'] = 'kg'
                                # self.set_parameter_value(patient_weight, parameter_weight)
                        # # Return to top of the [Parameter] list
                        # self.return_top(library, protocol, parameter_name)
                elif cmd.lower().rstrip(' \t\r\n\0') in ['rp', 'run protocol']:
                    # RP - Run Protocol (on the pump)
                    if library.get_library() is not None:
                        if protocol is not None:
                            protocl_name = protocol['content']['name']
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
                            print()
                            start_yes_no = input("run protocol - [{}]? (y/n): "\
                                    .format(protocl_name))
                            if start_yes_no.lower().find('y') != -1 or start_yes_no == '':
                                print('infusion start...')
                                # Run Protocol on the Pump
                                self.run_protocol(self.library, protocol)
                                # infusion.run_infusion()
                                if infusion.status in [InfusionStatus.PAUSED_AUTO_BOLUS, \
                                                       InfusionStatus.PAUSED_DEMAND_BOLUS, \
                                                       InfusionStatus.PAUSED_LOADING_DOSE, \
                                                       InfusionStatus.PAUSED_CLINICIAN_DOSE]:
                                    self.infusion_monitor.output_enabled = False
                                    print()
                                    resume_dose = input('resume dose? (y/n)') or 'y'
                                    if resume_dose == 'y':
                                        print('==')
                                        print('resume dose...')
                                        time.sleep(_TIMEOUT * 10)
                                        # Press [Ok] Key
                                        return_text = self.press_key(Key.OK_KEY, Key.SHORT_PRESS)
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
                                        return_text = self.press_key(Key.DOWN_KEY, Key.SHORT_PRESS)
                                        if len(return_text) == 4 and return_text[0:2] == 'KE':
                                            print('key: Down (short)')
                                        time.sleep(_TIMEOUT * 10) 
                                        # Press [Ok] Key
                                        return_text = self.press_key(Key.OK_KEY, Key.SHORT_PRESS)
                                        if len(return_text) == 4 and return_text[0:2] == 'KE':
                                            print('key: Ok/Enter (short)')
                                        time.sleep(_TIMEOUT * 10)
                                    self.infusion_monitor.output_enabled = True
                                        
                            else:
                                print('infusion aborted...')
                        else:
                            print('Empty Protocol: Use <SP> command to select protocol first.')
                    else:
                        print('Empty Library: Use <LL> command to load library first.')
                elif cmd.lower().rstrip(' \t\r\n\0') in ['cd', 'clinician dose']:
                    # Run [Clinician Dose] on the Pump
                    clinician_code = library.get_access_code('clinician')
                    switches = protocol['content']['program']['switches']
                    if switches.get('clinicianDose') and switches['clinicianDose']:
                        # Get the platform of the pump
                        platform = self.read_platform()
                        if platform in ['H', 'K']:
                            if infusion.status in \
                                  [InfusionStatus.RUNNING_AUTO_BOLUS, \
                                   InfusionStatus.RUNNING_DEMAND_BOLUS, \
                                   InfusionStatus.RUNNING_LOADING_DOSE]:
                                print('clinician dose NOT granted: infusion status = {}'\
                                        .format(infusion.previous_status.name))
                            else:
                                self.run_clinician_dose(clinician_code)
                        elif platform == 'C':
                            if infusion.status in [InfusionStatus.PAUSED_MPH_REACHED, \
                                                   InfusionStatus.PAUSED_MPI_REACHED] \
                                    and infusion.previous_status in \
                                                  [InfusionStatus.RUNNING_AUTO_BOLUS, \
                                                   InfusionStatus.RUNNING_DEMAND_BOLUS, \
                                                   InfusionStatus.RUNNING_LOADING_DOSE]:
                                print('clinician dose NOT granted: previous infusion status = {}'\
                                        .format(infusion.previous_status.name))
                            elif infusion.status in \
                                                  [InfusionStatus.RUNNING_AUTO_BOLUS, \
                                                   InfusionStatus.RUNNING_DEMAND_BOLUS, \
                                                   InfusionStatus.RUNNING_LOADING_DOSE]:
                                print('clinician dose NOT granted: infusion status = {}'\
                                        .format(self.status.name))
                            else:
                                self.run_clinician_dose(clinician_code)
                elif cmd.lower().rstrip(' \t\t\n\0') in ['ppl', 'parameter list']:
                    # Print Parameter List
                    parameter_list = get_parameter_list(library, protocol)
                    print('==')
                    print('Infusion Parameter List = {}'.format(parameter_list))
                elif cmd.lower().rstrip(' \t\r\n\0') in ['rtp', 'run test protocol']:
                    # rtp - Run Test Protocol
                    test_protocol_path = input('    Enter test protocol path: ').strip(' \t\r\n\0')
                    # Parse Test Protocol
                    test_protocol = test.parse_test_protocol(test_protocol_path)
                    if test_protocol != []:
                        # Stop Event Log monitor
                        self.stop_event_log_monitor()
                        # Stop Infusion Monitor
                        self.stop_infusion_monitor()
                        # Stop Socket Server
                        self.stop_socket_server()
                        # Run Test Protocol on Pump
                        test_result = test.run_test_protocol(miva, test_protocol)
                        # === Save Test Result ========================
                        test_protocol_name = path.basename(test_protocol_path)[:-4]
                        test_protocol_dir = path.dirname(test_protocol_path)
                        if test_protocol_dir == '':
                            test_protocol_dir = '.'
                        test_report_dir = test_protocol_dir + '/../test_report/'
                        # test_report_dir = self.pump_config['test_report_path']                        
                        if not path.exists(test_report_dir):
                            makedirs(test_report_dir)
                        time_stamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
                        if test_result['test_pass']:
                            test_report_name = 'Test_Report_[' + test_protocol_name + ']_' + time_stamp + '.txt'
                        else:
                            test_report_name = 'Test_Report_[' + test_protocol_name + ']_' + time_stamp + '_FAILED' + '.txt'
                        test_report_path = test_report_dir + test_report_name
                        abs_file_path = list_to_file(test_result['contents'], test_report_path)
                        print('Test report is saved to: [{}]'.format(abs_file_path))
                        # === Save Event Log ==========================
                        test_protocol_name = path.basename(test_protocol_path)[:-4]
                        test_protocol_dir = path.dirname(test_protocol_path)
                        if test_protocol_dir == '':
                            test_protocol_dir = '.'
                        event_log_dir = test_protocol_dir + '/../test_event_log/'
                        # event_log_dir = self.pump_config['event_log_path']                        
                        if not path.exists(event_log_dir):
                            makedirs(event_log_dir)
                        time_stamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
                        if test_result['test_pass']:
                            event_log_name = 'Event_Log_[' + test_protocol_name + ']_' + time_stamp + '.txt'
                        else:
                            event_log_name = 'Event_Log_[' + test_protocol_name + ']_' + time_stamp + '_FAILED' + '.txt'
                        event_log_path = event_log_dir + event_log_name
                        abs_file_path = json_to_file(test_result['event_logs'], event_log_path)
                        print('Event log is saved to: [{}]'.format(abs_file_path))
                        # Re-Start Event Log monitor
                        self.run_event_log_monitor()
                # ==============================================
                elif cmd in ['quit', 'status', 'db', 'bolus', 'cd', 'clinician dose', 'pause', 'parameters']:
                    # Run [Infusion Monitor] Command
                    pass
                # ==============================================
                # elif cmd.lower().rstrip(' \t\r\n\0') in ['clear', 'cls', 'ls', 'ls -l']:
                    # Run as system command
                    # system(cmd)
                else:
                    # Run as system command
                    system(cmd)
                # ==============================================
                if cmd in ['quit', 'status', 'pause', 'parameters']:
                    # Run [Infusion Monitor] Command
                    self.infusion_monitor.set_command(cmd)
                # ==============================================
                # Resume [Event Log Monitor]
                if self.event_log_monitor.is_on():
                    self.event_log_monitor.resume()
                # ==============================================
                # Enable [Infusion Monitor] Output
                self.infusion_monitor.enable_output()
            #
            print('Stopping Serial Port Connection...')
            self.close()
            print('Serial port stopped at [{}]'.format(time.strftime('%H:%M:%S', time.localtime())))
            print('==')
        except KeyboardInterrupt:
            print()
            print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))
        except serial.serialutil.SerialException:
            print()
            print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))
            traceback.print_exc()
        except (OSError, PermissionError, AttributeError):
            print()
            print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))
            raise
        except:
            raise
        finally:
            # Reset Infusion
            if self.infusion != None:
                self.infusion.reset()
            #
            print('stop event log monitor...')
            print('==')
            self.stop_event_log_monitor()
            #
            print('stop infusion monitor...')
            print('==')
            self.stop_infusion_monitor()
            #
            print('stop socket server...')
            print('==')
            self.stop_socket_server() 


def main(argv):
    '''main function'''
    try:
        current_file = path.basename(__file__)
        if len(argv) == 1:
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
            if re.match('com\d+', serial_port.lower().rstrip(' \t\r\n\0')):
                miva = Miva(serial_port)
                miva.start()
            else:
                print('Error: invalid port \'{}\' '.format(serial_port), end='')
                print('To start, type \'{}\' followed by the com port. '\
                        .format(current_file), end='')
                print('Ex: \'{} COM1\''.format(current_file))
    except KeyboardInterrupt:
        pass
    except serial.serialutil.SerialException:
        print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))


if __name__ == "__main__":
    main(sys.argv)
