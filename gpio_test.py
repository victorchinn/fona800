#!/usr/bin/python
import time
from gpio import PiGpio # from the gpio.py file get the PiGpio object

# create an instance of the pi gpio driver.
pi_gpio= PiGpio()  # the () starts the init function

# Blink the LEDS forever.
print('Blinking all my LEDs in sequence (Ctrl-C to stop)...')
while True:
# Get the current switch state and print
    switch = pi_gpio.read_switch()  # this is how switch is mapped into a string
    print('\n============ Switch: {0} ============'.format(switch))

    print('\nLED 1 ON (RED)')
    pi_gpio.set_led(1,True)
    print('LED1: {0}'.format(pi_gpio.get_led(1)))
    print('LED2: {0}'.format(pi_gpio.get_led(2)))
    print('LED3: {0}'.format(pi_gpio.get_led(3)))
    time.sleep(1.0)

    print('\nLED 2 ON (GRN)')
    pi_gpio.set_led(2,True)
    print('LED1: {0}'.format(pi_gpio.get_led(1)))
    print('LED2: {0}'.format(pi_gpio.get_led(2)))
    print('LED3: {0}'.format(pi_gpio.get_led(3)))
    time.sleep(1.0)

    print('\nLED 3 ON (BLU)')
    pi_gpio.set_led(3,True)
    print('LED1: {0}'.format(pi_gpio.get_led(1)))
    print('LED2: {0}'.format(pi_gpio.get_led(2)))
    print('LED3: {0}'.format(pi_gpio.get_led(3)))
    time.sleep(1.0)


    print('\nLED 1 OFF (RED)')
    pi_gpio.set_led(1,False)
    print('LED1: {0}'.format(pi_gpio.get_led(1)))
    print('LED2: {0}'.format(pi_gpio.get_led(2)))
    print('LED3: {0}'.format(pi_gpio.get_led(3)))
    time.sleep(1.0)

    print('\nLED 2 OFF (GRN)')
    pi_gpio.set_led(2,False)
    print('LED1: {0}'.format(pi_gpio.get_led(1)))
    print('LED2: {0}'.format(pi_gpio.get_led(2)))
    print('LED3: {0}'.format(pi_gpio.get_led(3)))
    time.sleep(1.0)

    print('\nLED 3 OFF (BLU)')
    pi_gpio.set_led(3,False)
    print('LED1: {0}'.format(pi_gpio.get_led(1)))
    print('LED2: {0}'.format(pi_gpio.get_led(2)))
    print('LED3: {0}'.format(pi_gpio.get_led(3)))
    time.sleep(1.0)

