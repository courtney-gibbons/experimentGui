import serial
import time
import tkinter as tk
# Define the pin mapping
pin_mapping = {
    'led1': 13,
    'led2': 12,
    'button1': 2,
    'button2': 3,
}
# Define a function to send the pin command to the Arduino
def send_pin_command():
    command = pin_entry.get()
    if command in pin_mapping:
        pin_number = pin_mapping[command]
        arduino.write(str(pin_number).encode())  # Encode the pin number as a string
    else:
        print('Invalid command')
# Define the GUI window
root = tk.Tk()
root.title('Arduino Pin Control')
# Create a label and entry for the serial port
port_label = tk.Label(root, text='Serial port:') # /dev/cu.usbserial-10
port_label.grid(row=0, column=0)
port_entry = tk.Entry(root)
port_entry.grid(row=0, column=1)
# Create a label and entry for the pin command
pin_label = tk.Label(root, text='Pin command:')
pin_label.grid(row=1, column=0)
pin_entry = tk.Entry(root)
pin_entry.grid(row=1, column=1)
# Create a button to send the pin command
send_button = tk.Button(root, text='Send', command=send_pin_command)
send_button.grid(row=2, column=1)
# Connect to Arduino when the Send button is clicked
def connect_arduino():
    global arduino
    port = port_entry.get()
    arduino = serial.Serial(port, 9600)
    time.sleep(2)  # Wait for the Arduino to initialize
connect_button = tk.Button(root, text='Connect', command=connect_arduino)
connect_button.grid(row=2, column=0)
# Run the GUI loop
root.mainloop()