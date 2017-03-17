import RPi.GPIO as GPIO

LED1_PIN    = 18    # cobbler pin 12 (GPIO18)
LED2_PIN    = 13    # cobbler pin 33 (GPIO13)
LED3_PIN    = 23    # cobbler pin 16 (GPIO23)
SWITCH_PIN  = 27    # cobbler pin 7  (GPIO27)

class PiGpio(object):
    """Raspberry Pi Internet 'IoT GPIO'."""

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED1_PIN, GPIO.OUT)      # RED LED as output
        GPIO.setup(LED2_PIN, GPIO.OUT)      # GRN LED as output
        GPIO.setup(LED3_PIN, GPIO.OUT)      # BLU LED as output
        GPIO.setup(SWITCH_PIN, GPIO.IN)     # Switch as input w/pu
        GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def read_switch(self):
        """Read the switch state."""
        switch = GPIO.input(SWITCH_PIN)
        # invert because of active low momentary switch
        if (switch == 0):
            switch=1
        else:
            switch=0
        return switch

    # set the particular LED to ON or OFF
    def set_led(self, led, value):
        """Change the LED to the passed in value, '1 ON or '0' OFF."""
        if(led == 1):
            GPIO.output(LED1_PIN, value)
        if(led == 2):
            GPIO.output(LED2_PIN, value)
        if(led == 3):
            GPIO.output(LED3_PIN, value)

    # get the state of an LED
    def get_led(self, led):
        """Return the state value of the LED, '1' ON or '0' OFF."""
        if(led == 1):
            return GPIO.input(LED1_PIN)
        if(led == 2):
            return GPIO.input(LED2_PIN)
        if(led == 3):
            return GPIO.input(LED3_PIN)

        

