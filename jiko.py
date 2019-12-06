import smbus2
import bme280
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#Definē nepieciešamās lietas priekš BME moduļa
port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

data = bme280.sample(bus, address, calibration_params)
#Definē uz kura GPIO pina ir pieslēgta poga
button = 26
#Definē pie kuriem GPIO piniem ir pieslēgtas diodes
GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
try:
    while True:
         button_state = GPIO.input(button)
            #Kods pasaka: kad poga tiek atlaista tad notiek sekundes pauze un iesledzas diode
         if button_state == GPIO.LOW:
            time.sleep(1)
            GPIO.output(16,GPIO.HIGH)
            print('iesledzas diode')
            #Kods pasaka, kad notiks 2 sekunžu pauze un tad izprintēs ka ieslēdzas 2. diode un tieši tāpat paralēli ieslēgsies tā
            time.sleep(2)
            print('iesledzas 2. diode')
            GPIO.output(20,GPIO.HIGH)
             #Kods pasaka, kad notieks 2 sekunžu pauze un tad izprintēs ka ieslēdzas 3. diode un tieši tāpat paralēli ieslēgsies tā
            time.sleep(2)
            print('iesledzas 3. diode')
            GPIO.output(21,GPIO.HIGH)
            #Kods pasaka, kad notiks sekundes pauze un tad izprintēs temperatūru, spiedienu, mitrumu kopā
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
except:
    GPIO.cleanup()
