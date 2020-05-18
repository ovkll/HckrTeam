import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN) #PIR
GPIO.setup(23, GPIO.OUT) #led rojo
GPIO.setup(24, GPIO.OUT) #led azul
GPIO.setup(25, GPIO.OUT) #Buzzer

try:
    #ESTADO= 0
    print ("SENSOR ENCENDIDO")
    GPIO.output(24, GPIO.HIGH) #led azul encendido
    print ("Azul Encendido")
    print ("################")
    time.sleep(2) # para estabilizar el inicio del sensor
    GPIO.output(23, GPIO.LOW) #led rojo apagado
    
    while True:
        ahora = datetime.now()
        fecha = ahora.strftime("%Y-%m-%d %H:%M:%S")
         #condición si se detecta movimiento
         #ESTADO= 1
        if GPIO.input(4):
            GPIO.output(25, True) #Buzzer activo
            GPIO.output(23, GPIO.HIGH) #Led rojo encendido
            print ("**************")
            print ("Rojo Encendido")
            
            GPIO.output(24, GPIO.LOW) #Led azul apagado
            time.sleep(0.5) #Buzzer encendido 0.5 segundos
            ###CAMBIO DE ESTADO= 0
            GPIO.output(25, False) #Buzzer  apagado
            GPIO.output(23, GPIO.LOW) #Led  rojo apagado
            GPIO.output(24, GPIO.HIGH) #Led azul encendido
            print ("Movimiento Detectado= " + fecha) # Notificación en shell
            print ("**************")
            print ("Azul encendido")
            time.sleep(5) #se evita la detección multiple
        time.sleep(0.1) #retraso de bucle, menor que el retraso de detección

except:
    GPIO.cleanup()
    print ("SENSOR APAGADO")