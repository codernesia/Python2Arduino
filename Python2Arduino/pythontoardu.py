import serial
arduino = serial.Serial('/dev/ttyACM0',9600);
def ledCountrol():
    cmd = input("masukan data : ")
    arduino.write(cmd.encode())
try:
    while(True):
        ledCountrol()
except KeyboardInterrupt:
    arduino.close()
    print("arduino has disconnect")
    
    