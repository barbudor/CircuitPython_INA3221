"""Sample code and test for barbudor_ina3221"""

import time
import board
from barbudor_ina3221_lite import INA3221

i2c_bus = board.I2C()
ina3221 = INA3221(i2c_bus)

ina3221.enable_channel(1)
ina3221.enable_channel(2)
ina3221.enable_channel(3)

while True:

    print("------------------------------")
    line_title=         "Measurement   "
    line_psu_voltage=   "PSU voltage   "
    line_load_voltage=  "Load voltage  "
    line_shunt_voltage= "Shunt voltage "
    line_current=       "Current       "

    for chan in range(1,4):
        if ina3221.is_channel_enabled(chan):
            #
            bus_voltage=   ina3221.bus_voltage(chan)
            shunt_voltage= ina3221.shunt_voltage(chan)
            current=       ina3221.current(chan)
            #
            line_title+=         "| Chan#{:d}      ".format(chan)
            line_psu_voltage+=   "| {:6.3f}    V ".format(bus_voltage + shunt_voltage)
            line_load_voltage+=  "| {:6.3f}    V ".format(bus_voltage)
            line_shunt_voltage+= "| {:9.6f} V ".format(shunt_voltage)
            line_current+=       "| {:9.6f} A ".format(current)

    print(line_title)
    print(line_psu_voltage)
    print(line_load_voltage)
    print(line_shunt_voltage)
    print(line_current)

    time.sleep(2.0)