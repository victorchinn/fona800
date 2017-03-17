import smbus
import struct
import time
from gpio import PiGpio # from the gpio.py file get the PiGpio object

# create an instance of the pi gpio driver.
pi_gpio= PiGpio()  # the () starts the init function


def bswap(val):
    return struct.unpack('<H', struct.pack('>H', val))[0]
def mread_word_data(adr, reg):
    return bswap(bus.read_word_data(adr, reg))
def mwrite_word_data(adr, reg, data):
    return bus.write_word_data(adr, reg, bswap(data))
def makeuint16(lsb, msb):
    return ((msb & 0xFF) << 8)  | (lsb & 0xFF)
def VL53L0X_decode_vcsel_period(vcsel_period_reg):
# Converts the encoded VCSEL period register value into the real
# period in PLL clocks
    vcsel_period_pclks = (vcsel_period_reg + 1) << 1;
    return vcsel_period_pclks;

def init_chip():
    val1 = bus.read_byte_data(address, VL53L0X_REG_IDENTIFICATION_REVISION_ID)
    #print "Revision ID: " + hex(val1)
    val1 = bus.read_byte_data(address, VL53L0X_REG_IDENTIFICATION_MODEL_ID)
    #print "Device ID: " + hex(val1)
    #	case VL53L0X_VCSEL_PERIOD_PRE_RANGE:
    #		Status = VL53L0X_RdByte(Dev,
    #			VL53L0X_REG_PRE_RANGE_CONFIG_VCSEL_PERIOD,
    #			&vcsel_period_reg);
    val1 = bus.read_byte_data(address, VL53L0X_REG_PRE_RANGE_CONFIG_VCSEL_PERIOD)
    #print "PRE_RANGE_CONFIG_VCSEL_PERIOD=" + hex(val1) + " decode: " + str(VL53L0X_decode_vcsel_period(val1))


    #	case VL53L0X_VCSEL_PERIOD_FINAL_RANGE:
    #		Status = VL53L0X_RdByte(Dev,
    #			VL53L0X_REG_FINAL_RANGE_CONFIG_VCSEL_PERIOD,
    #			&vcsel_period_reg);

    val1 = bus.read_byte_data(address, VL53L0X_REG_FINAL_RANGE_CONFIG_VCSEL_PERIOD)
    #print "FINAL_RANGE_CONFIG_VCSEL_PERIOD=" + hex(val1) + " decode: " + str(VL53L0X_decode_vcsel_period(val1))
    return


def inside_loop():
    internal_counter = 0
    loop_done = False
    while (loop_done == False):
        # Start the range detection loop -- write to 

        #		Status = VL53L0X_WrByte(Dev, VL53L0X_REG_SYSRANGE_START, 0x01);
        val1 = bus.write_byte_data(address, VL53L0X_REG_SYSRANGE_START, 0x01)

        #		Status = VL53L0X_RdByte(Dev, VL53L0X_REG_RESULT_RANGE_STATUS,
        #			&SysRangeStatusRegister);
        #		if (Status == VL53L0X_ERROR_NONE) {
        #			if (SysRangeStatusRegister & 0x01)
        #				*pMeasurementDataReady = 1;
        #			else
        #				*pMeasurementDataReady = 0;
        #		}

        cnt = 0
        while (cnt < 100): # 1 second waiting time max
	        time.sleep(0.010)
	        val = bus.read_byte_data(address, VL53L0X_REG_RESULT_RANGE_STATUS)
	        if (val & 0x01):
		        break
	        cnt += 1

        #if (val & 0x01):
	    #    print "ready"
        #else:
	    #    print "not ready"

        #	Status = VL53L0X_ReadMulti(Dev, 0x14, localBuffer, 12);
        data = bus.read_i2c_block_data(address, 0x14, 12)
        #print data
        #print "ambient count " + str(makeuint16(data[7], data[6]))
        #print "signal count " + str(makeuint16(data[9], data[8]))
        #		tmpuint16 = VL53L0X_MAKEUINT16(localBuffer[11], localBuffer[10]);

        Answer = str(makeuint16(data[11], data[10]))
        if (Answer != "20"):
            print "distance " + Answer
        
            if (int(Answer) < 600):
                pi_gpio.set_led(1,True)
                pi_gpio.set_led(2,False)
                pi_gpio.set_led(3,False)
            elif (int(Answer) < 1200):
                pi_gpio.set_led(1,False)
                pi_gpio.set_led(2,True)
                pi_gpio.set_led(3,False)
                internal_counter += 1
                if (internal_counter >= 20):
                    loop_done = True
            else:
                pi_gpio.set_led(1,False)
                pi_gpio.set_led(2,False)
                pi_gpio.set_led(3,True)

        DeviceRangeStatusInternal = ((data[0] & 0x78) >> 3)
        #print DeviceRangeStatusInternal
    return


VL53L0X_REG_IDENTIFICATION_MODEL_ID		= 0x00c0
VL53L0X_REG_IDENTIFICATION_REVISION_ID		= 0x00c2
VL53L0X_REG_PRE_RANGE_CONFIG_VCSEL_PERIOD	= 0x0050
VL53L0X_REG_FINAL_RANGE_CONFIG_VCSEL_PERIOD	= 0x0070
VL53L0X_REG_SYSRANGE_START			= 0x000

VL53L0X_REG_RESULT_INTERRUPT_STATUS 		= 0x0013
VL53L0X_REG_RESULT_RANGE_STATUS 		= 0x0014



bus = smbus.SMBus(1)
address = 0x29
pi_gpio.set_led(1,False)
pi_gpio.set_led(2,False)
pi_gpio.set_led(3,False)
init_chip()
inside_loop()



