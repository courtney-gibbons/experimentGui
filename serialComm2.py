import serial
import time
# Define the pin mapping
pin_mapping = {
    'led1': 13,
    'led2': 12,
    'button1': 2,
    'button2': 3,
}
# Connect to Arduino using the specified serial port
port = '/dev/cu.usbserial-10'  # Change this to match your serial port
arduino = serial.Serial(port, 9600)
time.sleep(2)  # Wait for the Arduino to initialize
# Send commands to control the pins
while True:
    command = input('Enter a pin command (led1, led2, button1, button2): ')
    if command in pin_mapping:
        pin_number = pin_mapping[command]
        arduino.write(str(pin_number).encode())  # Encode the pin number as a string
    else:
        print('Invalid command')