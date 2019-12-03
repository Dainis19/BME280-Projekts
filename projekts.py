import time
import RPi.GPIO as GPIO
import smbus2
import bme280

port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params=bme280.load_calibration_params(bus, address)

data=bme280.sample(bus, address,calibration_params)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button=26

GPIO.setup(button,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)


while True:
    try:
        button_state = GPIO.input(button)
        if button_state == GPIO.LOW:
            time.sleep(1)
            GPIO.output(16,GPIO.HIGH)
            print('iesledzas diode')
            time.sleep(2)
            print('iesledzas 2. diode')
            GPIO.output(20,GPIO.HIGH)
            time.sleep(2)
            print('iesledzas 3. diode')
            GPIO.output(21,GPIO.HIGH)
            time.sleep(1)
            print(data.id)
            print(data.timestamp)
            print(data.temperature)
            print(data.pressure)
            print(data.humidity)

            print(data)

        else: 
            GPIO.output(16,GPIO.LOW)
            GPIO.output(20,GPIO.LOW)
            GPIO.output(21,GPIO.LOW)       
except KeyboardInterupt:
    GPIO.cleanup()
break()