import gpiozero as gz
import time

def main():
    print("READY")
    #basic_on_off()
    traffic_light()


def basic_on_off():
    print("Basic on off control")
    red_led = gz.DigitalOutputDevice(18)
    green_led = gz.DigitalOutputDevice(15)
    blue_led = gz.DigitalOutputDevice(14)

    for _ in range(5):
        red_led.on()
        green_led.on()
        blue_led.on()

        time.sleep(1.0)

        red_led.off()
        green_led.off()
        blue_led.off()
        time.sleep(1.0)

def traffic_light():
    print("Traffic Light")
    red_led = gz.DigitalOutputDevice(18)
    green_led = gz.DigitalOutputDevice(15)
    blue_led = gz.DigitalOutputDevice(14)

    while True:
        blue_led.off()
        red_led.on()
        time.sleep(5.0)
        red_led.off()
        green_led.on()
        time.sleep(3.0)
        green_led.off()
        blue_led.on()
        time.sleep(10.0)

main()