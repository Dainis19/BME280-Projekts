# BME280 Projekts
 Mācību nolūkam un lai dabūtu vērtējumu taisu projektu priekš BME280
  
  Ideja ir nospiežot pogu ieslēdzas pirmā diode, pēc laika otrā un tad trešā pēc tam info nonāk uz BME sensoru, tad bme noslasa datus un izprintē visus parametrus.
  
  ## Būs nepieciešams :
  
  1. Vadi (14)
  2. Rezistori (3)
  3. BME280 
  4. Raspberry Pi 3B+
  5. Diodes (3)
  6. Breadbords
  7. Poga
  
  ## Blokshēma
  
   ![](https://github.com/Dainis19/BME280-Projekts/blob/master/BME280.png)
   
   
   ## Shēma dzelžiem
   
   ![](https://github.com/Dainis19/BME280-Projekts/blob/master/DZELZI.PNG)
   
   
   ## Kods
   
   import time
import RPi.GPIO as GPIO
import smbus2
import bme280

port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)


data = bme280.sample(bus, address, calibration_params)


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button = 26

GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

try:
    while True:
         button_state = GPIO.input(button)
         if button_state == GPIO.LOW:
             time.sleep(1)
             GPIO.output(16,GPIO.HIGH)
             print ('poga ir nospiesta')
             time.sleep(2)
             print ('iesledzas poga 2')
             GPIO.output(20,GPIO.HIGH)
             time.sleep(2)
             print ('iesledzas poga 3')
             GPIO.output(21,GPIO.HIGH)
             time.sleep(1)
             print (data.id)
             print (data.timestamp)
             print (data.temperature)
             print (data.pressure)
             print (data.humidity)

             print (data)


         else:
             GPIO.output(16,GPIO.LOW) 
             GPIO.output(20,GPIO.LOW) 
             GPIO.output(21,GPIO.LOW) 
    
except:
    GPIO.cleanup()
