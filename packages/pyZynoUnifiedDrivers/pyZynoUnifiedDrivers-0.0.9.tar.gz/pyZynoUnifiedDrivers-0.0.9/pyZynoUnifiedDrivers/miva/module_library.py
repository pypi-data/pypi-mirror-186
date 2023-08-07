'''module Library'''
from os import path
import time
import json
import struct
from binascii import hexlify
from pyZynoUnifiedDrivers.miva.module_utils import crc32c, crc_fill, byte_fill


def get_parameter_length(protocol, parameter_name):
    '''Get Parameter Length on the Pump
    The return value is a 2 element array.
    The first element is the total number of digits_str
    The second element is the number of digits of the fractional part'''
    gaurds = protocol['content']['program']['guards']
    parameter_guards = gaurds.get(parameter_name)
    max_value = parameter_guards[0]['max']
    min_value = parameter_guards[0]['min']
    demical_part_length = len(str(int(max_value)))
    print('decimal_part = {}'.format(str(int(max_value))))
    print('demical_part_length = {}'.format(len(str(int(max_value)))))
    fractional_part = 0
    fractional_part_length = 1
    if isinstance(min_value, float):
        fractional_part = min_value - int(min_value)
        fractional_part_length = len(str(fractional_part)) - 2
    if parameter_guards[0]['unit'] == 'mg/min':
        fractional_part_length = 2
    print('fractional_part = {}'.format(fractional_part))
    print('fractional_part_length = {}'.format(fractional_part_length))
    total_length = demical_part_length + fractional_part_length
    if parameter_guards[0]['unit'] == 'minute':
        fractional_part_length = 0
        hour_part_length = len(str(int(max_value / 60)))
        minute_part_length = 2
        total_length = hour_part_length + minute_part_length
    print([int(total_length), int(fractional_part_length)])    
    return [int(total_length), int(fractional_part_length)]


def get_parameter(protocol, parameter_name, infusion=None):
    '''Get Parameter from Protocol'''
    parameter = {'name':'',
                 'value':0,
                 'unit':''}
    if parameter_name == 'weight':
        parameter['name'] = 'weight'
        parameter['value'] = infusion.patient_weight
        parameter['unit'] = 'kg'
        parameter['length'] = 4
        parameter['fract_length'] = 1
        parameter['max'] = 999.9
        parameter['min'] = 1.0
        parameter['upper_limit'] = parameter['max']
        parameter['lower_limit'] = parameter['min']
        # Calculate upper limit and lower limit based on drug concentration
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
            weight_upper_guard = 999.9
            weight_lower_guard = 1
            weight_upper_limit = weight_upper_guard
            weight_lower_limit = weight_lower_guard
            if rate_unit == 'mg/kg/min' and dilute_volume > 0:
                weight_upper_limit = rate_upper_guard * drug_amount \
                        / (rate * 60 * dilute_volume * 1000)
                weight_lower_limit = rate_lower_guard * drug_amount \
                        / (rate * 60 * dilute_volume * 1000)
            if rate_unit == 'mcg/kg/min' and dilute_volume > 0:
                weight_upper_limit = rate_upper_guard * drug_amount \
                        / (rate * 60 * dilute_volume)
                weight_lower_limit = rate_lower_guard * drug_amount \
                        / (rate * 60 * dilute_volume)
            if weight_upper_limit > weight_upper_guard:
                weight_upper_limit = weight_upper_guard
            if weight_lower_limit < weight_lower_guard:
                weight_lower_limit = weight_lower_guard
            parameter['upper_limit'] = weight_upper_limit
            parameter['lower_limit'] = weight_lower_limit
    elif parameter_name == 'drugAmount':
        parameter['name'] = parameter_name
        parameter['value'] = protocol['content']['drug']['content']['drugAmount']['value']
        parameter['unit'] = protocol['content']['drug']['content']['drugAmount']['unit']
        parameter['max'] = 99.9
        parameter['min'] = 0.0
        parameter['length'] = 3
        parameter['fract_length'] = 1
    elif parameter_name == 'diluteVolume':
        parameter['name'] = parameter_name
        parameter['value'] = protocol['content']['drug']['content']['diluteVolume']['value']
        parameter['unit'] = protocol['content']['drug']['content']['diluteVolume']['unit']
        parameter['max'] = 999
        parameter['min'] = 0
        parameter['length'] = 3
        parameter['fract_length'] = 0
    else:
        parameter['name'] = parameter_name
        parameter['value'] = protocol['content']['program'][parameter_name]['value']
        parameter['unit'] = protocol['content']['program'][parameter_name]['unit']
        parameter['max'] = protocol['content']['program']['guards'][parameter_name][0]['max']
        parameter['min'] = protocol['content']['program']['guards'][parameter_name][0]['min']
        parameter_length = get_parameter_length(protocol, parameter_name)
        parameter['length'] = parameter_length[0]
        parameter['fract_length'] = parameter_length[1]
    return parameter


def get_parameter_list(library, protocol):
    '''get parameter indexes'''
    parameter_list = []
    switches = protocol['content']['program']['switches']
    switches_keys = switches.keys()
    for each_key in switches_keys:
        if switches.get(each_key):
            parameter_list.append(each_key)
    #
    extracted_views = library.library['content']['extractedViews']
    new_parameter_list = []
    for each_view in extracted_views:
        if each_view['content']['deliveryMode'] == protocol['content']['deliveryMode']:
            # sort parameter list according to the view
            view_parameters = each_view['content']['parameters']
            for each_view_parameter in view_parameters:
                for each_parameter in parameter_list:
                    if each_view_parameter['name'] == each_parameter:
                        new_parameter_list.append(each_parameter)
            break
    # check if it has ['drug']
    has_drug = protocol['content']['drug'] is not None
    # check if it has ['label']
    protocol_name = protocol['content']['name']
    node_children = library.library['content']['node']['children']
    has_label = find_label_set_name(protocol_name, node_children) is not None
    # check if it has [concentration] or [weight]
    has_concentration = False
    has_weight = False
    if protocol['content']['deliveryMode'] == 'continuousInfusion':
        rate_unit = protocol['content']['program']['rate']['unit']
        if rate_unit is not None:
            if rate_unit != 'mL/hr':
                has_concentration = True
            if rate_unit.lower() in ['mg/kg/min', 'mcg/kg/min']:
                has_weight = True
    #
    if has_drug:
        new_parameter_list.insert(0, 'drug')
    if has_label:
        new_parameter_list.insert(1, 'label')
    if has_concentration:
        new_parameter_list.append('concentration')
    if has_weight:
        new_parameter_list.append('weight')
    return new_parameter_list


def find_label_set_name(protocol_name, node_children):
    label_set_name = None
    temp_label_set_name = None
    for each in node_children:
        if (each['type'] == 'folder') and ('children' in each.keys()):
            sub_node_children = each['children']
            # DFS recursive algorithm
            temp_label_set_name = find_label_set_name(protocol_name, sub_node_children)
        elif each['type'] == 'protocol' and each['name'] == protocol_name:
            if each['labelSet'] is not None:
                temp_label_set_name = each['labelSet']['name']
        if temp_label_set_name is not None:
            label_set_name = temp_label_set_name
    
    return  label_set_name


def find_label_set(label_set_name, label_sets):
    '''find label set'''
    label_set = None
    for each in label_sets:
        if each['name'] == label_set_name:
            label_set = each
    return  label_set


def find_label_set_index(label_set_name, label_sets):
    '''find label set index'''
    label_set_index = int(0xFF)
    temp_label_set_index = 0
    for each in label_sets:
        if each['name'] == label_set_name:
            label_set_index = temp_label_set_index
        temp_label_set_index += 1
    return  label_set_index


def find_view_id(protocol_name, node_children):
    '''find view ID'''
    view_id = None
    temp_view_id = None
    for each in node_children:
        if (each['type'] == 'folder') and ('children' in each.keys()):
            sub_node_children = each['children']
            temp_view_id = find_view_id(protocol_name, sub_node_children)
        elif each['type'] == 'protocol' and each['name'] == protocol_name:
            if each['view'] is not None:
                temp_view_id = each['view']['id']
        if temp_view_id is not None:
            view_id = temp_view_id
    
    return  view_id


def find_view_index(view_id, views):
    '''find view index'''
    view_index = int(0xFF)
    temp_view_index = 0
    for each in views:
        if each['view']['id'] == int(view_id):
            view_index = temp_view_index
        temp_view_index += 1
    return  view_index


def get_children_index_array_bytes(initial_index, number_of_children):
    '''get children index array bytes
    Input:
        initial_index - the initial index to start with.
        number of children = the number of children that the parent node has
    Output:
        The byte array (10-byte) of the children index (ex. '01020300000000000000')
    '''
    children_index_array_bytes = bytearray(0)
    for offset in range(1, number_of_children + 1):
        children_index_array_bytes += int(initial_index + offset).to_bytes(1, 'little')
    # Append 0x00 - Children Index Array
    children_index_array_size = 10
    while len(children_index_array_bytes) < children_index_array_size:
        children_index_array_bytes += int(0).to_bytes(1, 'little')
    return children_index_array_bytes


def get_label_bytes(node):
    '''get label bytes
       Get the node name if it is NOT 'standbyRoot', 'configRoot' or 'infusionRoot'. 
       Otherwise, filled with [0x00]) (16-Byte String)
    '''
    label_bytes = bytearray(0)
    if node['name'] not in ['standbyRoot', 'configRoot', 'infusionRoot']:
        label_bytes = node['name'][0:15].encode()
    else:
        pass
    # Append 0x00 - Label
    label_size = 16
    while len(label_bytes) < label_size:
        label_bytes += int(0x00).to_bytes(1, 'little')
    return label_bytes


def get_content_bytes(node):
    '''get content bytes
       Get the node display name if exist. 
       Otherwise, get the node name (16-Byte String)
    '''
    content_bytes = bytearray(0)
    if node.get('displayName') != None and node['displayName'] != []:
        content_bytes = node['displayName'][0:15].encode()
    else:
        content_bytes = node['name'].encode()
    # Append 0x00 - Content
    content_size = 16
    while len(content_bytes) < content_size:
        content_bytes += int(0x00).to_bytes(1, 'little')
    return content_bytes


def get_type_bytes(node):
    '''get type bytes'''
    node_type = node['type']
    # type_bytes = bytearray(0)
    type_bytes = int(0).to_bytes(1, 'little')
    if node_type in ['next_layer', 'folder']:
        type_bytes = int(1).to_bytes(1, 'little')
    if node_type == 'protocol':
        type_bytes = int(2).to_bytes(1, 'little')
    if node_type == 'new_infusion':
        type_bytes = int(3).to_bytes(1, 'little')
    if node_type == 'resume_infusion':
        type_bytes = int(4).to_bytes(1, 'little')
    if node_type == 'review_rx':
        type_bytes = int(5).to_bytes(1, 'little')
    if node_type == 'titration':
        type_bytes = int(6).to_bytes(1, 'little')
    if node_type == 'request_clinician_dose':
        type_bytes = int(7).to_bytes(1, 'little')
    if node_type == 'patient_titrate':
        type_bytes = int(8).to_bytes(1, 'little')
    if node_type == 'clear_shift_total':
        type_bytes = int(9).to_bytes(1, 'little')
    if node_type == 'last_layer':
        type_bytes = int(10).to_bytes(1, 'little')
    if node_type == 'shift_total':
        type_bytes = int(11).to_bytes(1, 'little')
    if node_type == 'shift_total_volume':
        type_bytes = int(12).to_bytes(1, 'little')
    if node_type == 'shift_bolus_attempts':
        type_bytes = int(13).to_bytes(1, 'little')
    if node_type == 'shift_bolus_delivers':
        type_bytes = int(14).to_bytes(1, 'little')
    if node_type == 'shift_time':
        type_bytes = int(15).to_bytes(1, 'little')
    if node_type == 'clinician_dose_vol':
        type_bytes = int(16).to_bytes(1, 'little')
    if node_type == 'reset_battery':
        type_bytes = int(19).to_bytes(1, 'little')
    if node_type == 'pump_info':
        type_bytes = int(20).to_bytes(1, 'little')
    return type_bytes


def get_visibility_bytes(node):
    '''get visibility bytes
       return 0x00 if the node is visible
       otherwise, return 0x01
    '''
    if node.get('visibility') != None and node['visibility'] != None:
        visibility = 0 if node['visibility'] else 1
    else:
        visibility = 0
    return int(visibility).to_bytes(1, 'little')


def get_protocol_bytes(protocol):
    '''get protocol bytes
       get a byte array of the protocol (80-byte)
       protocol - python dict converted from JSON string'''
    infusion_mode = protocol['content']['deliveryMode']
    switches = protocol['content']['program']['switches']
    # Continuous Mode
    if infusion_mode == 'continuousInfusion':
        # 0:4 Rate 4-byte Float
        rate_bytes = float(0)
        if switches['rate']:
            rate_bytes = float(protocol['content']['program']['rate']['value'])
        else:
            rate_bytes = float(0)
        rate_bytes = bytearray(struct.pack("f", rate_bytes))        
        # 4:8 VTBI 4-byte Float
        if switches['vtbi']:
            vtbi_bytes = float(protocol['content']['program']['vtbi']['value'])
        else:
            vtbi_bytes = float(0)
        vtbi_bytes = bytearray(struct.pack("f", vtbi_bytes))
        # 8:12 Loading Dose 4-byte Float
        loading_dose_bytes = float(0)
        loading_dose_bytes = bytearray(struct.pack("f", loading_dose_bytes))
        # 12:16 Time 4-byte Integer
        if switches['time']:
            time_bytes = int(protocol['content']['program']['time']['value']) * 60
        else:
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
        # 20:24 KVO Rate 4-byte Float
        if switches.get('kvoRate') != None and switches['kvoRate']:
            kvo_rate_bytes = float(protocol['content']['program']['kvoRate']['value'])
        else:
            kvo_rate_bytes = float(0)
        kvo_rate_bytes = bytearray(struct.pack("f", kvo_rate_bytes))        
        # 24:28 Delay KVO Rate 4-byte Float
        if switches['delayKvoRate']:
            delay_kvo_rate_bytes = float(protocol['content']['program']['delayKvoRate']['value'])
        else:
            delay_kvo_rate_bytes = float(0)
        delay_kvo_rate_bytes = bytearray(struct.pack("f", delay_kvo_rate_bytes))
        # 28:32 Concentration 4-byte Float
        if protocol['content']['drug'] is not None:
            drug_amount_bytes = float(protocol['content']['drug']['content']['drugAmount']['value'])
            solvent_volume_bytes = float(protocol['content']['drug']['content']['diluteVolume']['value'])
            concentration_bytes = drug_amount_bytes / solvent_volume_bytes
            concentration_bytes = bytearray(struct.pack("f", concentration_bytes))
        else:
            concentration_bytes = bytearray(struct.pack("f", 0))
        # 32:36 Drug Amount 4-byte Float
        if protocol['content']['drug'] is not None:
            drug_amount_bytes = float(protocol['content']['drug']['content']['drugAmount']['value'])
            drug_amount_bytes = bytearray(struct.pack("f", drug_amount_bytes))
        else:
            drug_amount_bytes = bytearray(struct.pack("f", 0))
        # 36:40 Solvent Volume 4-byte Float
        if protocol['content']['drug'] is not None:
            solvent_volume_bytes = float(protocol['content']['drug']['content']['diluteVolume']['value'])
            solvent_volume_bytes = bytearray(struct.pack("f", solvent_volume_bytes))
        else:
            solvent_volume_bytes = bytearray(struct.pack("f", 0))
        # 40:44 Weight 4-byte Float
        # weight = get_patient_weight(protocol)
        weight = float(0)
        weight_bytes = bytearray(struct.pack("f", weight))

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
    if infusion_mode == 'bolusInfusion':
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
        # 24:28 Auto Bolus Interval 4-byte Integer
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
            clinician_dose = float(protocol['content']['program']['clinicianDose']['value'])
        else:
            clinician_dose = float(0)
        clinician_dose_bytes = bytearray(struct.pack("f", clinician_dose))
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
            drug_amount = float(protocol['content']['drug']['content']['drugAmount']['value'])
            drug_amount_bytes = bytearray(struct.pack("f", drug_amount))
        else:
            drug_amount_bytes = bytearray(struct.pack("f", 0))
        # 64:68 Solvent Volume 4-byte Float
        if protocol['content']['drug'] is not None:
            solvent_volume = float(protocol['content']['drug']['content']['diluteVolume']['value'])
            solvent_volume_bytes = bytearray(struct.pack("f", solvent_volume))
        else:
            solvent_volume_bytes = bytearray(struct.pack("f", 0))
        # 68 Weight 4-byte Float
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
    if infusion_mode == 'intermittentInfusion':
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
        # 36:40 Max Per Hour 4-Byte Float
        if switches['maxAmountPerHour']:
            max_amount_per_hour = float(protocol['content']['program']\
                    ['maxAmountPerHour']['value'])
        else:
            max_amount_per_hour = float(0)
            max_amount_per_hour = float(210)
        max_amount_per_hour_bytes = bytearray(struct.pack("f", max_amount_per_hour))
        # 40:44 Max Per Interval 4-Byte Float
        if switches['maxAmountPerInterval']:
            max_amount_per_interval = float(protocol['content']['program']\
                    ['maxAmountPerInterval']['value'])
            max_amount_per_interval_bytes = bytearray(struct.pack("f", max_amount_per_interval))
        else:
            max_amount_per_interval = float(0)
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
    protocol_union_size = 80
    protocol_bytes = byte_fill(protocol_bytes, protocol_union_size)
    return protocol_bytes


def get_switches_bytes(protocol):
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


def get_protocol_crc_bytes(protocol):
    protocol_crc_bytes = int(0).to_bytes(4, 'little')
    if len(protocol['crc']) == 8:
        protocol_crc_bytes = int(protocol['crc'], 16).to_bytes(4, 'little')
    if protocol['crc'].find('MD5--') != -1:
        # the crc is MD5
        md5_ascii = protocol['crc'][5:]
        md5_hex = hexlify(md5_ascii.encode()).decode()
        protocol_crc_bytes = crc32c(0, md5_hex).to_bytes(4, 'little')
    return protocol_crc_bytes


def get_rate_factor_bytes(protocol):
    '''get flow rate calibration factor
       in continuous mode'''
    switches = protocol['content']['program']['switches']
    if switches['flowRateCalibrationFactor']:
        rate_factor_bytes = int(protocol['content']['program']['flowRateCalibrationFactor']['value'])        
    else:
        rate_factor_bytes = int(100)
    rate_factor_bytes = rate_factor_bytes.to_bytes(2, 'little')
    return rate_factor_bytes


def get_infusion_mode_bytes(protocol):
    '''Get Infusion Mode Bytes'''
    infusion_mode = protocol['content']['deliveryMode']
    infusion_mode_bytes = int(0)
    # Continuous Mode
    if infusion_mode == 'continuousInfusion':
        infusion_mode_bytes = int(0)
    # Bolus Mode
    if infusion_mode == 'bolusInfusion':
        infusion_mode_bytes = int(1)
    # Intermittent Mode
    if infusion_mode == 'intermittentInfusion':
        infusion_mode_bytes = int(2)
    return infusion_mode_bytes.to_bytes(1, 'little')


def get_rate_unit_bytes(protocol):
    '''Get Rate Unit Bytes'''
    infusion_mode = protocol['content']['deliveryMode']
    rate_unit_bytes = int(0)
    # Continuous Mode
    if infusion_mode == 'continuousInfusion':
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
    if infusion_mode == 'bolusInfusion':
        rate_unit_bytes = int(0)
    # Intermittent Mode
    if infusion_mode == 'intermittentInfusion':
        rate_unit_bytes = int(0)
    return rate_unit_bytes.to_bytes(1, 'little')


def get_concentration_unit_bytes(protocol):
    concentration_unit_bytes = int(0)
    drug_unit = ''
    if protocol['content']['drug'] is not None: 
        drug_unit = protocol['content']['drug']['content']['drugAmount']['unit']
    if drug_unit == 'mg':
        concentration_unit_bytes = int(0)
    if drug_unit == 'mcg':
        concentration_unit_bytes = int(1)
    return concentration_unit_bytes.to_bytes(1, 'little')


def get_name_bytes(protocol):
    '''get name bytes 10-byte'''
    name = protocol['content']['name']
    if len(name) >= 9:
        name = name[0:9]
    name_bytes = name.encode()
    while len(name_bytes) < 10:
        name_bytes += int(0x0).to_bytes(1, 'little')
    return name_bytes


def get_drug_name_bytes(protocol):
    '''Get Drug Name Bytes 10-byte'''
    drug_name_bytes = int(0).to_bytes(1, 'little')
    if protocol['content']['drug'] is not None:
        drug_name = protocol['content']['drug']['content']['name']
        if len(drug_name) >= 9:
            drug_name = drug_name[0:9]
        drug_name_bytes = drug_name.encode()
    while len(drug_name_bytes) < 10:
        drug_name_bytes += int(0).to_bytes(1, 'little')
    return drug_name_bytes


def get_drug_components_bytes(protocol):
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

# def get_patient_weight(protocol):
    # patient_weight = 0
    # switches = protocol['content']['program']['switches']
    # if switches['rate']:
        # rate_str = protocol['content']['program']['rate']['value']
        # rate = float(rate_str)
        # rate_unit = protocol['content']['program']['rate']['unit']
        # # drug amount (mcg)
        # drug_amount = get_drug_amount(protocol)
        # # dilute volume (mL)
        # dilute_volume = get_dilute_volume(protocol)
        # # weight (kg)
        # if rate_unit in ('mg/kg/min', 'mcg/kg/min'):
            # rate_upper_guard = 135
            # rate_lower_guard = 0
            # if rate_unit == 'mg/kg/min':
                # weight_upper_limit = rate_upper_guard * drug_amount \
                            # / (rate * 60 * dilute_volume * 1000)
                # weight_lower_limit = rate_lower_guard * drug_amount \
                            # / (rate * 60 * dilute_volume * 1000)
            # if rate_unit == 'mcg/kg/min':
                # weight_upper_limit = rate_upper_guard * drug_amount \
                            # / (rate * 60 * dilute_volume)
                # weight_lower_limit = rate_lower_guard * drug_amount \
                            # / (rate * 60 * dilute_volume)
            
            # patient_weight = input("    Input Patient Weight ({0:3.1f} - {1:3.1f} kg): "\
                            # .format(weight_lower_limit, weight_upper_limit)) \
                            # or (weight_upper_limit - weight_lower_limit) / 2
            # try:
                # patient_weight = float(patient_weight)
            # except ValueError:
                # patient_weight = 0

            # if patient_weight > weight_upper_limit:
                # patient_weight = weight_upper_limit
            # elif patient_weight < weight_lower_limit:
                # patient_weight = weight_lower_limit
            # print('    patient weight = {:5.2f} kg'.format(patient_weight))
    # return float(patient_weight)


def parse_standby_nodes_hex(standby_nodes_hex):
    '''parse standby hex'''
    # each standby node is 1 block
    number_of_standby_nodes = 100
    block_size = 64
    # standby size = 64 * 100 = 6400
    standby_size = number_of_standby_nodes * block_size
    # convert standby_nodes_hex to standby_nodes_bytes
    standby_nodes_bytes = bytes.fromhex(standby_nodes_hex)
    print('standby nodes size: {} bytes'.format(len(standby_nodes_bytes)))
    if len(standby_nodes_bytes) != standby_size:
        return None
    standby_nodes = []
    # separate 100 standby nodes
    for index in range(number_of_standby_nodes):
        standby_nodes.append(standby_nodes_bytes[index * block_size:(index + 1) * block_size])
    for each_standby_bytes in standby_nodes:
        # convert each_standby_bytes to each_standby_hex
        each_standby_hex = each_standby_bytes.hex()
        print(each_standby_hex)
    print('==standby nodes parsing complete==')


def parse_config_nodes_hex(config_nodes_hex):
    '''parse config hex'''
    # each config node is 1 block
    number_of_config_nodes = 30
    block_size = 64
    # config size = 64 * 30 = 1920
    config_size = number_of_config_nodes * block_size
    # convert config_nodes_hex to config_nodes_bytes
    config_nodes_bytes = bytes.fromhex(config_nodes_hex)
    print('config nodes size: {} bytes'.format(len(config_nodes_bytes)))
    if len(config_nodes_bytes) != config_size:
        return None
    config_nodes = []
    # separate 30 config nodes
    for index in range(number_of_config_nodes):
        config_nodes.append(config_nodes_bytes[index * block_size:(index + 1) * block_size])
    for each_config_bytes in config_nodes:
        # convert each_config_bytes to each_config_hex
        each_config_hex = each_config_bytes.hex()
        print(each_config_hex)
    print('==config nodes parsing complete==')


def parse_infusion_nodes_hex(infusion_nodes_hex):
    '''parse infusion hex'''
    # each infusion node is 1 block
    number_of_blocks_infusion = 61
    block_size = 64
    # infusion size = 64 * 61 = 3904
    infusion_size = number_of_blocks_infusion * block_size
    # convert infusion_nodes_hex to infusion_nodes_bytes
    infusion_nodes_bytes = bytes.fromhex(infusion_nodes_hex)
    print('infusion nodes size: {} bytes'.format(len(infusion_nodes_bytes)))
    if len(infusion_nodes_bytes) != infusion_size:
        return None
    infusion_nodes = []
    # separate 61 config nodes
    for index in range(number_of_blocks_infusion):
        infusion_nodes.append(infusion_nodes_bytes[index * block_size:(index + 1) * block_size])
    for each_infusion_bytes in infusion_nodes:
        # convert each_infusion_bytes to each_infusion_hex
        each_infusion_hex = each_infusion_bytes.hex()
        print(each_infusion_hex)
    print('==infusion nodes parsing complete==')


def parse_meta_data_hex(meta_data_hex):
    '''parse meta data hex'''
    # the meta_data is 1 block
    number_of_blocks_meta_data = 1
    block_size = 64
    # meta data size = 64 * 1 = 64
    meta_data_size = number_of_blocks_meta_data * block_size
    # convert meta_data_hex to meta_data_bytes
    meta_data_bytes = bytes.fromhex(meta_data_hex)
    print('meta data size: {} bytes'.format(len(meta_data_bytes)))
    if len(meta_data_bytes) != meta_data_size:
        return None
    meta_data = []
    # separate 61 meta data
    for index in range(number_of_blocks_meta_data):
        meta_data.append(meta_data_bytes[index * block_size:(index + 1) * block_size])
    for each_meta_data_bytes in meta_data:
        # convert each_meta_data_bytes to each_infusion_hex
        each_meta_data_hex = each_meta_data_bytes.hex()
        print(each_meta_data_hex)
    print('==meta data parsing complete==')


def parse_navigation_hex(navigation_hex):
    '''parse navigation hex'''
    number_of_pages_navigation = 3
    page_size = 4096
    block_size = 64
    # navigation size = 3 * 4096 = 12288
    navigation_size = number_of_pages_navigation * page_size
    # convert navigation_hex to navigation_bytes
    navigation_bytes = bytes.fromhex(navigation_hex)
    print('navigation size: {} bytes'.format(len(navigation_bytes)))
    if len(navigation_bytes) != navigation_size:
        return None
    # 0:100 Standby Nodes (100 blocks)
    standby_nodes_bytes = navigation_bytes[0:block_size * 100]
    standby_nodes_hex = standby_nodes_bytes.hex()
    parse_standby_nodes_hex(standby_nodes_hex)
    # 100:130 Config Nodes (30 blocks)
    config_nodes_bytes = navigation_bytes[block_size * 100:block_size * 130]
    config_nodes_hex = config_nodes_bytes.hex()
    parse_config_nodes_hex(config_nodes_hex)
    # 130:191 Infusion Nodes (61 blocks)
    infusion_nodes_bytes = navigation_bytes[block_size * 130:block_size * 191]
    infusion_nodes_hex = infusion_nodes_bytes.hex()
    parse_infusion_nodes_hex(infusion_nodes_hex)
    # 191:192 Meta Data (1 blocks)
    meta_data_bytes = navigation_bytes[block_size * 191:block_size * 192]
    meta_data_hex = meta_data_bytes.hex()
    parse_meta_data_hex(meta_data_hex)
    print('==navigation parsing complete==')


def parse_protocols_hex(protocols_hex):
    '''parse protocols hex'''
    number_of_pages_protocols = 4
    page_size = 4096
    block_size = 64
    each_protocol_blocks = 4
    # protocol_size = 64 * 4 = 256
    protocol_size = block_size * each_protocol_blocks
    # total size = 4 * 4096 = 16384
    total_size = number_of_pages_protocols * page_size
    # total number of protocols = 16384 / 256 = 64
    total_protocols = int(total_size / protocol_size)
    # convert protocols_hex to protocols_bytes
    protocols_bytes = bytes.fromhex(protocols_hex)
    print('protocols size: {} bytes'.format(len(protocols_bytes)))
    if len(protocols_bytes) != total_size:
        return None
    protocols = []
    # separate 64 library protocols
    for index in range(total_protocols):
        protocols.append(protocols_bytes[index * protocol_size:(index + 1) * protocol_size])
    for each_protocol_bytes in protocols:
        # convert each_protocol_bytes to each_protocol_hex
        each_protocol_hex = each_protocol_bytes.hex()
        print(each_protocol_hex)
    print('==protocols parsing complete==')


def parse_constraints_hex(constraints_hex):
    '''parse constraints hex'''
    number_of_pages_constraints = 4
    page_size = 4096
    block_size = 64
    each_constraint_blocks = 4
    # constraint_size = 64 * 4 = 256
    constraint_size = block_size * each_constraint_blocks
    # total size = 4 * 4096 = 16384
    total_size = number_of_pages_constraints * page_size
    # total number of constraints = 16384 / 256 = 64
    total_constraints = int(total_size / constraint_size)
    # convert constraints_hex to constraints_bytes
    constraints_bytes = bytes.fromhex(constraints_hex)
    print('constraints size: {} bytes'.format(len(constraints_bytes)))
    if len(constraints_bytes) != total_size:
        return None
    constraints = []
    # separate 64 constraints
    for index in range(total_constraints):
        constraints.append(constraints_bytes[index * constraint_size:(index + 1) * constraint_size])
    for each_constraint_bytes in constraints:
        # convert each_constraint_bytes to each_constraint_hex
        each_constraint_hex = each_constraint_bytes.hex()
        print(each_constraint_hex)
    print('==constraints parsing complete==')


def parse_views_hex(views_hex):
    '''parse views hex'''
    number_of_pages_views = 4
    page_size = 4096
    block_size = 64
    each_view_blocks = 4
    # view_size = 64 * 4 = 256
    view_size = block_size * each_view_blocks
    # total size = 4 * 4096 = 16384
    total_size = number_of_pages_views * page_size
    # total number of views = 16384 / 256 = 64
    total_views = int(total_size / view_size)
    # convert views_hex to views_bytes
    views_bytes = bytes.fromhex(views_hex)
    print('views size: {} bytes'.format(len(views_bytes)))
    if len(views_bytes) != total_size:
        return None
    views = []
    # separate 64 views
    for index in range(total_views):
        views.append(views_bytes[index * view_size:(index + 1) * view_size])
    for each_view_bytes in views:
        # convert each_view_bytes to each_view_hex
        each_view_hex = each_view_bytes.hex()
        print(each_view_hex)
    print('==views parsing complete==')


def parse_default_views_hex(default_views_hex):
    '''parse default views hex'''
    number_of_pages_views = 1
    page_size = 4096
    block_size = 64
    each_view_blocks = 4
    # view_size = 64 * 4 = 256
    view_size = block_size * each_view_blocks
    # total size = 1 * 4096 = 4096
    total_size = number_of_pages_views * page_size
    # total number of views = 4096 / 256 = 16
    total_views = int(total_size / view_size)
    # convert default_views_hex to default_views_bytes
    default_views_bytes = bytes.fromhex(default_views_hex)
    print('default views size: {} bytes'.format(len(default_views_bytes)))
    if len(default_views_bytes) != total_size:
        return None
    default_views = []
    # separate 16 default_views
    for index in range(total_views):
        default_views.append(default_views_bytes[index * view_size:(index + 1) * view_size])
    for each_default_view_bytes in default_views:
        # convert each_default_view_bytes to each_default_view_hex
        each_default_view_hex = each_default_view_bytes.hex()
        print(each_default_view_hex)
    print('==default views parsing complete==')


def parse_globals_hex(globals_hex):
    '''parse globals hex'''
    number_of_blocks_globals = 8
    block_size = 64
    # globals_size = 64 * 8 = 512
    globals_size = block_size * number_of_blocks_globals
    # convert globals_hex to globals_bytes
    globals_bytes = bytes.fromhex(globals_hex)
    print('globals size: {} bytes'.format(len(globals_bytes)))
    if len(globals_bytes) != globals_size:
        print('wrong globals size: {0} bytes (expected {1} bytes)'\
                .format(len(globals_bytes), globals_size))
        return None
    print(globals_hex)
    print('==globals parsing complete==')


def parse_label_sets_hex(label_sets_hex):
    '''parse label sets hex'''
    # each label set is 1 block
    number_of_label_sets = 8
    block_size = 64
    # label_sets_size = 64 * 8 = 512
    label_sets_size = number_of_label_sets * block_size
    # convert label_sets_hex to label_sets_bytes
    label_sets_bytes = bytes.fromhex(label_sets_hex)
    print('label sets size: {} bytes'.format(len(label_sets_bytes)))
    if len(label_sets_bytes) != label_sets_size:
        print('wrong label sets size: {0} bytes (expected {1} bytes)'\
                .format(len(label_sets_bytes), label_sets_size))
        return None
    label_sets = []
    # separate 8 label sets
    for index in range(number_of_label_sets):
        label_sets.append(label_sets_bytes[index * block_size:(index + 1) * block_size])
    for each_label_set_bytes in label_sets:
        # convert each_label_set_bytes to each_label_set_hex
        each_label_set_hex = each_label_set_bytes.hex()
        print(each_label_set_hex)
    print('==label sets parsing complete==')

    
def parse_protocol_map_hex(protocol_map_hex):
    '''parse protocol map hex'''
    number_of_blocks_protocol_map = 16
    block_size = 64
    # protocol_map_size = 64 * 16 = 1024
    protocol_map_size = block_size * number_of_blocks_protocol_map
    # convert protocol_map_hex to protocol_map_bytes
    protocol_map_bytes = bytes.fromhex(protocol_map_hex)
    print('protocol_map size: {} bytes'.format(len(protocol_map_bytes)))
    if len(protocol_map_bytes) != protocol_map_size:
        print('wrong protocol map size: {0} bytes (expected {1} bytes)'\
                .format(len(protocol_map_bytes), protocol_map_size))
        return None
    # 0:512 protocol elements (512-Byte)
    # each protocol element is 8-byte
    element_size = 8
    total_elements_size = 512
    # number_of_elements = 512 / 8 = 64
    number_of_elements = int(total_elements_size / element_size)
    protocol_elements = []
    # separate 64 protocol elements
    for index in range(number_of_elements):
        protocol_elements.append(protocol_map_bytes[index * element_size:(index + 1) * element_size])
    for each_element_bytes in protocol_elements:
        # convert each_element_bytes to each_element_hex
        each_element_hex = each_element_bytes.hex()
        print(each_element_hex)
    # 512:1024 Protocol Indices (512-Byte)
    protocol_indices_bytes = protocol_map_bytes[512:1024]
    protocol_indices_hex = protocol_indices_bytes.hex()
    print(protocol_indices_hex)
    print('==protocol map parsing complete==')


def parse_user_config_hex(user_config_hex):
    '''parse user config hex'''
    number_of_pages_user_config = 1
    page_size = 4096
    block_size = 64
    # user config size = 1 * 4096 = 4096
    user_config_size = number_of_pages_user_config * page_size
    # convert user_config_hex to user_config_bytes
    user_config_bytes = bytes.fromhex(user_config_hex)
    print('user config size: {} bytes'.format(len(user_config_bytes)))
    if len(user_config_bytes) != user_config_size:
        print('wrong user config size: {0} bytes (expected {1} bytes)'\
                .format(len(user_config_bytes), user_config_size))
        return None
    # 0:8 Globals (8 blocks)
    globals_bytes = user_config_bytes[0:block_size * 8]
    globals_hex = globals_bytes.hex()
    parse_globals_hex(globals_hex)
    # 8:16 Label Sets (8 blocks)
    label_sets_bytes = user_config_bytes[block_size * 8:block_size * 16]
    label_sets_hex = label_sets_bytes.hex()
    parse_label_sets_hex(label_sets_hex)
    # 16:32 Protocol Map (16 blocks)
    protocol_map_bytes = user_config_bytes[block_size * 16:block_size * 32]
    protocol_map_hex = protocol_map_bytes.hex()
    parse_protocol_map_hex(protocol_map_hex)
    # 32:64 0xFF (32 blocks)
    print('==user config parsing complete==')


def parse_library_hex(library_hex):
    '''parse library hex'''
    number_of_pages_library = 17
    page_size = 4096
    # library size = 17 * 4096 = 69632
    library_size = number_of_pages_library * page_size
    # convert library_hex to library_bytes
    library_bytes = bytes.fromhex(library_hex)
    print('library size: {} bytes'.format(len(library_bytes)))
    print('==')
    if len(library_bytes) != library_size:
        print('wrong library size: {0} bytes (expected {1} bytes)'.format(len(library_bytes), library_size))
        return None
    # 1. Navigation (3-Page)
    navigation_bytes = library_bytes[0:page_size * 3]
    navigation_hex = navigation_bytes.hex()
    parse_navigation_hex(navigation_hex)
    # 2. Library Protocols (4-Page)
    protocols_bytes = library_bytes[page_size * 3:page_size * 7]
    protocols_hex = protocols_bytes.hex()
    parse_protocols_hex(protocols_hex)
    # 3. Constraint (4-Page)
    constraints_bytes = library_bytes[page_size * 7:page_size * 11]
    constraints_hex = constraints_bytes.hex()
    parse_constraints_hex(constraints_hex)
    # 4. View (4-Page)
    views_bytes = library_bytes[page_size * 11:page_size * 15]
    views_hex = views_bytes.hex()
    parse_views_hex(views_hex)
    # 5. Default Views (1-Page)
    default_views_bytes = library_bytes[page_size * 15:page_size * 16]
    default_views_hex = default_views_bytes.hex()
    parse_default_views_hex(default_views_hex)
    # 6. User Config (1-Page)
    user_config_bytes = library_bytes[page_size * 16:page_size * 17]
    user_config_hex = user_config_bytes.hex()
    parse_user_config_hex(user_config_hex)
    print('==library parsing complete==')


def encrypt_library(library_path):
    library = Library()
    library.load(library_path)
    library_bytes = library.get_library_bytes()
    #
    library_hex = library_bytes.hex()
    #
    # parse_library_hex(library_hex)
    #
    library_name = library.library['content']['name'].strip(' \t\r\n\0')
    library_version = str(library.library['version'])
    time_stamp = str(int(time.time() * 1000))
    hex_file_path = 'Library-[' + library_name + ']-[' + library_version + ']@' \
            +time_stamp + '.hex'
    # write hex file
    file = open(hex_file_path, "w")
    file.write(library_hex)
    file.close()
    print('library hex file is saved to: [{}]'.format(hex_file_path))
    # print('library_hex = \n{}'.format(library_hex))


view_map_continous = {
    'rate': 0,
    'vtbi': 1,
    'loadingDoseAmount': 2,
    'time': 3,
    'delayStart': 4,
    'kvo': 5,
    'delayKvoRate': 6,
    'concentration': 7,
    'weight': 10,
    'label': 11,
    'saveRx': 20,
    'drug': 22
}
view_map_bolus = {
    'basalRate': 0,
    'vtbi': 1,
    'loadingDoseAmount': 2,
    'time': 3,
    'delayStart': 4,
    'autoBolusAmount': 5,
    'bolusInterval': 6,
    'demandBolusAmount': 7,
    'lockoutTime': 8,
    'kvo': 9,
    'delayKvoRate': 10,
    'maxAmountPerHour': 11,
    'maxAmountPerInterval': 12,
    'clinicianDose': 13,
    'concentration': 14,
    'weight': 17,
    'label': 18,
    'saveRx': 20,
    'drug': 22
}
view_map_intermittent = {
    'doseRate': 0,
    'doseVtbi': 1,
    'loadingDoseAmount': 2,
    'totalTime': 3,
    'intervalTime': 4,
    'delayStart': 5,
    'intermittentKvoRate': 6,
    'kvoRate': 7,
    'delayKvoRate': 8,
    'maxAmountPerHour': 9,
    'maxAmountPerInterval': 10,
    'concentration': 11,
    'weight': 14,
    'label': 15,
    'saveRx': 20,
    'drug': 22
}


class Library:
    '''Library class'''

    def __init__(self):
        self.library = None
        self.protocols = None

    def load(self, library_path):
        '''load library'''
        # library_json = ""
        # read json file
        file = open(library_path, "r")
        library_json = file.read()
        file.close()
        # convert JSON to Python Dict
        self.library = json.loads(library_json)
        self.protocols = self.library['content']['extractedProtocols']

    def get_id(self):
        '''get id'''
        return self.library['id']

    def get_version(self):
        '''get version'''
        return self.library['version']

    def get_name(self):
        '''get name'''
        return self.library['content']['name']

    def get_library(self):
        '''get library'''
        return self.library

    def get_protocol(self, protocol_name):
        '''get protocol'''
        protocol = None
        for each_protocol in self.protocols:
            if each_protocol['content']['name'] == protocol_name or \
                            str(each_protocol['id']) == str(protocol_name):
                protocol = each_protocol
        return protocol

    def get_protocols(self):
        '''get protocols'''
        return self.protocols

    def get_library_crc(self):
        '''get library crc'''
        library_crc = self.library['crc']
        if self.library['crc'].find('MD5--') != -1:
            # the crc is MD5 (CRC hex in JSON is Big-endian)
            md5_ascii = self.library['crc'][5:]
            md5_hex = hexlify(md5_ascii.encode()).decode()
            library_crc = crc32c(0, md5_hex).to_bytes(4, 'big').hex()
            # library_crc = int(1).to_bytes(4, 'big').hex()
        return library_crc

    def get_library_id(self):
        '''get library id'''
        return self.library['id']
    
    def get_protocol_navi_path(self, protocol_id, node_children):
        '''Get protocol navi path'''
        protocol_navi_path = []
        current_layer_index = 0
        protocol_found = False
        # Use iterator to display contents of New Rx
        for each in node_children:
            if not protocol_found:
                navi_node = {'menu_position': 0,
                             'auth': []}
                for each_role in each['roles']:
                    auth_node = {}
                    auth_node['role'] = each_role
                    auth_node['pin'] = self.get_access_code(each_role)
                    navi_node['menu_position'] = current_layer_index
                    navi_node['auth'].append(auth_node)
                if each['type'] == 'protocol':
                    if each['data']['id'] == protocol_id:
                        protocol_navi_path.append(navi_node)
                        protocol_found = True
                elif (each['type'] == 'folder') and ('children' in each.keys()):
                    sub_node_children = each['children']
                    # DFS recursive algorithm
                    protocol_navi_path = self.get_protocol_navi_path(protocol_id, sub_node_children);
                    if protocol_navi_path != []:
                        protocol_navi_path.insert(0, navi_node)
                        protocol_found = True
                current_layer_index += 1
        if not protocol_found:
            protocol_navi_path = []
        return protocol_navi_path
        
    def get_protocol_view_index(self, protocol_name):
        '''get view index'''
        view_index = int(0xFF)
        if self.library['content']['views'] is not None:
            node_children = self.library['content']['node']['children']
            views = self.library['content']['views']
            view_id = find_view_id(protocol_name, node_children)
            if view_id is not None:
                view_index = find_view_index(view_id, views)
        return str(view_index)

    def get_protocol_label_set(self, protocol_name):
        '''get label set'''
        label_set = None
        if self.library['content']['labelSets'] is not None:
            node_children = self.library['content']['node']['children']
            label_sets = self.library['content']['labelSets']
            label_set_name = find_label_set_name(protocol_name, node_children)
            if label_set_name is not None:
                label_set = find_label_set(label_set_name, label_sets)
        return label_set
    
    def get_protocol_label_set_index(self, protocol_name):
        '''get label set index'''
        label_set_index = int(0xFF)
        if self.library['content']['labelSets'] is not None:
            node_children = self.library['content']['node']['children']
            label_sets = self.library['content']['labelSets']
            label_set_name = find_label_set_name(protocol_name, node_children)
            if label_set_name is not None:
                label_set_index = find_label_set_index(label_set_name, label_sets)
        return str(label_set_index)

    def get_roles_bytes(self, roles):
        '''get roles bytes'''
        roles_bytes = 0x0000
        default_roles = self.library['content']['defaultRoles']
        for each_role in roles:
            if each_role == 'anyone':
                roles_bytes = 0xFFFF
                break
            for each_default_role in default_roles:
                if each_role == each_default_role:
                    # get index of the role in the role list
                    roles_bytes |= (1 << (default_roles.index(each_default_role) - 1))
        return roles_bytes.to_bytes(2, 'little')
    
    def get_ref_bytes(self, node):
        '''get ref bytes
           If the node is a protocol node, 
           then return the position of the node in the [extracted protocol],
           otherwise, return 0x00
        '''
        extracted_protocols = self.library['content']['extractedProtocols']
        ref = 0
        if node['type'] == 'protocol':
            for each_protocol in extracted_protocols:
                if node['data']['id'] == each_protocol['id']:
                    ref = extracted_protocols.index(each_protocol)
        return ref.to_bytes(1, 'little')

    def get_navigation_nodes_bytes(self, index, standby_nodes):
        '''get navigation standby bytes'''
        navigation_nodes_bytes = bytearray(0)
        number_of_children = 0
        children_nodes = []
        for each_node in standby_nodes:
            node_bytes = bytearray(0)
            # 0:2 [Role] (2-byte Integer)
            roles = each_node['roles']
            role_bytes = self.get_roles_bytes(roles)
            #
            roles_hex = role_bytes.hex()
            print('roles_hex = {}'.format(roles_hex))
            # check to see if the key exists and the list is not empty
            if each_node.get('children') != None and each_node['children'] != []:
                number_of_children = len(each_node['children'])
                for each_child in each_node['children']:
                    children_nodes.append(each_child)
            else:
                number_of_children = 0
            # 2:12 [Children Index Array] (10-Byte Integer Array)
            children_index_array_bytes = get_children_index_array_bytes(index, number_of_children)
            # Update index
            index += number_of_children
            #
            children_index_array_hex = children_index_array_bytes.hex()
            print('children_index_array_hex = {}'.format(children_index_array_hex))
            # 12:13 [Number of Children] (1-Byte Integer)
            if each_node.get('children') != None and each_node['children'] != []:
                number_of_children = len(each_node['children'])
            else:
                number_of_children = 0
            number_of_children_bytes = number_of_children.to_bytes(1, 'little')
            #
            number_of_children_hex = number_of_children_bytes.hex()
            print('number_of_children_hex = {}'.format(number_of_children_hex))
            # 13:29 [Label] (16-Byte ASCII String)
            label_bytes = get_label_bytes(each_node)
            #
            label_hex = label_bytes.hex()
            print('label_hex = {}'.format(label_hex))
            # 29:45	[Content] (16-Byte String)
            content_bytes = get_content_bytes(each_node)
            #
            content_hex = content_bytes.hex()
            print('content_hex = {}'.format(content_hex))
            # 45:46	[Type] (1-Byte Integer)
            type_bytes = get_type_bytes(each_node)
            #
            type_hex = type_bytes.hex()
            print('type_hex = {}'.format(type_hex))
            # 46:47	[Ref] (1-Byte Integer)
            ref_bytes = self.get_ref_bytes(each_node)
            #
            ref_hex = ref_bytes.hex()
            print('ref_hex = {}'.format(ref_hex))
            # 47:48	[Visibility ] (1-Byte Integer)
            visibility_bytes = get_visibility_bytes(each_node)
            #
            visibility_hex = visibility_bytes.hex()
            print('visibility_hex = {}'.format(visibility_hex))
            #
            node_bytes += role_bytes
            node_bytes += children_index_array_bytes
            node_bytes += number_of_children_bytes
            node_bytes += label_bytes
            node_bytes += content_bytes
            node_bytes += type_bytes
            node_bytes += ref_bytes
            node_bytes += visibility_bytes
            # Append 0xFF - Infusion Nodes
            block_size = 64
            node_bytes = crc_fill(0, node_bytes, block_size)
            #
            node_hex = node_bytes.hex()
            print('node_hex = {}'.format(node_hex))
            # Updated navigation_nodes_bytes
            navigation_nodes_bytes += node_bytes
            #
            # navigation_nodes_hex = navigation_nodes_bytes.hex()
            # print('navigation_nodes_hex = {}'.format(navigation_nodes_hex))
        # Updated navigation_nodes_bytes for the current layer
        if len(children_nodes) != 0:
            navigation_nodes_bytes += self.get_navigation_nodes_bytes(index, children_nodes)
        return navigation_nodes_bytes

    def get_navigation_bytes(self):
        '''get navigation bytes'''
        block_size = 64
        initial_node_index = 0
        #
        # 0:100 Standby Nodes (100 blocks)
        standby_root = []
        # a single navigation standby node is 64 bytes
        standby_root.append(self.library['content']['defaultNavigationTree'][0])
        # move folders and infusion nodes under [New Rx]
        standby_root[0]['children'][2]['children'] = self.library['content']['node']['children']
        # BFS recursive algorithm
        standby_nodes_bytes = self.get_navigation_nodes_bytes(initial_node_index, standby_root)
        # non-empty nodes of standby_nodes
        standby_nodes_count = int(len(standby_nodes_bytes) / block_size)
        # append 0xFF - Standby Nodes
        number_of_blocks_standby_nodes = 100
        # standby nodes size = 100 * 64 = 6400
        standby_nodes_size = number_of_blocks_standby_nodes * block_size
        while len(standby_nodes_bytes) < standby_nodes_size:
            standby_nodes_bytes += int(0xFF).to_bytes(1, 'little')
        #
        standby_nodes_hex = standby_nodes_bytes.hex()
        print('len(standby_nodes_bytes) = {}'.format(len(standby_nodes_bytes)))
        print('standby_nodes_hex = \n{}'.format(standby_nodes_hex))
        #
        # 100:130 Config Nodes (30 blocks)
        config_root = []
        # a single navigation config node is 64 bytes
        config_root.append(self.library['content']['defaultNavigationTree'][1])
        config_nodes_bytes = self.get_navigation_nodes_bytes(initial_node_index, config_root)
        # non-empty nodes of config_nodes
        config_nodes_count = int(len(config_nodes_bytes) / block_size)
        # Append 0xFF - Config Nodes
        number_of_blocks_config_nodes = 30
        # config nodes size = 30 * 64 = 1920
        config_nodes_size = number_of_blocks_config_nodes * block_size
        while len(config_nodes_bytes) < config_nodes_size:
            config_nodes_bytes += int(0xFF).to_bytes(1, 'little')
        #
        config_nodes_hex = config_nodes_bytes.hex()
        print('len(config_nodes_bytes) = {}'.format(len(config_nodes_bytes)))
        print('config_nodes_hex = \n{}'.format(config_nodes_hex))
        #
        # 130:191 Infusion Nodes (61 blocks)
        infusion_root = []
        # a single navigation config node is 64 bytes
        infusion_root.append(self.library['content']['defaultNavigationTree'][2])
        infusion_nodes_bytes = self.get_navigation_nodes_bytes(initial_node_index, infusion_root)
        # non-empty nodes of infusion_nodes
        infusion_nodes_count = int(len(infusion_nodes_bytes) / block_size)
        # Append 0xFF - Infusion Nodes
        number_of_blocks_infusion_nodes = 61
        # infusion nodes size = 61 * 64 = 3904
        infusion_nodes_size = number_of_blocks_infusion_nodes * block_size
        while len(infusion_nodes_bytes) < infusion_nodes_size:
            infusion_nodes_bytes += int(0xFF).to_bytes(1, 'little')
        #
        infusion_nodes_hex = infusion_nodes_bytes.hex()
        print('len(infusion_nodes_bytes) = {}'.format(len(infusion_nodes_bytes)))
        print('infusion_nodes_hex = \n{}'.format(infusion_nodes_hex))
        #
        # 191:192 Meta Data (1 blocks)
        meta_data_bytes = bytearray(0)
        #
        # Standby Nodes Count
        standby_nodes_count_bytes = int(standby_nodes_count).to_bytes(1, 'little')
        # Append 0xFF - Standby Nodes Count
        # standby_nodes_count_size = 8
        standby_nodes_count_bytes = crc_fill(0, standby_nodes_count_bytes, 8)
        #
        # Config Nodes Count
        config_nodes_count_bytes = int(config_nodes_count).to_bytes(1, 'little')
        # Append 0xFF - Config Nodes Count
        # config_nodes_count_size = 8
        config_nodes_count_bytes = crc_fill(0, config_nodes_count_bytes, 8)
        #
        # Infusion Nodes Count
        infusion_nodes_count_bytes = int(infusion_nodes_count).to_bytes(1, 'little')
        # Append 0xFF - Infusion Nodes Count
        # infusion_nodes_count_size = 8
        infusion_nodes_count_bytes = crc_fill(0, infusion_nodes_count_bytes, 8)
        #
        meta_data_bytes += standby_nodes_count_bytes
        meta_data_bytes += config_nodes_count_bytes
        meta_data_bytes += infusion_nodes_count_bytes
        #
        # Append 0xFF - Meta Data
        number_of_blocks_meta_data = 1
        # meta data size = 1 * 64 = 64
        meta_data_size = number_of_blocks_meta_data * block_size
        while len(meta_data_bytes) < meta_data_size:
            meta_data_bytes += int(0xFF).to_bytes(1, 'little')
        #
        meta_data_hex = meta_data_bytes.hex()
        print('len(meta_data_bytes) = {}'.format(len(meta_data_bytes)))
        print('meta_data_hex = \n{}'.format(meta_data_hex))
        #
        navigation_bytes = bytearray(0)
        navigation_bytes += standby_nodes_bytes
        navigation_bytes += config_nodes_bytes
        navigation_bytes += infusion_nodes_bytes
        navigation_bytes += meta_data_bytes
        #
        # Append 0xFF - Total
        # number_of_blocks_total = 192
        number_of_pages_navigation = 3
        page_size = 4096
        # navigation size = 3 * 4096 = 12288
        navigation_size = number_of_pages_navigation * page_size
        while len(navigation_bytes) < navigation_size:
            navigation_bytes += int(0xFF).to_bytes(1, 'little')
        return navigation_bytes
        
    def get_library_protocols_bytes(self):
        '''get library protocols bytes'''
        library_protocols_bytes = bytearray(0)
        library_protocols = self.library['content']['extractedProtocols']
        for each_protocol in library_protocols:
            # 0:80 Protocol 80-byte 
            protocol_bytes = get_protocol_bytes(each_protocol)
            # 80:84 Switch 4-byte   
            switches_bytes = get_switches_bytes(each_protocol)
            # 84:88 Protocol CRC 4-byte
            protocol_crc_bytes = get_protocol_crc_bytes(each_protocol)
            # 88:90 Auth Role 2-byte
            auth_role_bytes = int(0xFFFF).to_bytes(2, 'little')
            # 90:92 Rate Factor 2-byte
            rate_factor_bytes = get_rate_factor_bytes(each_protocol)
            # 92:93 Concentration Modifiable 1-byte 
            if each_protocol['content']['drug'] != None and \
                    not each_protocol['content']['drug']['content']['concentrationImmutable']:
                concentration_modifiable_bytes = int(1).to_bytes(1, 'little')
            else:
                concentration_modifiable_bytes = int(0).to_bytes(1, 'little')
            # 93:94 Infusion Mode 1-byte
            infusion_mode_bytes = get_infusion_mode_bytes(each_protocol)
            # 94:95 ID 1-byte
            id_bytes = int(0xFF).to_bytes(1, 'little')
            # 95:96 Label Pool ID 1-byte
            label_pool_id_bytes = int(0xFF).to_bytes(1, 'little')
            # 96:97 Label ID 1-byte
            label_id_bytes = int(0).to_bytes(1, 'little')
            # 97:98 Rate Unit 1-byte
            rate_unit_bytes = get_rate_unit_bytes(each_protocol)
            # 98:99 Concentration Unit 1-byte
            concentration_unit_bytes = get_concentration_unit_bytes(each_protocol)
            # 99:109 Name 10-byte
            name_bytes = get_name_bytes(each_protocol)
            # 109:119 Drug Name 10-byte
            drug_name_bytes = get_drug_name_bytes(each_protocol)
            # 119:224 Drug Components 105-byte
            drug_components_bytes = get_drug_components_bytes(each_protocol)

            each_protocol_bytes = bytearray(0)        
            each_protocol_bytes += protocol_bytes
            each_protocol_bytes += switches_bytes 
            each_protocol_bytes += protocol_crc_bytes
            each_protocol_bytes += auth_role_bytes
            each_protocol_bytes += rate_factor_bytes
            each_protocol_bytes += concentration_modifiable_bytes
            each_protocol_bytes += infusion_mode_bytes
            each_protocol_bytes += id_bytes
            each_protocol_bytes += label_pool_id_bytes
            each_protocol_bytes += label_id_bytes
            each_protocol_bytes += rate_unit_bytes
            each_protocol_bytes += concentration_unit_bytes
            each_protocol_bytes += name_bytes
            each_protocol_bytes += drug_name_bytes
            each_protocol_bytes += drug_components_bytes
            # Append 0xFF and CRC
            each_protocol_size = 256
            each_protocol_bytes = crc_fill(0, each_protocol_bytes, each_protocol_size)
            #
            each_protocol_hex = each_protocol_bytes.hex()
            print('len({0}) = {1}'.format(each_protocol['content']['name'], len(each_protocol_bytes)))
            print(each_protocol_hex)
            #
            library_protocols_bytes += each_protocol_bytes
        # Append 0xFF
        number_of_pages_library_protocols = 4
        page_size = 4096
        # library protocols size = 4 * 4096 = 16384
        library_protocols_size = number_of_pages_library_protocols * page_size
        library_protocols_bytes = byte_fill(library_protocols_bytes, library_protocols_size)
        #
        print('len(library_protocols_bytes) = {}'.format(len(library_protocols_bytes)))
        library_protocols_hex = library_protocols_bytes.hex()
        print('library_protocols_hex = \n{}'.format(library_protocols_hex))
        return library_protocols_bytes

    def get_library_constraints_bytes(self):
        '''get constraint bytes'''
        library_constraints_bytes = bytearray(0)
        # each_constraints_size = 256
        library_protocols = self.library['content']['extractedProtocols']
        for each_protocol in library_protocols:
            infusion_mode = each_protocol['content']['deliveryMode']
            switches = each_protocol['content']['program']['switches']
            guards = each_protocol['content']['program']['guards']
            if infusion_mode == 'continuousInfusion':
                # 0:4 [rate_min] (4-byte Float)
                rate_min = float(0)
                if guards.get('rate') != None and guards['rate'][0]['min'] != None:
                    rate_min = float(guards['rate'][0]['min'])
                else:
                    rate_min = float(0)
                rate_min_bytes = bytearray(struct.pack("f", rate_min))
                # 4:8 [rate_max] (4-byte Float)
                rate_max = float(0)
                if guards.get('rate') != None and guards['rate'][0]['max'] != None:
                    rate_max = float(guards['rate'][0]['max'])
                else:
                    rate_max = float(0)
                rate_max_bytes = bytearray(struct.pack("f", rate_max))
                # 8:12 [vtbi_min] (4-byte Float)
                vtbi_min = float(0)
                if guards.get('vtbi') != None and guards['vtbi'][0]['min'] != None:
                    vtbi_min = float(guards['vtbi'][0]['min'])
                else:
                    vtbi_min = float(0)
                vtbi_min_bytes = bytearray(struct.pack("f", vtbi_min))
                # 12:16 [vtbi_max] (4-byte Float)
                vtbi_max = float(0)
                if guards.get('vtbi') != None and guards['vtbi'][0]['max'] != None:
                    vtbi_max = float(guards['vtbi'][0]['max'])
                else:
                    vtbi_max = float(0)
                vtbi_max_bytes = bytearray(struct.pack("f", vtbi_max))
                # 16:20 [loading_dose_min] (4-byte Float)
                loading_dose_min = float(0)
                if guards.get('loadingDoseAmount') != None and \
                        guards['loadingDoseAmount'][0]['min'] != None:
                    loading_dose_min = float(guards['loadingDoseAmount'][0]['min'])
                else:
                    loading_dose_min = float(0)
                loading_dose_min_bytes = bytearray(struct.pack("f", loading_dose_min))
                # 20:24 [loading_dose_max] (4-byte Float)
                loading_dose_max = float(0)
                if guards.get('loadingDoseAmount') != None and \
                        guards['loadingDoseAmount'][0]['max'] != None:
                    loading_dose_max = float(guards['loadingDoseAmount'][0]['max'])
                else:
                    loading_dose_max = float(0)
                loading_dose_max_bytes = bytearray(struct.pack("f", loading_dose_max))
                # 24:28 [time_min] (4-byte Integer)
                time_min = int(0)
                if guards.get('time') != None and guards['time'][0]['min'] != None:
                    time_min = int(guards['time'][0]['min']) * 60
                else:
                    time_min = int(0)
                time_min_bytes = time_min.to_bytes(4, 'little')
                # 28:32 [time_max] (4-byte Integer)
                time_max = int(0)
                if guards.get('time') != None and guards['time'][0]['max'] != None:
                    time_max = int(guards['time'][0]['max']) * 60
                else:
                    time_max = int(0)
                time_max_bytes = time_max.to_bytes(4, 'little')
                # 32:36 [delay_start_min] (4-byte Integer)
                delay_start_min = int(0)
                if guards.get('delayStart') != None and guards['delayStart'][0]['min'] != None:
                    delay_start_min = int(guards['delayStart'][0]['min']) * 60
                else:
                    delay_start_min = int(0)
                delay_start_min_bytes = delay_start_min.to_bytes(4, 'little')
                # 36:40 [delay_start_max] (4-byte Integer)
                delay_start_max = int(0)
                if guards.get('delayStart') != None and guards['delayStart'][0]['max'] != None:
                    delay_start_max = int(guards['delayStart'][0]['max']) * 60
                else:
                    delay_start_max = int(0)
                delay_start_max_bytes = delay_start_max.to_bytes(4, 'little')
                # 40:44 [kvo_rate_min] (4-byte Float)
                kvo_rate_min = float(0)
                if guards.get('kvoRate') != None and \
                        guards['kvoRate'][0]['min'] != None:
                    kvo_rate_min = float(guards['kvoRate'][0]['min'])
                else:
                    kvo_rate_min = float(0)
                kvo_rate_min_bytes = bytearray(struct.pack("f", kvo_rate_min))
                # 44:48 [kvo_rate_max] (4-byte Float)
                kvo_rate_max = float(0)
                if guards.get('kvoRate') != None and \
                        guards['kvoRate'][0]['max'] != None:
                    kvo_rate_max = float(guards['kvoRate'][0]['max'])
                else:
                    kvo_rate_max = float(0)
                kvo_rate_max_bytes = bytearray(struct.pack("f", kvo_rate_max))
                # 48:52 [delay_kvo_rate_min] (4-byte Float)
                delay_kvo_rate_min = float(0)
                if guards.get('delayKvoRate') != None and \
                        guards['delayKvoRate'][0]['min'] != None:
                    delay_kvo_rate_min = float(guards['delayKvoRate'][0]['min'])
                else:
                    delay_kvo_rate_min = float(0)
                delay_kvo_rate_min_bytes = bytearray(struct.pack("f", delay_kvo_rate_min))
                # 52:56 [delay_kvo_rate_max] (4-byte Float)
                delay_kvo_rate_max = float(0)
                if guards.get('delayKvoRate') != None and \
                        guards['delayKvoRate'][0]['max'] != None:
                    delay_kvo_rate_max = float(guards['delayKvoRate'][0]['max'])
                else:
                    delay_kvo_rate_max = float(0)
                delay_kvo_rate_max_bytes = bytearray(struct.pack("f", delay_kvo_rate_max))
                # 56:60 [concentration_min] (4-byte Float)
                concentration_min = float(0)
                if guards.get('concentration') != None and \
                        guards['concentration'][0]['min'] != None:
                    concentration_min = float(guards['concentration'][0]['min'])
                else:
                    concentration_min = float(0)
                concentration_min_bytes = bytearray(struct.pack("f", concentration_min))
                # 60:64 [concentration_max] (4-byte Float)
                concentration_max = float(0)
                if guards.get('concentration') != None and \
                        guards['concentration'][0]['max'] != None:
                    concentration_max = float(guards['concentration'][0]['max'])
                else:
                    concentration_max = float(0)
                concentration_max_bytes = bytearray(struct.pack("f", concentration_max))
                # 64:68 [drug_amount_min] (4-byte Float)
                drug_amount_min = float(0)
                if guards.get('drugAmount') != None and \
                        guards['drugAmount'][0]['min'] != None:
                    drug_amount_min = float(guards['drugAmount'][0]['min'])
                else:
                    drug_amount_min = float(0)
                drug_amount_min_bytes = bytearray(struct.pack("f", drug_amount_min))
                # 68:72 [drug_amount_max] (4-byte Float)
                drug_amount_max = float(0)
                if guards.get('drugAmount') != None and \
                        guards['drugAmount'][0]['max'] != None:
                    drug_amount_max = float(guards['drugAmount'][0]['max'])
                else:
                    drug_amount_max = float(99.9)
                drug_amount_max_bytes = bytearray(struct.pack("f", drug_amount_max))
                # 72:76 [solvent_volume_min] (4-byte Float)
                solvent_volume_min = float(0)
                if guards.get('diluteVolume') != None and \
                        guards['diluteVolume'][0]['min'] != None:
                    solvent_volume_min = float(guards['diluteVolume'][0]['min'])
                else:
                    solvent_volume_min = float(1)
                solvent_volume_min_bytes = bytearray(struct.pack("f", solvent_volume_min))
                # 76:80 [solvent_volume_max] (4-byte Float)
                solvent_volume_max = float(0)
                if guards.get('diluteVolume') != None and \
                        guards['diluteVolume'][0]['max'] != None:
                    solvent_volume_max = float(guards['diluteVolume'][0]['max'])
                else:
                    solvent_volume_max = float(999)
                solvent_volume_max_bytes = bytearray(struct.pack("f", solvent_volume_max))
                # 80:84 [weight_min] (4-byte Float)
                weight_min = float(0)
                if guards.get('weight') != None and \
                        guards['weight'][0]['min'] != None:
                    weight_min = float(guards['weight'][0]['min'])
                else:
                    weight_min = float(1)
                weight_min_bytes = bytearray(struct.pack("f", weight_min))
                # 84:88 [weight_max] (4-byte Float)
                weight_max = float(0)
                if guards.get('weight') != None and \
                        guards['weight'][0]['max'] != None:
                    weight_max = float(guards['weight'][0]['max'])
                else:
                    weight_max = float(999.9)
                weight_max_bytes = bytearray(struct.pack("f", weight_max))
                #
                each_guards_bytes = bytearray(0)
                each_guards_bytes += rate_min_bytes
                each_guards_bytes += rate_max_bytes
                each_guards_bytes += vtbi_min_bytes
                each_guards_bytes += vtbi_max_bytes
                each_guards_bytes += loading_dose_min_bytes
                each_guards_bytes += loading_dose_max_bytes
                each_guards_bytes += time_min_bytes
                each_guards_bytes += time_max_bytes
                each_guards_bytes += delay_start_min_bytes
                each_guards_bytes += delay_start_max_bytes
                each_guards_bytes += kvo_rate_min_bytes
                each_guards_bytes += kvo_rate_max_bytes
                each_guards_bytes += delay_kvo_rate_min_bytes
                each_guards_bytes += delay_kvo_rate_max_bytes
                each_guards_bytes += concentration_min_bytes
                each_guards_bytes += concentration_max_bytes
                each_guards_bytes += drug_amount_min_bytes
                each_guards_bytes += drug_amount_max_bytes
                each_guards_bytes += solvent_volume_min_bytes
                each_guards_bytes += solvent_volume_max_bytes
                each_guards_bytes += weight_min_bytes
                each_guards_bytes += weight_max_bytes
                # Append 0xFF and CRC
                each_guards_size = 256
                each_guards_bytes = crc_fill(0, each_guards_bytes, each_guards_size)
                each_guards_hex = each_guards_bytes.hex()
                print('guards_length({0}) = {1}'.format(each_protocol['content']['name'], len(each_guards_bytes)))
                print(each_guards_hex)
                #
                library_constraints_bytes += each_guards_bytes
            if infusion_mode == 'bolusInfusion':
                # 0:4 [basal_rate_min] (4-byte Float)
                basal_rate_min = float(0)
                if guards.get('basalRate') != None and guards['basalRate'][0]['min'] != None:
                    basal_rate_min = float(guards['basalRate'][0]['min'])
                else:
                    basal_rate_min = float(0)
                basal_rate_min_bytes = bytearray(struct.pack("f", basal_rate_min))
                # 4:8 [basal_rate_max] (4-byte Float)
                basal_rate_max = float(0)
                if guards.get('basalRate') != None and guards['basalRate'][0]['max'] != None:
                    basal_rate_max = float(guards['basalRate'][0]['max'])
                else:
                    basal_rate_max = float(0)
                basal_rate_max_bytes = bytearray(struct.pack("f", basal_rate_max))
                # 8:12 [vtbi_min] (4-byte Float)
                vtbi_min = float(0)
                if guards.get('vtbi') != None and guards['vtbi'][0]['min'] != None:
                    vtbi_min = float(guards['vtbi'][0]['min'])
                else:
                    vtbi_min = float(0)
                vtbi_min_bytes = bytearray(struct.pack("f", vtbi_min))
                # 12:16 [vtbi_max] (4-byte Float)
                vtbi_max = float(0)
                if guards.get('vtbi') != None and guards['vtbi'][0]['max'] != None:
                    vtbi_max = float(guards['vtbi'][0]['max'])
                else:
                    vtbi_max = float(0)
                vtbi_max_bytes = bytearray(struct.pack("f", vtbi_max))
                # 16:20 [loading_dose_min] (4-byte Float)
                loading_dose_min = float(0)
                if guards.get('loadingDoseAmount') != None and \
                        guards['loadingDoseAmount'][0]['min'] != None:
                    loading_dose_min = float(guards['loadingDoseAmount'][0]['min'])
                else:
                    loading_dose_min = float(0)
                loading_dose_min_bytes = bytearray(struct.pack("f", loading_dose_min))
                # 20:24 [loading_dose_max] (4-byte Float)
                loading_dose_max = float(0)
                if guards.get('loadingDoseAmount') != None and \
                        guards['loadingDoseAmount'][0]['max'] != None:
                    loading_dose_max = float(guards['loadingDoseAmount'][0]['max'])
                else:
                    loading_dose_max = float(0)
                loading_dose_max_bytes = bytearray(struct.pack("f", loading_dose_max))
                # 24:28 [time_min] (4-byte Integer)
                time_min = int(0)
                if guards.get('time') != None and guards['time'][0]['min'] != None:
                    time_min = int(guards['time'][0]['min']) * 60
                else:
                    time_min = int(0)
                time_min_bytes = time_min.to_bytes(4, 'little')
                # 28:32 [time_max] (4-byte Integer)
                time_max = int(0)
                if guards.get('time') != None and guards['time'][0]['max'] != None:
                    time_max = int(guards['time'][0]['max']) * 60
                else:
                    time_max = int(0)
                time_max_bytes = time_max.to_bytes(4, 'little')
                # 32:36 [delay_start_min] (4-byte Integer)
                delay_start_min = int(0)
                if guards.get('delayStart') != None and guards['delayStart'][0]['min'] != None:
                    delay_start_min = int(guards['delayStart'][0]['min']) * 60
                else:
                    delay_start_min = int(0)
                delay_start_min_bytes = delay_start_min.to_bytes(4, 'little')
                # 36:40 [delay_start_max] (4-byte Integer)
                delay_start_max = int(0)
                if guards.get('delayStart') != None and guards['delayStart'][0]['max'] != None:
                    delay_start_max = int(guards['delayStart'][0]['max']) * 60
                else:
                    delay_start_max = int(0)
                delay_start_max_bytes = delay_start_max.to_bytes(4, 'little')
                # 40:44 [auto_bolus_amount_min] (4-byte Float)
                auto_bolus_amount_min = float(0)
                if guards.get('autoBolusAmount') != None and \
                        guards['autoBolusAmount'][0]['min'] != None:
                    auto_bolus_amount_min = float(guards['autoBolusAmount'][0]['min'])
                else:
                    auto_bolus_amount_min = float(0)
                auto_bolus_amount_min_bytes = bytearray(struct.pack("f", auto_bolus_amount_min))
                # 44:48 [auto_bolus_amount_max] (4-byte Float)
                auto_bolus_amount_max = float(0)
                if guards.get('autoBolusAmount') != None and \
                        guards['autoBolusAmount'][0]['max'] != None:
                    auto_bolus_amount_max = float(guards['autoBolusAmount'][0]['max'])
                else:
                    auto_bolus_amount_max = float(0)
                auto_bolus_amount_max_bytes = bytearray(struct.pack("f", auto_bolus_amount_max))
                # 48:52 [bolus_interval_min] (4-byte Integer)
                bolus_interval_min = int(0)
                if guards.get('bolusInterval') != None and guards['bolusInterval'][0]['min'] != None:
                    bolus_interval_min = int(guards['bolusInterval'][0]['min']) * 60
                else:
                    bolus_interval_min = int(0)
                bolus_interval_min_bytes = bolus_interval_min.to_bytes(4, 'little')
                # 52:56 [bolus_interval_max] (4-byte Integer)
                bolus_interval_max = int(0)
                if guards.get('bolusInterval') != None and guards['bolusInterval'][0]['max'] != None:
                    bolus_interval_max = int(guards['bolusInterval'][0]['max']) * 60
                else:
                    bolus_interval_max = int(0)
                bolus_interval_max_bytes = bolus_interval_max.to_bytes(4, 'little')
                # 56:60 [demand_bolus_amount_min] (4-byte Float)
                demand_bolus_amount_min = float(0)
                if guards.get('demandBolusAmount') != None and \
                        guards['demandBolusAmount'][0]['min'] != None:
                    demand_bolus_amount_min = float(guards['demandBolusAmount'][0]['min'])
                else:
                    demand_bolus_amount_min = float(0)
                demand_bolus_amount_min_bytes = bytearray(struct.pack("f", demand_bolus_amount_min))
                # 60:64 [demand_bolus_amount_max] (4-byte Float)
                demand_bolus_amount_max = float(0)
                if guards.get('demandBolusAmount') != None and \
                        guards['demandBolusAmount'][0]['max'] != None:
                    demand_bolus_amount_max = float(guards['demandBolusAmount'][0]['max'])
                else:
                    demand_bolus_amount_max = float(0)
                demand_bolus_amount_max_bytes = bytearray(struct.pack("f", demand_bolus_amount_max))
                # 64:68 [lockout_time_min] (4-byte Integer)
                lockout_time_min = int(0)
                if guards.get('lockoutTime') != None and guards['lockoutTime'][0]['min'] != None:
                    lockout_time_min = int(guards['lockoutTime'][0]['min']) * 60
                else:
                    lockout_time_min = int(0)
                lockout_time_min_bytes = lockout_time_min.to_bytes(4, 'little')
                # 68:72 [lockout_time_max] (4-byte Integer)
                lockout_time_max = int(0)
                if guards.get('lockoutTime') != None and guards['lockoutTime'][0]['max'] != None:
                    lockout_time_max = int(guards['lockoutTime'][0]['max']) * 60
                else:
                    lockout_time_max = int(0)
                lockout_time_max_bytes = lockout_time_max.to_bytes(4, 'little')
                # 72:76 [kvo_rate_min] (4-byte Float)
                kvo_rate_min = float(0)
                if guards.get('kvoRate') != None and \
                        guards['kvoRate'][0]['min'] != None:
                    kvo_rate_min = float(guards['kvoRate'][0]['min'])
                else:
                    kvo_rate_min = float(0)
                kvo_rate_min_bytes = bytearray(struct.pack("f", kvo_rate_min))
                # 76:80 [kvo_rate_max] (4-byte Float)
                kvo_rate_max = float(0)
                if guards.get('kvoRate') != None and \
                        guards['kvoRate'][0]['max'] != None:
                    kvo_rate_max = float(guards['kvoRate'][0]['max'])
                else:
                    kvo_rate_max = float(0)
                kvo_rate_max_bytes = bytearray(struct.pack("f", kvo_rate_max))
                # 80:84 [delay_kvo_rate_min] (4-byte Float)
                delay_kvo_rate_min = float(0)
                if guards.get('delayKvoRate') != None and \
                        guards['delayKvoRate'][0]['min'] != None:
                    delay_kvo_rate_min = float(guards['delayKvoRate'][0]['min'])
                else:
                    delay_kvo_rate_min = float(0)
                delay_kvo_rate_min_bytes = bytearray(struct.pack("f", delay_kvo_rate_min))
                # 84:88 [delay_kvo_rate_max] (4-byte Float)
                delay_kvo_rate_max = float(0)
                if guards.get('delayKvoRate') != None and \
                        guards['delayKvoRate'][0]['max'] != None:
                    delay_kvo_rate_max = float(guards['delayKvoRate'][0]['max'])
                else:
                    delay_kvo_rate_max = float(0)
                delay_kvo_rate_max_bytes = bytearray(struct.pack("f", delay_kvo_rate_max))
                # 88:92 [max_per_hour_min] (4-byte Float)
                max_per_hour_min = float(0)
                if guards.get('maxAmountPerHour') != None and \
                        guards['maxAmountPerHour'][0]['min'] != None:
                    max_per_hour_min = float(guards['maxAmountPerHour'][0]['min'])
                else:
                    max_per_hour_min = float(0)
                max_per_hour_min_bytes = bytearray(struct.pack("f", max_per_hour_min))
                # 92:96 [max_per_hour_max] (4-byte Float)
                max_per_hour_max = float(0)
                if guards.get('maxAmountPerHour') != None and \
                        guards['maxAmountPerHour'][0]['max'] != None:
                    max_per_hour_max = float(guards['maxAmountPerHour'][0]['max'])
                else:
                    max_per_hour_max = float(0)
                max_per_hour_max_bytes = bytearray(struct.pack("f", max_per_hour_max))
                # 96:100 [max_per_interval_min] (4-byte Float)
                max_per_interval_min = float(0)
                if guards.get('maxAmountPerInterval') != None and \
                        guards['maxAmountPerInterval'][0]['min'] != None:
                    max_per_interval_min = float(guards['maxAmountPerInterval'][0]['min'])
                else:
                    max_per_interval_min = float(0)
                max_per_interval_min_bytes = bytearray(struct.pack("f", max_per_interval_min))
                # 100:104 [max_per_interval_max] (4-byte Float)
                max_per_interval_max = float(0)
                if guards.get('maxAmountPerInterval') != None and \
                        guards['maxAmountPerInterval'][0]['max'] != None:
                    max_per_interval_max = float(guards['maxAmountPerInterval'][0]['max'])
                else:
                    max_per_interval_max = float(0)
                max_per_interval_max_bytes = bytearray(struct.pack("f", max_per_interval_max))
                # 104:108 [clinician_dose_min] (4-byte Float)
                clinician_dose_min = float(0)
                if guards.get('clinicianDose') != None and \
                        guards['clinicianDose'][0]['min'] != None:
                    clinician_dose_min = float(guards['clinicianDose'][0]['min'])
                else:
                    clinician_dose_min = float(0)
                clinician_dose_min_bytes = bytearray(struct.pack("f", clinician_dose_min))
                # 108:112 [clinician_dose_max] (4-byte Float)
                clinician_dose_max = float(0)
                if guards.get('clinicianDose') != None and \
                        guards['clinicianDose'][0]['max'] != None:
                    clinician_dose_max = float(guards['clinicianDose'][0]['max'])
                else:
                    clinician_dose_max = float(0)
                clinician_dose_max_bytes = bytearray(struct.pack("f", clinician_dose_max))
                # 112:116 [concentration_min] (4-byte Float)
                concentration_min = float(0)
                if guards.get('concentration') != None and \
                        guards['concentration'][0]['min'] != None:
                    concentration_min = float(guards['concentration'][0]['min'])
                else:
                    concentration_min = float(0)
                concentration_min_bytes = bytearray(struct.pack("f", concentration_min))
                # 116:120 [concentration_max] (4-byte Float)
                concentration_max = float(0)
                if guards.get('concentration') != None and \
                        guards['concentration'][0]['max'] != None:
                    concentration_max = float(guards['concentration'][0]['max'])
                else:
                    concentration_max = float(0)
                concentration_max_bytes = bytearray(struct.pack("f", concentration_max))
                # 120:124 [drug_amount_min] (4-byte Float)
                drug_amount_min = float(0)
                if guards.get('drugAmount') != None and \
                        guards['drugAmount'][0]['min'] != None:
                    drug_amount_min = float(guards['drugAmount'][0]['min'])
                else:
                    drug_amount_min = float(0)
                drug_amount_min_bytes = bytearray(struct.pack("f", drug_amount_min))
                # 124:128 [drug_amount_max] (4-byte Float)
                drug_amount_max = float(0)
                if guards.get('drugAmount') != None and \
                        guards['drugAmount'][0]['max'] != None:
                    drug_amount_max = float(guards['drugAmount'][0]['max'])
                else:
                    drug_amount_max = float(99.9)
                drug_amount_max_bytes = bytearray(struct.pack("f", drug_amount_max))
                # 128:132 [solvent_volume_min] (4-byte Float)
                solvent_volume_min = float(0)
                if guards.get('diluteVolume') != None and \
                        guards['diluteVolume'][0]['min'] != None:
                    solvent_volume_min = float(guards['diluteVolume'][0]['min'])
                else:
                    solvent_volume_min = float(1)
                solvent_volume_min_bytes = bytearray(struct.pack("f", solvent_volume_min))
                # 132:136 [solvent_volume_max] (4-byte Float)
                solvent_volume_max = float(0)
                if guards.get('diluteVolume') != None and \
                        guards['diluteVolume'][0]['max'] != None:
                    solvent_volume_max = float(guards['diluteVolume'][0]['max'])
                else:
                    solvent_volume_max = float(999)
                solvent_volume_max_bytes = bytearray(struct.pack("f", solvent_volume_max))
                # 136:140 [weight_min] (4-byte Float)
                weight_min = float(0)
                if guards.get('weight') != None and \
                        guards['weight'][0]['min'] != None:
                    weight_min = float(guards['weight'][0]['min'])
                else:
                    weight_min = float(1)
                weight_min_bytes = bytearray(struct.pack("f", weight_min))
                # 140:144 [weight_max] (4-byte Float)
                weight_max = float(0)
                if guards.get('weight') != None and \
                        guards['weight'][0]['max'] != None:
                    weight_max = float(guards['weight'][0]['max'])
                else:
                    weight_max = float(999.9)
                weight_max_bytes = bytearray(struct.pack("f", weight_max))
                # 144:148 [patient_basal_rate_min] (4-byte Float)
                patient_basal_rate_min = float(0)
                if guards.get('basalRate') != None and len(guards['basalRate']) == 2 \
                        and guards['basalRate'][1]['min'] != None:
                    patient_basal_rate_min = float(guards['basalRate'][1]['min'])
                else:
                    patient_basal_rate_min = float(0)
                patient_basal_rate_min_bytes = bytearray(struct.pack("f", patient_basal_rate_min))
                # 148:152 [patient_basal_rate_max] (4-byte Float)
                patient_basal_rate_max = float(0)
                if guards.get('basalRate') != None and len(guards['basalRate']) == 2 \
                        and guards['basalRate'][1]['max'] != None:
                    patient_basal_rate_max = float(guards['basalRate'][1]['max'])
                else:
                    patient_basal_rate_max = float(0)
                patient_basal_rate_max_bytes = bytearray(struct.pack("f", patient_basal_rate_max))
                # 152:156 [patient_ab_volume_min] (4-byte Float)
                patient_ab_volume_min = float(0)
                if guards.get('autoBolusAmount') != None and len(guards['autoBolusAmount']) == 2 \
                        and guards['autoBolusAmount'][1]['min'] != None:
                    patient_ab_volume_min = float(guards['autoBolusAmount'][1]['min'])
                else:
                    patient_ab_volume_min = float(0)
                patient_ab_volume_min_bytes = bytearray(struct.pack("f", patient_ab_volume_min))
                # 156:160 [patient_ab_volume_max] (4-byte Float)
                patient_ab_volume_max = float(0)
                if guards.get('autoBolusAmount') != None and len(guards['autoBolusAmount']) == 2 \
                        and guards['autoBolusAmount'][1]['max'] != None:
                    patient_ab_volume_max = float(guards['autoBolusAmount'][1]['max'])
                else:
                    patient_ab_volume_max = float(0)
                patient_ab_volume_max_bytes = bytearray(struct.pack("f", patient_ab_volume_max))
                #
                each_guards_bytes = bytearray(0)
                each_guards_bytes += basal_rate_min_bytes
                each_guards_bytes += basal_rate_max_bytes
                each_guards_bytes += vtbi_min_bytes
                each_guards_bytes += vtbi_max_bytes
                each_guards_bytes += loading_dose_min_bytes
                each_guards_bytes += loading_dose_max_bytes
                each_guards_bytes += time_min_bytes
                each_guards_bytes += time_max_bytes
                each_guards_bytes += delay_start_min_bytes
                each_guards_bytes += delay_start_max_bytes
                each_guards_bytes += auto_bolus_amount_min_bytes
                each_guards_bytes += auto_bolus_amount_max_bytes
                each_guards_bytes += bolus_interval_min_bytes
                each_guards_bytes += bolus_interval_max_bytes
                each_guards_bytes += demand_bolus_amount_min_bytes
                each_guards_bytes += demand_bolus_amount_max_bytes
                each_guards_bytes += lockout_time_min_bytes
                each_guards_bytes += lockout_time_max_bytes
                each_guards_bytes += kvo_rate_min_bytes
                each_guards_bytes += kvo_rate_max_bytes
                each_guards_bytes += delay_kvo_rate_min_bytes
                each_guards_bytes += delay_kvo_rate_max_bytes
                each_guards_bytes += max_per_hour_min_bytes
                each_guards_bytes += max_per_hour_max_bytes
                each_guards_bytes += max_per_interval_min_bytes
                each_guards_bytes += max_per_interval_max_bytes
                each_guards_bytes += clinician_dose_min_bytes
                each_guards_bytes += clinician_dose_max_bytes
                each_guards_bytes += concentration_min_bytes
                each_guards_bytes += concentration_max_bytes
                each_guards_bytes += drug_amount_min_bytes
                each_guards_bytes += drug_amount_max_bytes
                each_guards_bytes += solvent_volume_min_bytes
                each_guards_bytes += solvent_volume_max_bytes
                each_guards_bytes += weight_min_bytes
                each_guards_bytes += weight_max_bytes
                each_guards_bytes += patient_basal_rate_min_bytes
                each_guards_bytes += patient_basal_rate_max_bytes
                each_guards_bytes += patient_ab_volume_min_bytes
                each_guards_bytes += patient_ab_volume_max_bytes
                # Append 0xFF and CRC
                each_guards_size = 256
                each_guards_bytes = crc_fill(0, each_guards_bytes, each_guards_size)
                each_guards_hex = each_guards_bytes.hex()
                print('guards_length({0}) = {1}'.format(each_protocol['content']['name'], len(each_guards_bytes)))
                print(each_guards_hex)
                #
                library_constraints_bytes += each_guards_bytes
            if infusion_mode == 'intermittentInfusion':
                # 0:4 [dose_rate_min] (4-byte Float)
                dose_rate_min = float(0)
                if guards.get('doseRate') != None and guards['doseRate'][0]['min'] != None:
                    dose_rate_min = float(guards['doseRate'][0]['min'])
                else:
                    dose_rate_min = float(0)
                dose_rate_min_bytes = bytearray(struct.pack("f", dose_rate_min))
                # 4:8 [dose_rate_max] (4-byte Float)
                dose_rate_max = float(0)
                if guards.get('doseRate') != None and guards['doseRate'][0]['max'] != None:
                    dose_rate_max = float(guards['doseRate'][0]['max'])
                else:
                    dose_rate_max = float(0)
                dose_rate_max_bytes = bytearray(struct.pack("f", dose_rate_max))
                # 8:12 [dose_vtbi_min] (4-byte Float)
                dose_vtbi_min = float(0)
                if guards.get('doseVtbi') != None and guards['doseVtbi'][0]['min'] != None:
                    dose_vtbi_min = float(guards['doseVtbi'][0]['min'])
                else:
                    dose_vtbi_min = float(0)
                dose_vtbi_min_bytes = bytearray(struct.pack("f", dose_vtbi_min))
                # 12:16 [dose_vtbi_max] (4-byte Float)
                dose_vtbi_max = float(0)
                if guards.get('doseVtbi') != None and guards['doseVtbi'][0]['max'] != None:
                    dose_vtbi_max = float(guards['doseVtbi'][0]['max'])
                else:
                    dose_vtbi_max = float(0)
                dose_vtbi_max_bytes = bytearray(struct.pack("f", dose_vtbi_max))
                # 16:20 [loading_dose_min] (4-byte Float)
                loading_dose_min = float(0)
                if guards.get('loadingDoseAmount') != None and \
                        guards['loadingDoseAmount'][0]['min'] != None:
                    loading_dose_min = float(guards['loadingDoseAmount'][0]['min'])
                else:
                    loading_dose_min = float(0)
                loading_dose_min_bytes = bytearray(struct.pack("f", loading_dose_min))
                # 20:24 [loading_dose_max] (4-byte Float)
                loading_dose_max = float(0)
                if guards.get('loadingDoseAmount') != None and \
                        guards['loadingDoseAmount'][0]['max'] != None:
                    loading_dose_max = float(guards['loadingDoseAmount'][0]['max'])
                else:
                    loading_dose_max = float(0)
                loading_dose_max_bytes = bytearray(struct.pack("f", loading_dose_max))
                # 24:28 [total_time_min] (4-byte Integer)
                total_time_min = int(0)
                if guards.get('totalTime') != None and guards['totalTime'][0]['min'] != None:
                    total_time_min = int(guards['totalTime'][0]['min']) * 60
                else:
                    total_time_min = int(0)
                total_time_min_bytes = total_time_min.to_bytes(4, 'little')
                # 28:32 [total_time_max] (4-byte Integer)
                total_time_max = int(0)
                if guards.get('totalTime') != None and guards['totalTime'][0]['max'] != None:
                    total_time_max = int(guards['totalTime'][0]['max']) * 60
                else:
                    total_time_max = int(0)
                total_time_max_bytes = total_time_max.to_bytes(4, 'little')
                # 32:36 [interval_time_min] (4-byte Integer)
                interval_time_min = int(0)
                if guards.get('intervalTime') != None and guards['intervalTime'][0]['min'] != None:
                    interval_time_min = int(guards['intervalTime'][0]['min']) * 60
                else:
                    interval_time_min = int(0)
                interval_time_min_bytes = interval_time_min.to_bytes(4, 'little')
                # 36:40 [interval_time_max] (4-byte Integer)
                interval_time_max = int(0)
                if guards.get('intervalTime') != None and guards['intervalTime'][0]['max'] != None:
                    interval_time_max = int(guards['intervalTime'][0]['max']) * 60
                else:
                    interval_time_max = int(0)
                interval_time_max_bytes = interval_time_max.to_bytes(4, 'little')
                # 40:44 [delay_start_min] (4-byte Integer)
                delay_start_min = int(0)
                if guards.get('delayStart') != None and guards['delayStart'][0]['min'] != None:
                    delay_start_min = int(guards['delayStart'][0]['min']) * 60
                else:
                    delay_start_min = int(0)
                delay_start_min_bytes = delay_start_min.to_bytes(4, 'little')
                # 44:48 [delay_start_max] (4-byte Integer)
                delay_start_max = int(0)
                if guards.get('delayStart') != None and guards['delayStart'][0]['max'] != None:
                    delay_start_max = int(guards['delayStart'][0]['max']) * 60
                else:
                    delay_start_max = int(0)
                delay_start_max_bytes = delay_start_max.to_bytes(4, 'little')
                # 48:52 [int_kvo_rate_min] (4-byte Float)
                int_kvo_rate_min = float(0)
                if guards.get('intermittentKvoRate') != None and \
                        guards['intermittentKvoRate'][0]['min'] != None:
                    int_kvo_rate_min = float(guards['intermittentKvoRate'][0]['min'])
                else:
                    int_kvo_rate_min = float(0)
                int_kvo_rate_min_bytes = bytearray(struct.pack("f", int_kvo_rate_min))
                # 52:56 [int_kvo_rate_max] (4-byte Float)
                int_kvo_rate_max = float(0)
                if guards.get('intermittentKvoRate') != None and \
                        guards['intermittentKvoRate'][0]['max'] != None:
                    int_kvo_rate_max = float(guards['intermittentKvoRate'][0]['max'])
                else:
                    int_kvo_rate_max = float(0)
                int_kvo_rate_max_bytes = bytearray(struct.pack("f", int_kvo_rate_max))
                # 56:60 [kvo_rate_min] (4-byte Float)
                kvo_rate_min = float(0)
                if switches.get('kvoRate') != None and switches['kvoRate'] and \
                        guards.get('kvoRate') != None and \
                        guards['kvoRate'][0]['min'] != None:
                    kvo_rate_min = float(guards['kvoRate'][0]['min'])
                else:
                    kvo_rate_min = float(0)
                kvo_rate_min_bytes = bytearray(struct.pack("f", kvo_rate_min))
                # 60:64 [kvo_rate_max] (4-byte Float)
                kvo_rate_max = float(0)
                if switches.get('kvoRate') != None and switches['kvoRate'] and \
                        guards.get('kvoRate') != None and \
                        guards['kvoRate'][0]['max'] != None:
                    kvo_rate_max = float(guards['kvoRate'][0]['max'])
                else:
                    kvo_rate_max = float(0)
                kvo_rate_max_bytes = bytearray(struct.pack("f", kvo_rate_max))
                # 64:68 [delay_kvo_rate_min] (4-byte Float)
                delay_kvo_rate_min = float(0)
                if guards.get('delayKvoRate') != None and \
                        guards['delayKvoRate'][0]['min'] != None:
                    delay_kvo_rate_min = float(guards['delayKvoRate'][0]['min'])
                else:
                    delay_kvo_rate_min = float(0)
                delay_kvo_rate_min_bytes = bytearray(struct.pack("f", delay_kvo_rate_min))
                # 68:72 [delay_kvo_rate_max] (4-byte Float)
                delay_kvo_rate_max = float(0)
                if guards.get('delayKvoRate') != None and \
                        guards['delayKvoRate'][0]['max'] != None:
                    delay_kvo_rate_max = float(guards['delayKvoRate'][0]['max'])
                else:
                    delay_kvo_rate_max = float(0)
                delay_kvo_rate_max_bytes = bytearray(struct.pack("f", delay_kvo_rate_max))
                # 72:76 [max_per_hour_min] (4-byte Float)
                max_per_hour_min = float(0)
                if guards.get('maxAmountPerHour') != None and \
                        guards['maxAmountPerHour'][0]['min'] != None:
                    max_per_hour_min = float(guards['maxAmountPerHour'][0]['min'])
                else:
                    max_per_hour_min = float(0)
                max_per_hour_min_bytes = bytearray(struct.pack("f", max_per_hour_min))
                # 76:80 [max_per_hour_max] (4-byte Float)
                max_per_hour_max = float(0)
                if guards.get('maxAmountPerHour') != None and \
                        guards['maxAmountPerHour'][0]['max'] != None:
                    max_per_hour_max = float(guards['maxAmountPerHour'][0]['max'])
                else:
                    max_per_hour_max = float(0)
                max_per_hour_max_bytes = bytearray(struct.pack("f", max_per_hour_max))
                # 80:84 [max_per_interval_min] (4-byte Float)
                max_per_interval_min = float(0)
                if guards.get('maxAmountPerInterval') != None and \
                        guards['maxAmountPerInterval'][0]['min'] != None:
                    max_per_interval_min = float(guards['maxAmountPerInterval'][0]['min'])
                else:
                    max_per_interval_min = float(0)
                max_per_interval_min_bytes = bytearray(struct.pack("f", max_per_interval_min))
                # 84:88 [max_per_interval_max] (4-byte Float)
                max_per_interval_max = float(0)
                if guards.get('maxAmountPerInterval') != None and \
                        guards['maxAmountPerInterval'][0]['max'] != None:
                    max_per_interval_max = float(guards['maxAmountPerInterval'][0]['max'])
                else:
                    max_per_interval_max = float(0)
                max_per_interval_max_bytes = bytearray(struct.pack("f", max_per_interval_max))
                # 88:92 [concentration_min] (4-byte Float)
                concentration_min = float(0)
                if guards.get('concentration') != None and \
                        guards['concentration'][0]['min'] != None:
                    concentration_min = float(guards['concentration'][0]['min'])
                else:
                    concentration_min = float(0)
                concentration_min_bytes = bytearray(struct.pack("f", concentration_min))
                # 92:96 [concentration_max] (4-byte Float)
                concentration_max = float(0)
                if guards.get('concentration') != None and \
                        guards['concentration'][0]['max'] != None:
                    concentration_max = float(guards['concentration'][0]['max'])
                else:
                    concentration_max = float(0)
                concentration_max_bytes = bytearray(struct.pack("f", concentration_max))
                # 96:100 [drug_amount_min] (4-byte Float)
                drug_amount_min = float(0)
                if guards.get('drugAmount') != None and \
                        guards['drugAmount'][0]['min'] != None:
                    drug_amount_min = float(guards['drugAmount'][0]['min'])
                else:
                    drug_amount_min = float(0)
                drug_amount_min_bytes = bytearray(struct.pack("f", drug_amount_min))
                # 100:104 [drug_amount_max] (4-byte Float)
                drug_amount_max = float(0)
                if guards.get('drugAmount') != None and \
                        guards['drugAmount'][0]['max'] != None:
                    drug_amount_max = float(guards['drugAmount'][0]['max'])
                else:
                    drug_amount_max = float(99.9)
                drug_amount_max_bytes = bytearray(struct.pack("f", drug_amount_max))
                # 104:108 [solvent_volume_min] (4-byte Float)
                solvent_volume_min = float(0)
                if guards.get('diluteVolume') != None and \
                        guards['diluteVolume'][0]['min'] != None:
                    solvent_volume_min = float(guards['diluteVolume'][0]['min'])
                else:
                    solvent_volume_min = float(1)
                solvent_volume_min_bytes = bytearray(struct.pack("f", solvent_volume_min))
                # 108:112 [solvent_volume_max] (4-byte Float)
                solvent_volume_max = float(0)
                if guards.get('diluteVolume') != None and \
                        guards['diluteVolume'][0]['max'] != None:
                    solvent_volume_max = float(guards['diluteVolume'][0]['max'])
                else:
                    solvent_volume_max = float(999)
                solvent_volume_max_bytes = bytearray(struct.pack("f", solvent_volume_max))
                # 112:116 [weight_min] (4-byte Float)
                weight_min = float(0)
                if guards.get('weight') != None and \
                        guards['weight'][0]['min'] != None:
                    weight_min = float(guards['weight'][0]['min'])
                else:
                    weight_min = float(1)
                weight_min_bytes = bytearray(struct.pack("f", weight_min))
                # 116:120 [weight_max] (4-byte Float)
                weight_max = float(0)
                if guards.get('weight') != None and \
                        guards['weight'][0]['max'] != None:
                    weight_max = float(guards['weight'][0]['max'])
                else:
                    weight_max = float(999.9)
                weight_max_bytes = bytearray(struct.pack("f", weight_max))
                #
                each_guards_bytes = bytearray(0)
                each_guards_bytes += dose_rate_min_bytes
                each_guards_bytes += dose_rate_max_bytes
                each_guards_bytes += dose_vtbi_min_bytes
                each_guards_bytes += dose_vtbi_max_bytes
                each_guards_bytes += loading_dose_min_bytes
                each_guards_bytes += loading_dose_max_bytes
                each_guards_bytes += total_time_min_bytes
                each_guards_bytes += total_time_max_bytes
                each_guards_bytes += interval_time_min_bytes
                each_guards_bytes += interval_time_max_bytes
                each_guards_bytes += delay_start_min_bytes
                each_guards_bytes += delay_start_max_bytes
                each_guards_bytes += int_kvo_rate_min_bytes
                each_guards_bytes += int_kvo_rate_max_bytes
                each_guards_bytes += kvo_rate_min_bytes
                each_guards_bytes += kvo_rate_max_bytes
                each_guards_bytes += delay_kvo_rate_min_bytes
                each_guards_bytes += delay_kvo_rate_max_bytes
                each_guards_bytes += max_per_hour_min_bytes
                each_guards_bytes += max_per_hour_max_bytes
                each_guards_bytes += max_per_interval_min_bytes
                each_guards_bytes += max_per_interval_max_bytes
                each_guards_bytes += concentration_min_bytes
                each_guards_bytes += concentration_max_bytes
                each_guards_bytes += drug_amount_min_bytes
                each_guards_bytes += drug_amount_max_bytes
                each_guards_bytes += solvent_volume_min_bytes
                each_guards_bytes += solvent_volume_max_bytes
                each_guards_bytes += weight_min_bytes
                each_guards_bytes += weight_max_bytes
                # Append 0xFF and CRC
                each_guards_size = 256
                each_guards_bytes = crc_fill(0, each_guards_bytes, each_guards_size)
                each_guards_hex = each_guards_bytes.hex()
                print('guards_length({0}) = {1}'.format(each_protocol['content']['name'], len(each_guards_bytes)))
                print(each_guards_hex)
                #
                library_constraints_bytes += each_guards_bytes
        # Append 0xFF
        number_of_pages_constraint = 4
        page_size = 4096
        # library constraints size = 4 * 4096 = 16384
        library_constraints_size = number_of_pages_constraint * page_size
        library_constraints_bytes = byte_fill(library_constraints_bytes, library_constraints_size)
        #
        print('len(library_constraints_bytes) = {}'.format(len(library_constraints_bytes)))
        library_constraints_hex = library_constraints_bytes.hex()
        print('library_constraints_hex = \n{}'.format(library_constraints_hex))
        return library_constraints_bytes

    def get_patient_view_bytes(self, view_mode):
        '''Get Patient View Bytes'''
        # view_map_continous = {
            # 'rate': 0,
            # 'vtbi': 1,
            # 'loadingDoseAmount': 2,
            # 'time': 3,
            # 'delayStart': 4,
            # 'kvo': 5,
            # 'delayKvoRate': 6,
            # 'concentration': 7,
            # 'weight': 10,
            # 'label': 11,
            # 'saveRx': 20,
            # 'drug': 22
        # }
        # view_map_bolus = {
            # 'basalRate': 0,
            # 'vtbi': 1,
            # 'loadingDoseAmount': 2,
            # 'time': 3,
            # 'delayStart': 4,
            # 'autoBolusAmount': 5,
            # 'bolusInterval': 6,
            # 'demandBolusAmount': 7,
            # 'lockoutTime': 8,
            # 'kvo': 9,
            # 'delayKvoRate': 10,
            # 'maxAmountPerHour': 11,
            # 'maxAmountPerInterval': 12,
            # 'clinicianDose': 13,
            # 'concentration': 14,
            # 'weight': 17,
            # 'label': 18,
            # 'saveRx': 20,
            # 'drug': 22
        # }
        # view_map_intermittent = {
            # 'doseRate': 0,
            # 'doseVtbi': 1,
            # 'loadingDoseAmount': 2,
            # 'totalTime': 3,
            # 'intervalTime': 4,
            # 'delayStart': 5,
            # 'intermittentKvoRate': 6,
            # 'kvoRate': 7,
            # 'delayKvoRate': 8,
            # 'maxAmountPerHour': 9,
            # 'maxAmountPerInterval': 10,
            # 'concentration': 11,
            # 'weight': 14,
            # 'label': 15,
            # 'saveRx': 20,
            # 'drug': 22
        # }
        patient_view_bytes = bytearray(0)
        library_views = self.library['content']['views']
        if library_views != []:
            view = {}
            for each_view in library_views:
                if each_view['mode'] == view_mode:
                    view = each_view
            if view['mode'] in ['continuousInfusion', 'bolusInfusion', 'intermittentInfusion']:
                if view['mode'] == 'continuousInfusion':
                    view_map = view_map_continous
                elif view['mode'] == 'bolusInfusion':
                    view_map = view_map_bolus
                elif view['mode'] == 'intermittentInfusion':
                    view_map = view_map_intermittent
                view_parameters = view['view']['content']['parameters']
                for each_parameter in view_parameters:
                    parameter_id = view_map[each_parameter['name']]
                    if each_parameter['enabledInPatientView']:
                        patient_view_bytes += int(parameter_id).to_bytes(1, 'little')
        patient_view_bytes = int(len(patient_view_bytes)).to_bytes(1, 'little') \
                +patient_view_bytes
        # Append 0xFF - Patient View
        # patient_view_size = 23 + 1 = 24 byte
        patient_view_size = 23 + 1
        patient_view_bytes = byte_fill(patient_view_bytes, patient_view_size)
        return patient_view_bytes

    def get_titration_view_bytes(self, view_mode):
        '''Get Titration View Bytes'''
        # view_map_continous = {
            # 'rate': 0,
            # 'vtbi': 1,
            # 'loadingDoseAmount': 2,
            # 'time': 3,
            # 'delayStart': 4,
            # 'kvo': 5,
            # 'delayKvoRate': 6,
            # 'concentration': 7,
            # 'weight': 10,
            # 'label': 11,
            # 'saveRx': 20,
            # 'drug': 22
        # }
        # view_map_bolus = {
            # 'basalRate': 0,
            # 'vtbi': 1,
            # 'loadingDoseAmount': 2,
            # 'time': 3,
            # 'delayStart': 4,
            # 'autoBolusAmount': 5,
            # 'bolusInterval': 6,
            # 'demandBolusAmount': 7,
            # 'lockoutTime': 8,
            # 'kvo': 9,
            # 'delayKvoRate': 10,
            # 'maxAmountPerHour': 11,
            # 'maxAmountPerInterval': 12,
            # 'clinicianDose': 13,
            # 'concentration': 14,
            # 'weight': 17,
            # 'label': 18,
            # 'saveRx': 20,
            # 'drug': 22
        # }
        # view_map_intermittent = {
            # 'doseRate': 0,
            # 'doseVtbi': 1,
            # 'loadingDoseAmount': 2,
            # 'totalTime': 3,
            # 'intervalTime': 4,
            # 'delayStart': 5,
            # 'intermittentKvoRate': 6,
            # 'kvoRate': 7,
            # 'delayKvoRate': 8,
            # 'maxAmountPerHour': 9,
            # 'maxAmountPerInterval': 10,
            # 'concentration': 11,
            # 'weight': 14,
            # 'label': 15,
            # 'saveRx': 20,
            # 'drug': 22
        # }
        titration_view_bytes = bytearray(0)
        library_views = self.library['content']['views']
        if library_views != []:
            view = {}
            for each_view in library_views:
                if each_view['mode'] == view_mode:
                    view = each_view
            if view['mode'] in ['continuousInfusion', 'bolusInfusion', 'intermittentInfusion']:
                if view['mode'] == 'continuousInfusion':
                    view_map = view_map_continous
                elif view['mode'] == 'bolusInfusion':
                    view_map = view_map_bolus
                elif view['mode'] == 'intermittentInfusion':
                    view_map = view_map_intermittent
                view_parameters = view['view']['content']['parameters']
                for each_parameter in view_parameters:
                    parameter_id = view_map[each_parameter['name']]
                    if each_parameter['enabledInTitrationView']:
                        titration_view_bytes += int(parameter_id).to_bytes(1, 'little')
        titration_view_bytes = int(len(titration_view_bytes)).to_bytes(1, 'little') \
                +titration_view_bytes
        # Append 0xFF - Patient View
        # titration_view_size = 23 + 1 = 24 byte
        titration_view_size = 23 + 1
        titration_view_bytes = byte_fill(titration_view_bytes, titration_view_size)
        return titration_view_bytes

    def get_views_bytes(self):
        '''get views bytes'''
        # view_map_continous = {
            # 'rate': 0,
            # 'vtbi': 1,
            # 'loadingDoseAmount': 2,
            # 'time': 3,
            # 'delayStart': 4,
            # 'kvo': 5,
            # 'delayKvoRate': 6,
            # 'concentration': 7,
            # 'weight': 10,
            # 'label': 11,
            # 'saveRx': 20,
            # 'drug': 22
        # }
        # view_map_bolus = {
            # 'basalRate': 0,
            # 'vtbi': 1,
            # 'loadingDoseAmount': 2,
            # 'time': 3,
            # 'delayStart': 4,
            # 'autoBolusAmount': 5,
            # 'bolusInterval': 6,
            # 'demandBolusAmount': 7,
            # 'lockoutTime': 8,
            # 'kvo': 9,
            # 'delayKvoRate': 10,
            # 'maxAmountPerHour': 11,
            # 'maxAmountPerInterval': 12,
            # 'clinicianDose': 13,
            # 'concentration': 14,
            # 'weight': 17,
            # 'label': 18,
            # 'saveRx': 20,
            # 'drug': 22
        # }
        # view_map_intermittent = {
            # 'doseRate': 0,
            # 'doseVtbi': 1,
            # 'loadingDoseAmount': 2,
            # 'totalTime': 3,
            # 'intervalTime': 4,
            # 'delayStart': 5,
            # 'intermittentKvoRate': 6,
            # 'kvoRate': 7,
            # 'delayKvoRate': 8,
            # 'maxAmountPerHour': 9,
            # 'maxAmountPerInterval': 10,
            # 'concentration': 11,
            # 'weight': 14,
            # 'label': 15,
            # 'saveRx': 20,
            # 'drug': 22
        # }
        #
        views_bytes = bytearray(0)
        extracted_views = self.library['content']['extractedViews']
        for each_view in extracted_views:
            # 0:181 - [View]
            each_view_bytes = bytearray(0)
            each_patient_view_bytes = bytearray(0)
            each_titration_view_bytes = bytearray(0)
            view_parameters = each_view['content']['parameters']
            view_map = {}
            if each_view['content']['deliveryMode'] == 'continuousInfusion':
                view_map = view_map_continous
            elif each_view['content']['deliveryMode'] == 'bolusInfusion':
                view_map = view_map_bolus
            elif each_view['content']['deliveryMode'] == 'intermittentInfusion':
                view_map = view_map_intermittent
            view_parameters_count = len(view_parameters)
            each_view_bytes += int(view_parameters_count).to_bytes(1, 'little')
            for each_parameter in view_parameters:
                parameter_id = view_map[each_parameter['name']]
                parameter_value = each_parameter['value']
                if len(parameter_value) >= 8: 
                    parameter_value = parameter_value[0:7]
                #
                each_view_bytes += int(parameter_id).to_bytes(1, 'little')
                each_view_bytes += byte_fill(parameter_value.encode(), 8, 0)
                #
                if each_parameter['enabledInPatientView']:
                    each_patient_view_bytes += int(parameter_id).to_bytes(1, 'little')
                #
                if each_parameter['enabledInTitrationView']:
                    each_titration_view_bytes += int(parameter_id).to_bytes(1, 'little')
            # Append 0x00 - [View]
            max_number_of_parameters = 20
            each_parameter_size = 9
            view_parameters_count_size = 1
            # each_view_size = 20 * 9 + 1 = 181
            each_view_size = max_number_of_parameters * each_parameter_size + view_parameters_count_size
            each_view_bytes = byte_fill(each_view_bytes, each_view_size, 0)                
            # 181:205 [Patient View]
            patient_view_bytes = int(len(each_patient_view_bytes)).to_bytes(1, 'little') \
                    +each_patient_view_bytes
            # Append 0xFF - [Patient View]
            patient_view_size = 23 + 1
            patient_view_bytes = byte_fill(patient_view_bytes, patient_view_size)
            # 205:229 [Titration View]
            titration_view_bytes = int(len(each_titration_view_bytes)).to_bytes(1, 'little') \
                    +each_titration_view_bytes
            # Append 0xFF - [Titration View]
            titration_view_size = 23 + 1
            titration_view_bytes = byte_fill(titration_view_bytes, titration_view_size)
            #
            full_view_bytes = bytearray(0)
            full_view_bytes += each_view_bytes
            full_view_bytes += patient_view_bytes
            full_view_bytes += titration_view_bytes
            # Append 0xFF and calculate CRC
            full_view_size = 256
            full_view_bytes = crc_fill(0, full_view_bytes, full_view_size)
            #
            full_view_hex = full_view_bytes.hex()
            print('view_length({0}) = {1}'.format(each_view['content']['deliveryMode'], \
                    len(full_view_bytes)))
            print(full_view_hex)
            #
            views_bytes += full_view_bytes
        #
        # Append 0xFF [Views]
        number_of_pages_views = 4
        page_size = 4096
        # view size = 4 * 4096 = 16384
        views_size = number_of_pages_views * page_size
        views_bytes = byte_fill(views_bytes, views_size)
        #
        print('len(views_bytes) = {}'.format(len(views_bytes)))
        views_hex = views_bytes.hex()
        print('views_hex = \n{}'.format(views_hex))
        return views_bytes

    def get_default_views_bytes(self):
        '''get default views bytes'''
        # view_map_continous = {
            # 'rate': 0,
            # 'vtbi': 1,
            # 'loadingDoseAmount': 2,
            # 'time': 3,
            # 'delayStart': 4,
            # 'kvo': 5,
            # 'delayKvoRate': 6,
            # 'concentration': 7,
            # 'weight': 10,
            # 'label': 11,
            # 'saveRx': 20,
            # 'drug': 22
        # }
        # view_map_bolus = {
            # 'basalRate': 0,
            # 'vtbi': 1,
            # 'loadingDoseAmount': 2,
            # 'time': 3,
            # 'delayStart': 4,
            # 'autoBolusAmount': 5,
            # 'bolusInterval': 6,
            # 'demandBolusAmount': 7,
            # 'lockoutTime': 8,
            # 'kvo': 9,
            # 'delayKvoRate': 10,
            # 'maxAmountPerHour': 11,
            # 'maxAmountPerInterval': 12,
            # 'clinicianDose': 13,
            # 'concentration': 14,
            # 'weight': 17,
            # 'label': 18,
            # 'saveRx': 20,
            # 'drug': 22
        # }
        # view_map_intermittent = {
            # 'doseRate': 0,
            # 'doseVtbi': 1,
            # 'loadingDoseAmount': 2,
            # 'totalTime': 3,
            # 'intervalTime': 4,
            # 'delayStart': 5,
            # 'intermittentKvoRate': 6,
            # 'kvoRate': 7,
            # 'delayKvoRate': 8,
            # 'maxAmountPerHour': 9,
            # 'maxAmountPerInterval': 10,
            # 'concentration': 11,
            # 'weight': 14,
            # 'label': 15,
            # 'saveRx': 20,
            # 'drug': 22
        # }
        #
        default_views_bytes = bytearray(0)
        library_default_views = self.library['content']['defaultViews']
        for each_view in library_default_views:
            if each_view['name'] in ['continuousInfusion', 'bolusInfusion', 'intermittentInfusion']:
                each_view_bytes = bytearray(0)
                #
                each_patient_view_bytes = bytearray(0)
                #
                each_titration_view_bytes = bytearray(0)
                #
                view_parameters = each_view['parameters']
                view_map = {}
                if each_view['name'] == 'continuousInfusion':
                    view_map = view_map_continous
                elif each_view['name'] == 'bolusInfusion':
                    view_map = view_map_bolus
                elif each_view['name'] == 'intermittentInfusion':
                    view_map = view_map_intermittent
                view_parameters_count = len(view_parameters)
                each_view_bytes += int(view_parameters_count).to_bytes(1, 'little')
                for each_parameter in view_parameters:
                    parameter_id = view_map[each_parameter['name']]
                    parameter_value = each_parameter['defaultValue']
                    if len(parameter_value) >= 8: 
                        parameter_value = parameter_value[0:7]
                    each_view_bytes += int(parameter_id).to_bytes(1, 'little')
                    each_view_bytes += byte_fill(parameter_value.encode(), 8, 0)
                # Append 0x00 - Full View
                max_number_of_parameters = 20
                each_parameter_size = 9
                view_parameters_count_size = 1
                # full_view_size = 20 * 9 + 1 = 181
                full_view_size = max_number_of_parameters * each_parameter_size + view_parameters_count_size
                each_view_bytes = byte_fill(each_view_bytes, full_view_size, 0)                
                # Append [Patient View]
                each_patient_view_bytes = self.get_patient_view_bytes(each_view['name'])
                each_view_bytes += each_patient_view_bytes
                # Append [Titration View]
                each_titration_view_bytes = self.get_titration_view_bytes(each_view['name'])
                each_view_bytes += each_titration_view_bytes
                # Append 0xFF and calculate CRC
                each_view_size = 256
                each_view_bytes = crc_fill(0, each_view_bytes, each_view_size)
                #
                each_view_hex = each_view_bytes.hex()
                print('each_view_length({0}) = {1}'.format(each_view['name'], len(each_view_bytes)))
                print(each_view_hex)
                #
                default_views_bytes += each_view_bytes
        # Append 0xFF
        number_of_pages_default_views = 1
        page_size = 4096
        # default view size = 1 * 4096 = 4096
        default_views_size = number_of_pages_default_views * page_size
        default_views_bytes = byte_fill(default_views_bytes, default_views_size)
        #
        print('len(default_views_bytes) = {}'.format(len(default_views_bytes)))
        default_views_hex = default_views_bytes.hex()
        print('default_views_hex = \n{}'.format(default_views_hex))
        #
        return default_views_bytes

    def get_access_code(self, role):
        '''Get Access Code (PIN)'''
        access_code = ''
        access_codes = self.library['content']['accessCodes']
        for each_access_code in access_codes:
            roles = each_access_code['roles']
            for each_role in roles:
                if each_role == role:
                    access_code = each_access_code['code']
                    break
        return access_code

    def get_role_map(self):
        '''Get Role Maps'''
        role_map = {}
        default_roles = self.library['content']['defaultRoles']
        # access_codes = self.library['content']['accessCodes']
        for each_role in default_roles:
            if each_role != 'anyone':
                role_map[each_role] = {'access_code': self.get_access_code(each_role), \
                                          'bit_mask': 1 << (default_roles.index(each_role) - 1)
                                      }
            else:
                role_map['anyone'] = {'access_code': '', \
                                      'bit_mask': 0xFFFF
                                      }
        #
        return role_map

    def get_role_bit_mask(self, roles):
        '''Get Role Bit Mask'''
        role_map = self.get_role_map()
        mask = 0x0
        for each_role in roles:
            mask ^= role_map[each_role]['bit_mask']
        return mask & 0xFFFF
            
    def get_view_index(self, view_id):
        extracted_views = self.library['content']['extractedViews']
        for each_view in extracted_views:
            if each_view['id'] == view_id:
                return extracted_views.index(each_view)
        #
        print("Error: View not found! (view id: {})".format(view_id))
        return 0xFF
        
    def get_label_index(self, label_name):
        labels = self.library['content']['labelSets']
        for each_label in labels:
            if each_label['name'] == label_name:
                return labels.index(each_label)
        #
        print("Error: Label not found!")
        return 0xFF
        
    def get_protocol_index(self, protocol_id):
        extracted_protcols = self.library['content']['extractedProtocols']
        for each_protocol in extracted_protcols:
            if each_protocol['id'] == protocol_id or \
                each_protocol['content']['name'] == protocol_id:
                return extracted_protcols.index(each_protocol)
        #
        print("Error: Protocol not found! (protocol id/name: {})".format(protocol_id))
        return -1
    
    def get_protocol_elements(self, node):
        # Initialize protocol_elements
        protocol_elements = []
        if node['type'] == 'protocol':
            # Add into protocol_elements
            protocol_element = {'role_bit_mask': self.get_role_bit_mask(node['roles']), \
                                'index': self.get_protocol_index(node['data']['id']), \
                                'view_index': 0xFF, \
                                'label_index': 0xFF
                                }
            if node['view'] != None:
                protocol_element['view_index'] = self.get_view_index(node['view']['id'])
            if node['labelSet'] != None: 
                protocol_element['label_index'] = self.get_label_index(node['labelSet']['name'])
            #     
            protocol_elements.append(protocol_element)
        elif (node['type'] == 'folder') and ('children' in node.keys()):
            for cur_node in node['children']:
                # DFS Recursive Algorithm
                protocol_elements += self.get_protocol_elements(cur_node)
        return protocol_elements
        
    def get_protocol_elements_bytes(self):
        '''get protocol elements bytes'''
        protocol_elements = self.get_protocol_elements(self.library['content']['node'])
        #
        protocol_elements_bytes = bytearray(0)
        for each_element in protocol_elements:
            # print("role_bit_mask is ,", each_element['role_bit_mask'])
            # print("index is ,", each_element['index'])
            # print("view_index is ,", each_element['view_index'])
            # print("label_index is ,", each_element['label_index'])
            
            role_bit_mask_bytes = int(each_element['role_bit_mask']).to_bytes(2, 'little')
            index_bytes = int(each_element['index']).to_bytes(1, 'little')
            view_index_bytes = int(each_element['view_index']).to_bytes(1, 'little')
            label_index_bytes = int(each_element['label_index']).to_bytes(1, 'little')
            #
            element_bytes = bytearray(0) 
            element_bytes += role_bit_mask_bytes
            element_bytes += index_bytes
            element_bytes += view_index_bytes
            element_bytes += label_index_bytes
            # Append 0xFF Element Bytes
            element_size = 8
            element_bytes = byte_fill(element_bytes, element_size)
            print(element_bytes.hex())
            #
            protocol_elements_bytes += element_bytes
        return protocol_elements_bytes

    def get_user_config_bytes(self):
        '''get user config bytes'''
        # Globals #
        global_params = self.library['content']['globals']
        # 1 0:4 Eventlog Bitmap (Bitmap 4-byte)
        eventlog_bitmap_bytes = int(0xFFFFFFFF).to_bytes(4, 'little')
        # 2 4:8 Total Time (hours -> seconds Integer 4-byte)
        total_time = global_params[4]['parameters'][5]['nuValue'] * 3600
        total_time_bytes = int(total_time).to_bytes(4, 'little')
        # 3 8:12 Total VINF (Float 4-byte)
        total_vinf = float(global_params[4]['parameters'][4]['nuValue'])
        total_vinf_bytes = bytearray(struct.pack("f", total_vinf))
        # 4 12:16 Service Time (hours -> seconds Integer 4-byte)
        service_time = global_params[4]['parameters'][3]['nuValue'] * 3600
        service_time_bytes = int(service_time).to_bytes(4, 'little')
        # 5 16:20 Service VINF (Float 4-byte)
        service_vinf = float(global_params[4]['parameters'][2]['nuValue'])
        service_vinf_bytes = bytearray(struct.pack("f", service_vinf))
        # 6 20:24 Battery Time (hours -> seconds Integer 4-byte)
        battery_time = global_params[4]['parameters'][1]['nuValue'] * 3600
        battery_time_bytes = int(battery_time).to_bytes(4, 'little')
        # 7 24:28 Battery VINF (Float 4-byte)
        battery_vinf = float(global_params[4]['parameters'][0]['nuValue'])
        battery_vinf_bytes = bytearray(struct.pack("f", battery_vinf))
        # 8 28:32 Battery Low Time (hours -> seconds Integer 4-byte)
        battery_low_time = global_params[4]['parameters'][7]['nuValue'] * 3600
        battery_low_time_bytes = int(battery_low_time).to_bytes(4, 'little')
        # 9 32:36 Battery Low VINF (Float 4-byte)
        battery_low_vinf = float(global_params[4]['parameters'][6]['nuValue'])
        battery_low_vinf_bytes = bytearray(struct.pack("f", battery_low_vinf))
        # 10 36:40 Infusion Backup Interval(seconds Integer 4-byte)
        infusion_backup_interval = global_params[1]['parameters'][1]['nuValue']
        infusion_backup_interval_bytes = int(infusion_backup_interval).to_bytes(4, 'little')
        # 11 40:44 Indicator ON time (seconds Integer 4-byte)
        indicator_on_time = global_params[3]['parameters'][0]['nuValue']
        indicator_on_time_bytes = int(indicator_on_time).to_bytes(4, 'little')
        # 12 44:48 Library CRC (Integer 4-byte)
        library_crc_bytes = int(0).to_bytes(4, 'little')    
        if len(self.library['crc']) == 8:
            # the crc is crc32c
            library_crc_bytes = int(self.library['crc'], 16).to_bytes(4, 'little')    
        if self.library['crc'].find('MD5--') != -1:
            # the crc is MD5
            md5_ascii = self.library['crc'][5:]
            md5_hex = hexlify(md5_ascii.encode()).decode()
            library_crc_bytes = crc32c(0, md5_hex).to_bytes(4, 'little')
            # library_crc_bytes = int(1).to_bytes(4, 'little')
        # 48:52 Library Number (Integer 4-byte)
        library_number_bytes = int(self.library['id']).to_bytes(4, 'little')
        # 52:116 Role Map (32 2-byte Integer Array 64-byte)
        # default_roles = self.library['content']['defaultRoles']
        access_codes = self.library['content']['accessCodes']
        roles_map_bytes = bytearray(0)
        for each_access_code in access_codes:
            roles = each_access_code['roles']
            role_bit_mask = self.get_role_bit_mask(roles)
            roles_map_bytes += int(role_bit_mask).to_bytes(2, 'little')
        # bit_mask = 0
        # for each_default_role in default_roles:
            # if each_default_role != 'anyone':
                # roles_map_bytes += int(1 << bit_mask).to_bytes(2, 'little')
                # bit_mask += 1
        # Append 0x00 Role Map
        roles_map_size = 64
        roles_map_bytes = byte_fill(roles_map_bytes, roles_map_size, 0x00)
        # 116:118 Auth Session Timeout (seconds Short 2-byte)
        auth_session_timeout_bytes = int(600).to_bytes(2, 'little')
        # 118:120 Tubing Calibration Data (Short 2-byte)
        tubing_calibration_data_bytes = int(100).to_bytes(2, 'little')
        # 120:122 Upstream Occlusion Delay (Short 2-byte)
        upstream_occlusion_delay = global_params[2]['parameters'][0]['nuValue']
        upstream_occlusion_delay_bytes = int(upstream_occlusion_delay).to_bytes(2, 'little')
        # 122:124 Downstream Occlusion Delay (Short 2-byte)
        downstream_occlusion_delay = global_params[2]['parameters'][1]['nuValue']
        downstream_occlusion_delay_bytes = int(downstream_occlusion_delay).to_bytes(2, 'little')
        # 124:125 Indicator Initial Brightness (Byte 1-byte)
        indicator_initial_brightness = global_params[3]['parameters'][1]['sValue']
        if indicator_initial_brightness == 'Off':
            indicator_initial_brightness = (0)
        elif indicator_initial_brightness == 'Low':
            indicator_initial_brightness = int(1)
        elif indicator_initial_brightness == 'Median':
            indicator_initial_brightness = int(2)
        elif indicator_initial_brightness == 'High':
            indicator_initial_brightness = int(3)
        indicator_initial_brightness_bytes = int(indicator_initial_brightness).to_bytes(1, 'little')
        # 125:126 Indicator Sequential Brightness (Byte 1-byte)
        indicator_sequential_brightness = global_params[3]['parameters'][2]['sValue']
        if indicator_sequential_brightness == 'Off':
            indicator_sequential_brightness = 0
        elif indicator_sequential_brightness == 'Low':
            indicator_sequential_brightness = 1
        elif indicator_sequential_brightness == 'Median':
            indicator_sequential_brightness = 2
        elif indicator_sequential_brightness == 'High':
            indicator_sequential_brightness = 3
        indicator_sequential_brightness_bytes = int(indicator_sequential_brightness).to_bytes(1, 'little')
        # 126:222 Codes Map (32 3-Byte Array 96-byte)
        codes_map_bytes = bytearray(0)
        access_codes = self.library['content']['accessCodes']
        for each_access_code in access_codes:
            codes_map_bytes += each_access_code['code'].encode('ascii')
        # Append 0x00 Code Map
        codes_map_size = 96
        codes_map_bytes = byte_fill(codes_map_bytes, codes_map_size, 0x00)
        # 222:242 Library Name With Version (ASCII Byte Array 20-byte)
        library_name = self.library['content']['name'] 
        library_version = str(self.library['version'])
        library_name_with_version_bytes = (library_name + ' ' + library_version).encode('ascii')
        # Append 0x00 Library Name With Version
        library_name_with_version_size = 20
        library_name_with_version_bytes = byte_fill(library_name_with_version_bytes, \
                library_name_with_version_size, 0x00)
        # 242:258 Model Name (ASCII Byte Array 16-byte)
        model_name = 'Nimbus ' + global_params[0]['parameters'][0]['sValue']
        model_name_bytes = model_name.encode('ascii')
        # Append 0x00 Library Name With Version
        model_name_size = 16
        model_name_bytes = byte_fill(model_name_bytes, model_name_size, 0x00)
                
        globals_bytes = bytearray(0)
        globals_bytes += eventlog_bitmap_bytes
        globals_bytes += total_time_bytes
        globals_bytes += total_vinf_bytes
        globals_bytes += service_time_bytes
        globals_bytes += service_vinf_bytes
        globals_bytes += battery_time_bytes
        globals_bytes += battery_vinf_bytes
        globals_bytes += battery_low_time_bytes
        globals_bytes += battery_low_vinf_bytes
        globals_bytes += infusion_backup_interval_bytes
        globals_bytes += indicator_on_time_bytes
        globals_bytes += library_crc_bytes
        globals_bytes += library_number_bytes
        globals_bytes += roles_map_bytes
        globals_bytes += auth_session_timeout_bytes
        globals_bytes += tubing_calibration_data_bytes
        globals_bytes += upstream_occlusion_delay_bytes
        globals_bytes += downstream_occlusion_delay_bytes
        globals_bytes += indicator_initial_brightness_bytes
        globals_bytes += indicator_sequential_brightness_bytes
        globals_bytes += codes_map_bytes
        globals_bytes += library_name_with_version_bytes
        globals_bytes += model_name_bytes

        # Append 0xFF - Globals
        globals_size = 512
        globals_bytes = crc_fill(0, globals_bytes, globals_size)
        #
        print('len(globals_bytes) = {}'.format(len(globals_bytes)))
        globals_hex = globals_bytes.hex()
        print(globals_hex)
        # Label Set #
        label_sets_bytes = bytearray(0)
        label_sets = self.library['content']['labelSets']
        # each label_set is 64-byte
        label_set_size = 64
        # each label is 10 bytes
        label_size = 10
        # each label set can contain up to 5 labels
        labels_per_set = 5
        for each_label_set in label_sets:
            labels = each_label_set['labels']
            labels_count = len(labels)
            label_set_bytes = bytearray(0)
            label_set_bytes += int(labels_count).to_bytes(1, 'little')
            for label in labels:
                label_bytes = label.encode()
                label_bytes = byte_fill(label_bytes, label_size, 0x00)
                label_set_bytes += label_bytes
            # Append 0x00 Label Set
            label_set_bytes = byte_fill(label_set_bytes, label_size * labels_per_set + 1, 0x00)
            # Append 0xFF and calculate CRC
            label_set_bytes = crc_fill(0, label_set_bytes, label_set_size)
            #
            print('len(label_set_bytes) = {}'.format(len(label_set_bytes)))
            label_set_hex = label_set_bytes.hex()
            print(label_set_hex)
            #
            label_sets_bytes += label_set_bytes
        # Append 0xFF - Label Sets
        number_of_label_set = 8
        # label sets size = 8 * 64 = 512
        label_sets_size = number_of_label_set * label_set_size
        label_sets_bytes = byte_fill(label_sets_bytes, label_sets_size)
        #
        print('len(label_sets_bytes) = {}'.format(len(label_sets_bytes)))
        label_sets_hex = label_sets_bytes.hex()
        print(label_sets_hex)
        #
        # Protocol Elements #
        protocol_elements_bytes = self.get_protocol_elements_bytes()
        # Append 0xFF - Protocol Elements        
        number_of_protocol_element = 64
        protocol_element_size = 8
        # protocol elements size = 8 * 64 = 512
        protocol_elements_size = number_of_protocol_element * protocol_element_size
        protocol_elements_bytes = byte_fill(protocol_elements_bytes, protocol_elements_size)
        #
        print('len(protocol_elements_bytes) = {}'.format(len(protocol_elements_bytes)))
        protocol_elements_hex = protocol_elements_bytes.hex()
        print(protocol_elements_hex)
        #
        # Protocol Indexes #
        extracted_protcols = self.library['content']['extractedProtocols']
        protocol_indexes_bytes = bytearray(0)
        for each_protocol_index in range(len(extracted_protcols)):
            protocol_indexes_bytes += int(each_protocol_index).to_bytes(1, 'little')
        # Append 0xFF - Protocol Indexes
        number_of_protocol_index = 64
        protocol_index_size = 1
        # protocol indexes size = 64 * 1 = 64
        protocol_indexes_size = number_of_protocol_index * protocol_index_size
        protocol_indexes_bytes = byte_fill(protocol_indexes_bytes, protocol_indexes_size)
        #
        print('len(protocol_indexes_bytes) = {}'.format(len(protocol_indexes_bytes)))
        protocol_indexes_hex = protocol_indexes_bytes.hex()
        print(protocol_indexes_hex)
        # Protocol Map #
        protocol_map_bytes = bytearray(0)
        protocol_map_bytes += protocol_elements_bytes
        protocol_map_bytes += protocol_indexes_bytes
        # Append 0xFF and calculate CRC - Protocol Indexes
        protocol_map_size = 1024
        protocol_map_bytes = crc_fill(0, protocol_map_bytes, protocol_map_size)
        #
        print('len(protocol_map_bytes) = {}'.format(len(protocol_map_bytes)))
        protocol_map_hex = protocol_map_bytes.hex()
        print(protocol_map_hex)
        #
        user_config_bytes = bytearray(0)
        user_config_bytes += globals_bytes
        user_config_bytes += label_sets_bytes
        user_config_bytes += protocol_map_bytes
        # Append 0xFF - User Config
        number_of_pages_user_config = 1
        page_size = 4096
        # user config size = 4096 * 1 = 4096
        user_config_size = number_of_pages_user_config * page_size
        user_config_bytes = byte_fill(user_config_bytes, user_config_size)
        return user_config_bytes

    def get_library_bytes(self):
        '''Get Library Bytes'''
        library_bytes = bytearray(0)
        # 1. Navigation (3-Page)
        library_bytes += self.get_navigation_bytes()
        # 2. Library Protocols (4-Page)
        library_bytes += self.get_library_protocols_bytes()
        # 3. Constraint (4-Page)
        library_bytes += self.get_library_constraints_bytes()
        # 4. View (4-Page)
        library_bytes += self.get_views_bytes()
        # 5. Default Views (1-Page)
        library_bytes += self.get_default_views_bytes()
        # 6. User Config (1-Page)
        library_bytes += self.get_user_config_bytes()
        # Append 0xFF
        number_of_pages_library = 17
        page_size = 4096
        # library size = 17 * 4096 = 69632
        library_size = number_of_pages_library * page_size
        library_bytes = byte_fill(library_bytes, library_size)
        # while len(library_bytes) < library_size:
            # library_bytes += int(0xFF).to_bytes(1, 'little')
        print('len(library_bytes) = {}'.format(len(library_bytes)))
        # library_hex = library_bytes.hex()
        # print(library_hex)
        ##########
        # library_hex = 'ffff0102030000000000000003000000000000000000000000000000007374616e646279526f6f740000000000010000ffffffffffffffffffffffff8ebd9eaaffff04050600000000000000034261747465727920527374000000000042617474657279205265736574000000010001ffffffffffffffffffffffff308ab0cdffff07080000000000000000024375725278000000000000000000000043757272656e74205278000000000000010001ffffffffffffffffffffffff0d2f55d9ffff090a0b0c0d0e0f100000084e6577527800000000000000000000004e657720527800000000000000000000010000fffffffffffffffffffffffff26e7413ffff000000000000000000000042617474657279204368616e6765640042617474657279204368616e67656400000000ffffffffffffffffffffffff76645a32ffff00000000000000000000005965730000000000000000000000000059657300000000000000000000000000130000ffffffffffffffffffffffff61839ae8ffff00000000000000000000004e6f00000000000000000000000000004e6f00000000000000000000000000000a0000ffffffffffffffffffffffffae6ecf1effff0000000000000000000000526573756d65496e6600000000000000526573756d6520496e667573696f6e00040001ffffffffffffffffffffffff42beda71ffff00000000000000000000004e6577496e66000000000000000000004e657720496e667573696f6e00000000030001ffffffffffffffffffffffff80645132ffff1112130000000000000003636f6e74000000000000000000000000636f6e74000000000000000000000000010000fffffffffffffffffffffffff47d1794ffff1415161718191a1b1c0009626f6c75730000000000000000000000626f6c75730000000000000000000000010000ffffffffffffffffffffffffe5d1845affff1d1e1f2021220000000006696e7400000000000000000000000000696e7400000000000000000000000000010000ffffffffffffffffffffffffe9af5d9effff23242526000000000000047765696768742062617365640000000077656967687420626173656400000000010000ffffffffffffffffffffffff5047a29effff2728000000000000000002646f7365206261736564000000000000646f7365206261736564000000000000010000ffffffffffffffffffffffff786aa563ffff292a2b2c2d2e2f3031320a636f6e745f7200000000000000000000636f6e745f7200000000000000000000010000ffffffffffffffffffffffff2d25b199ffff3334353637000000000005626f6c75735f6d706800000000000000626f6c75735f6d706800000000000000010000ffffffffffffffffffffffff8a6cb25fffff3800000000000000000001626f6c75735f6d706900000000000000626f6c75735f6d706900000000000000010000ffffffffffffffffffffffffa5776555ffff00000000000000000000007473745f7261746500000000000000007473745f726174650000000000000000020000ffffffffffffffffffffffff83e5676e040000000000000000000000007473745f74696d6520763100000000007473745f74696d652076310000000000020100ffffffffffffffffffffffff06b7ff4a080000000000000000000000007473745f7274207631000000000000007473745f727420763100000000000000020200ffffffffffffffffffffffff8ecc95b3ffff00000000000000000000007473745f6162000000000000000000007473745f616200000000000000000000020300ffffffffffffffffffffffff293539afffff00000000000000000000007473745f6462000000000000000000007473745f646200000000000000000000020400ffffffffffffffffffffffffbbc41445ffff00000000000000000000007473745f6c64207632000000000000007473745f6c6420763200000000000000020500ffffffffffffffffffffffff394d3bc3ffff00000000000000000000007473745f64656c61794b564f207631007473745f64656c61794b564f20763100020600ffffffffffffffffffffffffd6ab2c4bffff00000000000000000000007473745f64656c6179207631000000007473745f64656c617920763100000000020700ffffffffffffffffffffffffb3cc5276ffff00000000000000000000007473745f6d70682076310000000000007473745f6d7068207631000000000000020800ffffffffffffffffffffffff0cd72d94ffff00000000000000000000007473745f6d70692076330000000000007473745f6d7069207633000000000000020900ffffffffffffffffffffffffd0028eaaffff00000000000000000000007473745f6364207633000000000000007473745f636420763300000000000000020a00ffffffffffffffffffffffff05f3040bffff00000000000000000000007473745f646c796462207631000000007473745f646c79646220763100000000020b00ffffffffffffffffffffffff194f74fdffff00000000000000000000007473745f696e743031000000000000007473745f696e74303100000000000000020c00ffffffffffffffffffffffffc83d90d5ffff0000000000000000000000696e745f4b564f5f6e65772076310000696e745f4b564f5f6e65772076310000020d00ffffffffffffffffffffffff8dcb4400ffff0000000000000000000000696e745f646c79207631000000000000696e745f646c79207631000000000000020e00ffffffffffffffffffffffff69317ddbffff0000000000000000000000696e745f646c794b564f207631000000696e745f646c794b564f207631000000020f00ffffffffffffffffffffffffe9174623ffff0000000000000000000000696e745f6d7068207631000000000000696e745f6d7068207631000000000000021000ffffffffffffffffffffffffcf6508a1ffff0000000000000000000000696e745f6d7069207631000000000000696e745f6d7069207631000000000000021100ffffffffffffffffffffffff16849b71ffff00000000000000000000004457425231000000000000000000000044574252310000000000000000000000021200ffffffffffffffffffffffff0180ebdbffff00000000000000000000004457425232000000000000000000000044574252320000000000000000000000021300ffffffffffffffffffffffffb957443cffff00000000000000000000004457425233000000000000000000000044574252330000000000000000000000021400ffffffffffffffffffffffffc3101670ffff00000000000000000000004457425234000000000000000000000044574252340000000000000000000000021500ffffffffffffffffffffffff9371c631ffff00000000000000000000004442523100000000000000000000000044425231000000000000000000000000021600ffffffffffffffffffffffff6732410cffff00000000000000000000004442523200000000000000000000000044425232000000000000000000000000021700ffffffffffffffffffffffff909ce8edffff0000000000000000000000636f6e745f725f315f31300000000000636f6e745f725f315f31300000000000021800ffffffffffffffffffffffff2865c019ffff0000000000000000000000636f6e745f725f315f32300000000000636f6e745f725f315f32300000000000021900ffffffffffffffffffffffff79295ff0ffff0000000000000000000000636f6e745f725f315f33300000000000636f6e745f725f315f33300000000000021a00ffffffffffffffffffffffff80959e16ffff0000000000000000000000636f6e745f725f315f34300000000000636f6e745f725f315f34300000000000021b00ffffffffffffffffffffffff9ab710f8ffff0000000000000000000000636f6e745f725f315f35300000000000636f6e745f725f315f35300000000000021c00ffffffffffffffffffffffff78847d07ffff0000000000000000000000636f6e745f725f315f36300000000000636f6e745f725f315f36300000000000021d00ffffffffffffffffffffffff29c8e2eeffff0000000000000000000000636f6e745f725f315f37300000000000636f6e745f725f315f37300000000000021e00ffffffffffffffffffffffffd0742308ffff0000000000000000000000636f6e745f725f315f38300000000000636f6e745f725f315f38300000000000021f00ffffffffffffffffffffffff5c8a8fe8ffff0000000000000000000000636f6e745f725f315f39300000000000636f6e745f725f315f39300000000000022000ffffffffffffffffffffffff3ce36d8fffff0000000000000000000000636f6e745f725f315f31303000000000636f6e745f725f315f31303000000000022100ffffffffffffffffffffffff5785c81effff000000000000000000000064625f6d70685f31300000000000000064625f6d70685f313000000000000000022200ffffffffffffffffffffffff5dda62efffff000000000000000000000061625f6d70685f31300000000000000061625f6d70685f313000000000000000022300ffffffffffffffffffffffff0e50f950ffff00000000000000000000006c645f6d70685f3130000000000000006c645f6d70685f313000000000000000022400ffffffffffffffffffffffffd29533cfffff000000000000000000000063645f6d70685f31300000000000000063645f6d70685f313000000000000000022500ffffffffffffffffffffffffcbc98035ffff0000000000000000000000626173616c5f6d70685f313000000000626173616c5f6d70685f313000000000022600ffffffffffffffffffffffff83f09d88ffff000000000000000000000061625f6d70695f31300000000000000061625f6d70695f313000000000000000022700ffffffffffffffffffffffff6cfd710fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff010203040500000000000500000000000000000000000000000000636f6e666967526f6f74000000000000010000ffffffffffffffffffffffff95be321affff000000000000000000000050756d70496e666f000000000000000050756d7020496e666f00000000000000140000ffffffffffffffffffffffffe0975148ffff00000000000000000000004576656e744c6f6700000000000000004576656e74204c6f6700000000000000000001ffffffffffffffffffffffff8e02368dffff000000000000000000000050756d70436f6e66000000000000000050756d7020436f6e6669670000000000000001ffffffffffffffffffffffffda91df93ffff000000000000000000000042696f6d6564436f6e6600000000000042696f6d656420436f6e666967000000000001ffffffffffffffffffffffffbab412b3ffff06070800000000000000034261747465727920527374000000000042617474657279205265736574000000010000ffffffffffffffffffffffff111e2b15ffff000000000000000000000042617474657279204368616e6765640042617474657279204368616e67656400000000ffffffffffffffffffffffff76645a32ffff00000000000000000000005965730000000000000000000000000059657300000000000000000000000000130000ffffffffffffffffffffffff61839ae8ffff00000000000000000000004e6f00000000000000000000000000004e6f00000000000000000000000000000a0000ffffffffffffffffffffffffae6ecf1effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff010203040500000000000500000000000000000000000000000000696e667573696f6e526f6f7400000000010000ffffffffffffffffffffffffb73319d4ffff00000000000000000000005061745469747261746500000000000050617469656e74205469747261746500080000ffffffffffffffffffffffff88447d54ffff00000000000000000000005265766965775278000000000000000052657669657720527800000000000000050000ffffffffffffffffffffffffb78af7a4ffff060708090a0000000000055368696674546f740000000000000000536869667420546f74616c00000000000b0000ffffffffffffffffffffffff889e11a102000000000000000000000000546974726174696f6e00000000000000546974726174696f6e00000000000000060000ffffffffffffffffffffffffc326f63402000b0c0d0000000000000003436c696e446f73650000000000000000436c696e696369616e20446f73650000010000ffffffffffffffffffffffff45796848ffff0000000000000000000000546f7420566f6c000000000000000000546f7420566f6c0000000000000000000c0000ffffffffffffffffffffffff3517290affff0000000000000000000000422041746d7074000000000000000000422041746d70740000000000000000000d0000fffffffffffffffffffffffff2fee491ffff0000000000000000000000422044656c6976000000000000000000422044656c69760000000000000000000e0000ffffffffffffffffffffffff0dd12a1affff000000000000000000000053682054696d6500000000000000000053682054696d650000000000000000000f0000ffffffffffffffffffffffff14b1c9dfffff0e0f000000000000000002436c6561720000000000000000000000436c6561720000000000000000000000010000ffffffffffffffffffffffffd428a60bffff0000000000000000000000446f7356000000000000000000000000446f7356000000000000000000000000100000ffffffffffffffffffffffff48326ba3ffff00000000000000000000004f4b20746f20436f6e6669726d0000004f4b20746f20436f6e6669726d000000070000ffffffffffffffffffffffff1eb47485ffff000000000000000000000043616e63656c0000000000000000000043616e63656c000000000000000000000a0000ffffffffffffffffffffffff4c944771ffff00000000000000000000004f4b20746f20436c65617200000000004f4b20746f20436c6561720000000000090000ffffffffffffffffffffffff09c788b1ffff000000000000000000000043616e63656c0000000000000000000043616e63656c000000000000000000000a0000ffffffffffffffffffffffff4c944771ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff39ffffff254ed9ac09ffffff84b6f25c10ffffff91aee371ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0000f0420000804000000000000000003c000000000000000000a040cdcccc3d0000c84200007a4400000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff53004000db1feb28000064000000ffff0000007473745f72617465000058595a000000000000006162630000000000000000000000000000000000302e3035206d672f6d4c00000000006566670000000000000000000000000000000000302e3035206d672f6d4c00000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff904a176a0000000000002041000000002c01000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0a0000007004dbb8000064000000ffff0000007473745f74696d65000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff690d0d640000f04200000000000000002c01000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0900000027151b62000064000000ffff0000007473745f72740000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff769d06ca0000f0410000a0410000c040000000003c000000000000401c0200000000803f3c000000000000000000704100004041000040400000803f00000000000000000000000000000000fffffffffffffffff73d0000ca1349d4000064000001ffff0000007473745f61620000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff6172b0720000f0420000a04100000000000000003c00000000000000000000000000204100000000000000000000704200005243ffff7f7f0000000000000000000000000000803f00000000ffffffffffffffff93054000332bfe10000064000101ffff0000007473745f646200000000566172447275674d67004e6f20636f6d706f6e656e74730000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffb65c32b60000f0420000c8420000803f000000000000000000000000000000000000000000000000000000000000000000005243ffff7f7f0000000000000000000000000000000000000000ffffffffffffffff0700000018f83459000064000001ffff0000007473745f6c640000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffec7625370000f0420000c84200000000000000003c00000000000000000000000000000000000000000000000000704200005243ffff7f7f0000000000000000000000000000000000000000ffffffffffffffff13040000bd2463de000064000001ffff0000007473745f64656c61790000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff743a16230000f0420000c84200000000000000003c00000000000000000000000000000000000000000000000000000000005243ffff7f7f0000000000000000000000000000000000000000ffffffffffffffff130000005fc9b0e7000064000001ffff0000007473745f64656c61790000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffdd725e990000f042000020410000000000000000000000000000000000000000000000000000000000000000000000000000a040ffff7f7f0000000000000000000000000000000000000000ffffffffffffffff0308000061ce033c000064000001ffff0000007473745f6d706800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff629dbe1000008c420000c8420000000000000000000000000000803f780000000000000000000000000000000000000000005243000000400000000000000000000000000000000000000000ffffffffffffffff63100000f65fc88c000064000001ffff0000007473745f6d706900000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff034ffe650000f0420000c84200000000000000000000000000000000000000000000000000000000000000000000000000005243ffff7f7f0000803f00000000000000000000000000000000ffffffffffffffff032000007027c29e000064000001ffff0000007473745f63640000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff830673b30000f0420000803f00000000000000003c00000000000000000000000000803f00000000000000000000000000005243ffff7f7f0000000000000000000000000000000000000000ffffffffffffffff93010000b1c6bbc4000064000001ffff0000007473745f646c7964620000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff34b4002a0000f042000000400000000068010000780000003c0000000000404000004040000040400000a0410000204100000000000000000000000000000000fffffffffffffffffffffffffffffffffffffffffb0700008423c4ad000064000002ffff0000007473745f696e7430310000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff6f2980bd0000f0420000803f000000003c0000003c00000000000000000020410000a0410000000000005243ffff7f7f00000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffdb000000f718ded7000064000002ffff000000696e745f4b564f5f6e0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffe57f1d8f0000f0420000803f000000002c0100003c0000003c0000000000803f000000000000000000005243ffff7f7f00000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffff7b0000009f43f229000064000002ffff000000696e745f646c7900000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff6dda91ac0000f0420000803f000000002c0100003c0000003c0000000000803f000000000000803f00005243ffff7f7f00000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffff7b01000018612cda000064000002ffff000000696e745f646c794b560000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff58ea6e2d0000f0420000803f000000002c0100003c000000000000000000803f000000000000000000000040ffff7f7f00000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffff5b020000c541d5b5000064000002ffff000000696e745f6d706800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff780d9ca10000f04200000040000000005802000078000000000000000000803f0000000000000000000052430000803f00000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffff5b040000ca2c32ab000064000002ffff000000696e745f6d706900000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffb33defca0000803f0000c842000000000000000000000000000000000000000000002041000020410000803f00000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff83044000ed301480000064000100ffff00040144574252310000000000566172447275670000004e6f20636f6d706f6e656e74730000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff43e375e60ad7233c0000c842000000000000000000000000000000000000000000002041000020410000803f00000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff83044000609b8d2c000064000100ffff00020144574252320000000000566172447275670000004e6f20636f6d706f6e656e74730000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff070637a70000c8410000c84200000000000000000000000000000000000000000000803f000020410000204100000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff83044000a75c1631000064000100ffff00040044574252330000000000566172447275674d67004e6f20636f6d706f6e656e74730000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0b721bdcdcccc3d0000c84200000000000000000000000000000000000000000000803f000020410000204100000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff830440007bbb0107000064000100ffff00020044574252340000000000566172447275674d67004e6f20636f6d706f6e656e74730000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff224ba81b000020410000c842000000000000000000000000000000000000000000002041000020410000803f00000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff83004000f83dea6b000064000100ffff00030144425231000000000000566172447275670000004e6f20636f6d706f6e656e74730000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff14ef55540ad7233c0000c842000000000000000000000000000000000000000000002041000020410000803f00000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff830040006691017a000064000100ffff00010144425232000000000000566172447275670000004e6f20636f6d706f6e656e74730000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff62aae753000020410000803f0000000000000000000000000000000000000000cdcccc3d0000c84200007a4400000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff03004000ada4cb37000064000000ffff000000636f6e745f725f315f0058595a000000000000006162630000000000000000000000000000000000302e3035206d672f6d4c00000000006566670000000000000000000000000000000000302e3035206d672f6d4c00000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff103cc1600000a0410000803f0000000000000000000000000000000000000000cdcccc3d0000c84200007a4400000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff03004000ca8ea745000064000000ffff000000636f6e745f725f315f0058595a000000000000006162630000000000000000000000000000000000302e3035206d672f6d4c00000000006566670000000000000000000000000000000000302e3035206d672f6d4c00000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffbf0ab97c0000f0410000803f0000000000000000000000000000000000000000cdcccc3d0000c84200007a4400000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff030040001797836b000064000000ffff000000636f6e745f725f315f0058595a000000000000006162630000000000000000000000000000000000302e3035206d672f6d4c00000000006566670000000000000000000000000000000000302e3035206d672f6d4c00000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffc46a2e29000020420000803f0000000000000000000000000000000000000000cdcccc3d0000c84200007a4400000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0300400004da7fa1000064000000ffff000000636f6e745f725f315f0058595a000000000000006162630000000000000000000000000000000000302e3035206d672f6d4c00000000006566670000000000000000000000000000000000302e3035206d672f6d4c00000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff4dd26a18000048420000803f0000000000000000000000000000000000000000cdcccc3d0000c84200007a4400000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff03004000d9c35b8f000064000000ffff000000636f6e745f725f315f0058595a000000000000006162630000000000000000000000000000000000302e3035206d672f6d4c00000000006566670000000000000000000000000000000000302e3035206d672f6d4c00000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff27799d3c000070420000803f0000000000000000000000000000000000000000cdcccc3d0000c84200007a4400000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff03004000bee937fd000064000000ffff000000636f6e745f725f315f0058595a000000000000006162630000000000000000000000000000000000302e3035206d672f6d4c00000000006566670000000000000000000000000000000000302e3035206d672f6d4c00000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff450a704200008c420000803f0000000000000000000000000000000000000000cdcccc3d0000c84200007a4400000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0300400063f013d3000064000000ffff000000636f6e745f725f315f0058595a000000000000006162630000000000000000000000000000000000302e3035206d672f6d4c00000000006566670000000000000000000000000000000000302e3035206d672f6d4c00000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff0653213a0000a0420000803f0000000000000000000000000000000000000000cdcccc3d0000c84200007a4400000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff03004000d975beb3000064000000ffff000000636f6e745f725f315f0058595a000000000000006162630000000000000000000000000000000000302e3035206d672f6d4c00000000006566670000000000000000000000000000000000302e3035206d672f6d4c00000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff5dbda9350000b4420000803f000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff030000007cf615f4000064000000ffff000000636f6e745f725f315f0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffd7f466020000c8420000803f0000000000000000000000000000000000000000cdcccc3d0000c84200007a4400000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff030040007d7a96ec000064000000ffff000000636f6e745f725f315f0058595a000000000000006162630000000000000000000000000000000000302e3035206d672f6d4c00000000006566670000000000000000000000000000000000302e3035206d672f6d4c00000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffc30d7d15000000000000f04100000000000000000000000000000000000000000000f04100000000000000000000000000002041ffff7f7f00000000000000000000c84200007a4400000000ffffffffffffffff8309400042e100a8000064000001ffff00000064625f6d70685f31300058595a000000000000006162630000000000000000000000000000000000302e3035206d672f6d4c00000000006566670000000000000000000000000000000000302e3035206d672f6d4c00000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff1c80f25d0000803f0000f0410000000000000000000000000000f041580200000000000000000000000000000000000000002041ffff7f7f00000000000000000000c84200007a4400000000ffffffffffffffff630840003a8bef1d000064000001ffff00000061625f6d70685f31300058595a000000000000006162630000000000000000000000000000000000302e3035206d672f6d4c00000000006566670000000000000000000000000000000000302e3035206d672f6d4c00000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffafd2185d0000f0410000f0410000f041000000000000000000000000000000000000000000000000000000000000000000002041ffff7f7f0000000000000000000000000000000000000000ffffffffffffffff07080000cacaa9ad000064000001ffff0000006c645f6d70685f31300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff4c4124e00000803f0000f04100000000000000000000000000000000000000000000000000000000000000000000000000002041ffff7f7f0000f04100000000000000000000000000000000ffffffffffffffff03280000da284c25000064000001ffff00000063645f6d70685f31300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffdd137d490000f0410000f04100000000000000000000000000000000000000000000000000000000000000000000000000002041ffff7f7f0000000000000000000000000000000000000000ffffffffffffffff030800001596d90f000064000001ffff000000626173616c5f6d70680000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff871336fa0000803f0000f0410000000000000000000000000000f041580200000000000000000000000000000000000000005243000020410000000000000000000000000000000000000000ffffffffffffffff631000000d5b796f000064000001ffff00000061625f6d70695f31300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff529eafbdffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0000000000000743000000000080bb4400000000000000000000000000000000000000008051010000000000000000000000000000000743000000000000000000000000cdccc7420000803f00c079440000803f9af97944ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff230333470000000000000000000000000080bb440000000000000000000000004c2e0d00000000000000000000000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af97944fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff95c553a00000000000007430000000000000000000000000000000000000000002f0d00000000000000000000000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af97944ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeab64b910000000000000743000000000080bb44000000000000c84200000000000000000000000080510100000000000000c84200000000002f0d00000000000000c84200000000002f0d00000000000000000000000000000007430000000000005243000000000080bb44000000000000c842000000000000000000000000cdccc7420000803f00c079440000803f9af979440000000000000743000000000000c842ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff71f59db80000000000000743000000000080bb4400000000000000000000000000000000000000008051010000000000000000000000000000000000000000000000c84200000000002f0d0000000000000000000000000000000743000000000000000000000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af9794400000000000007430000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffb95d46450000000000000743000000000080bb44000000000000c84200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af9794400000000000007430000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc66116310000000000000743000000000080bb44000000000000000000000000000000000000000080510100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000743000000000000000000000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af9794400000000000007430000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffb9c600c60000000000000743000000000080bb44000000000000000000000000000000000000000080510100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af9794400000000000007430000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff34c253a40000000000000743000000000080bb44000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000524300000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af9794400000000000007430000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5a7c8aaf0000000000000743000000000080bb44000000000000000000000000000000000000000000000000000000000000c84200000000002f0d0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000080bb440000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af979440000000000000743000000000000c842ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0b0cc65a0000000000000743000000000080bb4400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000c842000000000000000000000000cdccc7420000803f00c079440000803f9af9794400000000000007430000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5fb981390000000000000743000000000080bb4400000000000000000000000000000000000000008051010000000000000000000000000000000000000000000000c84200000000002f0d0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af9794400000000000007430000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff345915270000000000000743000000000080bb44000000000000000000000000002f0d0000000000002f0d0000000000805101000000000000000743000000000000074300000000000007430000000000005243000000000080bb44000000000000000000000000cdccc7420000803f00c079440000803f9af97944ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe6eb25d60000000000000743000000000080bb44000000000000000000000000002f0d0000000000002f0d00000000000000000000000000000007430000000000000743000000000000000000000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af97944ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0c6b3d670000000000000743000000000080bb44000000000000000000000000002f0d0000000000002f0d00000000008051010000000000000007430000000000000000000000000000000000000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af97944ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc35a38b20000000000000743000000000080bb44000000000000000000000000002f0d0000000000002f0d00000000008051010000000000000007430000000000000000000000000000074300000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af97944ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5e1136580000000000000743000000000080bb44000000000000000000000000002f0d0000000000002f0d00000000000000000000000000000007430000000000000000000000000000000000000000000052430000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af97944ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe6dc28660000000000000743000000000080bb44000000000000000000000000002f0d0000000000002f0d0000000000000000000000000000000743000000000000000000000000000000000000000000000000000000000080bb44000000000000000000000000cdccc7420000803f00c079440000803f9af97944fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff318dc4200000000e1fac742000000000000484300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af97944ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffaf829be80000000000001041000000000000484300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af97944ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1b185f330000000000004842000000000000fa4300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af97944ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6c1b816b0000000000004842000000000000fa4300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af97944ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6c1b816b0000000000004842000000000000fa4300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af97944ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6c1b816b0000000000002041000000000000fa4300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af97944ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff59aea3d00000000000000743000000000080bb4400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af97944ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc49979fb0000000000000743000000000080bb4400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af97944ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc49979fb0000000000000743000000000080bb4400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af97944ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc49979fb0000000000000743000000000080bb4400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af97944ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc49979fb0000000000000743000000000080bb4400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af97944ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc49979fb0000000000000743000000000080bb4400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af97944ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc49979fb0000000000000743000000000080bb4400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af97944ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc49979fb0000000000000743000000000080bb4400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af97944ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc49979fb0000000000000743000000000080bb4400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af97944ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc49979fb0000000000000743000000000080bb4400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af97944ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc49979fb0000000000000743000000000080bb4400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000c84200000000002f0d0000000000000000000000000000000000000000000000524300000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af9794400000000000007430000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5ae7cc2c0000000000000743000000000080bb44000000000000000000000000000000000000000000000000000000000000c84200000000002f0d000000000000000000000000000000000000000000000000000000000000000000000000000000524300000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af979440000000000000743000000000000c842ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8cec73e0000000000000743000000000080bb44000000000000c84200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000524300000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af9794400000000000007430000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff10c5477e0000000000000743000000000080bb4400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000052430000000000000000000000000000c842000000000000000000000000cdccc7420000803f00c079440000803f9af9794400000000000007430000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff891dd0760000000000000743000000000080bb44000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000524300000000000000000000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af9794400000000000007430000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5a7c8aaf0000000000000743000000000080bb44000000000000000000000000000000000000000000000000000000000000c84200000000002f0d0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000080bb440000000000000000000000000000000000000000cdccc7420000803f00c079440000803f9af979440000000000000743000000000000c842ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0b0cc65affffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0a1644727567000000000053706565640000000b4c6162656c0000000444656c617900000006444b564f526174000156544249000000000354696d650000000007436f6e63000000000a5765696768740000054b564f526174650000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5bac060e0e164472756700000000124c6162656c0000000d436c696e446f7300024c445300000000000444656c61790000000a444b564f5261740001565442490000000000526174650000000005414220566f6c000006414220496e74000007444220566f6c0000084442204c636b00000b4d61782f680000000c4d61782f496e74000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000e16120d02040a0100050607080b0cffffffffffffffffff0401000507ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff696f6ae30c1644727567000000000f4c6162656c0000000544656c617900000008444b564f5261740001446f73565442490000446f73526174650006496e744b564f0000074b564f526174650004496e7454696d650003546f7454696d6500094d61782f680000000a4d61782f496e740000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000003000607ffffffffffffffffffffffffffffffffffffffff0c160f0508010006070403090affffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffec3161dfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0a1644727567000000000053706565640000000b4c6162656c0000000444656c617900000006444b564f526174000156544249000000000354696d650000000007436f6e63000000000a5765696768740000054b564f526174650000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5bac060e0e164472756700000000124c6162656c0000000d436c696e446f7300024c445300000000000444656c61790000000a444b564f5261740001565442490000000000526174650000000005414220566f6c000006414220496e74000007444220566f6c0000084442204c636b00000b4d61782f680000000c4d61782f496e74000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000e16120d02040a0100050607080b0cffffffffffffffffff0401000507ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff696f6ae30c1644727567000000000f4c6162656c0000000544656c617900000008444b564f5261740001446f73565442490000446f73526174650006496e744b564f0000074b564f526174650004496e7454696d650003546f7454696d6500094d61782f680000000a4d61782f496e740000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000003000607ffffffffffffffffffffffffffffffffffffffff0c160f0508010006070403090affffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffec3161dfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8033e10100409c468033e10100409c46f0200d000080bb4470910d000000c844050000000500000091cae2e96801000001000200040008000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000580264001400140002003030303132333939393232320000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000007473745f4c6962203736000000000000000000004e696d62757320446576000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe09900ce01454d53204c697400000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffff6ed181d2ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff000000ffffff040001ffffffffff080002ffffffffffffff0301ffffffffffff04ffffffffffffff05ffffffffffffff06ffffffffffffff07ffffffffffffff08ffffffffffffff09ffffffffffffff0affffffffffffff0bffffffffffffff0c02ffffffffffff0dffffffffffffff0effffffffffffff0fffffffffffffff10ffffffffffffff11ffffffffffffff12ffffffffffffff13ffffffffffffff14ffffffffffffff15ffffffffffffff16ffffffffffffff17ffffffffffffff18ffffffffffffff19ffffffffffffff1affffffffffffff1bffffffffffffff1cffffffffffffff1dffffffffffffff1effffffffffffff1fffffffffffffff20ffffffffffffff21ffffffffffffff22ffffffffffffff23ffffffffffffff24ffffffffffffff25ffffffffffffff26ffffffffffffff27ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2021222324252627ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5d841ee7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'
        # library_bytes = bytes.fromhex(library_hex)
        return library_bytes


def main():
    '''main function'''
    cmd = ''
    while cmd not in ['exit', 'quit']:
        cmd = input('>')
        if cmd.upper().rstrip(' \t\r\n\0') in ['HELP', '?']:
            print(' EL - Encrypt Library JSON To Byte Array')
            print(' PL - Parse Library Hex')
        # Encrypt Library JSON To Byte Array
        if cmd.lower().rstrip(' \t\r\n\0') in ['el', 'encrypt library']:
            # result = False
            print(' EL - Encrypt Library JSON To Byte Array')
            library_path = input('    Enter library path: ')
            if path.exists(library_path):
                encrypt_library(library_path)
            else:
                if library_path == '':
                    pass
                else:
                    print('Abort: path NOT exist')
        # Parse Library Hex
        if cmd.lower().rstrip(' \t\r\n\0') in ['pl', 'parse library']:
            # result = False
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


if __name__ == "__main__":
    main()
    
