'''Utility Module'''
import re
import sys
import time
import inspect
import json
import hashlib
import serial
import platform
import struct
from os import path, mkdir, system
from PIL import Image, ImageColor

re_time_str_format = r'(\d\d)(:)(\d\d)'
# Define Flash Structure the same as MIVA pump
FLASH_PAGE_SIZE = 4096
EVENT_LOG_NUMBER_OF_PAGES = 169
EVENT_LOG_SIZE = 16
# 4096 * 169 / 16 = 43264 (A900)
EVENT_LOG_NUMBER_OF_EVENTS = int((FLASH_PAGE_SIZE * EVENT_LOG_NUMBER_OF_PAGES) / EVENT_LOG_SIZE)
# Infusion Data Structure Occupies How Many Event Logs
EVENT_LOGS_PER_INFUSION_DATA_LOG = 16
# Define Regular Expressions
re_scpi_common_cmd = r'^\*[0-9a-zA-Z_]+(\?)?$'
re_scpi_get_cmd = r'^((:[0-9a-zA-Z_]+)+(\?))$'
re_scpi_set_cmd = r'^((:[a-zA-Z]+)+)(\s+)?(\d+)?(\.)?(\d+)?$'
re_get_key_list = r'(:)(key)(:)(list)(\?)((\s+)?(>)(\s+)?([a-z0-9_]+\.txt))?$'
re_get_screenshot = r'(screen(shot)?)((\s+)?(>)(\s+)?(.+\.(png|txt|jpg|json)))?$'
re_compare_screenshot = r'(screen(shot)?)(\s+)?(==)(\s+)?(.+\.(txt|json|jpg|png))?$'
re_query_screenshot_line = r':screen(shot)?:line:[0-8]\?'
re_checksum = r'^(checksum)\s+(status|good|bad)$'
re_clear_key_list = r'(:)(key)(:)(list)(:)(clear)$'
re_compare_parameters = r'^((:[a-zA-Z_]+)+(\?))(\s*)(==|>|>=|<=|<|!=)(\s*)(\S+)(\s+)?(delta(\s*)?==(\s*)?(\d+(\.\d*)?|\.\d+)(%)?)?(\s+)?$'
re_compare_list = r'((:[a-zA-Z]+)+(\?))(\s*)(==|>|>=|<=|<|!=)(\s*)(\[.*\])(\s*)'
re_query_event_timestamp = r'(:)(time(stamp)?)(:)([A-Za-z_]+)(\?)'
re_search_for_event = r'(:)(event(log)?)(:)([A-Za-z_]+)(\?)'
re_query_event_list = r'(:)(event(log)?)(:)(\d+)(\?)'
re_compare_dict_equal = r'^((:[a-zA-Z_]+)+(\?))(\s*)(==)(\s*)(\{.*\})(\s*)$'
re_compare_str = r'^((:[a-zA-Z_]+)+(\?))(\s*)(==|>|>=|<=|<|!=)(\s*)\"(.*)\"(\s+)?$' 
re_compare_str_equal = r'^((:[a-zA-Z_]+)+(\?))(\s*)(==)(\s*)\"(.*)\"(\s+)?$'
re_compare_scpi_return_number = r'^((:[a-zA-Z_]+)+(\?))(\s*)(==|>|>=|<=|<|!=)(\s*)((:[a-zA-Z_]+)+(\?))(\s+)?(delta(\s*)?==(\s*)?(\d+(\.\d*)?|\.\d+)(%)?)?(\s+)?$'
re_query_lockout = r'^(:)(prot(ocol)?|infu(sion)?)(:)(ld|db|sd|ed)(:)(lock(out)?)((:)(min|max|def(ault)?))?(\?)(\s+)?$'
re_qr_code_style = r'^(\d{32})$'
# ^      : matches the start of the string
# (re)   : must contain [re]
# (\s+)? : may contain 1 or more spaces (optional)
# (\d+)  : may contain 0 or more digits
# (\s+)? : may contain 1 or more spaces (optional)
# (>)?   : may contain 0 or 1 [>] (optional)
# (\s+)? : may contain 1 or more spaces (optional)
# ([a-zA-Z0-9_]+\.txt)? 
#        : the file name may contain 1 or more letter and digit 
#          and the underscore [_] and end with [.txt] (optional)
# $      : matches the start of the string 
re_read_event_log = r'^(re)(\s+)?(\d+)?((\s+)?(>)(\s+)?([a-z0-9_]+(\.txt|\.json)))?$'
# ^      : matches the start of the string
# (ref)      : must contain [ref]
# (\s+)?     : must contain 1 or more spaces (optional)
# (\d\d\d\d) : must be 4 digits start index
# (\s+)?     : must contain 1 or more spaces (optional)
# (\d\d\d\d) : must be 4 digits end index
# (>)?       : may contain 0 or 1 [>] (optional)
# (\s+)?     : may contain 1 or more spaces (optional)
# ([a-zA-Z0-9_]+\.txt)? 
#        : the file name may contain 1 or more letter and digit 
#          and the underscore [_] and end with [.txt] (optional)
# $      : matches the start of the string
re_read_event_log_hex = r'^(reh)(\s+)?((0x)?[a-f0-9]+)?(\s+)?((0x)?[a-f0-9]+)?((\s+)?(>)(\s+)?([a-z0-9_]+\.txt))?$'
re_query_help_file = r'^(help|main|\?)(\s+)(.+)(.\s+)?$'
re_ip_address = r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
re_serial_port = r'(com\d+)|(\/dev\/ttyusb\d+)'

# Define Key Type
_NONE_KEY = '0'
_UP_KEY = '1'
_DOWN_KEY = '2'
_INFO_KEY = '3'
_OK_KEY = '4'
_POWER_KEY = '5'
_RUN_KEY = '6'
_BOLUS_KEY = '7'
_STOP_KEY = '8'
# Define Key Duration
_SHORT_PRESS = '0'
_LONG_PRESS = '1'
_MID_PRESS = '2'

VISA_RESOURCE_CONFIG_FILE_PATH = 'visa_resource_config.json'
PUMP_CONFIG_FILE_PATH = 'pump_config.json'

LCD_MAX_ROWS = 8
LCD_MAX_COL_PIXEL = 128

# Global Variable Definition
_FLASHUTILCL_FILE_PATH = './flash_utilities/FlashUtilCL.exe'.replace('/', '\\')
_MIVA_8_BIT_FIRMWARE_PATH = './firmwares/miva_protective.hex'.replace('/', '\\')
_PYPROGRAMMERCLI_FILE_PATH = './flash_utilities/pyProgrammerCLI.exe'.replace('/', '\\')
_MIVA_32_BIT_FIRMWARE_PATH = './firmwares/miva-32-bit.hex'.replace('/', '\\')
_MFG_32_BIT_FIRMWARE_PATH = './firmwares/mfg-32-bit.hex'.replace('/', '\\')

    
def scan_serial_ports():
    '''Scan Serial Port'''
    ports = []
    if platform.system() == 'Linux':
        ports = ['/dev/ttyUSB%s' % (i) for i in range(0, 256)]
    else:
        ports = ['com%s' % (i) for i in range(1, 256)]
    result = []
    for port in ports:
        try:
            ser = serial.Serial(port)
            ser.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


def wait(seconds):
    '''Wait for number of seconds'''
    while seconds >= 0:
        for each_symbol in ['-', '\\', '|', '/']:
            print('{0}......[{1:.1f} sec]   '.format(each_symbol, seconds), end='\r')
            seconds -= 0.1
            time.sleep(0.1)
            if seconds < 0:
                break
            print('{0}......[{1:.1f} sec]'.format(each_symbol, seconds), end='\r')
            seconds -= 0.1
            time.sleep(0.1)
            if seconds < 0:
                break
            print('{0}......[{1:.1f} sec]'.format(each_symbol, seconds), end='\r')
            seconds -= 0.1
            time.sleep(0.1)
            if seconds < 0:
                break
    # time.sleep(1.5)
    print()
    

def get_line_number():
    '''Returns the current line number in the source code'''
    return inspect.currentframe().f_back.f_lineno


def crc32c(crc, data):
    '''Calculate the CRC32C as Digital Signature
        @param crc The initial CRC
        @param data The data that needs to be calculated, could be hexstring or byte array
        @return CRC of the command
    '''
    crc = (crc ^ 0xffffffff) & 0xffffffff
    i = 0
    poly = 0xedb88320
    # if the [data] is a byte array, convert it to hex string first
    if isinstance(data, bytes):
        data = data.hex().upper()

    while i < len(data):
        crc ^= (int(data[i] + data[i + 1], 16) & 0xff)
        j = 0
        while j < 8:
            crc = (crc >> 1) ^ poly if ((crc & 1) > 0) else crc >> 1
            j += 1
        i += 2
    crc = ~crc
    # return the CRC as a 4-byte integer
    return crc & 0xffffffff


def crc_fill(crc, data, length=-1):
    '''Calculate the CRC32C as Digital Signature and fill the bytes to the length
        @param crc The initial CRC
        @param data The data that needs to be calculated, must be bytes
        @param length The expected length of the output byte array
        @return Bytes with last four bytes been crc, length to be the length parsed in.
         None if length doesn't make sense
    '''
    result = None
    output_hex = False

    if isinstance(data, str):
        output_hex = True
        data = bytes.fromhex(data)
        if length % 2 == 0:
            length = int(length / 2)
        else:
            print("Error: invaild length ", length)
            length = 0

    if length > 5:
        while len(data) < length - 4:
            data += int(0xFF).to_bytes(1, 'little')

        data_hex = data.hex().upper()
        data += crc32c(crc, data_hex).to_bytes(4, 'little')
        if output_hex:
            result = data.hex().upper()
        else:
            result = data

    return result


def byte_fill(data, length, fill_byte=0xFF):
    '''Calculate the CRC32C as Digital Signature and fill the bytes to the length
        @param data The data that needs to be calculated, must be bytes
        @param length The expected length of the output byte array
        @return Bytes array of length. None if length doesn't make sense
    '''
    while len(data) < length:
        data += int(fill_byte).to_bytes(1, 'little')
    return data


def crc_checksum(command, symbol='+'):
    '''Calculate the CRC for Error-Detection Purpose
        @param command R/W+Index+Parameters
        @return CRC of the command
    '''
    summ = 0
    # crc = ''
    for i in range(len(command)):
        # += for nimbus II and CAPS, ^= for nimbus unified H
        if symbol == '+':
            summ += ord(command[i:i + 1])
        elif symbol == '^':
            summ ^= ord(command[i:i + 1])
        else:
            summ += ord(command[i:i + 1])
    crc = hex(summ)[2:].zfill(2)
    return crc[len(crc) - 2: len(crc)]


def ibm_crc16(command):
    '''IBM CRC 16
        Input - input command
        Output - 2-bytes CRC
    '''
    crc = 0xFFFF;
    for k in range(len(command)):
        # Note: Intel architecture sign extends 
        # a char to unsigned short type cast, 
        # so we must mask out the higher byte(s)
        crc ^= command[k] & 0xFF  
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ 0xA001
            else:
                crc = (crc >> 1)
    # convert integer to bytes
    crc = crc.to_bytes(2, 'big')
    return crc;


def lrc_checksum(command):
    '''Calculate the LRC (Longitudinal Redundancy Check) checksum
        @param command R/W+Index+Parameters
        @return CRC of the command
    '''
    lrc = 0
    for each_char in command:
        lrc = (lrc + ord(each_char)) & 0xFF
    lrc = ((lrc ^ 0xFF) + 1) & 0xFF
    crc = hex(lrc)[2:].zfill(2)
    print('crc = {}'.format(crc))
    return '0D'


def load_json_file(file_path):
    """Load data from a JSON file"""
    # read JSON file
    with open(file_path, "r", encoding='UTF-8') as file:
        content_json = file.read()
    
    # convert JSON to Python Dict
    config = json.loads(content_json)
    return config


def text_to_file(content, file_path):
    """Save text to a file"""
    dir_name = path.dirname(file_path)
    if dir_name != '':
        if not path.isdir(dir_name):
            mkdir(dir_name)
    if content == None:
        content = ''
    # Save to text file
    with open(file_path, "w+", encoding='UTF-8') as file:
        content = content.replace('\r\n', '\n')
        file.write(content)
    absolute_path = path.abspath(file_path)
    return absolute_path


def json_to_file(config, file_path):
    """Dump data to a JSON file"""
    dir_name = path.dirname(file_path)
    if dir_name != '':
        if not path.isdir(dir_name):
            mkdir(dir_name)   
    if config == None:
        config = {}
    # convert Python Dict to JSON:
    config_json = json.dumps(config, indent=4)
    # Save to JSON file
    with open(file_path, "w+", encoding='UTF-8') as file:
        file.write(config_json)
    absolute_path = path.abspath(file_path)
    return absolute_path


def file_to_list(file_path, ignore_empty_line=True, strip_line=True):
    '''Convert each line in a text file into a list'''
    text_line_list = []
    file = open(file_path, "r")
    for each_line in file:
        if ignore_empty_line:
            if each_line.strip() != '':
                if strip_line:
                    text_line_list.append(each_line.strip())
                else:
                    text_line_list.append(each_line.rstrip())
        else:
            if strip_line:
                text_line_list.append(each_line.strip())
            else:
                text_line_list.append(each_line.rstrip())
    return text_line_list


def list_to_file(content_list, file_path):
    '''Save each element of the list to a text file'''
    dir_name = path.dirname(file_path)
    if dir_name != '':
        if not path.isdir(dir_name):
            mkdir(dir_name)   
            
    file = open(file_path, "w")
    for each_element in content_list: 
        file.write(each_element)
        file.write('\n')
    file.close()
    absolute_path = path.abspath(file_path)
    return absolute_path


def hex_to_float(num_hex):
    '''convert 4-byte hex (little endian) to float 
    ex. '3f800000 -> 1.0' 
    '''
    return_text = struct.unpack('!f', bytes.fromhex(num_hex))[0]    
    return return_text


def float_to_hex(num):
    '''convert float to 4-byte hex (little endian)
    ex. 1.0 -> '3f800000' 
    '''
    return_text = hex(struct.unpack('<I', struct.pack('<f', num))[0])[2:].zfill(8)
    return return_text


def isfloat(num):
    '''Check if number string can be converted to float'''
    try:
        float(num)
        return True
    except ValueError:
        return False


def compare_numbers(num1, num2, operator, delta, delta_is_percentage):
    upper_limit = num2
    lower_limit = num2
    if delta is not None:
        if delta_is_percentage: 
            upper_limit = num2 * (1 + delta / 100)
            lower_limit = num2 * (1 - delta / 100)
        else:
            upper_limit = num2 + delta
            lower_limit = num2 - delta
    
    if operator == '<=':
        if delta is None:
            return (num1 <= num2)
        else:
            return num1 <= upper_limit
    elif operator == '<':
        if delta is None:
            return (num1 < num2)
        else:
            return num1 < upper_limit
    elif operator == '==':
        if delta is None:
            return (num1 == num2)
        else:
            return lower_limit <= num1 <= upper_limit 
    elif operator == '>=':
        if delta is None:
            return (num1 >= num2)
        else:
            return num1 >= lower_limit
    elif operator == '>':
        if delta is None:
            return (num1 > num2)
        else:
            return num1 > lower_limit


def int_to_time_str(time_int, time_format='hh:mm:ss'):
    '''Convert integer to time format [hh:mm] string'''
    time_hour_str = str(int(time_int / 3600)).zfill(2)
    time_minute_str = str(int((time_int % 3600) / 60)).zfill(2)
    time_second_str = str(int((time_int % 3600) % 60)).zfill(2)
    time_str = time_hour_str + ':' + time_minute_str + ':' + time_second_str
    if time_format == 'hh:mm':
        time_str = time_hour_str + ':' + time_minute_str
    return time_str  


def time_str_to_int(time_str):
    '''Convert time format [hh:mm] string to integer'''
    match_result = re.match(re_time_str_format, time_str)
    time_int = int(match_result[1]) * 3600 + int(match_result[3]) * 60
    return time_int  


def hex_to_bitmap(hex_list):
    '''Convert screenshot hex list to bitmap
        ex. the bitmap is a 64x128 list
    '''
    byte_array_list = []
    for i in range(len(hex_list)):
        # Convert each line Hex string to Byte array
        # ex. 'FFFFFFFF' -> b'\xFF\xFF\xFF\xFF'
        byte_array = bytes.fromhex(hex_list[i])
        byte_array_list.append(byte_array)
    
    bit_str_list_list = []
    for i in range(len(byte_array_list)):
        # Convert each line Byte array to bit string list
        bit_str_list = []
        for j in range(len(byte_array_list[i])):
            # Convert Byte to Bit string
            # ex. 255 -> '0b11111111'
            # and ignore the first '0b' in '0b11111111'
            # [bit_str] is the VERTICAL bit string of ONE BYTE
            bit_str = bin(byte_array_list[i][j])[2:].zfill(8)
            bit_str_list.append(bit_str)
        bit_str_list_list.append(bit_str_list)
    
    bitmap_str_list = []
    # print('len(bit_str_list_list) = {}'.format(len(bit_str_list_list)))
    for i in range(len(bit_str_list_list)):
        bit_str_list = bit_str_list_list[i]
        # print('bit_str_list = {}'.format(bit_str_list))
        # print('len(bit_str_list[0]) = {}'.format(len(bit_str_list[0])))
        for j in range(len(bit_str_list[0])):
            bitmap_str_line = ''
            for k in range(len(bit_str_list)):
                # [bitmap_str_line] is the HORIZONTAL bit string WHOLE LINE
                bitmap_str_line += bit_str_list[k][7 - j]
            print(bitmap_str_line)
            bitmap_str_list.append(bitmap_str_line)
    return bitmap_str_list   


def screenshot_hex_to_bitmap(screenshot_hex):
    '''Convert screenshot hex to bitmap
        ex. the bitmap is a 64x128 list
    '''
    
    # convert screenshot_hex to hex_list
    hex_list = []
    for i in range(LCD_MAX_ROWS):
        hex_list.append(screenshot_hex[i * LCD_MAX_COL_PIXEL * 2: (i + 1) * LCD_MAX_COL_PIXEL * 2])
    
    byte_array_list = []
    for i in range(len(hex_list)):
        # Convert each line Hex string to Byte array
        # ex. 'FFFFFFFF' -> b'\xFF\xFF\xFF\xFF'
        byte_array = bytes.fromhex(hex_list[i])
        byte_array_list.append(byte_array)
    
    bit_str_list_list = []
    for i in range(len(byte_array_list)):
        # Convert each line Byte array to bit string list
        bit_str_list = []
        for j in range(len(byte_array_list[i])):
            # Convert Byte to Bit string
            # ex. 255 -> '0b11111111'
            # and ignore the first '0b' in '0b11111111'
            # [bit_str] is the VERTICAL bit string of ONE BYTE
            bit_str = bin(byte_array_list[i][j])[2:].zfill(8)
            bit_str_list.append(bit_str)
        bit_str_list_list.append(bit_str_list)
    
    bitmap_str_list = []
    # print('len(bit_str_list_list) = {}'.format(len(bit_str_list_list)))
    for i in range(len(bit_str_list_list)):
        bit_str_list = bit_str_list_list[i]
        # print('bit_str_list = {}'.format(bit_str_list))
        # print('len(bit_str_list[0]) = {}'.format(len(bit_str_list[0])))
        for j in range(len(bit_str_list[0])):
            bitmap_str_line = ''
            for k in range(len(bit_str_list)):
                # [bitmap_str_line] is the HORIZONTAL bit string WHOLE LINE
                bitmap_str_line += bit_str_list[k][7 - j]
            print(bitmap_str_line)
            bitmap_str_list.append(bitmap_str_line)
    return bitmap_str_list   


def apply_screenshot_masks(screenshot_bitmap, bitmap_masks):
    '''Apply screenshot masks'''
    if bitmap_masks != []:
        for each_mask in bitmap_masks:
            for i in range(each_mask['height']):
                if each_mask['name'] != 'progress_bar':
                    screenshot_bitmap[each_mask['row'] + i] = \
                        screenshot_bitmap[each_mask['row'] + i][:each_mask['column']] \
                        +screenshot_bitmap[each_mask['row']][each_mask['column']] * each_mask['width'] \
                        +screenshot_bitmap[each_mask['row'] + i][each_mask['column'] + each_mask['width']:]
                else:
                    screenshot_bitmap[each_mask['row'] + i] = \
                        screenshot_bitmap[each_mask['row'] + i][:each_mask['column']] \
                        +'0' * each_mask['width'] \
                        +screenshot_bitmap[each_mask['row'] + i][each_mask['column'] + each_mask['width']:]
    
    return screenshot_bitmap


def bitmap_to_image(bitmap_str_list, image_path, bitmap_masks=[]):
    '''Generate photo from Bitmap'''
    # Create directory if not exist
    dir_name = path.dirname(image_path)
    if dir_name != '':
        if not path.isdir(dir_name):
            mkdir(dir_name)
    # Apply masks
    bitmap_str_list = apply_screenshot_masks(bitmap_str_list, bitmap_masks)
    # Create image
    num_line = len(bitmap_str_list)
    num_colume = len(bitmap_str_list[0])
    image = Image.new('1', (num_colume, num_line), color=1)  # create the Image of size 1 pixel 
    for i in range(num_line):
        for j in range(num_colume):
            if bitmap_str_list[i][j] == '1': 
                image.putpixel((j, i), ImageColor.getcolor('black', '1'))
    image = image.resize((num_colume * 1, num_line * 1), resample=0)
    image.save(image_path)
    absolute_path = path.abspath(image_path)
    return absolute_path


def compare_file_equal(file_path, ref_file_path):
    '''Compare two files equal by using MD5'''
    realtime_md5 = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
    reference_md5 = hashlib.md5(open(ref_file_path, 'rb').read()).hexdigest()
    if realtime_md5 == reference_md5:
        return True
    else:
        return False

    
def compare_event_log_equal(event_log, event_log_ref):
    if 'event_type' in event_log and 'event_type' in event_log_ref:
        if event_log['event_type'] == event_log['event_type']:
            return True
        else:
            return False
    else:
        if event_log == event_log_ref:
            return True
        else:
            return False


def validate_qr_code(qr_code, re_qr_code_style):
    # Validate if the QR code is valid
    qr_code = qr_code.strip(' \t\r\n\0')
    if re.match(re_qr_code_style, qr_code.strip(' \t\r\n\0')):
        return True
    return False


def create_pump_config_file(pump_config_file_path):
    # create a [pump_config.json] file
    pump_config = { 
                    "library_path": "",
                    "protocol_selected": "",
                    "rx_path": "",
                    "interval_time": 1,
                    "test_report_path": "./test_report",
                    "event_log": "./event_log",
                    "help_file_path": "./help/miva",
                    "mfg_32_bit_firmware_path": _MFG_32_BIT_FIRMWARE_PATH,
                    "miva_8_bit_firmware_path": _MIVA_8_BIT_FIRMWARE_PATH,
                    "miva_32_bit_firmware_path": _MIVA_32_BIT_FIRMWARE_PATH,
                    "programmer_8_bit_path": _FLASHUTILCL_FILE_PATH,
                    "programmer_32_bit_path": _PYPROGRAMMERCLI_FILE_PATH
                    }
    json_to_file(pump_config, pump_config_file_path)
    return pump_config


def download_mfg_32_bit():
    '''Download MFG 32-bit Firmware'''
    status = False
    #
    # Pump Config
    pump_config = None
    if not path.exists(PUMP_CONFIG_FILE_PATH):
        pump_config = create_pump_config_file(PUMP_CONFIG_FILE_PATH)
    else:
        pump_config = load_json_file(PUMP_CONFIG_FILE_PATH)
    if not 'programmer_32_bit_path' in pump_config:
        pump_config['programmer_32_bit_path'] = _PYPROGRAMMERCLI_FILE_PATH
        print(pump_config)
        json_to_file(pump_config, PUMP_CONFIG_FILE_PATH)
    if not 'mfg_32_bit_firmware_path' in pump_config:
        pump_config['mfg_32_bit_firmware_path'] = _MFG_32_BIT_FIRMWARE_PATH
        json_to_file(pump_config, PUMP_CONFIG_FILE_PATH)
    programmer_32_bit_path = pump_config['programmer_32_bit_path']
    mfg_32_bit_firmware_path = pump_config['mfg_32_bit_firmware_path']
    #
    if not path.exists(programmer_32_bit_path):
        file_basename = path.basename(programmer_32_bit_path)
        print('Fail: 32-bit programmer [{}] NOT exist!'.format(file_basename))
        return
    #
    if not path.exists(mfg_32_bit_firmware_path):
        file_basename = path.basename(mfg_32_bit_firmware_path)
        print('Fail: 32-bit mfg firmware [{}] NOT exist!'.format(file_basename))
        return
    # Download [.hex] with [pyProgrammerCLI.exe]
    # FlashUtilCL Flash [file.hex]
    # [file.hex]: mfg-32-bit.hex
    # .\flash_utilities\pyProgrammerCLI.exe flash .\firmwares\mfg-32-bit.hex> mfg_32_bit_download_log.txt
    command = programmer_32_bit_path + ' flash ' + mfg_32_bit_firmware_path + ' > mfg_32_bit_download_log.txt'
    system(command)
    with open('mfg_32_bit_download_log.txt', "r", encoding='UTF-8') as file:
        file_content = file.read()
        if file_content.strip(' \t\r\n\0') == 'Program done.':
            print("Success: Download [mfg 32-bit firmware] with [pyProgrammerCLI.exe]")
            status = True
        else:
            print(file_content)
    return status


def download_miva_8_bit():
    '''callback function - Download MFG Firmware'''
    status = False
    #
    pump_config = {}
    if not path.exists(PUMP_CONFIG_FILE_PATH):
        pump_config = create_pump_config_file(PUMP_CONFIG_FILE_PATH)
    else:
        pump_config = load_json_file(PUMP_CONFIG_FILE_PATH)
    if not 'programmer_8_bit_path' in pump_config:
        pump_config['programmer_8_bit_path'] = _FLASHUTILCL_FILE_PATH
        json_to_file(pump_config, PUMP_CONFIG_FILE_PATH)
    if not 'miva_8_bit_firmware_path' in pump_config:
        pump_config['miva_8_bit_firmware_path'] = _MIVA_8_BIT_FIRMWARE_PATH
        json_to_file(pump_config, PUMP_CONFIG_FILE_PATH)    
    #
    programmer_8_bit_path = pump_config['programmer_8_bit_path']
    miva_8_bit_firmware_path = pump_config['miva_8_bit_firmware_path']
    
    if not path.exists(programmer_8_bit_path):
        file_basename = path.basename(programmer_8_bit_path)
        print('Fail: 8-bit programmer [{}] NOT exist!'.format(file_basename))
        return
    
    if not path.exists(miva_8_bit_firmware_path):
        file_basename = path.basename(miva_8_bit_firmware_path)
        print('Fail: 8-bit firmware [{}] NOT exist!'.format(file_basename))
        return
    # Download [.hex] with [FlashUtilCL.exe]
    # FlashUtilCL DownloadUSB [-Option Flags] [file.hex] [Serial Number String] [Power On Disconnect] [Debug Interface]
    # [-Option Flags]: N/A
    # [file.hex]: miva-8-bit.hex
    # [Serial Number String]: "" - The serial number of the USB Debug Adapter. 
    #                              An empty string can be used if only one USB 
    #                              Debug Adapter is available.
    # [Power On Disconnect]: 1 - Power will continue to be provided by the USB Debug 
    #                            Adapter to the target device after disconnecting.
    # [Debug Interface]: 1 - C2 Debug Interface (F3XX devices)
    # .\flash_utilities\FlashUtilCL.exe downloadusb .\firmwares\miva_protective.hex "" 1 1 > miva_8_bit_download_log.txt
    command = programmer_8_bit_path + ' downloadusb ' + miva_8_bit_firmware_path + ' \"\" 1 1 > miva_8_bit_download_log.txt'
    system(command)
    # print(command)
    with open('miva_8_bit_download_log.txt', "r", encoding='UTF-8') as file:
        file_content = file.read()
        if file_content.strip(' \t\r\n\0') == '':
            print("Success: Download [miva 8-bit firmware] with [FlashUtilCL.exe]")                
            status = True
        else:
            print(file_content)
            print("Failed: Download [miva 8-bit firmware] with [FlashUtilCL.exe]")
    #
    return status

    
def download_miva_32_bit():
    '''Flash MIVA 32-bit Firmware'''
    status = False
    #
    pump_config = None
    if not path.exists(PUMP_CONFIG_FILE_PATH):
        pump_config = create_pump_config_file(PUMP_CONFIG_FILE_PATH)
    else:
        pump_config = load_json_file(PUMP_CONFIG_FILE_PATH)
    if 'programmer_32_bit_path' not in pump_config:
        pump_config['programmer_32_bit_path'] = _PYPROGRAMMERCLI_FILE_PATH
        json_to_file(pump_config, PUMP_CONFIG_FILE_PATH)
    if not 'miva_32_bit_firmware_path' in pump_config:
        pump_config['miva_32_bit_firmware_path'] = _MIVA_32_BIT_FIRMWARE_PATH
        json_to_file(pump_config, PUMP_CONFIG_FILE_PATH)
    #
    programmer_32_bit_path = pump_config['programmer_32_bit_path']
    miva_32_bit_firmware_path = pump_config['miva_32_bit_firmware_path']
    
    if not path.exists(programmer_32_bit_path):
        file_basename = path.basename(programmer_32_bit_path)
        print('Fail: 32-bit programmer [{}] NOT exist!'.format(file_basename))
        return status
    
    if not path.exists(miva_32_bit_firmware_path):
        file_basename = path.basename(miva_32_bit_firmware_path)
        print('Fail: 32-bit firmware [{}] NOT exist!'.format(file_basename))
        return status
    
    # Download [.hex] with [pyProgrammerCLI.exe]
    # FlashUtilCL Flash [file.hex]
    # [file.hex]: miva-32-bit.hex
    # .\flash_utilities\pyProgrammerCLI.exe flash .\firmwares\miva-32-bit.hex> miva_32_bit_download_log.txt
    command = programmer_32_bit_path + ' flash ' + miva_32_bit_firmware_path + ' > miva_32_bit_download_log.txt'
    system(command)
    # print(command)
    with open('miva_32_bit_download_log.txt', "r", encoding='UTF-8') as file:
        file_content = file.read()
        if file_content.strip(' \t\r\n\0') == 'Program done.':
            print("Success: Download [miva 32-bit firmware] with [pyProgrammerCLI.exe]")
            status = True
        else:
            print(file_content + "\n")
    return status

   
def main(argv):
    '''main function'''
    print(len(argv))
    print('line #: {}'.format(get_line_number()))
    

if __name__ == "__main__":
    main(sys.argv)
