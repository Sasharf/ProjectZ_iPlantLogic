from random import randint
import Adafruit_ADS1x15


class WaterLvl:
    pin_num = None
    try:
        adc = Adafruit_ADS1x15.ADS1015()
    except Exception as err:
        print(err)

    def __init__(self, pin):
        self.pin_num = pin

    def get_status(self):
        return randint(0, 100)

    def get_real_water_lvl(self):
        try:
            return self.adc.read_adc(self.pin_num, gain=1)
        except Exception as err:
            return 0

    def get_water_lvl(selfs):
        return randint(0, 100)