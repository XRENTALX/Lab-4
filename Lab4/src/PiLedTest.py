import time
from time import sleep

from hal import hal_led as led
from hal import hal_input_switch as switch


def led_blink_tenhz():
    led.init()
    led.set_output(0, 1)
    time.sleep(0.1)
    led.set_output(0, 0)
    time.sleep(0.1)



def main():
    led.init()
    switch.init()
    y = 0
    while True:
        if switch.read_slide_switch() == 1 and y == 0:
            led.set_output(0, 1)
            time.sleep(0.2)
            led.set_output(0, 0)
            time.sleep(0.2)
            y = 1

        else:

            led_blink_tenhz()
            y = 0


# Main entry point
if __name__ == "__main__":
    main()