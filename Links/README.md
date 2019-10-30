## Te compartimos algunos ejemplos para que puedas conectar tus sensores.
* [Sensor Magnetico](https://www.alexisabarca.com/2016/01/usar-un-sensor-de-puerta-magnetico-en-un-raspberry-pi/)
* [Lector RFID USB](https://tutorial.cytron.io/2019/07/25/create-a-simple-gui-for-usb-rfid-reader-em4100-using-raspberry-pi/)
* [RFID RC522 Reader and record data on IOTA](https://medium.com/coinmonks/for-beginners-how-to-set-up-a-raspberry-pi-rfid-rc522-reader-and-record-data-on-iota-865f67843a2d)
* [Sensor de presencia](https://www.internetdelascosas.cl/2013/05/13/sensor-de-presencia-en-raspberry-pi/)
* [Sensor DHT11](https://github.com/adafruit/Adafruit_Python_DHT)

    #### Configuracion del tipo de sensor DHT

        import RPi.GPIO as GPIO
        import Adafruit_DHT
        sensor = Adafruit_DHT.DHT11
        #humedad
        pin = 23

        GPIO.setwarnings(False) # Ignore warning for now
        GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

        def humCallback(pin):
                humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
                #print(temperatura)
                if temperatura >21:
                    GPIO.output(led_pin, GPIO.HIGH)
                else:
                    GPIO.output(led_pin, GPIO.LOW)

        while True:
            humCallback(pin)``


