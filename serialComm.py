import tkinter as tk
import time
from serial import Serial

# create GUI window
root = tk.Tk()
root.title("Communicating Via Serial")

ser = Serial('/dev/cu.usbserial-10', 9600)

# create serial port input
serialPort_label = tk.Label(root, text="Type Serial Port (COM9, /dev/cu.usbserial-10, etc.):")
serialPort_label.pack()
serialPort_entry = tk.Entry(root)
serialPort_entry.pack()

# create label and entry widget
string_label = tk.Label(root, text="Type Command (white, blue, red, all, off):")
string_label.pack()
string_entry = tk.Entry(root)
string_entry.pack()

# function to send delay time to the serial port
def send_string():
    string = string_entry.get()
    # create serial object
    ser = Serial(serialPort_entry.get(), 9600)  # 'COM9' # '/dev/cu.usbserial-10'
    time.sleep(2)
    ser.write(string.encode())
    print(string)

# create button to send string to serial port
send_button = tk.Button(root, text="Set Command", command=send_string)
send_button.pack()

# start GUI event loop
root.mainloop()
