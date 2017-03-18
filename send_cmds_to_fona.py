#!/usr/bin/python
import serial
import time
from bmp280 import PiBMP280
from vl53l0x import *

# create an instance of the pi gpio driver.
pi_gpio= PiGpio()  # the () starts the init function



#ATI - Get the module name and revision
#AT+CMEE=2 - Turn on verbose errors (handy for when you are trying out commands!)
#AT+CCID 
#AT+COPS? Check that you're connected to the network, in this case T-Mobile
#AT+CSQ - Check the 'signal strength' - the first # is dB strength, it should be higher than around 5. Higher is better. Of course it depends on your antenna and location!
#AT+CBC - will return the lipo battery state. The second number is the % full (in this case its 92%) and the third number is the actual voltage in mV (in this case, 3.877 V)
#AT+CMGF=1 - this will set it to TEXT mode not PDU (data) mode. You must do this because otherwise you cannot just type out the message.
#AT+CMGS="nnnnnn" - send a text message! You will get a '>' prompt for typing. Type out your message and when you are done send a [Control-Z] on an empty line to send


def setup():

    ser.write('ATI \r\n')
    time.sleep(0.1)
    read_val = ser.read(size=64)
    #print read_val

    ser.write('AT+CCID \r\n')
    time.sleep(0.1)
    read_val = ser.read(size=64)
    #print read_val

    ser.write('AT+COPS?\r\n')
    time.sleep(0.1)
    read_val = ser.read(size=64)
    print read_val

    ser.write('AT+CSQ\r\n')
    time.sleep(0.1)
    read_val = ser.read(size=64)
    #print read_val

    ser.write('AT+CBC\r\n')
    time.sleep(0.1)
    read_val = ser.read(size=64)
    #print read_val

    return


def send_sms(_phone_number,_text_to_send):

    ser.write('AT+CMGF=1\r\n')
    time.sleep(0.1)
    read_val = ser.read(size=64)
    #print read_val

    ser.write('AT+CMGS="')
    ser.write(_phone_number)
    ser.write('"\r\n')
    time.sleep(0.1)
    read_val = ser.read(size=64)

    ser.write(_text_to_send)
    ser.write('\r\n\x1a')
    time.sleep(0.1)
    read_val = ser.read(size=64)

    return


def connect_to_phone_and_send():

    
    
    phone_number = raw_input('Enter Phone #:')
    name = raw_input('Enter Name:')
    
    setup()
    print "Sending to Phone # ",phone_number
    #print "Message: ",text_message


    # Read the Sensor Temp/Pressure values.
    (temperature, pressure) = pi_bmp280.readBMP280All()
    preamble = name + ": from exactly where you are standing now, the "
    
    temperature_f = (temperature * 9/5) + 32 
    
    text_message = preamble + "measured Temp = " + str(temperature_f) + "F, and Pressure =  " + str(pressure) + "hPa"
    print text_message

    send_sms(phone_number,text_message)
   
    ser.close()
    return

def open_gprs_session():

   #setup?
   setup()

   # AT+SAPBR=3,1,"Contype","GPRS"
   # OK
   ser.write('AT+SAPBR=3,1,\"CONTYPE\",\"GPRS\"\r\n')
   time.sleep(0.1)
   read_val = ser.read(size=64)
   print read_val

   # Set bearer parameter
   # AT+SAPBR=3,1,"APN","CMNET"
   # OK
   ser.write('AT+SAPBR=3,1,\"APN\","fast.t-mobile.com\"\r\n')
   time.sleep(0.1)
   read_val = ser.read(size=64)
   print read_val

   # Set bearer context
   # AT+SAPBR=2,1
   # OK
   ser.write('AT+SAPBR=2,1\r\n')
   time.sleep(0.1)
   read_val = ser.read(size=64)
   print read_val


   # Get current longitude , latitude

   ser.write('AT+CIPGSMLOC=1,1\r\n')
   time.sleep(2.0)
   read_val = ser.read(size=128)
   print read_val

   return

def open_fm_radio():

#AT+FMOPEN=0
#AT+FMVOLUME=0
#AT+FMFREQ=885
#AT+FMSIGNAL=885
#AT+FMCLOSE

    return
# get the temperature and pressure

# create an instance of my pi bmp280 sensor object
pi_bmp280 = PiBMP280()

# open the serial port to connect to the Fona 800
ser = serial.Serial('/dev/ttyS0', 9600, timeout=0.5)
ser.write('AT\r\n')
time.sleep(0.1)
read_val = ser.read(size=64)
#print read_val

bus = smbus.SMBus(1)
address = 0x29
pi_gpio.set_led(1,False)
pi_gpio.set_led(2,False)
pi_gpio.set_led(3,False)


#initialize the bmp280 chip
#init_chip() 
#run a loop until an object is held at the midway point above the IR sensor (green light will hold)
#inside_loop()

#send an SMS message to the phone by reading input phone # and add a name
#connect_to_phone_and_send()

#open a GPRS session for testing

open_gprs_session()



