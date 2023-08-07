'''module SendRx'''
from os import path
import time
# import sys
import json
# import math
import struct
from binascii import hexlify
from pyZynoUnifiedDrivers.miva.module_utils import crc32c


def get_dilute_volume(protocol):
    '''get dilute volume'''
    dilute_volume = None
    if protocol['content']['drug'] is not None:
        dilute_volume_str = protocol['content']['drug']['content']['diluteVolume']['value']
        dilute_volume = float(dilute_volume_str)
    return dilute_volume


def get_drug_amount(protocol):
    '''get drug amount
       This function converts the drug amount unit to micro gram'''

    drug_amount = None
    if protocol['content']['drug'] is not None:
        drug_amount_str = protocol['content']['drug']['content']['drugAmount']['value']
        drug_amount_unit_str = protocol['content']['drug']['content']['drugAmount']['unit']
        drug_amount = float(drug_amount_str)
        if drug_amount_unit_str == 'mg':
            drug_amount = drug_amount * 1000
    return drug_amount


def get_patient_weight(protocol):
    patient_weight = 0
    switches = protocol['content']['program']['switches']
    if switches['rate']:
        rate_str = protocol['content']['program']['rate']['value']
        rate = float(rate_str)
        rate_unit = protocol['content']['program']['rate']['unit']
        # drug amount (mcg)
        drug_amount = get_drug_amount(protocol)
        # dilute volume (mL)
        dilute_volume = get_dilute_volume(protocol)
        # weight (kg)
        if rate_unit in ('mg/kg/min', 'mcg/kg/min'):
            rate_upper_guard = 135
            rate_lower_guard = 0
            if rate_unit == 'mg/kg/min':
                weight_upper_limit = rate_upper_guard * drug_amount \
                            / (rate * 60 * dilute_volume * 1000)
                weight_lower_limit = rate_lower_guard * drug_amount \
                            / (rate * 60 * dilute_volume * 1000)
            if rate_unit == 'mcg/kg/min':
                weight_upper_limit = rate_upper_guard * drug_amount \
                            / (rate * 60 * dilute_volume)
                weight_lower_limit = rate_lower_guard * drug_amount \
                            / (rate * 60 * dilute_volume)
            
            patient_weight = input("    Input Patient Weight ({0:3.1f} - {1:3.1f} kg): "\
                            .format(weight_lower_limit, weight_upper_limit)) \
                            or (weight_upper_limit - weight_lower_limit) / 2
            try:
                patient_weight = float(patient_weight)
            except ValueError:
                patient_weight = 0

            if patient_weight > weight_upper_limit:
                patient_weight = weight_upper_limit
            elif patient_weight < weight_lower_limit:
                patient_weight = weight_lower_limit
            print('    patient weight = {:5.2f} kg'.format(patient_weight))
    return float(patient_weight)


def parse_rx_hex(rx_hex):
    '''parse rx hex'''
    rx_size = 512
    # convert rx_hex to rx_bytes
    rx_bytes = bytes.fromhex(rx_hex)
    print('rx size: {} bytes'.format(len(rx_bytes)))
    print('==')
    if len(rx_bytes) != rx_size:
        print('wrong rx size: {0} bytes (expected {1} bytes)'.format(len(rx_bytes), rx_size))
        return None
    #
    # 0:80 80-byte [Protocol]
    protocol_bytes = rx_bytes[0:80]
    protocol_hex = protocol_bytes.hex()
    print(protocol_hex)
    print('==[Protocol] parsing complete==')
    # 80:84 4-byte [Switches]
    switches_bytes = rx_bytes[80:84]
    switches_hex = switches_bytes.hex()
    print(switches_hex)
    print('==[Switches] parsing complete==')
    # 84:88 4-byte [Protocol CRC]
    protocol_crc_bytes = rx_bytes[84:88]
    protocol_crc_hex = protocol_crc_bytes.hex()
    print(protocol_crc_hex)
    print('==[Protocol CRC] parsing complete==')
    # 88:90 2-byte [Auth Role]
    auth_role_bytes = rx_bytes[88:90]
    auth_role_hex = auth_role_bytes.hex()
    print(auth_role_hex)
    print('==[Auth Role] parsing complete==')
    # 90:92 2-byte [Rate Factor]
    rate_factor_bytes = rx_bytes[88:90]
    rate_factor_hex = rate_factor_bytes.hex()
    print(rate_factor_hex)
    print('==[Rate Factor] parsing complete==')
    # 92:93 1-byte [Concentration Modifiable]
    concentration_modifiable_bytes = rx_bytes[92:93]
    concentration_modifiable_hex = concentration_modifiable_bytes.hex()
    print(concentration_modifiable_hex)
    print('==[Concentration Modifiable] parsing complete==')
    # 93:94 1-byte [Infusion Mode]
    infusion_mode_bytes = rx_bytes[93:94]
    infusion_mode_hex = infusion_mode_bytes.hex()
    print(infusion_mode_hex)
    print('==[Infusion Mode] parsing complete==')
    # 94:95 1-byte [ID]
    id_bytes = rx_bytes[94:95]
    id_hex = id_bytes.hex()
    print(id_hex)
    print('==[ID] parsing complete==')
    # 95:96 1-byte [Label Pool ID]
    label_pool_id_bytes = rx_bytes[95:96]
    label_pool_id_hex = label_pool_id_bytes.hex()
    print(label_pool_id_hex)
    print('==[Label Pool ID] parsing complete==')
    # 96:97 1-byte [Label ID]
    label_id_bytes = rx_bytes[96:97]
    label_id_hex = label_id_bytes.hex()
    print(label_id_hex)
    print('==[Label ID] parsing complete==')
    # 97:98 1-byte [Rate Unit]
    rate_unit_bytes = rx_bytes[97:98]
    rate_unit_hex = rate_unit_bytes.hex()
    print(rate_unit_hex)
    print('==[Rate Unit] parsing complete==')
    # 98:99 1-byte [Concentration Unit]
    concentration_unit_bytes = rx_bytes[98:99]
    concentration_unit_hex = concentration_unit_bytes.hex()
    print(concentration_unit_hex)
    print('==[Concentration Unit] parsing complete==')
    # 99:109 10-byte [Protocol Name]
    protocol_name_bytes = rx_bytes[99:109]
    protocol_name_hex = protocol_name_bytes.hex()
    print(protocol_name_hex)
    print('==[Protocol Name] parsing complete==')
    # 109:119 10-byte [Drug Name]
    drug_name_bytes = rx_bytes[109:119]
    drug_name_hex = drug_name_bytes.hex()
    print(drug_name_hex)
    print('==[Drug Name] parsing complete==')
    # 119:224 105-byte [Drug Components]
    drug_components_bytes = rx_bytes[119:224]
    drug_components_hex = drug_components_bytes.hex()
    print(drug_components_hex)
    print('==[Drug Components] parsing complete==')
    # 224:252 28-byte 0xFF
    #
    # 252:256 4-byte CRC
    crc_bytes = rx_bytes[252:256]
    crc_hex = crc_bytes.hex()
    print(crc_hex)
    print('==[CRC] parsing complete==')
    # 256:257 1-byte [Protocol Index]
    protocol_index_bytes = rx_bytes[256:257]
    protocol_index_hex = protocol_index_bytes.hex()
    print(protocol_index_hex)
    print('==[Protocol Index] parsing complete==')
    # 257:258 1-byte [View Index]
    view_index_bytes = rx_bytes[257:258]
    view_index_hex = view_index_bytes.hex()
    print(view_index_hex)
    print('==[View Index] parsing complete==')
    # 258:259 1-byte [Label Index]
    label_index_bytes = rx_bytes[258:259]
    label_index_hex = label_index_bytes.hex()
    print(label_index_hex)
    print('==[Label Index] parsing complete==')


    # 259:512 253-byte 0xFF
    #
def encrypt_rx(rx_path):
    rx = SendRx()
    rx.load(rx_path)
    rx_hex = rx.get_rx_hex()
    #
    parse_rx_hex(rx_hex)
    #
    rx_name = rx.send_rx['sendRxProtocol']['content']['name'].strip(' \t\r\n\0')
    # replace '\' or '/' or ' ' charactor to '' or '_' in the [rx_name]
    rx_name = rx_name.replace('\\', '')
    rx_name = rx_name.replace('/', '')
    rx_name = rx_name.replace(' ', '_')
    #
    rx_id = str(rx.send_rx['sendRxProtocol']['id'])
    time_stamp = str(int(time.time() * 1000))
    hex_file_path = 'SendRx-[' + rx_name + ']-[' + rx_id + ']@' \
            +time_stamp + '.hex'
    # write hex file
    file = open(hex_file_path, "w")
    file.write(rx_hex)
    file.close()
    print('Rx hex file is saved to: [{}]'.format(hex_file_path))
    # print('rx_hex = \n{}'.format(rx_hex))


class SendRx:
    
    PROTOCOL_UNION_SIZE = 80
    
    '''Send Rx class'''

    def __init__(self):
        self.send_rx = None
        self.pump_sn = ''
        self.library_crc = ''
        self.library_number = 0
        self.protocol_index = 0
        self.view_index = 255
        self.label_index = 255
        self.protocol = None
        self.weight = None

    def load(self, send_rx_path):
        '''load send rx'''
        # send_rx_json = ""
        # read json file
        file = open(send_rx_path, "r")
        send_rx_json = file.read()
        file.close()
        # convert JSON to Python Dict
        self.send_rx = json.loads(send_rx_json)
        # serialNumber: Pump Serial Number (should match the pump S/N)        
        self.pump_sn = self.send_rx['serialNumber']
        # libraryCrc: [crc] in library JSON
        self.library_crc = self.send_rx['libraryCrc']
        # libraryNumber: [id] in library JSON
        self.library_number = self.send_rx['libraryNumber']
        # protocolIndex: index of [extractedProtocols] list in library JSON
        self.protocol_index = self.send_rx['protocolIndex']
        # viewIndex: index of [views] list in library JSON (255: use [defaultViews] instead)
        self.view_index = self.send_rx['viewIndex']
        # labelIndex: index of [labelSets] list in library JSON (255: No Label)
        self.label_index = self.send_rx['labelIndex']
        # send rx protocol
        self.protocol = self.send_rx['sendRxProtocol']

    def get_pump_sn(self):
        '''get pump sn'''
        return self.pump_sn

    def get_library_crc(self):
        '''get library crc'''
        return self.library_crc

    def get_library_number(self):
        '''get library number'''
        return self.library_number

    def get_protocol_index(self):
        '''get protocol index'''
        return self.protocol_index

    def get_view_index(self):
        '''get view index'''
        return self.view_index

    def get_label_index(self):
        '''get label index'''
        return self.label_index

    def get_protocol(self):
        '''get protocol'''
        return self.protocol
        
    def get_weight(self):
        '''get weight'''
        return self.weight
        
    def get_rx_hex(self):
        '''get sendRx hex string'''
        # Get the bytes array
        # 0:80 80-byte [Protocol]
        protocol_bytes = self.get_protocol_bytes(self.protocol)
        # 80:84 4-byte [Switches]
        switches_bytes = self.get_switches_bytes(self.protocol)
        # 84:88 4-byte [Protocol CRC]
        protocol_crc_bytes = self.get_protocol_crc_bytes(self.protocol)
        # 88:90 2-byte [Auth Role]
        auth_role_bytes = int(0xFFFF).to_bytes(2, 'little')
        # 90:92 2-byte [Rate Factor]
        rate_factor_bytes = self.get_rate_factor_bytes(self.protocol)
        # 92:93 1-byte [Concentration Modifiable]
        concentration_modifiable_bytes = int(0).to_bytes(1, 'little')
        # 93:94 1-byte [Infusion Mode]
        infusion_mode_bytes = self.get_infusion_mode_bytes(self.protocol)
        # 94:95 1-byte [ID]
        id_bytes = int(0xFF).to_bytes(1, 'little')
        # 95:96 1-byte [Label Pool ID]
        label_pool_id_bytes = int(0xFF).to_bytes(1, 'little')
        # 96:97 1-byte [Label ID]
        label_id_bytes = int(0).to_bytes(1, 'little')
        # 97:98 1-byte [Rate Unit]
        rate_unit_bytes = self.get_rate_unit_bytes(self.protocol)
        # 98:99 1-byte [Concentration Unit]
        concentration_unit_bytes = self.get_concentration_unit_bytes(self.protocol)
        # 99:109 10-byte [Protocol Name]
        protocol_name_bytes = self.get_protocol_name_bytes(self.protocol)
        # 109:119 10-byte [Drug Name]
        drug_name_bytes = self.get_drug_name_bytes(self.protocol)
        # 119:224 105-byte [Drug Components]
        drug_components_bytes = self.get_drug_components_bytes(self.protocol)
        #
        send_rx_bytes = b''        
        send_rx_bytes += protocol_bytes
        send_rx_bytes += switches_bytes 
        send_rx_bytes += protocol_crc_bytes
        send_rx_bytes += auth_role_bytes
        send_rx_bytes += rate_factor_bytes
        send_rx_bytes += concentration_modifiable_bytes
        send_rx_bytes += infusion_mode_bytes
        send_rx_bytes += id_bytes
        send_rx_bytes += label_pool_id_bytes
        send_rx_bytes += label_id_bytes
        send_rx_bytes += rate_unit_bytes
        send_rx_bytes += concentration_unit_bytes
        send_rx_bytes += protocol_name_bytes
        send_rx_bytes += drug_name_bytes
        send_rx_bytes += drug_components_bytes
        # Append 0xFF
        while len(send_rx_bytes) < 256 - 4:
            send_rx_bytes += int(0xFF).to_bytes(1, 'little')
        send_rx_hex = send_rx_bytes.hex().upper()
        crc_bytes = crc32c(0, send_rx_hex).to_bytes(4, 'little')
        send_rx_bytes += crc_bytes
        #
        # 256:227 1-byte [Protocol Index]
        if int(self.protocol_index) >= 0:
            protocol_index_bytes = int(self.protocol_index).to_bytes(1, 'little')
        else:
            protocol_index_bytes = int(0xFF).to_bytes(1, 'little')
        # 257:258 1-byte [View Index]
        view_index_bytes = int(self.view_index).to_bytes(1, 'little')
        # 258:259 1-byte [Label Index]
        label_index_bytes = int(self.label_index).to_bytes(1, 'little')
        #
        send_rx_bytes += protocol_index_bytes
        send_rx_bytes += view_index_bytes
        send_rx_bytes += label_index_bytes
        # Append 0x00
        while len(send_rx_bytes) < 512:
            send_rx_bytes += int(0x00).to_bytes(1, 'little')
        # Convert byte array to hex string
        send_rx_hex = send_rx_bytes.hex().upper()
        # send_rx_hex = '000070420000a04100000040000000003c000000000070413c0000000000000000000000000000000000000000005243ffff7f7f00000000000000000000c84200007a4400000000ffffffffffffffff77004000ca46961cffff64000001ffff00000050726f746f636f6c200058595a000000000000006162630000000000000000000000000000000000302e3035206d672f6d6c00000000006566670000000000000000000000000000000000302e3035206d672f6d6c00000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffbbb5984305ffff00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        return send_rx_hex
        
    def get_infusion_mode_bytes(self, protocol):
        '''Get Infusion Mode Bytes'''
        deliveryMode = protocol['content']['deliveryMode']
        delivery_mode_bytes = int(0)
        # Continuous Mode
        if deliveryMode == 'continuousInfusion':
            delivery_mode_bytes = int(0)
        # Bolus Mode
        if deliveryMode == 'bolusInfusion':
            delivery_mode_bytes = int(1)
        # Intermittent Mode
        if deliveryMode == 'intermittentInfusion':
            delivery_mode_bytes = int(2)
        return delivery_mode_bytes.to_bytes(1, 'little')

    def get_concentration_unit_bytes(self, protocol):
        concentration_unit_bytes = int(0)
        drug_unit = ''
        if protocol['content']['drug'] is not None: 
            drug_unit = protocol['content']['drug']['content']['drugAmount']['unit']
        if drug_unit == 'mg':
            concentration_unit_bytes = int(0)
        if drug_unit == 'mcg':
            concentration_unit_bytes = int(1)
        return concentration_unit_bytes.to_bytes(1, 'little')

    def get_rate_unit_bytes(self, protocol):
        '''Get Rate Unit Bytes'''
        delivery_mode = protocol['content']['deliveryMode']
        rate_unit_bytes = int(0)
        # Continuous Mode
        if delivery_mode == 'continuousInfusion':
            rate_unit = protocol['content']['program']['rate']['unit']
            rate_unit_bytes = int(0)
            if rate_unit == 'mL/hr':
                rate_unit_bytes = int(0)
            if rate_unit == 'mg/min':
                rate_unit_bytes = int(1)
            if rate_unit == 'mg/kg/min':
                rate_unit_bytes = int(2)
            if rate_unit == 'mcg/min':
                rate_unit_bytes = int(3)
            if rate_unit == 'mcg/kg/min':
                rate_unit_bytes = int(4)
        # Bolus Mode
        if delivery_mode == 'bolusInfusion':
            rate_unit_bytes = int(0)
        # Intermittent Mode
        if delivery_mode == 'intermittentInfusion':
            rate_unit_bytes = int(0)
        return rate_unit_bytes.to_bytes(1, 'little')

    def get_protocol_crc_bytes(self, protocol):
        protocol_crc_bytes = int(0).to_bytes(4, 'little')
        if len(protocol['crc']) == 8:
            # the crc is crc32c
            protocol_crc_bytes = int(protocol['crc'], 16).to_bytes(4, 'little')
        if protocol['crc'].find('MD5--') != -1:
            # the crc is MD5
            md5_ascii = protocol['crc'][5:]
            md5_hex = hexlify(md5_ascii.encode()).decode()
            protocol_crc_bytes = crc32c(0, md5_hex).to_bytes(4, 'little')
            # protocol_crc_bytes = int(1).to_bytes(4, 'little')
        return protocol_crc_bytes

    def get_drug_components_bytes(self, protocol):
        drug_components = None
        drug_components_bytes = b''
        if protocol['content']['drug'] is not None:
            drug_components = protocol['content']['drug']['content']['components']
            if drug_components != []:
                # print('drug_components = {}'.format(drug_components))
                for each in drug_components:
                    component_name = each['name']
                    component_name = component_name.encode()                
                    while len(component_name) < 20:
                        component_name += int(0x0).to_bytes(1, 'little')

                    component_concentration = each['concentration']
                    component_concentration = component_concentration.encode()
                    while len(component_concentration) < 15:
                        component_concentration += int(0x0).to_bytes(1, 'little')

                    drug_components_bytes += component_name
                    drug_components_bytes += component_concentration
            else:
                drug_components = 'No components'
                drug_components_bytes = 'No components'.encode()            
        while len(drug_components_bytes) < 105:
            drug_components_bytes += int(0).to_bytes(1, 'little')
        return drug_components_bytes

    def get_drug_name_bytes(self, protocol):
        '''Get Drug Name Bytes'''
        drug_name_bytes = int(0).to_bytes(1, 'little')
        if protocol['content']['drug'] is not None:
            drug_name_bytes = protocol['content']['drug']['content']['name']
            drug_name_bytes = drug_name_bytes.encode()
        while len(drug_name_bytes) < 10:
            drug_name_bytes += int(0).to_bytes(1, 'little')
        return drug_name_bytes

    def get_protocol_name_bytes(self, protocol):
        '''get protocol name bytes'''
        protocol_name = protocol['content']['name'].rstrip(' \t\r\n\0')
        if len(protocol_name) >= 9:
            protocol_name = protocol_name[0:9]
        protocol_name_bytes = protocol_name.encode()
        while len(protocol_name_bytes) < 10:
            protocol_name_bytes += int(0x0).to_bytes(1, 'little')
        return protocol_name_bytes

    def get_rate_factor_bytes(self, protocol):
        '''get flow rate calibration factor
           in continuous mode'''
        switches = protocol['content']['program']['switches']
        if switches['flowRateCalibrationFactor']:
            rate_factor_bytes = int(protocol['content']['program']['flowRateCalibrationFactor']['value'])        
        else:
            rate_factor_bytes = int(100)
        rate_factor_bytes = rate_factor_bytes.to_bytes(2, 'little')
        return rate_factor_bytes

    def get_switches_bytes(self, protocol):
        '''get switches of the protocol
           in continuous mode
           
           protocol - python dict converted from JSON string
           switches - 32-bit (4-byte) integer
           
           Description: 
           If the parameter is used, the corresponding bit is set, 
           otherwise, the corresponding bit is cleared
        '''
        switches = protocol['content']['program']['switches']
        protocol_switches = int(0)
        if protocol['content']['deliveryMode'] == 'continuousInfusion':
            # Rate
            if switches['rate']:
                protocol_switches |= 1 << 0
            # Vtbi
            if switches['vtbi']:
                protocol_switches |= 1 << 1
            # Time
            if switches['time']:
                protocol_switches |= 1 << 3
            # Delay Start
            if switches['delayStart']:
                protocol_switches |= 1 << 4
            # KVO Rate
            if switches.get('kvoRate') != None and switches['kvoRate']:
                protocol_switches |= 1 << 5
            # Delay KVO Rate
            if switches['delayKvoRate']:
                protocol_switches |= 1 << 6
        
            rate_unit = protocol['content']['program']['rate']['unit']
            if rate_unit is not None:
                # Concentration
                if rate_unit != 'mL/hr':
                    protocol_switches |= 1 << 7
                # Weight
                if rate_unit == 'mg/kg/min' or rate_unit == 'mcg/kg/min':
                    protocol_switches |= 1 << 10
            # Drug Amount
            if protocol['content']['drug'] is not None:
                protocol_switches |= 1 << 22
        if protocol['content']['deliveryMode'] == 'bolusInfusion':
            # Basal Rate
            if switches['basalRate']:
                protocol_switches |= 1 << 0
            # VTBI
            if switches['vtbi']:
                protocol_switches |= 1 << 1
            # Loading Dose Amount
            if switches['loadingDoseAmount']:
                protocol_switches |= 1 << 2
            # Delay Start
            if switches['delayStart']:
                protocol_switches |= 1 << 4
            # Auto Bolus Amount
            if switches['autoBolusAmount']:
                protocol_switches |= 1 << 5
            # Bolus Interval
            if switches['bolusInterval']:
                protocol_switches |= 1 << 6
            # Demand Bolus Amount
            if switches['demandBolusAmount']:
                protocol_switches |= 1 << 7
            # Lockout Time
            if switches['lockoutTime']:
                protocol_switches |= 1 << 8
            # Delay KVO Rate
            if switches['delayKvoRate']:
                protocol_switches |= 1 << 10
            # Max Amount Per Hour
            if switches['maxAmountPerHour']:
                protocol_switches |= 1 << 11
            # Max Amount Per Interval
            if switches['maxAmountPerInterval']:
                protocol_switches |= 1 << 12
            # Clinician Dose
            if switches['clinicianDose']:
                protocol_switches |= 1 << 13
            # Concentration
            basal_rate_unit = protocol['content']['program']['basalRate']['unit']
            if basal_rate_unit != 'mL/hr':
                protocol_switches |= 1 << 14
            if protocol['content']['drug'] is not None:
                # Drug Amount
                # protocol_switches |= 1 << 15
                # Dilute Volume
                # protocol_switches |= 1 << 16
                pass
            # Weight
            if basal_rate_unit == 'mg/kg/min' or basal_rate_unit == 'mcg/kg/min':
                protocol_switches |= 1 << 17
            # Drug Amount
            if protocol['content']['drug'] is not None:
                protocol_switches |= 1 << 22
        if protocol['content']['deliveryMode'] == 'intermittentInfusion':
            # Dose Rate
            if switches['doseRate']:
                protocol_switches |= 1 << 0
            # Dose VTBI
            if switches['doseVtbi']:
                protocol_switches |= 1 << 1
            # Total Time
            if switches['totalTime']:
                protocol_switches |= 1 << 3
            # Interval Time
            if switches['intervalTime']:
                protocol_switches |= 1 << 4
            # Delay Start
            if switches['delayStart']:
                protocol_switches |= 1 << 5
            # Intermittent KVO Rate
            if switches['intermittentKvoRate']:
                protocol_switches |= 1 << 6
            # KVO Rate
            if switches.get('kvoRate') != None and switches['kvoRate']:
                protocol_switches |= 1 << 7
            # Delay KVO Rate
            if switches['delayKvoRate']:
                protocol_switches |= 1 << 8
            # Max Amount Per Hour
            if switches['maxAmountPerHour']:
                protocol_switches |= 1 << 9
            # Max Amount Per Interval
            if switches['maxAmountPerInterval']:
                protocol_switches |= 1 << 10
            # Concentration
            dose_rate_unit = protocol['content']['program']['doseRate']['unit']
            if dose_rate_unit != 'mL/hr':
                protocol_switches |= 1 << 11
            if protocol['content']['drug'] is not None:
                # Drug Amount
                # protocol_switches |= 1 << 12
                # Dilute Volume
                # protocol_switches |= 1 << 13
                pass
            # Weight
            if dose_rate_unit == 'mg/kg/min' or dose_rate_unit == 'mcg/kg/min':
                protocol_switches |= 1 << 14
            # Drug Amount
            if protocol['content']['drug'] is not None:
                protocol_switches |= 1 << 22
        return protocol_switches.to_bytes(4, 'little')

    def get_protocol_bytes(self, protocol):
        '''get protocol bytes
           get a byte array of the protocol (80-byte)
           protocol - python dict converted from JSON string'''
        deliveryMode = protocol['content']['deliveryMode']
        switches = protocol['content']['program']['switches']
        # Continuous Mode
        if deliveryMode == 'continuousInfusion':
            # 0:4 Rate 4-byte
            rate_bytes = float(0)
            if switches['rate']:
                rate_bytes = float(protocol['content']['program']['rate']['value'])
            else:
                rate_bytes = float(0)
            rate_bytes = bytearray(struct.pack("f", rate_bytes))        
            # 4:8 VTBI 4-byte
            if switches['vtbi']:
                vtbi_bytes = float(protocol['content']['program']['vtbi']['value'])
            else:
                vtbi_bytes = float(0)
            vtbi_bytes = bytearray(struct.pack("f", vtbi_bytes))
            # 8:12 Loading Dose 4-byte
            loading_dose_bytes = float(0)
            loading_dose_bytes = bytearray(struct.pack("f", loading_dose_bytes))
            # 12:16 Time 4-byte
            if switches['time']:
                time_bytes = int(protocol['content']['program']['time']['value']) * 60
            else:
                time_bytes = int(0)
            time_bytes = time_bytes.to_bytes(4, 'little')
            # 16:20 Delay Start 4-byte
            if switches['delayStart']:
                delay_start_bytes = int(protocol['content']['program']['delayStart']['value'])
                # convert minutes to seconds
                delay_start_bytes = delay_start_bytes * 60
            else:
                delay_start_bytes = int(0)
            delay_start_bytes = delay_start_bytes.to_bytes(4, 'little')
            # 20:24 KVO Rate 4-byte
            if switches.get('kvoRate') != None and switches['kvoRate']:
                kvo_rate_bytes = float(protocol['content']['program']['kvoRate']['value'])
            else:
                kvo_rate_bytes = float(0)
            kvo_rate_bytes = bytearray(struct.pack("f", kvo_rate_bytes))        
            # 24:28 Delay KVO Rate 4-byte
            if switches['delayKvoRate']:
                delay_kvo_rate_bytes = float(protocol['content']['program']['delayKvoRate']['value'])
            else:
                delay_kvo_rate_bytes = float(0)
            delay_kvo_rate_bytes = bytearray(struct.pack("f", delay_kvo_rate_bytes))
            # 28:32 Concentration 4-byte
            if protocol['content']['drug'] is not None:
                drug_amount_bytes = float(protocol['content']['drug']['content']['drugAmount']['value'])
                solvent_volume_bytes = float(protocol['content']['drug']['content']['diluteVolume']['value'])
                concentration_bytes = drug_amount_bytes / solvent_volume_bytes
                concentration_bytes = bytearray(struct.pack("f", concentration_bytes))
            else:
                concentration_bytes = bytearray(struct.pack("f", 0))
            # 32:36 Drug Amount 4-byte
            if protocol['content']['drug'] is not None:
                drug_amount_bytes = float(protocol['content']['drug']['content']['drugAmount']['value'])
                drug_amount_bytes = bytearray(struct.pack("f", drug_amount_bytes))
            else:
                drug_amount_bytes = bytearray(struct.pack("f", 0))
            # 36:40 Solvent Volume 4-byte
            if protocol['content']['drug'] is not None:
                solvent_volume_bytes = float(protocol['content']['drug']['content']['diluteVolume']['value'])
                solvent_volume_bytes = bytearray(struct.pack("f", solvent_volume_bytes))
            else:
                solvent_volume_bytes = bytearray(struct.pack("f", 0))
            # 40:44 Weight 4-byte
            if self.weight is None: 
                self.weight = get_patient_weight(protocol)
            weight_bytes = bytearray(struct.pack("f", self.weight))

            protocol_bytes = b''
            protocol_bytes += rate_bytes
            protocol_bytes += vtbi_bytes
            protocol_bytes += loading_dose_bytes
            protocol_bytes += time_bytes
            protocol_bytes += delay_start_bytes
            protocol_bytes += kvo_rate_bytes
            protocol_bytes += delay_kvo_rate_bytes
            protocol_bytes += concentration_bytes
            protocol_bytes += drug_amount_bytes
            protocol_bytes += solvent_volume_bytes
            protocol_bytes += weight_bytes

        # Bolus Mode
        if deliveryMode == 'bolusInfusion':
            # 0:4 Basal Rate 4-byte Float
            basal_rate_bytes = float(0)
            if switches['basalRate']:
                basal_rate_bytes = float(protocol['content']['program']['basalRate']['value'])
            else:
                basal_rate_bytes = float(0)
            basal_rate_bytes = bytearray(struct.pack("f", basal_rate_bytes))        
            # 4:8 VTBI 4-byte Float
            if switches['vtbi']:
                vtbi_bytes = float(protocol['content']['program']['vtbi']['value'])
            else:
                vtbi_bytes = float(0)
            vtbi_bytes = bytearray(struct.pack("f", vtbi_bytes))
            # 8:12 Loading Dose 4-byte Float
            if switches['loadingDoseAmount']:
                loading_dose_bytes = float(protocol['content']['program']['loadingDoseAmount']['value'])
            else:
                loading_dose_bytes = float(0)
            loading_dose_bytes = bytearray(struct.pack("f", loading_dose_bytes))
            # 12:16 Time 4-byte Integer
            time_bytes = int(0)
            time_bytes = time_bytes.to_bytes(4, 'little')
            # 16:20 Delay Start 4-byte Integer
            if switches['delayStart']:
                delay_start_bytes = int(protocol['content']['program']['delayStart']['value'])
                # convert minutes to seconds
                delay_start_bytes = delay_start_bytes * 60
            else:
                delay_start_bytes = int(0)
            delay_start_bytes = delay_start_bytes.to_bytes(4, 'little')
            # 20:24 Auto Bolus Amount 4-byte Float
            if switches['autoBolusAmount']:
                auto_bolus_amount_bytes = float(protocol['content']['program']['autoBolusAmount']['value'])
            else:
                auto_bolus_amount_bytes = float(0)
            auto_bolus_amount_bytes = bytearray(struct.pack("f", auto_bolus_amount_bytes))
            # 24:28 Auto Bolus Interval 4-byte Integer (Minute)
            if switches['bolusInterval']:
                auto_bolus_interval_bytes = int(protocol['content']['program']['bolusInterval']['value'])
                # convert minutes to seconds
                auto_bolus_interval_bytes = auto_bolus_interval_bytes * 60
            else:
                auto_bolus_interval_bytes = int(0)
            auto_bolus_interval_bytes = auto_bolus_interval_bytes.to_bytes(4, 'little')
            # 28:32 Demand Bolus Volume 4-byte Float
            if switches['demandBolusAmount']:
                demand_bolus_amount_bytes = float(protocol['content']['program']['demandBolusAmount']['value'])
            else:
                demand_bolus_amount_bytes = float(0)
            demand_bolus_amount_bytes = bytearray(struct.pack("f", demand_bolus_amount_bytes))
            # 32:36 Demand Bolus Lockout Time 4-byte Integer
            if switches['lockoutTime']:
                lockout_time_bytes = int(protocol['content']['program']['lockoutTime']['value'])
                # convert minutes to seconds
                lockout_time_bytes = lockout_time_bytes * 60
            else:
                lockout_time_bytes = int(0)
            lockout_time_bytes = lockout_time_bytes.to_bytes(4, 'little')
            # 36:40 KVO Rate 4-byte Float
            kvo_rate_bytes = float(0)
            kvo_rate_bytes = bytearray(struct.pack("f", kvo_rate_bytes))        
            # 40:44 Delay KVO Rate 4-byte Float
            if switches['delayKvoRate']:
                delay_kvo_rate_bytes = float(protocol['content']['program']['delayKvoRate']['value'])
            else:
                delay_kvo_rate_bytes = float(0)
            delay_kvo_rate_bytes = bytearray(struct.pack("f", delay_kvo_rate_bytes))
            # 44:48 Max Amount Per Hour 4-byte Float
            if switches['maxAmountPerHour']:
                max_amount_per_hour = float(protocol['content']['program']\
                        ['maxAmountPerHour']['value'])
            else:
                max_amount_per_hour = float(0)
                max_amount_per_hour = float(210)
            max_amount_per_hour_bytes = bytearray(struct.pack("f", max_amount_per_hour))
            # 48:52 Max Amount Per Interval 4-byte Float
            if switches['maxAmountPerInterval']:
                max_amount_per_interval = float(protocol['content']['program']\
                        ['maxAmountPerInterval']['value'])
                max_amount_per_interval_bytes = bytearray(struct.pack("f", max_amount_per_interval))
            else:
                max_amount_per_interval = float(0)
                max_amount_per_interval_bytes = bytearray.fromhex('ffff7f7f')
            # 52:56 Clinician Dose 4-byte Float
            if switches['clinicianDose']:
                clinician_dose_bytes = float(protocol['content']['program']['clinicianDose']['value'])
            else:
                clinician_dose_bytes = float(0)
            clinician_dose_bytes = bytearray(struct.pack("f", clinician_dose_bytes))
            # 56:60 Concentration 4-byte Float
            if protocol['content']['drug'] is not None:
                # drug_amount_bytes = float(protocol['content']['drug']['content']['drugAmount']['value'])
                # solvent_volume_bytes = float(protocol['content']['drug']['content']['diluteVolume']['value'])
                # concentration = drug_amount_bytes / solvent_volume_bytes
                # concentration_bytes = bytearray(struct.pack("f", concentration))
                concentration_bytes = bytearray(struct.pack("f", float(0)))
            else:
                concentration_bytes = bytearray(struct.pack("f", 0))
            # 60:64 Drug Amount 4-byte Float
            if protocol['content']['drug'] is not None:
                drug_amount_bytes = float(protocol['content']['drug']['content']['drugAmount']['value'])
                drug_amount_bytes = bytearray(struct.pack("f", drug_amount_bytes))
            else:
                drug_amount_bytes = bytearray(struct.pack("f", 0))
            # 64:68 Solvent Volume 4-byte Float
            if protocol['content']['drug'] is not None:
                solvent_volume_bytes = float(protocol['content']['drug']['content']['diluteVolume']['value'])
                solvent_volume_bytes = bytearray(struct.pack("f", solvent_volume_bytes))
            else:
                solvent_volume_bytes = bytearray(struct.pack("f", 0))
            # 68:72 Weight 4-byte Float
            weight_bytes = float(0)
            weight_bytes = bytearray(struct.pack("f", weight_bytes))

            protocol_bytes = b''
            protocol_bytes += basal_rate_bytes
            protocol_bytes += vtbi_bytes
            protocol_bytes += loading_dose_bytes
            protocol_bytes += time_bytes
            protocol_bytes += delay_start_bytes
            protocol_bytes += auto_bolus_amount_bytes
            protocol_bytes += auto_bolus_interval_bytes
            protocol_bytes += demand_bolus_amount_bytes
            protocol_bytes += lockout_time_bytes
            protocol_bytes += kvo_rate_bytes
            protocol_bytes += delay_kvo_rate_bytes
            protocol_bytes += max_amount_per_hour_bytes
            protocol_bytes += max_amount_per_interval_bytes
            protocol_bytes += clinician_dose_bytes
            protocol_bytes += concentration_bytes
            protocol_bytes += drug_amount_bytes
            protocol_bytes += solvent_volume_bytes
            protocol_bytes += weight_bytes

        # Intermittent Mode
        if deliveryMode == 'intermittentInfusion':
            # 0:4 Dose Rate 4-Byte Float
            dose_rate_bytes = float(0)
            if switches['doseRate']:
                dose_rate_bytes = float(protocol['content']['program']['doseRate']['value'])
            else:
                dose_rate_bytes = float(0)
            dose_rate_bytes = bytearray(struct.pack("f", dose_rate_bytes))        
            # 4:8 Dose VTBI 4-Byte Float
            if switches['doseVtbi']:
                dose_vtbi_bytes = float(protocol['content']['program']['doseVtbi']['value'])
            else:
                dose_vtbi_bytes = float(0)
            dose_vtbi_bytes = bytearray(struct.pack("f", dose_vtbi_bytes))
            # 8:12 Loading Dose 4-Byte Float
            loading_dose_bytes = float(0)
            loading_dose_bytes = bytearray(struct.pack("f", loading_dose_bytes))
            # 12:16 Total Time 4-Byte Integer (Minute)
            if switches['totalTime']:
                total_time_bytes = int(protocol['content']['program']['totalTime']['value']) * 60
            else:
                total_time_bytes = int(0)
            total_time_bytes = total_time_bytes.to_bytes(4, 'little')
            # 16:20 Interval Time 4-Byte Integer (Minute)
            if switches['intervalTime']:
                interval_time_bytes = int(protocol['content']['program']['intervalTime']['value']) * 60
            else:
                interval_time_bytes = int(0)
            interval_time_bytes = interval_time_bytes.to_bytes(4, 'little')
            # 20:24 Delay Start 4-Byte Integer (Minute)
            if switches['delayStart']:
                delay_start_bytes = int(protocol['content']['program']['delayStart']['value'])
                # convert minutes to seconds
                delay_start_bytes = delay_start_bytes * 60
            else:
                delay_start_bytes = int(0)
            delay_start_bytes = delay_start_bytes.to_bytes(4, 'little')
            # 24:28 Intermittent KVO Rate 4-Byte Float
            if switches['intermittentKvoRate']:
                intermittent_kvo_rate_bytes = float(protocol['content']['program']['intermittentKvoRate']['value'])
            else:
                intermittent_kvo_rate_bytes = float(0)
            intermittent_kvo_rate_bytes = bytearray(struct.pack("f", intermittent_kvo_rate_bytes))        
            # 28:32 KVO Rate 4-Byte Float
            if switches.get('kvoRate') != None and switches['kvoRate']:
                kvo_rate_bytes = float(protocol['content']['program']['kvoRate']['value'])
            else:
                kvo_rate_bytes = float(0)
            kvo_rate_bytes = bytearray(struct.pack("f", kvo_rate_bytes))        
            # 32:36 Delay KVO Rate 4-Byte Float
            if switches['delayKvoRate']:
                delay_kvo_rate_bytes = float(protocol['content']['program']['delayKvoRate']['value'])
            else:
                delay_kvo_rate_bytes = float(0)
            delay_kvo_rate_bytes = bytearray(struct.pack("f", delay_kvo_rate_bytes))
            # 36:40 Max Amount Per Hour 4-Byte Float
            if switches['maxAmountPerHour']:
                max_amount_per_hour = float(protocol['content']['program']\
                        ['maxAmountPerHour']['value'])
            else:
                max_amount_per_hour = float(0)
                max_amount_per_hour = float(210)
            max_amount_per_hour_bytes = bytearray(struct.pack("f", max_amount_per_hour))
            # 40:44 Max Amount Per Interval 4-Byte Float
            if switches['maxAmountPerInterval']:
                max_amount_per_interval = float(protocol['content']['program']\
                        ['maxAmountPerInterval']['value'])
                max_amount_per_interval_bytes = bytearray(struct.pack("f", max_amount_per_interval))
            else:
                max_amount_per_interval_bytes = float(0)
                max_amount_per_interval_bytes = bytearray.fromhex('ffff7f7f')
            # 44:48 Concentration 4-Byte Float
            if protocol['content']['drug'] is not None:
                # drug_amount_bytes = float(protocol['content']['drug']['content']['drugAmount']['value'])
                # solvent_volume_bytes = float(protocol['content']['drug']['content']['diluteVolume']['value'])
                # concentration = drug_amount_bytes/solvent_volume_bytes
                # concentration_bytes = bytearray(struct.pack("f", concentration))
                concentration_bytes = bytearray(struct.pack("f", float(0)))
            else:
                concentration_bytes = bytearray(struct.pack("f", 0))
            # 48:52 Drug Amount  4-Byte Float
            if protocol['content']['drug'] is not None:
                drug_amount_bytes = float(protocol['content']['drug']['content']['drugAmount']['value'])
                drug_amount_bytes = bytearray(struct.pack("f", drug_amount_bytes))
            else:
                drug_amount_bytes = bytearray(struct.pack("f", 0))
            # 52:56 Solvent Volume 4-Byte Float
            if protocol['content']['drug'] is not None:
                solvent_volume_bytes = float(protocol['content']['drug']['content']['diluteVolume']['value'])
                solvent_volume_bytes = bytearray(struct.pack("f", solvent_volume_bytes))
            else:
                solvent_volume_bytes = bytearray(struct.pack("f", 0))
            # 56:60 Weight 4-Byte Float
            weight_bytes = float(0)
            weight_bytes = bytearray(struct.pack("f", weight_bytes))

            protocol_bytes = b''
            protocol_bytes += dose_rate_bytes
            protocol_bytes += dose_vtbi_bytes
            protocol_bytes += loading_dose_bytes
            protocol_bytes += total_time_bytes
            protocol_bytes += interval_time_bytes
            protocol_bytes += delay_start_bytes
            protocol_bytes += intermittent_kvo_rate_bytes
            protocol_bytes += kvo_rate_bytes
            protocol_bytes += delay_kvo_rate_bytes
            protocol_bytes += max_amount_per_hour_bytes
            protocol_bytes += max_amount_per_interval_bytes
            protocol_bytes += concentration_bytes
            protocol_bytes += drug_amount_bytes
            protocol_bytes += solvent_volume_bytes
            protocol_bytes += weight_bytes
        # Padding with 0xFF
        while (len(protocol_bytes) < self.PROTOCOL_UNION_SIZE):
            protocol_bytes += int(0xFF).to_bytes(1, 'little')
        return protocol_bytes


def main():
    '''main function'''
    cmd = ''
    while cmd not in ['exit', 'quit']:
        cmd = input('>')
        if cmd.upper().rstrip(' \t\r\n\0') in ['HELP', '?']:
            print(' ER - Encrypt Rx JSON To Byte Array')
            print(' PR - Parse Rx Hex')
        # Encrypt Rx JSON To Byte Array
        if cmd.lower().rstrip(' \t\r\n\0') in ['er', 'encrypt rx']:
            # result = False
            print(' ER - Encrypt Rx JSON To Byte Array')
            rx_path = input('    Enter Rx path: ')
            if path.exists(rx_path):
                encrypt_rx(rx_path)
            else:
                if rx_path == '':
                    pass
                else:
                    print('Abort: path NOT exist')
        # Parse Rx Hex
        if cmd.lower().rstrip(' \t\r\n\0') in ['pr', 'parse rx']:
            # result = False
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


if __name__ == "__main__":
    main()
    
