 import serial
import time

# Cambia COM3 por el puerto donde esté conectado tu Arduino
arduino = serial.Serial('COM3', 9600)

time.sleep(2)

print("Leyendo datos del Arduino...")

while True:
    dato = arduino.readline().decode('utf-8').strip()
    print("Dato recibido:", dato)


