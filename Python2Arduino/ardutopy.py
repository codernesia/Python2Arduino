import serial

arduino = serial.Serial('/dev/ttyACM0',9600);


def doSomething():
    data = str(arduino.readline())
    print(data)
    
    
try:
    while(True): 
        doSomething()
except KeyboardInterrupt:
        arduino.close()
        print('has closed connection')