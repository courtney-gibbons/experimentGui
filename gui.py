import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

def confirm_button_click():
    num_experiments = int(num_experiments_var.get())
    experiment_times = [0] * num_experiments
    for i in range(num_experiments):
        experiment_times[i] = int(experiment_time_entries[i].get())
    print("Number of Experiments:", num_experiments)
    print("Experiment Times:", experiment_times)

root = ctk.CTk()
root.geometry("600x500")
root.title("Experiment GUI")

num_experiments_label = ctk.CTkLabel(root, text="How many experiments are you running?", font=("Helvetica", 20))
num_experiments_label.pack()


num_experiments_var = tk.IntVar()
num_experiments_var.set(1)

num_experiments_options = [("1", 1), ("2", 2), ("3", 3), ("4", 4)]
for text, value in num_experiments_options:
    radioButton = ctk.CTkRadioButton(root, text=text, variable=num_experiments_var, value=value, command=lambda v=value: show_entries(v))
    radioButton.pack(padx=3, pady=3)

blank_line = ctk.CTkLabel(root, text="", height=1)
blank_line.pack()

experiment_time_label = ctk.CTkLabel(root, text="How long is each experiment?", font=("Helvetica", 20))
experiment_time_label.pack()

experiment_time_entries = []

def show_entries(value):
    for label in experiment_time_labels:
        label.pack_forget()
    experiment_time_labels.clear()
    for entry in experiment_time_entries:
        entry.pack_forget()
    experiment_time_entries.clear()
    for i in range(value):
        experiment_time_label = ctk.CTkLabel(root, text=f"Experiment {i+1} Time:")
        experiment_time_label.pack()
        experiment_time_labels.append(experiment_time_label)
        entry = ctk.CTkEntry(root)
        entry.pack()
        experiment_time_entries.append(entry)

experiment_time_labels = []
show_entries(num_experiments_var.get())

confirm_button = ctk.CTkButton(root, text="Confirm", command=confirm_button_click)
confirm_button.pack(side="bottom", fill="x")

root.mainloop()
