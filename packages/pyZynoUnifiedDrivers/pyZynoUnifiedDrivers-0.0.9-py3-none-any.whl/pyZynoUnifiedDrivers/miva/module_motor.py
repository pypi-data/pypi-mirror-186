'''class_motor'''
import sys
import math
import queue
#import threading
from threading import Thread, Lock
import time
#
# from infusion_mode import InfusionMode

from enum import Enum

class MotorStatus(Enum):
    '''infusion mode'''
    STOPPED = 0
    RUNNING = 1
    PAUSED = 2

# the time needed for the motor to finish one rotation
_INTERVAL = 0.01
_REFRESH_TIMER = 0.1

class Motor:
    '''motor class
    mph - max per hour
    mpi - max per interval
    '''
    def __init__(self):
        self.rate = 0
        self.previous_rate = 0
        self.rate_basal = 0
        self.vinf = 0
        # auto bolus vinf for each ab interval
        self.vinf_ab = 0
        # demand bolus vinf for each demand bolus
        self.vinf_db = 0
        # clinician dose vinf for each clinician dose
        self.vinf_cd = 0
        # intermittent dose vinf for each intermittent dose interval
        self.vinf_dose = 0
        # mph - max per hour counter
        self.mph = 0
        self.mph_queue = None
        # mpi - max per interval counter
        self.mpi = 0
        self.time_passed = 0
        # time passed since auto bolus start
        self.time_passed_ab = 0
        # time passed since demand bolus start
        self.time_passed_db = 0
        # time passed since clinician dose start
        self.time_passed_cd = 0
        # time passed since intermittent dose start
        self.time_passed_id = 0
        # time passed since delay start
        self.time_passed_dl = 0
        self.status = MotorStatus.STOPPED
        # Create a mutex
        self.lock = Lock()

    def pause(self):
        '''pause motor'''
        ############################################################################
        ##                         CRITICAL SECTION START                         ##
        #                                                                          #

        # Acquire Mutex
        self.lock.acquire()

        self.status = MotorStatus.PAUSED

        # Release Mutex
        self.lock.release()

        #                                                                          #
        ##                         CRITICAL SECTION END                           ##
        ############################################################################

    def resume(self):
        '''resume motor'''
        ############################################################################
        ##                         CRITICAL SECTION START                         ##
        #                                                                          #

        # Acquire Mutex
        self.lock.acquire()

        self.status = MotorStatus.RUNNING

        # Release Mutex
        self.lock.release()

        #                                                                          #
        ##                         CRITICAL SECTION END                           ##
        ############################################################################

    def set_rate(self, motor_rate):
        '''set rate'''
        ############################################################################
        ##                         CRITICAL SECTION START                         ##
        #                                                                          #

        # Acquire Mutex
        self.lock.acquire()

        self.rate = motor_rate

        # Release Mutex
        self.lock.release()

        #                                                                          #
        ##                         CRITICAL SECTION END                           ##
        ############################################################################
    def set_previous_rate(self, motor_rate):
        '''set previous rate'''
        ############################################################################
        ##                         CRITICAL SECTION START                         ##
        #                                                                          #

        # Acquire Mutex
        self.lock.acquire()

        self.previous_rate = motor_rate

        # Release Mutex
        self.lock.release()

        #                                                                          #
        ##                         CRITICAL SECTION END                           ##
        ############################################################################
    def set_rate_basal(self, basal_rate):
        '''set rate'''
        ############################################################################
        ##                         CRITICAL SECTION START                         ##
        #                                                                          #

        # Acquire Mutex
        self.lock.acquire()

        self.rate_basal = basal_rate

        # Release Mutex
        self.lock.release()

        #                                                                          #
        ##                         CRITICAL SECTION END                           ##
        ############################################################################

    def set_vinf(self, motor_vinf):
        '''set rate'''
        ############################################################################
        ##                         CRITICAL SECTION START                         ##
        #

        # Acquire Mutex
        self.lock.acquire()

        self.vinf = motor_vinf

        # Release Mutex
        self.lock.release()

        #                                                                          #
        ##                         CRITICAL SECTION END                           ##
        ############################################################################

    def set_vinf_ab(self, vinf):
        '''set auto bolus vinf'''
        ############################################################################
        ##                         CRITICAL SECTION START                         ##
        #

        # Acquire Mutex
        self.lock.acquire()

        self.vinf_ab = vinf

        # Release Mutex
        self.lock.release()

        #                                                                          #
        ##                         CRITICAL SECTION END                           ##
        ############################################################################

    def set_vinf_db(self, vinf):
        '''set demand bolus vinf'''
        ############################################################################
        ##                         CRITICAL SECTION START                         ##
        #

        # Acquire Mutex
        self.lock.acquire()

        self.vinf_db = vinf

        # Release Mutex
        self.lock.release()

        #                                                                          #
        ##                         CRITICAL SECTION END                           ##
        ############################################################################

    def set_vinf_cd(self, vinf):
        '''set clinician dose vinf'''
        ############################################################################
        ##                         CRITICAL SECTION START                         ##
        #

        # Acquire Mutex
        self.lock.acquire()

        self.vinf_cd = vinf

        # Release Mutex
        self.lock.release()

        #                                                                          #
        ##                         CRITICAL SECTION END                           ##
        ############################################################################

    def set_vinf_dose(self, vinf):
        '''set intermittent dose vinf'''
        ############################################################################
        ##                         CRITICAL SECTION START                         ##
        #

        # Acquire Mutex
        self.lock.acquire()

        self.vinf_dose = vinf

        # Release Mutex
        self.lock.release()

        #                                                                          #
        ##                         CRITICAL SECTION END                           ##
        ############################################################################

    def set_time_passed(self, time_passed):
        '''set time passed'''
        ############################################################################
        ##                         CRITICAL SECTION START                         ##
        #

        # Acquire Mutex
        self.lock.acquire()

        self.time_passed = time_passed

        # Release Mutex
        self.lock.release()

        #                                                                          #
        ##                         CRITICAL SECTION END                           ##
        ############################################################################


    def set_time_passed_ab(self, time_passed):
        '''set time passed of the auto bolus interval'''
        ############################################################################
        ##                         CRITICAL SECTION START                         ##
        #

        # Acquire Mutex
        self.lock.acquire()

        self.time_passed_ab = time_passed

        # Release Mutex
        self.lock.release()

        #                                                                          #
        ##                         CRITICAL SECTION END                           ##
        ############################################################################

    def set_time_passed_db(self, time_passed):
        '''set time passed since demand bolus start'''
        ############################################################################
        ##                         CRITICAL SECTION START                         ##
        #

        # Acquire Mutex
        self.lock.acquire()

        self.time_passed_db = time_passed

        # Release Mutex
        self.lock.release()

        #                                                                          #
        ##                         CRITICAL SECTION END                           ##
        ############################################################################

    def set_time_passed_cd(self, time_passed):
        '''set time passed since clinician dose start'''
        ############################################################################
        ##                         CRITICAL SECTION START                         ##
        #

        # Acquire Mutex
        self.lock.acquire()

        self.time_passed_cd = time_passed

        # Release Mutex
        self.lock.release()

        #                                                                          #
        ##                         CRITICAL SECTION END                           ##
        ############################################################################

    def set_time_passed_id(self, time_passed):
        '''set time passed since intermittent dose start'''
        ############################################################################
        ##                         CRITICAL SECTION START                         ##
        #

        # Acquire Mutex
        self.lock.acquire()

        self.time_passed_id = time_passed

        # Release Mutex
        self.lock.release()

        #                                                                          #
        ##                         CRITICAL SECTION END                           ##
        ############################################################################
    def set_time_passed_dl(self, time_passed):
        '''set time passed since delay start'''
        ############################################################################
        ##                         CRITICAL SECTION START                         ##
        #

        # Acquire Mutex
        self.lock.acquire()

        self.time_passed_dl = time_passed

        # Release Mutex
        self.lock.release()

        #                                                                          #
        ##                         CRITICAL SECTION END                           ##
        ############################################################################
    def set_mph(self, max_per_hour_counter):
        '''set max per hour counter'''
        ############################################################################
        ##                         CRITICAL SECTION START                         ##
        #

        # Acquire Mutex
        self.lock.acquire()

        self.mph = max_per_hour_counter

        # Release Mutex
        self.lock.release()

        #                                                                          #
        ##                         CRITICAL SECTION END                           ##
        ############################################################################

    def set_mpi(self, max_per_interval_counter):
        '''set max per interval counter'''
        ############################################################################
        ##                         CRITICAL SECTION START                         ##
        #

        # Acquire Mutex
        self.lock.acquire()

        self.mpi = max_per_interval_counter

        # Release Mutex
        self.lock.release()

        #                                                                          #
        ##                         CRITICAL SECTION END                           ##
        ############################################################################

    def set_status(self, motor_status):
        '''set status'''
        ############################################################################
        ##                         CRITICAL SECTION START                         ##
        #
        # Acquire Mutex
        self.lock.acquire()

        self.status = motor_status

        # Release Mutex
        self.lock.release()

        #                                                                          #
        ##                         CRITICAL SECTION END                           ##
        ############################################################################

    def run(self):
        '''motor run'''
        try:
            # Motor Run
            # print("Motor started at [{}]".format(time.strftime('%H:%M:%S', time.localtime())))
            # print("Motor running ...")
            #
            self.status = MotorStatus.RUNNING
            mph_queue_size = math.ceil(3600/_INTERVAL)
            self.mph_queue = queue.Queue(mph_queue_size)
            while self.status not in [MotorStatus.STOPPED]:
                if self.status == MotorStatus.RUNNING:
                    delta_volume_ab = (self.rate - self.rate_basal) / 3600 * _INTERVAL \
                        if self.rate > self.rate_basal else 0
                    delta_volume = self.rate / 3600 * _INTERVAL
                    self.vinf_ab += delta_volume_ab
                    self.vinf_db += delta_volume_ab
                    self.vinf_cd += delta_volume_ab
                    self.vinf += delta_volume
                    self.vinf_dose += delta_volume
                    self.time_passed += _INTERVAL
                    self.time_passed_ab += _INTERVAL
                    self.time_passed_db += _INTERVAL
                    self.time_passed_cd += _INTERVAL
                    self.time_passed_id += _INTERVAL
                    self.time_passed_dl += _INTERVAL
                    #
                    self.mph += delta_volume
                    self.mph_queue.put(delta_volume)
                    if self.mph_queue.full():
                        self.mph -= self.mph_queue.get()
                    #
                    self.mpi += delta_volume
                    #
                else:
                    # When motor is paused
                    self.time_passed += _INTERVAL
                    self.time_passed_ab += _INTERVAL
                    self.time_passed_db += _INTERVAL
                    self.time_passed_cd += _INTERVAL
                    self.time_passed_id += _INTERVAL
                    #
                    self.mph_queue.put(0)
                    if self.mph_queue.full():
                        self.mph -= self.mph_queue.get()
                    #
                time.sleep(_INTERVAL)
        except KeyboardInterrupt:
            print()
            print('Motor stopped: KeyboardInterrupt')
        except (AttributeError, NameError, OSError):
            print()
            print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))

    def reset(self):
        self.rate = 0
        self.rate_basal = 0
        self.vinf = 0
        # auto bolus vinf for each ab interval
        self.vinf_ab = 0
        # demand bolus vinf for each demand bolus
        self.vinf_db = 0
        # clinician dose vinf for each clinician dose
        self.vinf_cd = 0
        # intermittent dose vinf for each intermittent dose interval
        self.vinf_dose = 0
        # mph - max per hour counter
        self.mph = 0
        # mpi - max per interval counter
        self.mpi = 0
        self.time_passed = 0
        # time passed since auto bolus start
        self.time_passed_ab = 0
        # time passed since demand bolus start
        self.time_passed_db = 0
        # time passed since clinician dose start
        self.time_passed_cd = 0
        # time passed since intermittent dose start
        self.time_passed_id = 0
        # time passed since delay start
        self.time_passed_dl = 0
        self.status = MotorStatus.STOPPED

def main():
    '''main function'''
    try:
        motor = Motor()
        motor.set_rate(120)
        motor_thread = Thread(target=motor.run, args=())
        motor_thread.start()
        print("Motor started at [{}]".format(time.strftime('%H:%M:%S', time.localtime())))
        print("Motor running ...")
        vtbi = 0.5
        before = time.perf_counter()
        while motor.vinf <= vtbi and motor.status != MotorStatus.STOPPED:
            progress = math.ceil(1000 * motor.vinf / vtbi) / 10
            current = time.perf_counter()
            time_passed = time.strftime('%H:%M:%S', time.gmtime(current - before))
            volume_left = vtbi - motor.vinf if vtbi > motor.vinf else 0
            time_left = time.strftime('%H:%M:%S', time.gmtime(3600 * volume_left / motor.rate))
            print("rate: {:6.2f} ml/h".format(motor.rate), \
                  "vinf: {:6.2f} ml".format(motor.vinf),  \
                  "vtbi: {:6.2f} ml".format(volume_left), \
                  "progress: {:5.1f}%".format(progress), \
                  "time passed: {:4.1f} second".format(motor.time_passed), \
                  "time passed: {} second".format(time_passed), \
                  "time left: {}".format(time_left), sep='  |  ', end='\r')
            time.sleep(_REFRESH_TIMER)
        print()
        print('motor.vinf = {} mL'.format(motor.vinf))
        print('vtbi = {} mL'.format(vtbi))
        motor.set_status(MotorStatus.STOPPED)
        after = time.perf_counter()
        duration = time.strftime('%H:%M:%S', time.gmtime(after - before))
        print('Motor stopped ...')
        print('Motor stopped at [{}]'.format(time.strftime('%H:%M:%S', time.localtime())))
        print('Expected duration = {}'.format(duration))
    except KeyboardInterrupt:
        motor.set_status(MotorStatus.STOPPED)
    except OSError:
        motor.set_status(MotorStatus.STOPPED)
        print()
        print("{0}: {1}\n".format(sys.exc_info()[0], sys.exc_info()[1]))

if __name__ == "__main__":
    main()
    