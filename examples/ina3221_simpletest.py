"""Sample code and test for barbudor_ina3221"""

import time
import board
from barbudor_ina3221 import INA3221

# To enable relay on pin A1 to switch-on the test-load
#import digitalio
#pin = digitalio.DigitalInOut(board.A1)
#pin.switch_to_output()

i2c_bus = board.I2C()
ina3221 = INA3221(i2c_bus)

ina3221.enable_channel(1)

while True:

    print("------------------------------")
    for chan in (1, 2, 3):
        if ina3221.is_channel_enabled(chan):
            print("Channel %d" % chan)
            bus_voltage = ina3221.bus_voltage(chan)
            shunt_voltage = ina3221.shunt_voltage(chan)
            current = ina3221.current(chan)
            print("  PSU Voltage:   {:6.3f} V".format(bus_voltage + shunt_voltage))
            print("  Shunt Voltage: {:9.6f} V".format(shunt_voltage))
            print("  Load Voltage:  {:6.3f} V".format(bus_voltage))
            print("  Current:       {:9.6f} A".format(current))
            print("")

    time.sleep(2.0)
