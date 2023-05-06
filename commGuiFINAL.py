import json
import tkinter as tk
from serial import Serial
import time

global arduino
# arduino = Serial('/dev/cu.usbserial-10', 9600)

root = tk.Tk()
root.geometry("1200x400")
root.title("Experiment GUI")

# Create a frame for the first column
frame1 = tk.Frame(root)
frame1.pack(side="left")

# 1. Connect Serial Port
port_label = tk.Label(frame1, text="1. Connect Serial Port:", font=("Helvetica", 20))
port_label.pack()
port_label = tk.Label(frame1, text="(COM9, /dev/cu.usbserial-10, etc.)")
port_label.pack()
port_entry = tk.Entry(frame1)
port_entry.pack(fill="x")

def connect_arduino():
    port = port_entry.get()
    arduino = Serial(port, 9600)
    time.sleep(2)  # Wait for the Arduino to initialize
connect_button = tk.Button(frame1, text='Connect', command=connect_arduino)
connect_button.pack(fill="x")

blank_line = tk.Label(frame1, text="", height=1)
blank_line.pack()

# 2. Set Number of Experiments
num_experiments_label = tk.Label(frame1, text="2. Set Number of Experiments:", font=("Helvetica", 20))
num_experiments_label.pack()
num_experiments_var = tk.IntVar()
num_experiments_var.set(0)
num_experiments_options = tk.OptionMenu(frame1, num_experiments_var, 1, 2, 3, 4)
num_experiments_options.pack(fill="x")

experiment_time_entries = []
experiment_b_entries = []
experiment_freq_entries = []

def show_entries(value):
    for frame in frames:
        frame.destroy()

    for label in experiment_labels:
        label.pack_forget()
    experiment_labels.clear()

    for label in experiment_time_labels:
        label.pack_forget()
    experiment_time_labels.clear()
    for entry in experiment_time_entries:
        entry.pack_forget()
    experiment_time_entries.clear()

    for label in experiment_b_labels:
        label.pack_forget()
    experiment_b_labels.clear()
    for entry in experiment_b_entries:
        entry.pack_forget()
    experiment_b_entries.clear()

    for label in experiment_freq_labels:
        label.pack_forget()
    experiment_freq_labels.clear()
    for entry in experiment_freq_entries:
        entry.pack_forget()
    experiment_freq_entries.clear()

    for i in range(value):
        # Create a frame for the ith column
        framei = tk.Frame(root)
        framei.pack(side="left")
        frames.append(framei)

        experiment_label = tk.Label(framei, text=f"Experiment {i+1}:", font=("Helvetica", 20))
        experiment_label.pack()
        experiment_labels.append(experiment_label)

        experiment_time_label = tk.Label(framei, text=f"Time (min):")
        experiment_time_label.pack()
        experiment_time_labels.append(experiment_time_label)
        entry = tk.Entry(framei)
        entry.pack()
        experiment_time_entries.append(entry)

        experiment_b_label = tk.Label(framei, text=f"Magnetic Field (mT):")
        experiment_b_label.pack()
        experiment_b_labels.append(experiment_b_label)
        entry = tk.Entry(framei)
        entry.pack()
        experiment_b_entries.append(entry)

        experiment_freq_label = tk.Label(framei, text=f"Frequency (Hz):")
        experiment_freq_label.pack()
        experiment_freq_labels.append(experiment_freq_label)
        entry = tk.Entry(framei)
        entry.pack()
        experiment_freq_entries.append(entry)

frames = []
experiment_labels = []
experiment_time_labels = []
experiment_b_labels = []
experiment_freq_labels = []

def set_num_experiments():
    show_entries(num_experiments_var.get())
set_num_experiments_button = tk.Button(frame1, text='Set Number', command=set_num_experiments)
set_num_experiments_button.pack(fill="x")

blank_line = tk.Label(frame1, text="", height=1)
blank_line.pack()

# 3. Set Experiment Values
experiment_vals_label = tk.Label(frame1, text="3. Set Experiment Values:", font=("Helvetica", 20))
experiment_vals_label.pack()

blank_line = tk.Label(frame1, text="", height=1)
blank_line.pack()

# Start and Abort Buttons
buttons_label = tk.Label(frame1, text="4. Start or Abort:", font=("Helvetica", 20))
buttons_label.pack()

experiment_running = tk.IntVar()
experiment_running.set(0)

def start_button_click():
    experiment_running.set(1)
    num_experiments = int(num_experiments_var.get())
    running = int(experiment_running.get())

    dict = {
        "start/abort": running,
        "num experiments": num_experiments
    }

    for i in range(num_experiments):
        temp_dict = {
            "time": int(experiment_time_entries[i].get()),
            "magnetic field": int(experiment_b_entries[i].get()),
            "frequency": int(experiment_freq_entries[i].get())
        }
        dict[f"experiment {i+1}"] = (temp_dict)

    data = json.dumps(dict)
    print(data)
    arduino.write(data.encode())

def abort_button_click():
    experiment_running.set(0)
    running = int(experiment_running.get())

    dict = {
        "start/abort": running
    }

    data = json.dumps(dict)
    print(data)
    arduino.write(data.encode())

start_button = tk.Button(frame1, text="Start", command=start_button_click)
start_button.pack(fill="x")

abort_button = tk.Button(frame1, text="Abort", command=abort_button_click)
abort_button.pack(fill="x")

root.mainloop()
