'''module Test'''
import sys
from os import path
import math
import re
import json
from enum import Enum
import time
from threading import Thread, Lock
#
from pyZynoUnifiedDrivers.miva.module_motor import Motor, MotorStatus
from pyZynoUnifiedDrivers.miva.module_script import Script, get_drug_amount, get_dilute_volume
from pyZynoUnifiedDrivers.miva.module_utils import get_line_number, wait, compare_numbers, isfloat, int_to_time_str
from pyZynoUnifiedDrivers.miva.module_utils import re_scpi_get_cmd, re_scpi_set_cmd, re_compare_parameters
from pyZynoUnifiedDrivers.miva.module_utils import re_compare_list, re_compare_dict_equal
from pyZynoUnifiedDrivers.miva.module_utils import compare_event_log_equal, re_compare_str, re_compare_str_equal
from pyZynoUnifiedDrivers.miva.module_utils import re_compare_scpi_return_number, re_query_lockout, re_get_screenshot
from pyZynoUnifiedDrivers.miva.module_utils import re_compare_screenshot
from pyZynoUnifiedDrivers.miva.module_utils import time_str_to_int, re_time_str_format, hex_to_bitmap, list_to_file
from pyZynoUnifiedDrivers.miva.module_utils import json_to_file, load_json_file, bitmap_to_image
from pyZynoUnifiedDrivers.miva.module_utils import apply_screenshot_masks, compare_file_equal
from pyZynoUnifiedDrivers.miva.module_utils import EVENT_LOG_NUMBER_OF_EVENTS 

# max per hour detection margin (mL)
_MPH_MARGIN = 0.1
# refresh interval (second)
_REFRESH_TIMER = 0.1
# BOLUS infusion rate (mL/hr)
_BOLUS_RATE = 250


def generate_command_list(test_protocol, loop_num=0):
    '''Generate Command List from Test Protocol'''
    print('test_protocol = {}'.format(test_protocol))
    print('len(test_protocol) = {}'.format(len(test_protocol)))
    extracted_command_list = []
    expended_command_list = []
    # i -- Test Protocol Index
    i = 0
    while i < len(test_protocol):
        if re.match(r'(loop)(\s+)?(\d+)', test_protocol[i].strip().lower()):
            re_match_result = re.match(r'(loop)(\s+)?(\d+)', test_protocol[i].strip().lower())
            loop_num = int(re_match_result[3])
            [sub_command_list, sub_len] = generate_command_list(test_protocol[i + 1:], loop_num)
            extracted_command_list = extracted_command_list + sub_command_list
            print('i = {}'.format(i))
            print('sub_len = {}'.format(sub_len))
            i = i + sub_len + 1
            print('i + sub_len = {}'.format(i))
            
        elif re.match(r'(end)(\s+)?(loop)', test_protocol[i].strip().lower()):
            for k in range(loop_num):
                expended_command_list.append('# Looping {}/{}'.format(k + 1, loop_num))
                expended_command_list = expended_command_list + extracted_command_list
            expended_command_list.append('# End of Loop')
            return [expended_command_list, i]
        else:
            extracted_command_list.append(test_protocol[i])
        i = i + 1
    # print(command_list)
    print('extracted_command_list = {}'.format(extracted_command_list))
    print('i = {}'.format(i))
    # return command_list
    return [extracted_command_list, i]


class TestStatus(Enum):
    '''infusion mode'''
    IDLE = 0
    RUNNING_DELAY = 1
    RUNNING = 2
    RUNNING_AUTO_BOLUS = 3
    RUNNING_DEMAND_BOLUS = 4
    RUNNING_LOADING_DOSE = 5
    RUNNING_CLINICIAN_DOSE = 6
    RUNNING_INT = 7
    RUNNING_INT_KVO = 8
    RUNNING_KVO = 9
    STOPPED = 10
    PAUSED = 11
    KVO = 12
    FINISHED = 13
    PAUSED_MPH_REACHED = 14
    PAUSED_MPI_REACHED = 15
    PAUSED_DELAY = 16
    PAUSED_AUTO_BOLUS = 17
    PAUSED_DEMAND_BOLUS = 18
    PAUSED_LOADING_DOSE = 19
    PAUSED_CLINICIAN_DOSE = 20


class Test:
    '''Test class'''

    def __init__(self):
        self.test_protocol = None
        self.status = TestStatus.STOPPED
        self.previous_status = None
        self.patient_weight = None
        self.motor = Motor()
        self.db_tempt = False
        self.db_enabled = True
        self.vinf_db = 0
        self.vinf_ab = 0
        self.vinf_cd = 0
        self.vinf_dose = 0
        self.time_next_db = 0
        self.cd_tempt = False
        self.cd_enabled = True
        self.output_enabled = True
        
        # Create a mutex
        self.lock = Lock()
        
        # Infusion Parameters
        self.parameters = {'delay':
                               {'rate':{'value':0, 'unit':''},
                                'progress':{'value':0, 'unit':''},
                                'time_passed':{'value':0, 'unit':''},
                                'time_left':{'value':0, 'unit':''}},
                           'cont':
                               {'rate':{'value':0, 'unit':''},
                                'vinf':{'value':0, 'unit':''},
                                'vtbi':{'value':0, 'unit':''},
                                'progress':{'value':0, 'unit':''},
                                'time_passed':{'value':0, 'unit':''},
                                'time_left':{'value':0, 'unit':''}},
                           'bolus':
                               {'rate':{'value':0, 'unit':''},
                                'vinf':{'value':0, 'unit':''},
                                'vtbi':{'value':0, 'unit':''},
                                'progress':{'value':0, 'unit':''},
                                'vinf_ld':{'value':0, 'unit':''},
                                'progress_ld':{'value':0, 'unit':''},
                                'vinf_ab':{'value':0, 'unit':''},
                                'next_ab':{'value':0, 'unit':''},
                                'progress_ab':{'value':0, 'unit':''},
                                'vinf_db':{'value':0, 'unit':''},
                                'next_db':{'value':0, 'unit':''},
                                'progress_db':{'value':0, 'unit':''},
                                'vinf_cd':{'value':0, 'unit':''},
                                'progress_cd':{'value':0, 'unit':''},
                                'mph':{'value':0, 'unit':''},
                                'mph_qsize':{'value':0, 'unit':''},
                                'mpi':{'value':0, 'unit':''},
                                'time_passed':{'value':0, 'unit':''},
                                'time_left':{'value':0, 'unit':''}},
                            'int':
                               {'rate':{'value':0, 'unit':''},
                                'vinf':{'value':0, 'unit':''},
                                'progress':{'value':0, 'unit':''},
                                'vinf_dose':{'value':0, 'unit':''},
                                'next_dose':{'value':0, 'unit':''},
                                'progress_dose':{'value':0, 'unit':''},
                                'mph':{'value':0, 'unit':''},
                                'mph_qsize':{'value':0, 'unit':''},
                                'mpi':{'value':0, 'unit':''},
                                'time_passed':{'value':0, 'unit':''},
                                'time_left':{'value':0, 'unit':''}}
                           }    
                           
        self.delay_time_left = 0
        self.time_left = 0
        self.progress = 0

    def set_test_protocol(self, test_protocol):
        '''set protocol'''
        self.test_protocol = test_protocol

    def set_status(self, infustion_status):
        '''set status'''
        ############################################################################
        # #                         CRITICAL SECTION START                         ##
        #
        # Acquire Mutex
        self.lock.acquire()

        self.status = infustion_status

        # Release Mutex
        self.lock.release()

        #                                                                          #
        # #                         CRITICAL SECTION END                           ##
        ############################################################################

    def set_patient_weight(self, weight):
        '''set patient weight'''
        ############################################################################
        # #                         CRITICAL SECTION START                         ##
        #
        # Acquire Mutex
        self.lock.acquire()

        self.patient_weight = weight

        # Release Mutex
        self.lock.release()

        #                                                                          #
        # #                         CRITICAL SECTION END                           ##
        ############################################################################

    def set_vinf_db(self, vinf_db):
        '''set patient weight'''
        ############################################################################
        # #                         CRITICAL SECTION START                         ##
        #
        # Acquire Mutex
        self.lock.acquire()

        self.vinf_db = vinf_db

        # Release Mutex
        self.lock.release()

        #                                                                          #
        # #                         CRITICAL SECTION END                           ##
        ############################################################################

    def set_vinf_ab(self, vinf_ab):
        '''set patient weight'''
        ############################################################################
        # #                         CRITICAL SECTION START                         ##
        #
        # Acquire Mutex
        self.lock.acquire()

        self.vinf_ab = vinf_ab

        # Release Mutex
        self.lock.release()

        #                                                                          #
        # #                         CRITICAL SECTION END                           ##
        ############################################################################

    def set_vinf_cd(self, vinf):
        '''set patient weight'''
        ############################################################################
        # #                         CRITICAL SECTION START                         ##
        #
        # Acquire Mutex
        self.lock.acquire()

        self.vinf_cd = vinf

        # Release Mutex
        self.lock.release()

        #                                                                          #
        # #                         CRITICAL SECTION END                           ##
        ############################################################################

    def set_time_next_db(self, time_next_db):
        '''set time to next demand bolus'''
        ############################################################################
        # #                         CRITICAL SECTION START                         ##
        #
        # Acquire Mutex
        self.lock.acquire()

        self.time_next_db = time_next_db

        # Release Mutex
        self.lock.release()

        #                                                                          #
        # #                         CRITICAL SECTION END                           ##
        ############################################################################

    def get_rate(self, protocol):
        ''' get infusion rate
            this function converts the infusion rate to ml/hour'''
        switches = protocol['content']['program']['switches']
        rate = 0
        if protocol['content']['deliveryMode'] == 'continuousInfusion':
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
                    if self.patient_weight is None:
                        weight = input("    Input Patient Weight ({0:3.1f} - {1:3.1f} kg): "\
                                .format(weight_lower_limit, weight_upper_limit)) \
                                or (weight_upper_limit - weight_lower_limit) / 2
                        try:
                            self.patient_weight = float(weight)
                        except ValueError:
                            self.patient_weight = 0
                    if self.patient_weight > weight_upper_limit:
                        self.patient_weight = weight_upper_limit
                    elif self.patient_weight < weight_lower_limit:
                        self.patient_weight = weight_lower_limit
                    weight = self.patient_weight
                if rate_unit == 'mg/min':
                    rate = rate * 60 * dilute_volume * 1000 / drug_amount
                if rate_unit == 'mcg/min':
                    rate = rate * 60 * dilute_volume / drug_amount
                if rate_unit == 'mg/kg/min':
                    rate = rate * 60 * dilute_volume * 1000 * weight / drug_amount
                if rate_unit == 'mcg/kg/min':
                    rate = rate * 60 * dilute_volume * weight / drug_amount
            if switches['time'] and switches['vtbi']:
                duration = protocol['content']['program']['time']['value']
                vtbi = protocol['content']['program']['vtbi']['value']
                rate = float(vtbi * 60 / duration)

        if protocol['content']['deliveryMode'] == 'bolusInfusion':
            if switches['basalRate']:
                rate = float(protocol['content']['program']['basalRate']['value'])

        if protocol['content']['deliveryMode'] == 'intermittentInfusion':
            if switches['doseRate']:
                rate = float(protocol['content']['program']['doseRate']['value'])

        return float(rate)

    def get_vtbi(self, protocol):
        '''get vtbi'''
        switches = protocol['content']['program']['switches']
        vtbi = 0
        if protocol['content']['deliveryMode'] == 'continuousInfusion':
            if switches['vtbi']:
                vtbi_str = protocol['content']['program']['vtbi']['value']
                vtbi = float(vtbi_str)
            else:
                rate = self.get_rate(protocol)
                duration = int(protocol['content']['program']['time']['value'])
                vtbi = rate * duration / 60

        if protocol['content']['deliveryMode'] == 'bolusInfusion':
            if switches['vtbi']:
                vtbi_str = protocol['content']['program']['vtbi']['value']
                vtbi = float(vtbi_str)
        if protocol['content']['deliveryMode'] == 'intermittentInfusion':
            pass

        return vtbi
    # def pause(self):
        # '''pause infusion'''
        # self.status = TestStatus.PAUSED
        # self.motor.pause()

    def init_motor(self):
        '''initialize motor'''
        #################################
        # create a motor running thread #
        #################################
        # self.motor = Motor()
        motor_thread = Thread(target=self.motor.run, args=())
        motor_thread.start()
        print('motor.status = [{}]'.format(self.motor.status.name))

    def init_mph_monitor(self):
        '''initialize [max / hr] monitor'''
        ######################################
        # create a [max / hr] monitor thread #
        ######################################
        max_per_hr_monitor_thread = Thread(target=self.run_mph_monitor, args=())
        max_per_hr_monitor_thread.start()

    def init_mpi_monitor(self):
        '''initialize [max / int] monitor'''
        #################################
        # create a [max / int] monitor thread #
        #################################
        max_per_int_monitor_thread = Thread(target=self.run_mpi_monitor, args=())
        max_per_int_monitor_thread.start()

    def init_test_monitor(self):
        '''initialize test monitor'''
        #####################################
        # create an test monitor thread #
        #####################################
        test_monitor = TestMonitor()
        test_monitor_thread = Thread(target=test_monitor.start(), args=([self]))
        test_monitor_thread.start()

    # def init_ab_monitor(self):
        # '''initialize auto bolus monitor'''
        # ########################################
        # # create a auto bolus monitor thread #
        # ########################################

        # ab_monitor_thread = Thread(target=self.run_ab_monitor, args=())
        # ab_monitor_thread.start()

    def init_db_monitor(self):
        '''initialize demand bolus monitor'''
        ########################################
        # create a demand bolus monitor thread #
        ########################################

        db_monitor_thread = Thread(target=self.run_db_monitor, args=())
        db_monitor_thread.start()

    def init_cd_monitor(self):
        '''initialize clinician dose monitor'''

        ###########################################
        # create a clinician dose monitor thread  #
        ###########################################
        cd_monitor_thread = Thread(target=self.run_cd_monitor, args=())
        cd_monitor_thread.start()

    def stop(self):
        '''Stop Infusion'''
        self.motor.set_status(MotorStatus.STOPPED)

    def run_infusion(self):
        '''Run Infusion In A New Thread'''
        if self.status == TestStatus.STOPPED:
            ##############################
            # create a [infusion] thread #
            ##############################
            infusion_thread = Thread(target=self.run, args=())
            infusion_thread.start()
        else:
            print('Aborted: Infusion already running')
    
    def run(self):
        '''run infusion'''
        self.status = TestStatus.RUNNING
        delivery_mode = self.test_protocol['content']['deliveryMode']
        switches = self.test_protocol['content']['program']['switches']
        self.init_motor()
        while self.motor.status != MotorStatus.RUNNING:
            pass
        print("Motor started at [{}]".format(time.strftime('%H:%M:%S', time.localtime())))
        if switches['delayStart']:
            # run infusion delay start
            #
            self.run_delay_start()
        if delivery_mode == 'continuousInfusion':
            # run infusion in continuous mode
            #
            self.run_cont()
        if delivery_mode == 'bolusInfusion':
            # run infusion in bolus mode
            #
            # run mph check
            self.init_mph_monitor()
            # run mpi check
            self.init_mpi_monitor()
            # # run auto bolus monitor
            # self.init_ab_monitor()
            # run demand bolus monitor
            self.init_db_monitor()
            # run clinician dose monitor
            self.init_cd_monitor()
            # run loading dose
            self.run_loading_dose()
            # run bolus
            self.run_bolus()
        if delivery_mode == 'intermittentInfusion':
            # run infusion in intermittent mode
            #
            self.run_int()
        # Reset Infusion        
        self.reset()

    def run_mph_monitor(self):
        '''run [max per hour] monitor'''
        try:
            time_passed_ab = 0
            motor = self.motor
            start_time = time.strftime('%H:%M:%S', time.localtime())
            print("[max/hr] check started at [{}]".format(start_time))
            #
            switches = self.test_protocol['content']['program']['switches']
            if switches['maxAmountPerHour']:
                max_amount_per_hour = \
                        self.test_protocol['content']['program']['maxAmountPerHour']['value']
                while motor.status != MotorStatus.STOPPED:
                    if motor.status == MotorStatus.RUNNING \
                            and self.status != TestStatus.RUNNING_CLINICIAN_DOSE:
                        if motor.mph > max_amount_per_hour + _MPH_MARGIN:
                            current = time.strftime('%H:%M:%S', time.localtime())
                            print()
                            print("infusion paused at [{0}]: MPH limit Reached [{1} mL/hr]"\
                                    .format(current, max_amount_per_hour))
                            # log the time_passed_ab when infusion paused on MPH
                            time_passed_ab = self.motor.time_passed_ab
                            motor.set_status(MotorStatus.PAUSED)
                            self.previous_status = self.status
                            self.status = TestStatus.PAUSED_MPH_REACHED
                            motor.set_previous_rate(motor.rate)
                            print()
                            print('line {0}: motor.set_rate({1:.2f}) [{2}]'\
                                    .format(get_line_number(), 0, \
                                    time.strftime('%H:%M:%S', time.localtime())))
                            motor.set_rate(0)
                    elif motor.status == MotorStatus.PAUSED and \
                                self.status == TestStatus.PAUSED_MPH_REACHED:
                        if motor.mph < max_amount_per_hour - _MPH_MARGIN:
                            current = time.strftime('%H:%M:%S', time.localtime())
                            print()
                            print("mph infusion resumed at [{0}]".format(current))
                            # restore the motor time_passed_ab
                            motor.set_time_passed_ab(time_passed_ab)
                            #
                            motor.set_status(MotorStatus.RUNNING)
                            # self.status = TestStatus.RUNNING
                            self.status = self.previous_status
                            print()
                            print('line {0}: motor.set_rate({1:.2f}) [{2}]'\
                                    .format(get_line_number(), motor.previous_rate, \
                                    time.strftime('%H:%M:%S', time.localtime())))
                            motor.set_rate(motor.previous_rate)
                            
                    time.sleep(_REFRESH_TIMER * 10)
            #
            print("[max/hr] check stopped at [{}]"\
                    .format(time.strftime('%H:%M:%S', time.localtime())))
        except KeyboardInterrupt:
            print()
            print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))
        except AttributeError:
            print()
            print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))
        except OSError:
            print()
            print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))

    def run_mpi_monitor(self):
        '''run [max per interval] monitor'''
        try:
            motor = self.motor
            start_time = time.strftime('%H:%M:%S', time.localtime())
            print("[max/int] check started at [{}]".format(start_time))
            #
            switches = self.test_protocol['content']['program']['switches']
            if switches['maxAmountPerInterval']:
                max_amount_per_interval = \
                        self.test_protocol['content']['program']['maxAmountPerInterval']['value']
                while motor.status != MotorStatus.STOPPED:
                    if motor.status == MotorStatus.RUNNING \
                            and self.status != TestStatus.RUNNING_CLINICIAN_DOSE:
                        if motor.mpi > max_amount_per_interval:
                            current = time.strftime('%H:%M:%S', time.localtime())
                            print()
                            print("infusion paused at [{0}]: MPI limit Reached [{1} mL/int]"\
                                .format(current, max_amount_per_interval))
                            motor.set_status(MotorStatus.PAUSED)
                            self.previous_status = self.status
                            self.status = TestStatus.PAUSED_MPI_REACHED
                            print()
                            print('line {0}: motor.set_rate({1:.2f}) [{2}]'\
                                    .format(get_line_number(), 0, \
                                    time.strftime('%H:%M:%S', time.localtime())))
                            motor.set_rate(0)
                    time.sleep(_REFRESH_TIMER * 10)
            #
            print("[max/int] check stopped at [{}]"\
                    .format(time.strftime('%H:%M:%S', time.localtime())))
        except KeyboardInterrupt:
            print()
            print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))
        except AttributeError:
            print()
            print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))
        except OSError:
            print()
            print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))
    
    def run_db_monitor(self):
        '''run demand bolus monitor'''
        basal_rate = self.get_rate(self.test_protocol)
        vtbi = self.get_vtbi(self.test_protocol)
        try:
            motor = self.motor
            db_volume = 0
            db_lock = 0
            db_duration = 0
            #
            ab_volume = 0
            # ab_interval = 0
            ab_duration = 0
            delivery_mode = self.test_protocol['content']['deliveryMode']
            switches = self.test_protocol['content']['program']['switches']
            if delivery_mode == 'bolusInfusion' and switches['autoBolusAmount']:
                ab_volume = self.test_protocol['content']['program']['autoBolusAmount']['value']
                # ab_interval = self.test_protocol['content']['program']['bolusInterval']['value']
            if delivery_mode == 'bolusInfusion' and switches['demandBolusAmount']:
                db_volume = self.test_protocol['content']['program']['demandBolusAmount']['value']
                db_lock = 60 * self.test_protocol['content']['program']['lockoutTime']['value']
                while motor.status != MotorStatus.STOPPED and db_volume > 0:
                    if self.status == TestStatus.RUNNING:
                        if ab_duration > 0 \
                                and motor.time_passed_ab <= ab_duration + db_lock:
                            # Auto Bolus has finished but DB Lock time has NOT passed
                            time_next_db = db_lock + ab_duration - motor.time_passed_ab
                            self.set_time_next_db(time_next_db)
                        elif ab_duration > 0:
                            # Auto Bolus has finished and DB Lockout time has passed 
                            self.set_time_next_db(0)
                            self.db_enabled = True
                            ab_duration = 0
                        if db_duration > 0 \
                                and motor.time_passed_db <= db_duration + db_lock:
                            # Demand Bolus has finished but DB Lock time has NOT passed
                            time_next_db = db_lock + db_duration - motor.time_passed_db
                            self.set_time_next_db(time_next_db)
                        elif db_duration > 0:
                            # Demand Bolus has finished and DB Lock time has passed
                            self.set_time_next_db(0)
                            self.db_enabled = True
                            db_duration = 0
                    if self.status == TestStatus.RUNNING_DEMAND_BOLUS:
                        progress_db = math.ceil(1000 * self.vinf_db / db_volume) / 10 \
                                if self.vinf_db < db_volume else 100.0
                        if progress_db < 100:
                            # Demand Bolus is on going
                            self.vinf_db = motor.vinf_db
                            # Set Demand Bolus duration
                            db_duration = motor.time_passed_db
                        elif progress_db >= 100.0:
                            progress_db = 100.0
                            print()
                            print('line {0}: motor.set_rate({1:.2f}) [{2}]'\
                                    .format(get_line_number(), basal_rate, \
                                    time.strftime('%H:%M:%S', time.localtime())))
                            motor.set_rate(basal_rate)
                            self.status = TestStatus.RUNNING
                            self.vinf_db = db_volume
                            continue
                        if motor.vinf >= vtbi:
                            # Infusion shall terminate
                            motor.set_status(MotorStatus.STOPPED)
                            continue
                    if self.status == TestStatus.RUNNING_AUTO_BOLUS:
                        progress_ab = math.ceil(1000 * self.vinf_ab / ab_volume) / 10 \
                                if self.vinf_ab < ab_volume else 100.0
                        if progress_ab < 100:
                            # Auto Bolus is on going
                            # Set Auto Bolus duration
                            ab_duration = motor.time_passed_ab
                        elif progress_ab > 100.0:
                            progress_ab = 100.0
                            continue
                    time.sleep(_REFRESH_TIMER)
            print()
            print("db monitor stopped at [{}]".format(time.strftime('%H:%M:%S', time.localtime())))
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

    def run_cd_monitor(self):
        '''run clinician dose monitor'''
        basal_rate = self.get_rate(self.test_protocol)
        vtbi = self.get_vtbi(self.test_protocol)
        try:
            motor = self.motor
            cd_volume = 0
            delivery_mode = self.test_protocol['content']['deliveryMode']
            switches = self.test_protocol['content']['program']['switches']
            if delivery_mode == 'bolusInfusion' and switches['clinicianDose']:
                cd_volume = self.test_protocol['content']['program']['clinicianDose']['value']
                while motor.status != MotorStatus.STOPPED:
                    if self.cd_tempt and cd_volume > 0:
                        progress_cd = 0
                        while motor.status != MotorStatus.STOPPED \
                                and self.status == TestStatus.RUNNING_CLINICIAN_DOSE:
                            if progress_cd < 100:
                                self.vinf_cd = motor.vinf_cd
                                progress_cd = math.ceil(1000 * self.vinf_cd / cd_volume) / 10 \
                                    if self.vinf_cd < cd_volume else 100.0
                            if progress_cd >= 100.0:
                                # Clinician Dose has finished
                                progress_cd = 100.0
                                print()
                                print('line {0}: motor.set_rate({1:.2f}) [{2}]'\
                                        .format(get_line_number(), basal_rate, \
                                        time.strftime('%H:%M:%S', time.localtime())))
                                motor.set_rate(basal_rate)
                                self.status = TestStatus.RUNNING
                                self.vinf_cd = cd_volume
                                break
                            if motor.vinf >= vtbi:
                                # Infusion shall terminate
                                motor.set_status(MotorStatus.STOPPED)
                                break
                            time.sleep(_REFRESH_TIMER)
                        self.cd_tempt = False
                        self.cd_enabled = True
                    time.sleep(_REFRESH_TIMER)
            print()
            print("cd monitor stopped at [{}]".format(time.strftime('%H:%M:%S', time.localtime())))
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

    def run_loading_dose(self):
        '''run loading dose'''
        ld_volume = 0
        ab_volume = 0
        cd_volume = 0
        ab_interval = 0
        switches = self.test_protocol['content']['program']['switches']
        if switches['loadingDoseAmount']:
            ld_volume = self.test_protocol['content']['program']['loadingDoseAmount']['value']
        if switches['autoBolusAmount']:
            ab_volume = self.test_protocol['content']['program']['autoBolusAmount']['value']
            ab_interval = 60 * self.test_protocol['content']['program']['bolusInterval']['value']
        if switches['demandBolusAmount']:
            db_volume = self.test_protocol['content']['program']['demandBolusAmount']['value']
        if switches['clinicianDose']:
            cd_volume = self.test_protocol['content']['program']['clinicianDose']['value']
        basal_rate = self.get_rate(self.test_protocol)
        vtbi = self.get_vtbi(self.test_protocol)
        print("Converted Parameters:")
        print("basal rate = {} mL/hr".format(basal_rate))
        print("vtbi = {} mL".format(vtbi))
        try:
            motor = self.motor
            # run loading dose
            if ld_volume > 0 and motor.vinf <= vtbi and motor.status == MotorStatus.RUNNING:
                motor.set_rate_basal(basal_rate)
                print('line {0}: motor.set_rate({1:.2f}) [{2}]'\
                        .format(get_line_number(), _BOLUS_RATE, \
                        time.strftime('%H:%M:%S', time.localtime())))
                motor.set_rate(_BOLUS_RATE)
                motor.set_vinf_ab(0)
                motor.set_time_passed_ab(0)
                motor.set_mpi(0)
                motor.set_mph(0)
                motor.mph_queue.queue.clear()
                self.status = TestStatus.RUNNING_LOADING_DOSE
                while motor.status != MotorStatus.STOPPED:
                    if motor.vinf_ab <= ab_volume and motor.time_passed_ab < ab_interval:
                        self.vinf_ab = motor.vinf_ab
                    if motor.vinf_ab > ld_volume and motor.time_passed_ab < ab_interval:
                        # infuse with basal rate till the end
                        if motor.status == MotorStatus.RUNNING and \
                            self.status == TestStatus.RUNNING_LOADING_DOSE and \
                            not self.db_tempt:
                            # The Laoding dose is delivered
                            # infuse will continue with basal rate till the ab interval is finished
                            print()
                            print("Laoding dose is delivered at [{}]".format(\
                                    time.strftime('%H:%M:%S', time.localtime())))
                            print()
                            print('line {0}: motor.set_rate({1:.2f}) [{2}]'\
                                    .format(get_line_number(), basal_rate, \
                                    time.strftime('%H:%M:%S', time.localtime())))
                            motor.set_rate(basal_rate)
                            self.vinf_ab = ld_volume
                            self.status = TestStatus.RUNNING
                    if motor.time_passed_ab >= ab_interval and motor.vinf < vtbi:
                        # The current ab interval is finished
                        if motor.status == MotorStatus.RUNNING:
                            # The infusion is still RUNNING
                            # The loading dose section shall terminate
                            print()
                            print('line {0}: motor.set_rate({1:.2f}) [{2}]'\
                                    .format(get_line_number(), basal_rate, \
                                    time.strftime('%H:%M:%S', time.localtime())))
                            motor.set_rate(basal_rate)
                            self.status = TestStatus.RUNNING
                            break
                        if self.status == TestStatus.PAUSED_MPH_REACHED:
                            # The infusion is on MPH PAUSE
                            # The loading dose infusion loope shall continue
                            motor.set_time_passed_ab(0)
                        if self.status == TestStatus.PAUSED_MPI_REACHED:
                            # The infusion is on MPI PAUSE
                            current = time.strftime('%H:%M:%S', time.localtime())
                            print()
                            print("loading dose end at [{0}]".format(current))
                            # The loading dose section shall terminate
                            print()
                            print('line {0}: motor.set_rate({1:.2f}) [{2}]'\
                                    .format(get_line_number(), basal_rate, \
                                    time.strftime('%H:%M:%S', time.localtime())))
                            motor.set_rate(basal_rate)
                            motor.set_status(MotorStatus.RUNNING)
                            self.status = TestStatus.RUNNING
                            break
                    if motor.vinf >= vtbi:
                        # Infusion shall terminate
                        motor.set_status(MotorStatus.STOPPED)
                        break
                    volume_left = vtbi - motor.vinf if vtbi > motor.vinf else 0
                    progress = math.ceil(1000 * motor.vinf / vtbi) / 10
                    #
                    # time_left_ab = time.strftime('%H:%M:%S', \
                    #         time.gmtime(ab_interval - motor.time_passed_ab))
                    progress_ld = math.ceil(1000 * motor.vinf_ab / ld_volume) / 10 \
                            if motor.vinf_ab < ld_volume else 100.0
                    #
                    if switches['demandBolusAmount']:
                        progress_db = math.ceil(1000 * self.vinf_db / db_volume) / 10 \
                                if self.vinf_db < db_volume else 100.0
                    #
                    if switches['clinicianDose']:
                        progress_cd = math.ceil(1000 * self.vinf_cd / cd_volume) / 10 \
                                if self.vinf_cd < cd_volume else 100.0
                    #
                    # time_passed = time.strftime('%H:%M:%S', time.gmtime(motor.time_passed))
                    #
                    if motor.rate == 0:
                        time_left = None
                    else:
                        time_left = int(3600 * volume_left / motor.rate)
                    #
                    self.parameters['bolus']['rate']['value'] = motor.rate
                    self.parameters['bolus']['rate']['unit'] = 'ml/h'
                    self.parameters['bolus']['vinf']['value'] = motor.vinf
                    self.parameters['bolus']['vinf']['unit'] = 'ml'
                    self.parameters['bolus']['vtbi']['value'] = volume_left
                    self.parameters['bolus']['vtbi']['unit'] = 'ml'
                    self.parameters['bolus']['progress']['value'] = progress
                    self.parameters['bolus']['progress']['unit'] = '%'
                    if switches['loadingDoseAmount']:
                        self.parameters['bolus']['vinf_ld']['value'] = self.vinf_ab
                        self.parameters['bolus']['vinf_ld']['unit'] = 'ml'
                        self.parameters['bolus']['next_ab']['value'] = ab_interval - motor.time_passed_ab
                        self.parameters['bolus']['next_ab']['unit'] = 'sec'
                        self.parameters['bolus']['progress_ld']['value'] = progress_ld
                        self.parameters['bolus']['progress_ld']['unit'] = '%'
                    if switches['demandBolusAmount']:
                        self.parameters['bolus']['vinf_db']['value'] = self.vinf_db
                        self.parameters['bolus']['vinf_db']['unit'] = 'ml'
                        self.parameters['bolus']['next_db']['value'] = self.time_next_db
                        self.parameters['bolus']['next_db']['unit'] = 'sec'
                        self.parameters['bolus']['progress_db']['value'] = progress_db
                        self.parameters['bolus']['progress_db']['unit'] = '%'
                    if switches['clinicianDose'] \
                            and self.status == TestStatus.RUNNING_CLINICIAN_DOSE:
                        self.parameters['bolus']['vinf_cd']['value'] = self.vinf_cd
                        self.parameters['bolus']['vinf_cd']['unit'] = 'ml'
                        self.parameters['bolus']['progress_cd']['value'] = progress_cd
                        self.parameters['bolus']['progress_cd']['unit'] = '%'
                    if switches['maxAmountPerHour'] \
                            and self.status == TestStatus.PAUSED_MPH_REACHED:
                        self.parameters['bolus']['mph']['value'] = motor.mph
                        self.parameters['bolus']['mph']['unit'] = 'ml'
                        self.parameters['bolus']['mph_qsize']['value'] = motor.mph_queue.qsize()
                        self.parameters['bolus']['mph_qsize']['unit'] = ''
                    if switches['maxAmountPerInterval'] \
                            and self.status == TestStatus.PAUSED_MPI_REACHED:
                        self.parameters['bolus']['mpi']['value'] = motor.mpi
                        self.parameters['bolus']['mpi']['unit'] = 'ml'
                    self.parameters['bolus']['time_passed']['value'] = motor.time_passed
                    self.parameters['bolus']['time_passed']['unit'] = 'sec'
                    self.parameters['bolus']['time_left']['value'] = time_left
                    self.parameters['bolus']['time_left']['unit'] = 'sec'
                    #
                    time.sleep(_REFRESH_TIMER)
            print()
        except KeyboardInterrupt:
            print()
        except AttributeError:
            print()
            print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))
        except OSError:
            print()
            print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))

    def run_bolus(self):
        '''run bolus mode'''
        ab_volume = 0
        ab_interval = 0
        switches = self.test_protocol['content']['program']['switches']
        if switches['autoBolusAmount']:
            ab_volume = self.test_protocol['content']['program']['autoBolusAmount']['value']
            ab_interval = 60 * self.test_protocol['content']['program']['bolusInterval']['value']
        if switches['demandBolusAmount']:
            db_volume = self.test_protocol['content']['program']['demandBolusAmount']['value']
            # db_lock = 60 * self.test_protocol['content']['program']['lockoutTime']['value']
        if switches['clinicianDose']:
            cd_volume = self.test_protocol['content']['program']['clinicianDose']['value']
        basal_rate = self.get_rate(self.test_protocol)
        vtbi = self.get_vtbi(self.test_protocol)
        try:
            motor = self.motor
            # run auto bolus
            if ab_volume > 0:
                print()
                print('line {0}: motor.set_rate({1:.2f}) [{2}]'\
                        .format(get_line_number(), _BOLUS_RATE, \
                        time.strftime('%H:%M:%S', time.localtime())))
                motor.set_rate(_BOLUS_RATE)
                self.status = TestStatus.RUNNING_AUTO_BOLUS
            else:
                print()
                print('line {0}: motor.set_rate({1:.2f}) [{2}]'\
                        .format(get_line_number(), basal_rate, \
                        time.strftime('%H:%M:%S', time.localtime())))
                motor.set_rate(basal_rate)
                self.status = TestStatus.RUNNING
            motor.set_rate_basal(basal_rate)
            motor.set_vinf_ab(0)
            motor.set_time_passed_ab(0)
            motor.set_mpi(0)
            while motor.vinf <= vtbi and motor.status != MotorStatus.STOPPED:
                if ab_volume > 0 and motor.vinf_ab <= ab_volume and \
                        motor.time_passed_ab < ab_interval:
                    # Auto Bolus is on going
                    self.vinf_ab = motor.vinf_ab
                if ab_volume > 0 and motor.vinf_ab > ab_volume and \
                            motor.time_passed_ab < ab_interval:
                    # Auto Bolus is delivered
                    if motor.status == MotorStatus.RUNNING and \
                            self.status == TestStatus.RUNNING_AUTO_BOLUS and \
                            not self.db_tempt:
                        # Infusion will continue with Basal Rate till the end
                        print()
                        print("Auto bolus is delivered at [{}]".format(\
                                time.strftime('%H:%M:%S', time.localtime())))
                        print()
                        print('line {0}: motor.set_rate({1:.2f}) [{2}]'\
                                .format(get_line_number(), basal_rate, \
                                time.strftime('%H:%M:%S', time.localtime())))
                        motor.set_rate(basal_rate)
                        self.vinf_ab = ab_volume
                        self.status = TestStatus.RUNNING
                if ab_volume > 0 and motor.time_passed_ab >= ab_interval:
                    if motor.status == MotorStatus.RUNNING:
                        # Auto Bolus Interval is passed
                        # Auto Bolus cycle should restart
                        #
                        if ab_volume > 0:
                            print()
                            print('line {0}: motor.set_rate({1:.2f}) [{2}]'\
                                    .format(get_line_number(), _BOLUS_RATE, \
                                    time.strftime('%H:%M:%S', time.localtime())))
                            motor.set_rate(_BOLUS_RATE)
                            self.status = TestStatus.RUNNING_AUTO_BOLUS
                        else:
                            print()
                            print('line {0}: motor.set_rate({1:.2f}) [{2}]'\
                                    .format(get_line_number(), basal_rate, \
                                    time.strftime('%H:%M:%S', time.localtime())))
                            motor.set_rate(basal_rate)
                            self.status = TestStatus.RUNNING
                        motor.set_vinf_ab(0)
                        motor.set_time_passed_ab(0)
                        motor.set_mpi(0)
                        continue
                    if self.status == TestStatus.PAUSED_MPI_REACHED:
                        # auto bolus cycle should restart
                        current = time.strftime('%H:%M:%S', time.localtime())
                        print()
                        print("mpi infusion resumed at [{0}]".format(current))
                        motor.set_status(MotorStatus.RUNNING)
                        if ab_volume > 0:
                            print()
                            print('line {0}: motor.set_rate({1:.2f}) [{2}]'\
                                    .format(get_line_number(), _BOLUS_RATE, \
                                    time.strftime('%H:%M:%S', time.localtime())))
                            motor.set_rate(_BOLUS_RATE)
                            self.status = TestStatus.RUNNING_AUTO_BOLUS
                        else:
                            print()
                            print('line {0}: motor.set_rate({1:.2f}) [{2}]'\
                                    .format(get_line_number(), basal_rate, \
                                    time.strftime('%H:%M:%S', time.localtime())))
                            motor.set_rate(basal_rate)
                            self.status = TestStatus.RUNNING
                        motor.set_vinf_ab(0)
                        motor.set_time_passed_ab(0)
                        motor.set_mpi(0)
                        continue
                    if self.status == TestStatus.PAUSED_MPH_REACHED:
                        # auto bolus loop shall continue to wait
                        motor.set_time_passed_ab(0)
                if motor.vinf > vtbi:
                    # Motor should Stop
                    motor.vinf = vtbi
                    motor.set_status(MotorStatus.STOPPED)
                    continue
                volume_left = vtbi - motor.vinf if vtbi > motor.vinf else 0
                progress = math.ceil(1000 * motor.vinf / vtbi) / 10
                # time_left_ab = time.strftime('%H:%M:%S', \
                #        time.gmtime(ab_interval - motor.time_passed_ab))
                progress_ab = math.ceil(1000 * self.vinf_ab / ab_volume) / 10 \
                        if motor.vinf_ab < ab_volume else 100.0
                #
                if switches['demandBolusAmount']:
                    progress_db = math.ceil(1000 * self.vinf_db / db_volume) / 10 \
                            if self.vinf_db < db_volume else 100.0
                #
                if switches['clinicianDose']:
                    progress_cd = math.ceil(1000 * self.vinf_cd / cd_volume) / 10 \
                            if self.vinf_cd < cd_volume else 100.0
                # time_passed = time.strftime('%H:%M:%S', time.gmtime(motor.time_passed))
                #
                if motor.rate == 0:
                    time_left = None
                else:
                    time_left = int(3600 * volume_left / motor.rate)
                # Update Infusion Parameters
                self.parameters['bolus']['rate']['value'] = motor.rate
                self.parameters['bolus']['rate']['unit'] = 'ml/h'
                self.parameters['bolus']['vinf']['value'] = motor.vinf
                self.parameters['bolus']['vinf']['unit'] = 'ml'
                self.parameters['bolus']['vtbi']['value'] = volume_left
                self.parameters['bolus']['vtbi']['unit'] = 'ml'
                self.parameters['bolus']['progress']['value'] = progress
                self.parameters['bolus']['progress']['unit'] = '%'
                if switches['autoBolusAmount'] \
                        and self.status == TestStatus.RUNNING_AUTO_BOLUS:
                    self.parameters['bolus']['vinf_ab']['value'] = self.vinf_ab
                    self.parameters['bolus']['vinf_ab']['unit'] = 'ml'
                    self.parameters['bolus']['next_ab']['value'] = ab_interval - motor.time_passed_ab
                    self.parameters['bolus']['next_ab']['unit'] = 'sec'
                    self.parameters['bolus']['progress_ab']['value'] = progress_ab
                    self.parameters['bolus']['progress_ab']['unit'] = '%'
                elif switches['autoBolusAmount']:
                    self.parameters['bolus']['next_ab']['value'] = ab_interval - motor.time_passed_ab
                    self.parameters['bolus']['next_ab']['unit'] = 'sec'
                if switches['demandBolusAmount'] \
                        and self.status == TestStatus.RUNNING_DEMAND_BOLUS:
                    self.parameters['bolus']['vinf_db']['value'] = self.vinf_db
                    self.parameters['bolus']['vinf_db']['unit'] = 'ml'
                    self.parameters['bolus']['next_db']['value'] = self.time_next_db
                    self.parameters['bolus']['next_db']['unit'] = 'sec'
                    self.parameters['bolus']['progress_db']['value'] = progress_db
                    self.parameters['bolus']['progress_db']['unit'] = '%'
                elif switches['demandBolusAmount']:
                    self.parameters['bolus']['next_db']['value'] = self.time_next_db
                    self.parameters['bolus']['next_db']['unit'] = 'sec'
                if switches['clinicianDose'] \
                        and self.status == TestStatus.RUNNING_CLINICIAN_DOSE:
                    self.parameters['bolus']['vinf_cd']['value'] = self.vinf_cd
                    self.parameters['bolus']['vinf_cd']['unit'] = 'ml'
                    self.parameters['bolus']['progress_cd']['value'] = progress_cd
                    self.parameters['bolus']['progress_cd']['unit'] = '%'
                if switches['maxAmountPerHour'] \
                        and self.status == TestStatus.PAUSED_MPH_REACHED:
                    self.parameters['bolus']['mph']['value'] = motor.mph
                    self.parameters['bolus']['mph']['unit'] = 'ml'
                    self.parameters['bolus']['mph_qsize']['value'] = motor.mph_queue.qsize()
                    self.parameters['bolus']['mph_qsize']['unit'] = ''
                if switches['maxAmountPerInterval'] \
                        and self.status == TestStatus.PAUSED_MPI_REACHED:
                    self.parameters['bolus']['mpi']['value'] = motor.mpi
                    self.parameters['bolus']['mpi']['unit'] = 'ml'
                self.parameters['bolus']['time_passed']['value'] = motor.time_passed
                self.parameters['bolus']['time_passed']['unit'] = 'sec'
                self.parameters['bolus']['time_left']['value'] = time_left
                self.parameters['bolus']['time_left']['unit'] = 'sec'
                #
                time.sleep(_REFRESH_TIMER)
            duration = time.strftime('%H:%M:%S', time.gmtime(motor.time_passed))
            print()
            print("Infusion simulator finished at [{}]"\
                    .format(time.strftime('%H:%M:%S', time.localtime())))
            print('Expected duration: [{}] (Bolus Mode)'.format(duration))
        except KeyboardInterrupt:
            print()
            print('line {0}: Motor Stopped'.format(get_line_number()))
            motor.set_status(MotorStatus.STOPPED)
        except (AttributeError, NameError, OSError):
            print()
            print('line {0}: Motor Stopped'.format(get_line_number()))
            motor.set_status(MotorStatus.STOPPED)
            print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))

    def run_cont(self):
        '''run coninuous mode'''
        rate = self.get_rate(self.test_protocol)
        vtbi = self.get_vtbi(self.test_protocol)
        print("Converted Parameters:")
        print("rate = {} mL/hr".format(rate))
        print("vtbi = {} mL".format(vtbi))
        try:
            motor = self.motor
            self.status = TestStatus.RUNNING
            print('line {0}: motor.set_rate({1:.2f}) [{2}]'\
                    .format(get_line_number(), rate, \
                    time.strftime('%H:%M:%S', time.localtime())))
            motor.set_rate(rate)
            motor.set_mph(0)
            motor.mph_queue.queue.clear()
            while motor.vinf <= vtbi and motor.status != MotorStatus.STOPPED:
                progress = math.ceil(1000 * motor.vinf / vtbi) / 10
                # time_passed = time.strftime('%H:%M:%S', time.gmtime(motor.time_passed))
                volume_left = vtbi - motor.vinf if vtbi > motor.vinf else 0
                if rate > 0:
                    # time_left = time.strftime('%H:%M:%S', \
                    #        time.gmtime(3600 * volume_left / motor.rate))
                    pass
                else:
                    print('infusion aborted: rate = {} '.format(rate))
                    break
                #
                # Update Infusion Parameters
                self.parameters['cont']['rate']['value'] = motor.rate
                self.parameters['cont']['rate']['unit'] = 'ml/h'
                self.parameters['cont']['vinf']['value'] = motor.vinf
                self.parameters['cont']['vinf']['unit'] = 'ml'
                self.parameters['cont']['vtbi']['value'] = volume_left
                self.parameters['cont']['vtbi']['unit'] = 'ml'
                self.parameters['cont']['progress']['value'] = progress
                self.parameters['cont']['progress']['unit'] = '%'
                self.parameters['cont']['time_passed']['value'] = motor.time_passed
                self.parameters['cont']['time_passed']['unit'] = 'sec'
                self.parameters['cont']['time_left']['value'] = int(3600 * volume_left / motor.rate)
                self.parameters['cont']['time_left']['unit'] = 'sec'
                #
                time.sleep(_REFRESH_TIMER)
            duration = time.strftime('%H:%M:%S', time.gmtime(motor.time_passed))
            print()
            print("Infusion simulator finished at [{}]"\
                    .format(time.strftime('%H:%M:%S', time.localtime())))
            print('Expected duration: [{}] (Continuous Mode)'.format(duration))
        except KeyboardInterrupt:
            print()
            print('line {0}: Motor Stopped'.format(get_line_number()))
            motor.set_status(MotorStatus.STOPPED)
        except (TypeError, OSError):
            print()
            print('line {0}: Motor Stopped'.format(get_line_number()))
            motor.set_status(MotorStatus.STOPPED)
            print()
            print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))

    def run_int(self):
        '''run intermittent mode'''
        dose_rate = 0
        dose_volume = 0
        dose_interval = 0
        total_time = 0
        int_kvo_rate = 0
        # kvo_rate = 0

        switches = self.test_protocol['content']['program']['switches']
        if switches['doseRate']:
            dose_rate = self.test_protocol['content']['program']['doseRate']['value']
        if switches['doseVtbi']:
            dose_volume = self.test_protocol['content']['program']['doseVtbi']['value']
        if switches['intervalTime']:
            dose_interval = 60 * self.test_protocol['content']['program']['intervalTime']['value']
        if switches['totalTime']:
            total_time = 60 * self.test_protocol['content']['program']['totalTime']['value']
        if switches['intermittentKvoRate']:
            int_kvo_rate = self.test_protocol['content']['program']['intermittentKvoRate']['value']
        if switches['kvoRate']:
            # kvo_rate = self.test_protocol['content']['program']['kvoRate']['value']
            pass

        try:
            motor = self.motor
            # run intermittent
            if dose_volume > 0:
                print()
                print('line {0}: motor.set_rate({1:.2f}) [{2}]'\
                        .format(get_line_number(), dose_rate, \
                        time.strftime('%H:%M:%S', time.localtime())))
                motor.set_rate(dose_rate)
                self.status = TestStatus.RUNNING_INT
            else:
                print()
                print('line {0}: motor.set_rate({1:.2f}) [{2}]'\
                        .format(get_line_number(), int_kvo_rate, \
                        time.strftime('%H:%M:%S', time.localtime())))
                motor.set_rate(int_kvo_rate)
                self.status = TestStatus.RUNNING_INT_KVO
            motor.set_vinf(0)
            motor.set_vinf_dose(0)
            motor.set_time_passed_id(0)
            motor.set_mpi(0)
            motor.set_mph(0)
            motor.mph_queue.queue.clear()
            while motor.time_passed <= total_time and motor.status != MotorStatus.STOPPED:
                if motor.vinf_dose <= dose_volume and motor.time_passed_id < dose_interval:
                    # intermittent dose is not delivered yet
                    self.vinf_dose = motor.vinf_dose
                if motor.vinf_dose > dose_volume and motor.time_passed_id < dose_interval:
                    # infuse with intermittent kvo rate till the end
                    if motor.status == MotorStatus.RUNNING \
                            and self.status == TestStatus.RUNNING_INT:
                        # intermittent dose is delivered
                        # infuse will continue with intermittent kvo rate
                        print()
                        print('line {0}: motor.set_rate({1:.2f}) [{2}]'\
                                .format(get_line_number(), int_kvo_rate, \
                                time.strftime('%H:%M:%S', time.localtime())))
                        motor.set_rate(int_kvo_rate)
                        self.status = TestStatus.RUNNING_INT_KVO
                        self.vinf_dose = dose_volume
                if motor.time_passed_id >= dose_interval:
                    if motor.status == MotorStatus.RUNNING:
                        # intermittent cycle should restart
                        #
                        if dose_volume > 0:
                            print()
                            print('line {0}: motor.set_rate({1:.2f}) [{2}]'\
                                    .format(get_line_number(), dose_rate, \
                                    time.strftime('%H:%M:%S', time.localtime())))
                            motor.set_rate(dose_rate)
                            self.status = TestStatus.RUNNING_INT
                        else:
                            print()
                            print('line {0}: motor.set_rate({1:.2f}) [{2}]'\
                                    .format(get_line_number(), int_kvo_rate, \
                                    time.strftime('%H:%M:%S', time.localtime())))
                            motor.set_rate(int_kvo_rate)
                            self.status = TestStatus.RUNNING_INT_KVO
                        motor.set_vinf_dose(0)
                        motor.set_time_passed_id(0)
                        motor.set_mpi(0)
                        continue
                    if self.status == TestStatus.PAUSED_MPI_REACHED:
                        # intermittent cycle should restart
                        current = time.strftime('%H:%M:%S', time.localtime())
                        print()
                        print("intermittent dose resumed at [{0}]".format(current))
                        motor.set_status(MotorStatus.RUNNING)
                        #
                        if dose_volume > 0:
                            print()
                            print('line {0}: motor.set_rate({1:.2f}) [{2}]'\
                                    .format(get_line_number(), dose_rate, \
                                    time.strftime('%H:%M:%S', time.localtime())))
                            motor.set_rate(dose_rate)
                            self.status = TestStatus.RUNNING_INT
                        else:
                            print()
                            print('line {0}: motor.set_rate({1:.2f}) [{2}]'\
                                    .format(get_line_number(), int_kvo_rate, \
                                    time.strftime('%H:%M:%S', time.localtime())))
                            motor.set_rate(int_kvo_rate)
                            self.status = TestStatus.RUNNING_INT_KVO
                        motor.set_vinf_ab(0)
                        motor.set_time_passed_ab(0)
                        motor.set_mpi(0)
                        continue
                    if self.status == TestStatus.PAUSED_MPH_REACHED:
                        # intermittent dose loop shall continue to wait
                        motor.set_time_passed_id(0)
                if motor.time_passed > total_time:
                    # infusion shall finish
                    motor.set_time_passed(total_time)
                    continue
                progress = math.ceil(1000 * motor.time_passed / total_time) / 10
                time_left_dose = int(dose_interval - motor.time_passed_id)
                progress_dose = math.ceil(1000 * self.vinf_dose / dose_volume) / 10 \
                        if motor.vinf_dose < dose_volume else 100.0
                time_left = total_time - motor.time_passed \
                        if total_time > motor.time_passed else 0
                # Update Infusion Parameters
                self.parameters['int']['rate']['value'] = motor.rate
                self.parameters['int']['rate']['unit'] = 'ml/h'
                self.parameters['int']['vinf']['value'] = motor.vinf
                self.parameters['int']['vinf']['unit'] = 'ml'
                self.parameters['int']['progress']['value'] = progress
                self.parameters['int']['progress']['unit'] = '%'
                if switches['doseVtbi'] and self.status == TestStatus.RUNNING_INT:
                    self.parameters['int']['vinf_dose']['value'] = self.vinf_dose
                    self.parameters['int']['vinf_dose']['unit'] = 'ml'
                    self.parameters['int']['next_dose']['value'] = time_left_dose
                    self.parameters['int']['next_dose']['unit'] = 'sec'
                    self.parameters['int']['progress_dose']['value'] = progress_dose
                    self.parameters['int']['progress_dose']['unit'] = '%'
                elif switches['doseVtbi'] and self.status == TestStatus.RUNNING_INT_KVO:
                    self.parameters['int']['next_dose']['value'] = time_left_dose
                    self.parameters['int']['next_dose']['unit'] = 'sec'
                if switches['maxAmountPerHour'] \
                        and self.status == TestStatus.PAUSED_MPH_REACHED:
                    self.parameters['int']['mph']['value'] = motor.mph
                    self.parameters['int']['mph']['unit'] = 'ml'
                    self.parameters['int']['mph_qsize']['value'] = motor.mph_queue.qsize()
                    self.parameters['int']['mph_qsize']['unit'] = ''
                if switches['maxAmountPerInterval'] \
                        and self.status == TestStatus.PAUSED_MPI_REACHED:
                    self.parameters['int']['mpi']['value'] = motor.mpi
                    self.parameters['int']['mpi']['unit'] = 'ml'
                self.parameters['int']['time_passed']['value'] = motor.time_passed
                self.parameters['int']['time_passed']['unit'] = 'sec'
                self.parameters['int']['time_left']['value'] = time_left
                self.parameters['int']['time_left']['unit'] = 'sec'
                #
                time.sleep(_REFRESH_TIMER)
            duration = time.strftime('%H:%M:%S', time.gmtime(motor.time_passed))
            print()
            print("Infusion simulator finished at [{}]"\
                    .format(time.strftime('%H:%M:%S', time.localtime())))
            print('Expected duration: [{}] (Intermittent Mode)'.format(duration))
            # # Run KVO - Infusion Finished
            # if kvo_rate > 0 and motor.status != MotorStatus.STOPPED:
                # print()
                # print('line {0}: motor.set_rate({1:.2f}) [{2}]'\
                        # .format(get_line_number(), kvo_rate, \
                        # time.strftime('%H:%M:%S', time.localtime())))
                # motor.set_rate(kvo_rate)
                # self.status = TestStatus.RUNNING_KVO
                # while motor.status != MotorStatus.STOPPED:
                    # # Update Infusion Parameters
                    # self.parameters['int']['rate']['value'] = motor.rate
                    # self.parameters['int']['rate']['unit'] = 'ml/h'
                    # self.parameters['int']['time_passed']['value'] = motor.time_passed
                    # self.parameters['int']['time_passed']['unit'] = 'sec'
                    # time.sleep(_REFRESH_TIMER)
            # else:
                # print()
                # print('line {0}: Motor Stopped'.format(get_line_number()))
                # motor.set_status(MotorStatus.STOPPED)
        except KeyboardInterrupt:
            print()
            print('line {0}: Motor Stopped'.format(get_line_number()))
            motor.set_status(MotorStatus.STOPPED)
        except (AttributeError, NameError, OSError):
            print()
            print('line {0}: Motor Stopped'.format(get_line_number()))
            motor.set_status(MotorStatus.STOPPED)
            print()
            print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))

    def run_delay_start(self):
        '''run delay'''
        delay_start = 0
        delay_kvo_rate = 0
        protocol = self.test_protocol
        swithes = protocol['content']['program']['switches']
        if swithes['delayStart']:
            delay_start = 60 * protocol['content']['program']['delayStart']['value']
        if swithes['delayKvoRate']:
            delay_kvo_rate = protocol['content']['program']['delayKvoRate']['value']
        try:
            motor = self.motor
            # run delay
            motor.set_rate(delay_kvo_rate)
            motor.set_vinf(0)
            motor.set_time_passed(0)
            motor.set_mpi(0)
            motor.set_mph(0)
            motor.mph_queue.queue.clear()
            motor.set_time_passed_dl(0)
            self.status = TestStatus.RUNNING_DELAY
            print("Delay started at [{}]".format(time.strftime('%H:%M:%S', time.localtime())))
            while motor.time_passed_dl <= delay_start and \
                    motor.status not in [MotorStatus.STOPPED]:
                progress = math.ceil(1000 * motor.time_passed_dl / delay_start) / 10
                if delay_start > motor.time_passed_dl:
                    time_left = delay_start - motor.time_passed_dl
                else:
                    time_left = 0
                # Update Infusion Parameters
                self.parameters['delay']['rate']['value'] = delay_kvo_rate
                self.parameters['delay']['rate']['unit'] = 'ml/h'
                self.parameters['delay']['progress']['value'] = progress
                self.parameters['delay']['progress']['unit'] = '%'
                self.parameters['delay']['time_passed']['value'] = motor.time_passed
                self.parameters['delay']['time_passed']['unit'] = 'sec'
                self.parameters['delay']['time_left']['value'] = time_left
                self.parameters['delay']['time_left']['unit'] = 'sec'
                #
                time.sleep(_REFRESH_TIMER)
            duration = time.strftime('%H:%M:%S', time.gmtime(motor.time_passed))
            print()
            print("Delay finished at [{}]"\
                    .format(time.strftime('%H:%M:%S', time.localtime())))
            print('Expected duration: [{}] (Delay)'.format(duration))
        except KeyboardInterrupt:
            print()
            print('delay skipped ...')
        except (TypeError, OSError, NameError):
            print()
            print('line {0}: Motor Stopped'.format(get_line_number()))
            motor.set_status(MotorStatus.STOPPED)
            print()
            print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))

    def trigger_db(self):
        '''trigger demand bolus'''
        delivery_mode = self.test_protocol['content']['deliveryMode']
        switches = self.test_protocol['content']['program']['switches']
        if delivery_mode == 'bolusInfusion' and switches['demandBolusAmount']:
            if self.db_enabled and self.status == TestStatus.RUNNING:
                print('bolus granted')
                print('line {0}: motor.set_rate({1:.2f})'.format(get_line_number(), _BOLUS_RATE))
                self.motor.set_rate(_BOLUS_RATE)
                self.status = TestStatus.RUNNING_DEMAND_BOLUS
                self.vinf_db = 0
                self.set_time_next_db(0)
                self.motor.set_vinf_db(0)
                self.motor.set_time_passed_db(0)
                #
                self.db_tempt = True
                self.db_enabled = False
            else:
                if self.status != TestStatus.RUNNING:
                    print('bolus NOT granted: infusion status = {}'\
                            .format(self.status.name))
                elif not self.db_enabled:
                    if self.time_next_db > 0:
                        print('bolus NOT granted: next DB in {}'\
                                .format(time.strftime('%H:%M:%S', \
                                time.gmtime(self.time_next_db))))
                    else: 
                        print('bolus NOT granted: db_enabled = {}'\
                            .format(self.db_enabled))
                else:
                    print('bolus NOT granted')

    def trigger_cd(self):
        '''trigger clinician dose'''
        delivery_mode = self.test_protocol['content']['deliveryMode']
        switches = self.test_protocol['content']['program']['switches']
        if delivery_mode == 'bolusInfusion' and switches['clinicianDose']:
            if self.cd_enabled and self.status in [TestStatus.RUNNING, \
                                                   TestStatus.PAUSED_MPI_REACHED, \
                                                   TestStatus.PAUSED_MPH_REACHED]:
                print('Clinician Dose granted')
                print('line {0}: motor.set_rate({1:.2f})'.format(get_line_number(), _BOLUS_RATE))
                self.motor.set_rate(_BOLUS_RATE)
                self.set_vinf_cd(0)
                self.motor.set_vinf_cd(0)
                self.motor.set_time_passed_cd(0)
                self.motor.set_status(MotorStatus.RUNNING)
                self.status = TestStatus.RUNNING_CLINICIAN_DOSE
                #
                self.cd_tempt = True
                self.cd_enabled = False
            else:
                if self.status != TestStatus.RUNNING:
                    print('clinician dose NOT granted: infusion status = {}'\
                            .format(self.status.name))
                elif not self.cd_enabled:
                    print('clinician dose NOT granted: cd_enabled = {}'\
                            .format(self.cd_enabled))
                else:
                    print('clinician dose NOT granted')

    def get_runtime_parameters(self):
        '''get infusion runtime parameters'''
        if 'DELAY' in self.status.name:
            return self.parameters['delay']
        elif self.test_protocol['content']['deliveryMode'] == 'continuousInfusion':
            return self.parameters['cont']
        elif self.test_protocol['content']['deliveryMode'] == 'bolusInfusion':
            return self.parameters['bolus']
        elif self.test_protocol['content']['deliveryMode'] == 'intermittentInfusion':
            return self.parameters['int']

    def print_parameters(self):
        '''Print Infusion Parameters'''
        print("==")
        print("Extracted Parameters:")
        if self.test_protocol['content']['deliveryMode'] == 'continuousInfusion':
            self.print_cont_parameters()
        if self.test_protocol['content']['deliveryMode'] == 'bolusInfusion':
            self.print_bolus_parameters()
        if self.test_protocol['content']['deliveryMode'] == 'intermittentInfusion':
            self.print_int_parameters()
    
    def print_cont_parameters(self):
        ''' print continuous mode parameters only'''
        protocol = self.test_protocol
        switches = protocol['content']['program']['switches']
        if switches['delayStart']:
            print('    {0:14s} = {1:7.2f} {2:10s} (delayStart)'\
                    .format('delay start', \
                    protocol['content']['program']['delayStart']['value'], \
                    protocol['content']['program']['delayStart']['unit']))
        if switches['delayKvoRate']:
            print('    {0:14s} = {1} {2:10s} (delayKvoRate)'\
                    .format('delay kvo rate', \
                    protocol['content']['program']['delayKvoRate']['value'], \
                    protocol['content']['program']['delayKvoRate']['unit']))
        if switches['rate'] and switches['time']:
            print('    {0:14s} = {1:7.2f} {2}'\
                    .format('rate', \
                    protocol['content']['program']['rate']['value'], \
                    protocol['content']['program']['rate']['unit']))
            print('    {0:14s} = {1:7.2f} {2}'.format('time', \
                    protocol['content']['program']['time']['value'], \
                    protocol['content']['program']['time']['unit']))
        if switches['rate'] and switches['vtbi']:
            print('    {0:14s} = {1:7.2f} {2}'\
                    .format('rate', \
                    protocol['content']['program']['rate']['value'], \
                    protocol['content']['program']['rate']['unit']))
            print('    {0:14s} = {1:7.2f} {2}'\
                    .format('vtbi', \
                    protocol['content']['program']['vtbi']['value'], \
                    protocol['content']['program']['vtbi']['unit']))
        if switches['time'] and switches['vtbi']:
            print('    {0:14s} = {1:7.2f} {2}'\
                    .format('time', \
                    protocol['content']['program']['time']['value'], \
                    protocol['content']['program']['time']['unit']))
            print('    {0:14s} = {1:7.2f} {2}'\
                    .format('vtbi', \
                    protocol['content']['program']['vtbi']['value'], \
                    protocol['content']['program']['vtbi']['unit']))
        if protocol['content']['drug'] is not None:
            print('    {0:14s} = {1:7.2f} {2:10s} (drugAmount)'\
                    .format('drug amount', \
                    protocol['content']['drug']['content']['drugAmount']['value'], \
                    protocol['content']['drug']['content']['drugAmount']['unit']))
            print('    {0:14s} = {1:7.2f} {2:10s} (diluteVolume)'\
                    .format('dilute volume', \
                    protocol['content']['drug']['content']['diluteVolume']['value'], \
                    protocol['content']['drug']['content']['diluteVolume']['unit']))
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
                if self.patient_weight is None:
                    self.patient_weight = 0
                    # self.patient_weight = input("    Input Patient Weight ({0:.1f} - {1:.1f} kg): "\
                            # .format(weight_lower_limit, weight_upper_limit)) \
                            # or (weight_upper_limit + weight_lower_limit) / 2
                    # try:
                        # self.patient_weight = int(float(self.patient_weight) * 10) / 10
                    # except ValueError:
                        # self.patient_weight = (weight_upper_limit + weight_lower_limit) / 2
                        # self.patient_weight = int(float(self.patient_weight) * 10) / 10

                # if self.patient_weight > weight_upper_limit:
                    # self.patient_weight = weight_upper_limit
                # elif self.patient_weight < weight_lower_limit:
                    # self.patient_weight = weight_lower_limit
                print('    {0:14s} = {1:7.2f} {2:10s} (weight)'\
                        .format('patient weight', self.patient_weight, 'kg'))

    def print_bolus_parameters(self):
        ''' print bolus mode parameters only'''
        protocol = self.test_protocol
        switches = protocol['content']['program']['switches']
        if switches['delayStart']:
            print('    {0:14s} = {1:7.2f} {2:10s} (delayStart)'\
                    .format('delay start', \
                    protocol['content']['program']['delayStart']['value'], \
                    protocol['content']['program']['delayStart']['unit']))
        if switches['delayKvoRate']:
            print('    {0:14s} = {1:7.2f} {2:10s} (delayKvoRate)'\
                    .format('delay kvo rate', \
                    protocol['content']['program']['delayKvoRate']['value'], \
                    protocol['content']['program']['delayKvoRate']['unit']))
        if switches['vtbi']:
            print('    {0:14s} = {1:7.2f} {2}'\
                    .format('vtbi', \
                    protocol['content']['program']['vtbi']['value'], \
                    protocol['content']['program']['vtbi']['unit']))
        if switches['basalRate']:
            print('    {0:14s} = {1:7.2f} {2:10s} (basalRate)'\
                    .format('basal rate', \
                    protocol['content']['program']['basalRate']['value'], \
                    protocol['content']['program']['basalRate']['unit']))
        if switches['clinicianDose']:
            print('    {0:14s} = {1:7.2f} {2:10s} (clinicianDose)'\
                    .format('clinician dose', \
                    protocol['content']['program']['clinicianDose']['value'], \
                    protocol['content']['program']['clinicianDose']['unit']))
        if switches['autoBolusAmount']:
            print('    {0:14s} = {1:7.2f} {2:10s} (autoBolusAmount)'\
                    .format('ab volume', \
                    protocol['content']['program']['autoBolusAmount']['value'], \
                    protocol['content']['program']['autoBolusAmount']['unit']))
        if switches['bolusInterval']:
            print('    {0:14s} = {1:7.2f} {2:10s} (bolusInterval)'\
                    .format('ab interval', \
                    protocol['content']['program']['bolusInterval']['value'], \
                    protocol['content']['program']['bolusInterval']['unit']))
        if switches['maxAmountPerHour']:
            print('    {0:14s} = {1:7.2f} {2:10s} (maxAmountPerHour)'.format('max/hour', \
                    protocol['content']['program']['maxAmountPerHour']['value'], \
                    protocol['content']['program']['maxAmountPerHour']['unit']))
        if switches['demandBolusAmount']:
            print('    {0:14s} = {1:7.2f} {2:10s} (demandBolusAmount)'\
                    .format('db volume', \
                    protocol['content']['program']['demandBolusAmount']['value'], \
                    protocol['content']['program']['demandBolusAmount']['unit']))
        if switches['lockoutTime']:
            print('    {0:14s} = {1:7.2f} {2:10s} (lockoutTime)'\
                    .format('db lock', \
                    protocol['content']['program']['lockoutTime']['value'], \
                    protocol['content']['program']['lockoutTime']['unit']))
        if switches['loadingDoseAmount']:
            print('    {0:14s} = {1:7.2f} {2:10s} (loadingDoseAmount)'\
                    .format('loading dose', \
                    protocol['content']['program']['loadingDoseAmount']['value'], \
                    protocol['content']['program']['loadingDoseAmount']['unit']))
        if switches['maxAmountPerInterval']:
            print('    {0:14s} = {1:7.2f} {2:10s} (maxAmountPerInterval)'\
                    .format('max/int', \
                    protocol['content']['program']['maxAmountPerInterval']['value'], \
                    protocol['content']['program']['maxAmountPerInterval']['unit']))

    def print_int_parameters(self):
        ''' print intermittent mode parameters only'''
        protocol = self.test_protocol
        switches = protocol['content']['program']['switches']
        if switches['kvoRate']:
            print('    {0:14s} = {1:7.2f} {2:10s} (kvoRate)'\
                    .format('kvo rate', \
                    protocol['content']['program']['kvoRate']['value'], \
                    protocol['content']['program']['kvoRate']['unit']))
        if switches['doseRate']:
            print('    {0:14s} = {1:7.2f} {2:10s} (doseRate)'\
                    .format('dose rate', \
                    protocol['content']['program']['doseRate']['value'], \
                    protocol['content']['program']['doseRate']['unit']))
        if switches['doseVtbi']:
            print('    {0:14s} = {1:7.2f} {2:10s} (doseVtbi)'\
                    .format('dose vtbi', \
                    protocol['content']['program']['doseVtbi']['value'], \
                    protocol['content']['program']['doseVtbi']['unit']))
        if switches['totalTime']:
            print('    {0:14s} = {1:7.2f} {2:10s} (totalTime)'\
                    .format('total time', \
                    protocol['content']['program']['totalTime']['value'], \
                    protocol['content']['program']['totalTime']['unit']))
        if switches['delayStart']:
            print('    {0:14s} = {1:7.2f} {2:10s} (delayStart)'\
                    .format('delay start', \
                    protocol['content']['program']['delayStart']['value'], \
                    protocol['content']['program']['delayStart']['unit']))
        if switches['delayKvoRate']:
            print('    {0:14s} = {1:7.2f} {2:10s} (delayKvoRate)'\
                    .format('delay kvo rate', \
                    protocol['content']['program']['delayKvoRate']['value'], \
                    protocol['content']['program']['delayKvoRate']['unit']))
        if switches['intervalTime']:
            print('    {0:14s} = {1:7.2f} {2:10s} (intervalTime)'\
                    .format('interval time', \
                    protocol['content']['program']['intervalTime']['value'], \
                    protocol['content']['program']['intervalTime']['unit']))
        if switches['maxAmountPerHour']:
            print('    {0:14s} = {1:7.2f} {2:10s} (maxAmountPerHour)'\
                    .format('max/hour', \
                    protocol['content']['program']['maxAmountPerHour']['value'], \
                    protocol['content']['program']['maxAmountPerHour']['unit']))
        if switches['intermittentKvoRate']:
            print('    {0:14s} = {1:7.2f} {2:10s} (intermittentKvoRate)'\
                    .format('int kvo rate', \
                    protocol['content']['program']['intermittentKvoRate']['value'], \
                    protocol['content']['program']['intermittentKvoRate']['unit']))
        if switches['maxAmountPerInterval']:
            print('    {0:14s} = {1:7.2f} {2:10s} (maxAmountPerInterval)'\
                    .format('max/int', \
                    protocol['content']['program']['maxAmountPerInterval']['value'], \
                    protocol['content']['program']['maxAmountPerInterval']['unit']))

    def print_runtime_parameters(self):
        '''print runtime infusion parameters'''
        if self.motor.status not in [MotorStatus.STOPPED] and self.output_enabled:
            delivery_mode = self.test_protocol['content']['deliveryMode']
            switches = self.test_protocol['content']['program']['switches']
            if self.status in [TestStatus.RUNNING_DELAY, TestStatus.PAUSED_DELAY]:
                # display runtime delay parameters
                delay_kvo_rate = self.parameters['delay']['rate']['value']
                progress = self.parameters['delay']['progress']['value']
                time_passed = self.parameters['delay']['time_passed']['value']
                time_left = self.parameters['delay']['time_left']['value']
                #
                print("delay_kvo_rate: {:4.2f} ml/h | ".format(delay_kvo_rate), end='')
                print("delay_progress: {:3.1f}% | ".format(progress), end='')
                print("time_passed: {} | "\
                        .format(time.strftime('%H:%M:%S', \
                                time.gmtime(time_passed))), end='')
                print("time_left: {}"\
                        .format(time.strftime('%H:%M:%S', \
                                time.gmtime(time_left))), end='')
                print("{:20s}".format(' '), end='\r')
            elif delivery_mode == 'continuousInfusion':
                rate = self.parameters['cont']['rate']['value']
                vinf = self.parameters['cont']['vinf']['value']
                vtbi = self.parameters['cont']['vtbi']['value']
                progress = self.parameters['cont']['progress']['value']
                time_passed = self.parameters['cont']['time_passed']['value']
                time_left = self.parameters['cont']['time_left']['value']
                #
                print("rate: {0:4.2f} ml/h | ".format(rate), end='')
                print("vinf: {:4.2f} ml | ".format(vinf), end='')
                print("vtbi: {:4.2f} ml | ".format(vtbi), end='')
                print("progress: {:4.1f}% | ".format(progress), end='')
                print("time_passed: {} | "\
                        .format(time.strftime('%H:%M:%S', \
                                time.gmtime(time_passed))), end='')
                print("time_left: {}"\
                        .format(time.strftime('%H:%M:%S', \
                                time.gmtime(time_left))), end='')
                print("{:20s}".format(' '), end='\r')
            elif delivery_mode == 'bolusInfusion':
                # display runtime infusion parameters in [Bolus] mode
                rate = self.parameters['bolus']['rate']['value']
                vinf = self.parameters['bolus']['vinf']['value']
                volume_left = self.parameters['bolus']['vtbi']['value']
                progress = self.parameters['bolus']['progress']['value']
                if switches['autoBolusAmount']:
                    vinf_ab = self.parameters['bolus']['vinf_ab']['value']
                    next_ab = self.parameters['bolus']['next_ab']['value']
                    progress_ab = self.parameters['bolus']['progress_ab']['value']
                if switches['demandBolusAmount']:
                    vinf_db = self.parameters['bolus']['vinf_db']['value']                                
                    next_db = self.parameters['bolus']['next_db']['value']
                    progress_db = self.parameters['bolus']['progress_db']['value']
                if switches['clinicianDose'] and \
                            self.status == TestStatus.RUNNING_CLINICIAN_DOSE:
                    vinf_cd = self.parameters['bolus']['vinf_cd']['value']
                    progress_cd = self.parameters['bolus']['progress_cd']['value']
                if switches['maxAmountPerHour'] and self.status == \
                        TestStatus.PAUSED_MPH_REACHED:
                    mph = self.parameters['bolus']['mph']['value']
                    mph_qsize = self.parameters['bolus']['mph_qsize']['value']
                if switches['maxAmountPerInterval'] and self.status == \
                        TestStatus.PAUSED_MPI_REACHED:
                    mpi = self.parameters['bolus']['mpi']['value']
                if switches['loadingDoseAmount'] and self.status == \
                        TestStatus.RUNNING_LOADING_DOSE:
                    vinf_ld = self.parameters['bolus']['vinf_ld']['value']
                    next_ab = self.parameters['bolus']['next_ab']['value']
                    progress_ld = self.parameters['bolus']['progress_ld']['value']
                time_passed = self.parameters['bolus']['time_passed']['value']
                time_left = self.parameters['bolus']['time_left']['value']
                #
                if self.status == TestStatus.RUNNING:
                    print("rate: {0:4.2f} ml/h | ".format(rate), end='')
                    print("vinf: {:4.2f} ml | ".format(vinf), end='')
                    print("vtbi: {:4.2f} ml | ".format(volume_left), end='')
                    print("progress: {:4.1f}% | ".format(progress), end='')
                else:
                    print("rate: {0:4.2f} ml/h | ".format(rate), end='')
                if switches['autoBolusAmount'] and self.status == \
                        TestStatus.RUNNING_AUTO_BOLUS:
                    print("vinf_ab: {:4.2f} ml | ".format(vinf_ab), end='')
                    print("next_ab: {} | "\
                        .format(time.strftime('%H:%M:%S', \
                                time.gmtime(next_ab))), end='')
                    print("progress_ab: {:4.1f}% | ".format(progress_ab), end='')
                elif switches['autoBolusAmount'] and self.status == \
                        TestStatus.RUNNING:
                    print("next_ab: {} | "\
                        .format(time.strftime('%H:%M:%S', \
                                time.gmtime(next_ab))), end='')
                if switches['demandBolusAmount'] and self.status == \
                        TestStatus.RUNNING_DEMAND_BOLUS:
                    print("vinf_db: {:4.2f} ml | ".format(vinf_db), end='')
                    print("next_db: {} | "\
                        .format(time.strftime('%H:%M:%S', \
                                time.gmtime(next_db))), end='')
                    print("progress_db: {:4.1f}% | ".format(progress_db), end='')
                elif switches['demandBolusAmount'] and self.status == \
                        TestStatus.RUNNING:
                    print("next_db: {} | "\
                        .format(time.strftime('%H:%M:%S', \
                                time.gmtime(next_db))), end='')
                if switches['clinicianDose'] and self.status == \
                        TestStatus.RUNNING_CLINICIAN_DOSE:
                    print("vinf_cd: {:4.2f} ml | ".format(vinf_cd), end='')
                    print("progress_cd: {:4.1f}% | ".format(progress_cd), end='')
                if switches['maxAmountPerHour'] and self.status == \
                        TestStatus.PAUSED_MPH_REACHED:
                    print("mph: {:4.2f} ml | ".format(mph), end='')
                    print("mph_qsize: {:4d} | ".format(mph_qsize), end='')
                if switches['maxAmountPerInterval'] \
                        and self.status == TestStatus.PAUSED_MPI_REACHED:
                    print("mpi: {:4.2f} ml | ".format(mpi), end='')
                    print("next_ab: {} | "\
                        .format(time.strftime('%H:%M:%S', \
                                time.gmtime(next_ab))), end='')
                if switches['loadingDoseAmount'] and self.status == \
                        TestStatus.RUNNING_LOADING_DOSE:
                    print("vinf_ld: {:4.2f} ml | ".format(vinf_ld), end='')
                    print("next_ab: {} | "\
                        .format(time.strftime('%H:%M:%S', \
                                time.gmtime(next_ab))), end='')
                    print("progress_ld: {:4.1f}% | ".format(progress_ld), end='')
                print("time_passed: {} | "\
                        .format(time.strftime('%H:%M:%S', \
                                time.gmtime(time_passed))), end='')
                print("time_left: {}"\
                        .format(time.strftime('%H:%M:%S', \
                                time.gmtime(time_left))), end='')
                print("{:20s}".format(' '), end='\r')
                #
            elif delivery_mode == 'intermittentInfusion':
                # display infusion parameters in [Intermittent] mode
                rate = self.parameters['int']['rate']['value']
                vinf = self.parameters['int']['vinf']['value']
                progress = self.parameters['int']['progress']['value']
                if switches['doseVtbi'] and \
                        self.status == TestStatus.RUNNING_INT:
                    vinf_dose = self.parameters['int']['vinf_dose']['value']
                    time_left_dose = self.parameters['int']['next_dose']['value']
                    progress_dose = self.parameters['int']['progress_dose']['value']
                elif switches['doseVtbi'] and \
                            self.status == TestStatus.RUNNING_INT_KVO:
                    time_left_dose = self.parameters['int']['next_dose']['value']
                if switches['maxAmountPerHour'] \
                        and self.status == TestStatus.PAUSED_MPH_REACHED:
                    mph = self.parameters['int']['mph']['value']
                    mph_qsize = self.parameters['int']['mph_qsize']['value']
                if switches['maxAmountPerInterval'] \
                        and self.status == TestStatus.PAUSED_MPI_REACHED:
                    mpi = self.parameters['int']['mpi']['value']
                time_passed = self.parameters['int']['time_passed']['value']
                time_left = self.parameters['int']['time_left']['value']
                #
                print("rate: {0:4.2f} ml/h | ".format(rate), end='')
                if switches['doseVtbi'] and self.status == TestStatus.RUNNING_INT:
                    print("vinf_dose: {:4.2f} ml | ".format(vinf_dose), end='')
                    print("next_dose: {} | ".format(time.strftime('%H:%M:%S', \
                            time.gmtime(time_left_dose))), end='')
                    print("progress_dose: {:4.1f}% | ".format(progress_dose), end='')
                elif switches['doseVtbi'] and self.status == TestStatus.RUNNING_INT_KVO:
                    print("vinf: {:4.2f} ml | ".format(vinf), end='')
                    print("progress: {:4.1f}% | ".format(progress), end='')
                    print("next_dose: {} | ".format(time.strftime('%H:%M:%S', \
                            time.gmtime(time_left_dose))), end='')
                elif switches['doseVtbi'] and self.status == TestStatus.RUNNING_KVO:
                    print("vinf: {:4.2f} ml | ".format(vinf), end='')
                    print("progress: {:4.1f}% | ".format(progress), end='')
                if switches['maxAmountPerHour'] \
                        and self.status == TestStatus.PAUSED_MPH_REACHED:
                    print("mph: {:4.2f} ml | ".format(mph), end='')
                    print("mph_qsize: {:4d} | ".format(mph_qsize), end='')
                if switches['maxAmountPerInterval'] \
                        and self.status == TestStatus.PAUSED_MPI_REACHED:
                    print("mpi: {:4.2f} ml | ".format(mpi), end='')
                print("time_passed: {} | ".format(time.strftime('%H:%M:%S', \
                        time.gmtime(time_passed))), end='')
                print("time_left: {}".format(time.strftime('%H:%M:%S', \
                        time.gmtime(time_left))), end='')
                print("{:20s}".format(' '), end='\r')
            # End of <parameter output>

    def pause(self):
        '''pause infusion'''
        if self.status == TestStatus.PAUSED:
            print('infusion resume')
            self.motor.set_status(MotorStatus.RUNNING)
            self.status = TestStatus.RUNNING
            #
        elif self.status in [TestStatus.RUNNING, \
                             TestStatus.RUNNING_INT, \
                             TestStatus.RUNNING_INT_KVO, \
                             TestStatus.RUNNING_KVO]:
            print('infusion pause')
            self.motor.set_status(MotorStatus.PAUSED)
            self.status = TestStatus.PAUSED
            #
        elif self.status in [TestStatus.RUNNING_AUTO_BOLUS]:
            print('infusion pause')
            self.motor.set_status(MotorStatus.PAUSED)
            self.status = TestStatus.PAUSED_AUTO_BOLUS
        elif self.status in [TestStatus.PAUSED_AUTO_BOLUS]:
            print('infusion resume')
            self.motor.set_status(MotorStatus.RUNNING)
            self.status = TestStatus.RUNNING_AUTO_BOLUS
            #
        elif self.status in [TestStatus.RUNNING_LOADING_DOSE]:
            print('infusion pause')
            self.motor.set_status(MotorStatus.PAUSED)
            self.status = TestStatus.PAUSED_LOADING_DOSE
        elif self.status in [TestStatus.PAUSED_LOADING_DOSE]:
            print('infusion resume')
            self.motor.set_status(MotorStatus.RUNNING)
            self.status = TestStatus.RUNNING_LOADING_DOSE
            #
        elif self.status in [TestStatus.RUNNING_DEMAND_BOLUS]:
            print('infusion pause')
            self.motor.set_status(MotorStatus.PAUSED)
            self.status = TestStatus.PAUSED_DEMAND_BOLUS
        elif self.status in [TestStatus.PAUSED_DEMAND_BOLUS]:
            print('infusion resume')
            self.motor.set_status(MotorStatus.RUNNING)
            self.status = TestStatus.RUNNING_DEMAND_BOLUS
            #
        elif self.status in [TestStatus.RUNNING_CLINICIAN_DOSE]:
            print('infusion pause')
            self.motor.set_status(MotorStatus.PAUSED)
            self.status = TestStatus.PAUSED_CLINICIAN_DOSE
        elif self.status in [TestStatus.PAUSED_CLINICIAN_DOSE]:
            print('infusion resume')
            self.motor.set_status(MotorStatus.RUNNING)
            self.status = TestStatus.RUNNING_CLINICIAN_DOSE
            #
        elif self.status == TestStatus.RUNNING_DELAY:
            print('delay pause')
            self.motor.set_status(MotorStatus.PAUSED)
            self.status = TestStatus.PAUSED_DELAY
        elif self.status == TestStatus.PAUSED_DELAY:
            print('delay resume')
            self.motor.set_status(MotorStatus.RUNNING)
            self.status = TestStatus.RUNNING_DELAY

    def reset(self):
        '''reset infusion'''
        self.status = TestStatus.STOPPED
        self.motor.reset()

    def parse_test_protocol(self, test_protocol_path):
        '''Parse Test Protocol from File on PC'''
        test_protocol = []
        # Remove Leading / Trailing Whitespace from String
        test_protocol_path = test_protocol_path.strip(' \t\r\n\0')
        if path.exists(test_protocol_path):
            file = open(test_protocol_path, "r")
            for each_line in file:
                # Remove Leading / Trailing Whitespace from String
                each_line = each_line.strip(' \t\r\n\0')
                # (?!#) means does NOT match [#] if the Sub Test Protocol is written in a comment
                if re.match(r'(?!#)(.+)?(sub_test_protocol_)(.+)(\.txt)', each_line.lower()):
                    # Recursive Call to Sub Test Protocol
                    test_protocol_name = path.basename(each_line)[:-4]
                    test_protocol.append('#[{0}] Begin'.format(test_protocol_name))
                    test_protocol += self.parse_test_protocol(each_line)
                    test_protocol.append('#[{0}] End'.format(test_protocol_name))
                elif each_line != '':
                    test_protocol.append(each_line)
        else:
            print('File NOT exists! [{0}]'.format(test_protocol_path))
        return test_protocol
    
    def run_test_protocol(self, miva, test_protocol):
        '''Run Test Protocol (on the pump)
            test_protocol - a list of test instructions;
                            The test protocol needs to be translated into 
                            a list of commands that can be recognized
                            by the pump first.
        '''
        # Read the current event log index head
        event_log_index = miva.read_event_log_indices()
        previous_head = int(event_log_index['head'], 16)
        #        
        test_pass = True
        interval_time = miva.pump_config['interval_time']
        test_report_list = []
        print()
        print('\t Test Protocol is Running...')
        print()
        [command_list, loop_len] = generate_command_list(test_protocol)
        if command_list is None:
            command_list = ['down', 'ok', 'ok', 'ok', 'run', 'wait 3', 'ok', 'wait 10', \
                            ':infu:mode? == CONT', ':infu:run? == True', ':infu:rate? == 45', \
                            'stop', 'back', 'back']
        total_test_cases = 0
        failed_test_cases = 0 
        for each_command in command_list:
            if re.match(r'(wait)(\s*)(\d+)(\s*)', each_command.lower()):
                # wait for n seconds
                re_match_result = re.match(r'(wait)(\s+)(\d+)(\s+)?', each_command.lower())
                seconds_to_wait = int(re_match_result[3])
                print('wait {} sec'.format(seconds_to_wait))
                #
                test_report_list.append('wait {} sec'.format(seconds_to_wait))
                #
                wait(seconds_to_wait)
            elif re.match(re_compare_scpi_return_number, each_command):
                # Compare two value return from SCPI commands, Ex:
                # :timestamp:unattended? < :pump:timestamp? delta == 60
                # ^((:[a-zA-Z_]+)+(\?))(\s*)(==|>|>=|<=|<|!=)(\s*)((:[a-zA-Z_]+)+(\?))(\s+)?(delta(\s*)?==(\s*)?(\d+(\.\d*)?|\.\d+)(%)?)?(\s+)?$
                re_match_result = re.match(re_compare_scpi_return_number, each_command)
                command_to_send = re_match_result[1]
                compare_operator = re_match_result[5]
                command_to_compare = re_match_result[7]
                delta = re_match_result[14]
                if delta is not None:
                    delta = float(delta)
                delta_is_percentage = False
                if  re_match_result[13] == '%':
                    delta_is_percentage = True
                else:
                    delta_is_percentage = False
                #
                return_text = miva.send_command(command_to_send)
                compare_text = miva.send_command(command_to_compare)
                #
                print('{0} == {1}'.format(command_to_send, return_text))
                print('{0} == {1}'.format(command_to_compare, compare_text))
                #
                test_report_list.append('{0} == {1}'.format(command_to_send, return_text))
                test_report_list.append('{0} == {1}'.format(command_to_compare, compare_text))
                #
                compare_result = False
                if return_text is not None and compare_text is not None:
                    if isfloat(return_text) and isfloat(compare_text):
                        compare_result = compare_numbers(return_text, compare_text, compare_operator, delta, delta_is_percentage)
                if compare_result:
                    print('Verify \t [{}] \t .......... \tPASS'.format(each_command))
                    # print()
                    #
                    test_report_list.append('Verify \t [{}] \t .......... \tPASS'.format(each_command))
                    test_report_list.append('\n')
                    #
                    total_test_cases += 1
                else:
                    print('Verify \t [{}] \t .......... \tFAIL'.format(each_command))
                    # print()
                    #
                    test_report_list.append('Verify \t [{}] \t .......... \tFAIL'.format(each_command))
                    test_report_list.append('\n')
                    #
                    test_pass = False
                    total_test_cases += 1
                    failed_test_cases += 1
                time.sleep(interval_time)
            elif re.match(re_compare_dict_equal, each_command):
                # Compare parameters to [dict] type. Ex:
                # :event:power_on? == {"event_type": "POWER_ON", "time": "2022-03-23 08:07:53 (0xD31B - 54043 sec)", "battery_voltage (V)": 0.0, "battery_vinf (mL)": 0.0}
                #
                re_match_result = re.match(re_compare_dict_equal, each_command)
                command_to_send = re_match_result[1]
                compare_operator = re_match_result[5]
                text_to_compare = re_match_result[7]
                return_text = miva.send_command(command_to_send)
                #            
                print('{0} == {1}'.format(command_to_send, return_text))
                #
                test_report_list.append('{0} == {1}'.format(command_to_send, return_text))
                # compare python dict such as:
                # :event:unattended? == {'event_type': 'UNATTENDED_ALARM', 'time': '2022-03-22 08:47:00 (0x261 - 609 sec)'}
                text_to_compare = re.match(re_compare_dict_equal, each_command)[7]
                dict_to_compare = json.loads(text_to_compare)
                # expression to compare two list
                event_log_equal = compare_event_log_equal(return_text, dict_to_compare)
                if event_log_equal:
                    print('Verify \t [{}] \t .......... \tPASS'.format(each_command))
                    # print()
                    #
                    test_report_list.append('Verify \t [{}] \t .......... \tPASS'.format(each_command))
                    test_report_list.append('\n')
                    #
                    total_test_cases += 1
                else:
                    print('Verify \t [{}] \t .......... \tFAIL'.format(each_command))
                    # print()
                    #
                    test_report_list.append('Verify \t [{}] \t .......... \tFAIL'.format(each_command))
                    test_report_list.append('\n')
                    #
                    test_pass = False
                    total_test_cases += 1
                    failed_test_cases += 1
                time.sleep(interval_time)
            elif re.match(re_compare_str_equal, each_command):
                # ex. :protocol:name? == "DAILY 1"
                re_match_result = re.match(re_compare_str_equal, each_command)
                command_to_send = re_match_result[1]
                compare_operator = re_match_result[5]
                text_to_compare = re_match_result[7]
                return_text = miva.send_command(command_to_send)
                #
                print('{0} == \"{1}\"'.format(command_to_send, return_text))
                #
                test_report_list.append('{0} == \"{1}\"'.format(command_to_send, return_text))
                #
                text_to_compare = re_match_result[7]
                # print('return_text = {}'.format(return_text))
                # print('text_to_compare = {}'.format(text_to_compare))
                string_equal = (return_text == text_to_compare)
                if string_equal:
                    print('Verify \t [{}] \t .......... \tPASS'.format(each_command))
                    # print()
                    #
                    test_report_list.append('Verify \t [{}] \t .......... \tPASS'.format(each_command))
                    test_report_list.append('\n')
                    #
                    total_test_cases += 1
                else:
                    print('Verify \t [{}] \t .......... \tFAIL'.format(each_command))
                    # print()
                    #
                    test_report_list.append('Verify \t [{}] \t .......... \tFAIL'.format(each_command))
                    test_report_list.append('\n')
                    #
                    test_pass = False
                    total_test_cases += 1
                    failed_test_cases += 1
                time.sleep(interval_time)
            elif re.match(re_compare_parameters, each_command):
                # r'^((:[a-zA-Z_]+)+(\?))(\s*)(==|>|>=|<=|<|!=)(\s*)(\S+)(\s+)?(delta(\s*)?==(\s*)?(\d+(\.\d*)?|\.\d+)(%)?)?(\s+)?$
                # Compare parameters to certain value with delta if it is float. Ex:
                #     :infu:mode? == CONT
                #     :infu:run? == True
                #     :infu:rate? == 50
                #     :infu:time? == 15 delta == 10%
                #     :infu:rate:unit? == ML/HR
                #     :infu:bolus:running? == True
                #     :protocol:db:volume? == 1.00
                #     :protocol:name? == DAILY 1
                #     :protocol:sd:lockout? == 20:00
                verify_expression = 'False'
                re_match_result = re.match(re_compare_parameters, each_command)
                command_to_send = re_match_result[1]
                compare_operator = re_match_result[5]
                text_to_compare = re_match_result[7]
                return_text = miva.send_command(command_to_send)
                #
                if re.match(re_query_lockout, command_to_send):
                    # Format an integer to [HH:MM] time string
                    print('{0} == {1}'.format(command_to_send, int_to_time_str(return_text)))
                else:
                    print('{0} == {1}'.format(command_to_send, return_text))
                #
                test_report_list.append('{0} == {1}'.format(command_to_send, return_text))
                #
                if type(return_text) in [int, float]:
                    delta = re_match_result[12]
                    if delta is not None:
                        delta = float(delta)
                    delta_is_percentage = False
                    if  re_match_result[13] == '%':
                        delta_is_percentage = True
                    else:
                        delta_is_percentage = False
                    if re.match(re_time_str_format, text_to_compare):
                        # convert HH:MM string to integer
                        text_to_compare = time_str_to_int(text_to_compare)
                    text_to_compare = float(text_to_compare)
                    compare_result = False
                    if return_text is not None and text_to_compare is not None:
                        if isfloat(return_text) and isfloat(text_to_compare):
                            compare_result = compare_numbers(return_text, \
                                    text_to_compare, compare_operator, delta, \
                                    delta_is_percentage)
                    if compare_result:
                        verify_expression = 'True'
                    else:
                        verify_expression = 'False'
                elif type(return_text) in [bool]:
                    if text_to_compare in ['TRUE']:
                        text_to_compare = 'True'
                    elif text_to_compare in ['FALSE']:
                        text_to_compare = 'False'
                    verify_expression = str(return_text) + \
                                        ' ' + compare_operator + ' ' + \
                                        text_to_compare
                elif type(return_text) in [list]:
                    # Compare key press list such as:
                    # :key:list? == ["down", "ok", "ok", "down"]
                    text_to_compare = re.match(re_compare_list, each_command)[7]
                    list_to_compare = json.loads(text_to_compare)
                    # expression to compare two list
                    verify_expression = 'return_text' + ' ' + compare_operator + ' ' + 'list_to_compare'
                elif type(return_text) in [str]:
                    re_match_result = re.match(re_compare_str, each_command)
                    text_to_compare = re_match_result[7]
                    # print('return_text = {}'.format(return_text))
                    # print('text_to_compare = {}'.format(text_to_compare))
                    verify_expression = '\'' + return_text + '\'' + \
                                        ' ' + compare_operator + ' ' + \
                                        '\'' + text_to_compare + '\''
                else:
                    verify_expression = '\'' + str(return_text) + '\'' + \
                                        ' ' + compare_operator + ' ' + \
                                        '\'' + text_to_compare + '\''
                if eval(verify_expression):
                    print('Verify \t [{}] \t .......... \tPASS'.format(each_command))
                    # print()
                    #
                    test_report_list.append('Verify \t [{}] \t .......... \tPASS'\
                                            .format(each_command))
                    test_report_list.append('\n')
                    #
                    total_test_cases += 1
                else:
                    print('Verify \t [{}] \t .......... \tFAIL'.format(each_command))
                    # print()
                    #
                    test_report_list.append('Verify \t [{}] \t .......... \tFAIL'\
                                            .format(each_command))
                    test_report_list.append('\n')
                    #
                    test_pass = False
                    total_test_cases += 1
                    failed_test_cases += 1
                time.sleep(interval_time)
            elif each_command.lower() in ['info', 'up', 'down', 'ok', 'run', 'stop', \
                                          'back', 'power', 'mute', 'bolus']:
                # simulate the key press
                miva.send_command(each_command)
                #
                test_report_list.append(each_command)
                #
                time.sleep(interval_time)
            elif re.match(r'(\S+)(\s+)((not(\s+))?in)(\s+)(:)(event(log)?)(:)(\d+)(\?)', \
                          each_command):
                # Check to see if certain event happens in the last n events
                # ex. INFUSION_DATA in eventlog:20?
                re_match_result = re.match(r'(\S+)(\s+)((not(\s+))?in)(\s+)(:)(event(log)?)(:)(\d+)(\?)', each_command)
                compare_operator = re_match_result[3]
                command_to_send = ':event:' + str(re_match_result[11]) + '?'
                text_to_compare = re_match_result[1]
                return_text = miva.send_command(command_to_send)
                verify_expression = '\'' + text_to_compare + '\'' + \
                                    ' ' + compare_operator + ' ' + \
                                    json.dumps(return_text)
                if eval(verify_expression):
                    print('Verify \t [{}] \t .......... \tPASS'.format(each_command))
                    print()
                    #
                    test_report_list.append('Verify \t [{}] \t .......... \tPASS'.format(each_command))
                    test_report_list.append('\n')
                    #
                    total_test_cases += 1
                else:
                    print('Verify \t [{}] \t .......... \tFAIL'.format(each_command))
                    print()
                    #
                    test_report_list.append('Verify \t [{}] \t .......... \tFAIL'.format(each_command))
                    test_report_list.append('\n')
                    #
                    total_test_cases += 1
                    failed_test_cases += 1
                time.sleep(interval_time)
            elif re.match(re_get_screenshot, each_command):
                # Get screenshot from the pump 
                # Command -- 'SCREENshot'
                # r'(screen(shot)?)((\s+)?(>)(\s+)?([a-z0-9_]+\.(txt|png|jpg|json)))?$'
                re_match_result = re.match(re_get_screenshot, each_command.lower())
                screenshot_hex_list = miva.get_screenshot_hex_list()
                screenshot_bitmap = hex_to_bitmap(screenshot_hex_list)
                # \u00D7 is a multiply sign [X]
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
                                                          'row':6,
                                                          'column':114,
                                                          'width':11,
                                                          'height':4},
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
                #
                test_report_list.append(each_command)
                #
                time.sleep(interval_time)
            elif re.match(re_compare_screenshot, each_command):
                # Compare screenshot from the pump with the bitmaps file
                # r'(screen(shot)?)(\s+)?(==)(\s+)?(.+\.(txt))?$'
                re_match_result = re.match(re_compare_screenshot, each_command)
                screenshot_hex_list = miva.get_screenshot_hex_list()
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
                        #
                        print('Verify \t [{}] \t .......... \tPASS'.format(each_command))
                        print()
                        #
                        test_report_list.append('Verify \t [{}] \t .......... \tPASS'.format(each_command))
                        test_report_list.append('\n')
                        #
                        total_test_cases += 1
                    else:
                        print('Verify \t [{}] \t .......... \tFAIL'.format(each_command))
                        print()
                        #
                        test_report_list.append('Verify \t [{}] \t .......... \tFAIL'.format(each_command))
                        test_report_list.append('\n')
                        #
                        total_test_cases += 1
                        failed_test_cases += 1
                else:
                    print('Verify \t [{}] \t .......... \tFAIL'.format(each_command))
                    print()
                    #
                    test_report_list.append('Verify \t [{}] \t .......... \tFAIL'.format(each_command))
                    test_report_list.append('\n')
                    #
                    total_test_cases += 1
                    failed_test_cases += 1
                time.sleep(interval_time)
            elif re.match(re_scpi_get_cmd, each_command):
                # SCPI get commands, such as:
                # :protocol:rate?
                # :key:list?
                return_text = miva.send_command(each_command)
                test_report_list.append(each_command.upper())
                if type(return_text) in [dict]:
                    return_text = json.dumps(return_text)
                elif type(return_text) in [int]:
                    if re.match(re_query_lockout, each_command):
                        # Format an integer to [HH:MM] time string
                        if type(return_text) in [int]:
                            return_text = int_to_time_str(return_text)
                elif type(return_text) in [str]:
                    return_text = '\"' + return_text + '\"'
                print('{0} == {1}'.format(each_command.upper(), return_text))
            elif re.match(re_scpi_set_cmd, each_command):
                # SCPI set commands, such as:
                # :protocol:rate 20.0
                # :key:list:clear
                return_text = miva.query(each_command.upper())
                test_report_list.append(each_command.upper())
                print(each_command.upper())
            elif re.match(r'(#)(\s+)?(.+)', each_command):
                # Print the Title - Title starts with [# ]
                re_match_result = re.match(r'(#)(\s+)?(.+)', each_command)
                print()
                print('####{}####'.format('#' * len(re_match_result[3])))
                print('#   {}   #'.format(re_match_result[3]))
                print('####{}####'.format('#' * len(re_match_result[3])))
                #
                test_report_list.append('\n')
                test_report_list.append('####{}####'.format('#' * len(re_match_result[3])))
                test_report_list.append('#   {}   #'.format(re_match_result[3]))
                test_report_list.append('####{}####'.format('#' * len(re_match_result[3])))
                #
            elif re.match(r'(//)(\s+)?(.+)', each_command):
                # Ignore Comments - Comment starts with [//]
                pass
            else:
                print()
                print('Invalid command: [{0}]'.format(each_command))
                #
                test_report_list.append('\n')
                test_report_list.append('Invalid command: [{0}]'.format(each_command))
                #
        # Return Test Report
        if test_pass:
            print()
            print('###################{0}#{0}############'.format('#' * len(str(total_test_cases))))
            print('#   TEST RESULT - ({0}/{0}) PASSED   #'.format(total_test_cases))
            print('###################{0}#{0}############'.format('#' * len(str(total_test_cases))))
            print()
            #
            test_report_list.append('\n')
            test_report_list.append('###################{0}#{0}############'.format('#' * len(str(total_test_cases))))
            test_report_list.append('#   TEST RESULT - ({0}/{0}) PASSED   #'.format(total_test_cases))
            test_report_list.append('###################{0}#{0}############'.format('#' * len(str(total_test_cases))))
            test_report_list.append('\n')
            #
        else:
            print()
            print('###################{0}#{1}############'.format('#' * len(str(failed_test_cases)), \
                                                                  '#' * len(str(total_test_cases))))
            print('#   TEST RESULT - ({0}/{1}) FAILED   #'.format(failed_test_cases, \
                                                                  total_test_cases))
            print('###################{0}={1}############'.format('#' * len(str(failed_test_cases)), \
                                                                  '#' * len(str(total_test_cases))))
            print()
            #
            test_report_list.append('\n')
            test_report_list.append('###################{0}#{1}############'.format('#' * len(str(failed_test_cases)), \
                                                                                    '#' * len(str(total_test_cases))))
            test_report_list.append('#   TEST RESULT - ({0}/{1}) FAILED   #'.format(failed_test_cases, \
                                                                                    total_test_cases))
            test_report_list.append('###################{0}={1}############'.format('#' * len(str(failed_test_cases)), \
                                                                                    '#' * len(str(total_test_cases))))
            test_report_list.append('\n')
        # Read the current event log index head
        event_log_index = miva.read_event_log_indices()
        head = int(event_log_index['head'], 16)
        total_length = head - previous_head if head >= previous_head else \
                head + EVENT_LOG_NUMBER_OF_EVENTS - previous_head
        event_logs = []
        if total_length > 0:
            event_logs = miva.read_range_event_log(previous_head, head)
            print('--')
            print('total_length = [{}]'.format(total_length))
            print('--')
            event_logs_json = json.dumps(event_logs, indent=4)
            print(event_logs_json)
            print('Total Event Log Printed: [{}]'.format(len(event_logs)))
            print('--')
        #
        test_result = {'test_pass': test_pass,
                       'total_num': total_test_cases,
                       'failed_num': failed_test_cases,
                       'contents': test_report_list,
                       'event_logs': event_logs
                       }
        #
        return test_result


class TestMonitor:

    def __init__(self):
        '''__init__'''
        self._is_on = False
        self._is_paused = True
        self.output_enabled = True
        self.timestamp_infusion_start = None
        self.local_time_infusion_start = None
        self.cmd = ''
        self.test = None
        # Create a mutex
        self.lock = Lock()

    def start(self, test):
        '''start'''
        #
        self.test = test
        #
        self._is_on = True
        self._is_paused = False
        self.output_enabled = True
        # print('start event log monitor...')
        try:
            # motor = test.motor
            # while self._is_on and motor.status != MotorStatus.STOPPED:
            while self._is_on:
                try:
                    if self._is_paused:
                        time.sleep(_REFRESH_TIMER * 10)
                        continue
                    #
                    cmd = self.cmd.lower().rstrip(' \t\r\n\0')
                    #
                    if cmd == '':
                        if self.output_enabled:
                            test.print_runtime_parameters()
                        time.sleep(_REFRESH_TIMER)
                        continue
                    else:
                        # Disable [Infusion Monitor] Output
                        self.disable_output()
                        
                        # Process [Infusion Command]
                        self.process_command()
                        
                        # Enable [Infusion Monitor] Output
                        self.enable_output()
                except KeyboardInterrupt:
                    # press Ctrl + C
                    print()
                    print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))
                    self.cmd = ''
                except EOFError:
                    # press Ctrl + C
                    pass
                    self.cmd = ''
                except OSError:
                    print()
                    print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))
                    self.cmd = ''
            print("Infusion monitor stopped at [{}]"\
                    .format(time.strftime('%H:%M:%S', time.localtime())))
        except KeyboardInterrupt:
            # press Ctrl + C
            print()
            print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))
        except AttributeError:
            raise
            print()
            print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))
        except EOFError:
            # press Ctrl + C
            pass
        except OSError:
            print()
            print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))
        # Stop test monitor
        self.stop()

    def stop(self):
        '''stop'''
        # print('\nstop test monitor...')
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
            print('Abort: Infusion monitor is [OFF]')
            is_paused = None
        return is_paused

    def pause(self):
        ''''pause test monitor'''
        if self._is_on:
            self._is_paused = True
        else:
            print('Pause IM Aborted: Infusion monitor is [OFF]')

    def resume(self):
        if self._is_on:
            self._is_paused = False
        else:
            print('Resume IM Aborted:: Infusion monitor is [OFF]')
    
    def set_command(self, cmd):
        '''Set Command'''
        ############################################################################
        # #                         CRITICAL SECTION START                         ##
        #                                                                          #

        # Acquire Mutex
        self.lock.acquire()
        
        self.cmd = cmd
        
        # Release Mutex
        self.lock.release()

        #                                                                          #
        # #                         CRITICAL SECTION END                           ##
        ############################################################################
    
    def process_command(self):
        '''Process Command'''
        ############################################################################
        # #                         CRITICAL SECTION START                         ##
        #                                                                          #

        # Acquire Mutex
        self.lock.acquire()
        #
        
        cmd = self.cmd.strip(' \t\r\n\0')
        if cmd.upper() in ['QUIT']:
            self.test.reset()
        elif cmd.upper() in ['STATUS']:
            infusion_status = self.test.status.name
            print('infusion status = [{}]'.format(infusion_status))
            motor_status = self.test.motor.status.name
            print('motor status = [{}]'.format(motor_status))
        elif cmd.upper() in ['STOP', 'PAUSE']:
            self.test.pause()
        elif cmd.upper() in ['DB', 'BOLUS']:
            self.test.trigger_db()
        elif cmd.lower().rstrip(' \t\r\n\0') in ['cd', 'clinician dose']:
            self.test.trigger_cd()
        elif cmd.lower().rstrip(' \t\r\n\0') in ['pp', 'parameters']:
            self.test.print_parameters()
        #
        # reset command to empty
        self.cmd = ''
        time.sleep(_REFRESH_TIMER)
        # Release Mutex
        self.lock.release()

        #                                                                          #
        # #                         CRITICAL SECTION END                           ##
        ############################################################################

    def enable_output(self):
        '''Enable Output'''
        self.output_enabled = True

    def disable_output(self):
        '''Disable Output'''
        self.output_enabled = False
    
    def is_output_enabled(self):
        '''output is enabled'''
        return self.output_enabled

    
def main():
    '''main function'''
    test = Test()
    test.set_status(TestStatus.STOPPED)
    print("test status = {}".format(test.status.name))
    ###########################
    # Enter Script Path:     #
    #                         #
    script_path = "Script-[MIVA]-[1]@1607457498490.json"
    #                         #
    ######################### #
    script = Script()
    script.load(script_path)
    print("script id = {}".format(script.get_id()))
    print("script name = {}".format(script.get_name()))
    test_protocols = script.get_test_protocols()
    print("test_protocol: ")
    for each_test_protocol in test_protocols:
        print("id: {:d}".format(each_test_protocol['id']), \
              "name: {:15s}".format(each_test_protocol['content']['name']), \
              "mode: {:15s}".format(each_test_protocol['content']['deliveryMode']), \
              sep='   ||   ')
    print("Total [{}] test protocols extracted".format(len(test_protocols)))
    ###########################
    # Enter Protocol Name:    #
    #                         #
    test_protocol_name = 'Test Protocol 1'
    #                         #
    ######################### #
    print("Next will run Test Protocol [{}]:".format(test_protocol_name))
    test_protocol = script.get_test_protocol(test_protocol_name)
    print("id: {:d}   ||   ".format(test_protocol['id']), end='')
    print("name: {:15s}   ||   ".format(test_protocol['content']['name']), end='')
    print("mode: {:15s}   ||   ".format(test_protocol['content']['deliveryMode']))
    print("Extracted Parameters:")
    test.set_test_protocol(test_protocol)
    if test_protocol['content']['deliveryMode'] == 'continuousInfusion':
        test.print_cont_parameters()
    if test_protocol['content']['deliveryMode'] == 'bolusInfusion':
        test.print_bolus_parameters()
    if test_protocol['content']['deliveryMode'] == 'intermittentInfusion':
        test.print_int_parameters()
    # run test monitor #
    test_monitor = TestMonitor()
    ######################################
    # create a [test monitor] thread #
    ######################################
    test_monitor_thread = Thread(target=test_monitor.start, \
            args=([test]))
    test_monitor_thread.start()
    #
    # run infusion #
    ######################################
    # create a [infusion] thread #
    ######################################
    infusion_thread = Thread(target=test.run, args=())
    infusion_thread.start()
    #
    cmd = ''
    try:
        while cmd not in ['exit']:
            try:
                cmd = input('>')
                cmd = cmd.lower().rstrip(' \t\r\n\0')
                if cmd != '':
                    test_monitor.set_command(cmd)
            except KeyboardInterrupt:
                # press Ctrl + C
                test.reset()
                # print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))
                print()
            except EOFError:
                # press Ctrl + C
                pass
            except OSError:
                print()
                print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))
            # time.sleep(_REFRESH_TIMER * 3)
        # Reset Infusion
        test.reset()
        # Stop test monitor
        test_monitor.stop()
    except KeyboardInterrupt:
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


if __name__ == "__main__":
    main()
