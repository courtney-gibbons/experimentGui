import tkinter as tk

def start_button_click():
    experiment_running.set(1)
    num_experiments = int(num_experiments_var.get())
    experiment_times = [0] * num_experiments
    experiment_bs = [0] * num_experiments
    experiment_freqs = [0] * num_experiments
    for i in range(num_experiments):
        experiment_times[i] = int(experiment_time_entries[i].get())
        experiment_bs[i] = int(experiment_b_entries[i].get())
        experiment_freqs[i] = int(experiment_freq_entries[i].get())
    print("Number of Experiments:", num_experiments)
    print("Experiment Times:", experiment_times)
    print("Experiment Magnetic Fields:", experiment_bs)
    print("Experiment Magnetic Fields:", experiment_freqs)

def abort_button_click():
    experiment_aborted.set(1)

root = tk.Tk()
root.geometry("600x450")
root.title("Experiment GUI")

num_experiments_label = tk.Label(root, text="How many experiments are you running?", font=("Helvetica", 20))
num_experiments_label.pack()

num_experiments_var = tk.IntVar()
num_experiments_var.set(1)

num_experiments_options = [("1", 1), ("2", 2), ("3", 3), ("4", 4)]
for text, value in num_experiments_options:
    tk.Radiobutton(root, text=text, variable=num_experiments_var, value=value, command=lambda v=value: show_entries(v)).pack()

blank_line = tk.Label(root, text="", height=1)
blank_line.pack()

experiment_label = tk.Label(root, text="Experiment Information", font=("Helvetica", 20))
experiment_label.pack()

experiment_time_entries = []
experiment_b_entries = []
experiment_freq_entries = []

def show_entries(value):
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
        experiment_label = tk.Label(root, text=f"Experiment {i+1}:")
        experiment_label.pack()
        experiment_labels.append(experiment_label)

        experiment_time_label = tk.Label(root, text=f"Time (min):")
        experiment_time_label.pack()
        experiment_time_labels.append(experiment_time_label)
        entry = tk.Entry(root)
        entry.pack()
        experiment_time_entries.append(entry)

        experiment_b_label = tk.Label(root, text=f"Magnetic Field (mT):")
        experiment_b_label.pack()
        experiment_b_labels.append(experiment_b_label)
        entry = tk.Entry(root)
        entry.pack()
        experiment_b_entries.append(entry)

        experiment_freq_label = tk.Label(root, text=f"Frequency (Hz):")
        experiment_freq_label.pack()
        experiment_freq_labels.append(experiment_freq_label)
        entry = tk.Entry(root)
        entry.pack()
        experiment_freq_entries.append(entry)

experiment_labels = []
experiment_time_labels = []
experiment_b_labels = []
experiment_freq_labels = []
show_entries(num_experiments_var.get())

experiment_running = tk.BooleanVar()
experiment_running.set(0)
experiment_aborted = tk.BooleanVar()
experiment_aborted.set(0)

abort_button = tk.Button(root, text="Abort", command=abort_button_click)
abort_button.pack(side="bottom", fill="x")

start_button = tk.Button(root, text="Start", command=start_button_click)
start_button.pack(side="bottom", fill="x")

root.mainloop()