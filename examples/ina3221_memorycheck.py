### Memory test for barbudor_ina3221 ###
# Copy below sequence into

import board
import gc

i2c_bus = board.I2C()

gc.collect(); gc.collect(); gc.collect(); before = gc.mem_free();

from barbudor_ina3221 import INA3221

gc.collect(); gc.collect(); gc.collect(); after = gc.mem_free();

ina3221 =  INA3221(i2c_bus)

gc.collect(); gc.collect(); gc.collect(); instance = gc.mem_free();

print( "Import used    : %d bytes" % (before - after))
print( "Instance used  : %d bytes" % (after - instance))
