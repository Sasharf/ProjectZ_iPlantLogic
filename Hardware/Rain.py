from random import randint
import time

# import RPi.GPIO as GPIO
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)

class Rain:
    pin_num = None
    sleep_time = 0.2

    def __init__(self, pin):
        self.pin_num = pin
        # GPIO.setup(pin, GPIO.IN)

    def get_status(self):
        return randint(0, 1000)

    # def get_real_status(self):
    #     drop_counter = 0
    #     try:
    #         for i in range(0, 10):
    #             state = GPIO.input(self.pin_num)
    #             if state == 0:
    #                 drop_counter += 1
    #             if drop_counter == 2:
    #                 return 1  # rainy
    #             time.sleep(self.sleep_time)
    #         return 0
    #
    #     except Exception as err:
    #         return -1
