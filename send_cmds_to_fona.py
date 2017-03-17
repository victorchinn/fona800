#!/usr/bin/python
import serial
import time


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
    print read_val

    ser.write('AT+CCID \r\n')
    time.sleep(0.1)
    read_val = ser.read(size=64)
    print read_val

    ser.write('AT+COPS?\r\n')
    time.sleep(0.1)
    read_val = ser.read(size=64)
    print read_val

    ser.write('AT+CSQ\r\n')
    time.sleep(0.1)
    read_val = ser.read(size=64)
    print read_val

    ser.write('AT+CBC\r\n')
    time.sleep(0.1)
    read_val = ser.read(size=64)
    print read_val

    ser.write('AT+COPS?\r\n')
    time.sleep(0.1)
    read_val = ser.read(size=64)
    print read_val
    return


def send_sms(_phone_number,_text_to_send):

    ser.write('AT+CMGF=1\r\n')
    time.sleep(0.1)
    read_val = ser.read(size=64)
    print read_val

    ser.write('AT+CMGS="')
    ser.write(_phone_number)
    ser.write("\r\n')
    time.sleep(0.1)
    read_val = ser.read(size=64)

    ser.write(_text_to_send)
    ser.write('\r\n\x1a')
    time.sleep(0.1)
    read_val = ser.read(size=64)

    return


# open the serial port to connect to the Fona 800
ser = serial.Serial('/dev/ttyS0', 9600, timeout=0.5)
ser.write('AT\r\n')
time.sleep(0.1)

read_val = ser.read(size=64)
print read_val

phone_number = raw_input('Enter Phone #:')
text_message = raw_input('Enter Message:')

setup()
send_sms(phone_number,text_message)


ser.close()

