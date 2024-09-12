import gpiozero as gz
import time
import signal

# red_led = gz.LED(18)
# green_led = gz.LED(15)
# blue_led = gz.LED(14)
# red_led = gz.PWMLED(18)
# green_led = gz.PWMLED(15)
# blue_led = gz.PWMLED(14)

def main():
    print("READY")
    # fancy_blink()
    # led_pwm()
    # led_board()
    traffic_light()
    

def fancy_blink():
    print("Fancy Blink")
    # red_led.blink(4,1,3, False)
    red_led.blink()
    green_led.blink()
    # time.sleep(5.0)
    signal.pause()
    print("Goodbye")

def led_pwm():
    print("LED PWM")
    while True:
        for k in range(10):
            red_led.value = k/5
            time.sleep(0.5)

def led_board():
    print("LED Board")
    leds = gz.LEDBoard(14,15,18)
    leds.on()
    time.sleep(1)
    leds.off()
    time.sleep(1)
    leds.value = (1,0,1)
    time.sleep(1)
    leds.off()
    time.sleep(1)

def traffic_light():
    light = gz.TrafficLights(14,15,18)
    light.green.on()

    while True:
        time.sleep(10)
        light.green.off()
        light.amber.on()
        time.sleep(1)
        light.amber.off()
        light.red.on()
        time.sleep(10)
        light.amber.on()
        time.sleep(1)
        light.green.on()
        light.amber.off()
        light.red.off()

main()