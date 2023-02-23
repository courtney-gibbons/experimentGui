import tkinter as tk

class ExperimentGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Experiment GUI")

        # Variables for user input
        self.numExperiments = tk.IntVar()
        self.running = tk.IntVar()
        self.abort = tk.IntVar()
        self.experimentTimes = []
        self.fields = []
        self.freqs = []

        # Create widgets for user input
        tk.Label(self.master, text="How many experiments are you running?").grid(row=0, column=1, sticky=tk.E)
        self.numExperimentsBox = tk.Entry(self.master, textvariable=self.numExperiments)
        self.numExperimentsBox.grid(row=0, column=2)

        # Create sections for each experiment
        for i in range(1, 5):
            tk.Label(self.master, text=f"Experiment {i}", font="bold").grid(row=3+(i-1)*4, column=0, sticky=tk.W)
            tk.Label(self.master, text="Time (min)").grid(row=4+(i-1)*4, column=0, sticky=tk.W)
            experimentTime = tk.IntVar()
            self.experimentTimes.append(experimentTime)
            tk.Entry(self.master, textvariable=experimentTime).grid(row=4+(i-1)*4, column=1, sticky=tk.W)

            tk.Label(self.master, text="B (mT)").grid(row=5+(i-1)*4, column=0, sticky=tk.W)
            field = tk.IntVar()
            self.fields.append(field)
            tk.Entry(self.master, textvariable=field).grid(row=5+(i-1)*4, column=1, sticky=tk.W)

            tk.Label(self.master, text="f (Hz)").grid(row=6+(i-1)*4, column=0, sticky=tk.W)
            freq = tk.IntVar()
            self.freqs.append(freq)
            tk.Entry(self.master, textvariable=freq).grid(row=6+(i-1)*4, column=1, sticky=tk.W)
        
        tk.Label(self.master, text="").grid(row=1)

        tk.Button(self.master, text="Turn On", command=self.turn_on).grid(row=2, column=1)
        tk.Button(self.master, text="Abort", command=self.abort_experiment).grid(row=2, column=2)

    def turn_on(self):
        self.running.set(1)
        num_experiments = self.numExperiments.get()
        experiment_times = [0] * num_experiments
        experiment_bs = [0] * num_experiments
        experiment_freqs = [0] * num_experiments
        for i in range(num_experiments):
            experiment_times[i] = int(self.experimentTimes[i].get())
        for i in range(num_experiments):
            experiment_bs[i] = int(self.fields[i].get())
        for i in range(num_experiments):
            experiment_freqs[i] = int(self.freqs[i].get())
        print("Number of Experiments:", num_experiments)
        print("Experiment Times:", experiment_times)
        print("Experiment Fields:", experiment_bs)
        print("Experiment Freqs:", experiment_freqs)

    def abort_experiment(self):
        self.abort.set(1)
        self.running.set(0)

if __name__ == "__main__":
    root = tk.Tk()
    app = ExperimentGUI(root)
    root.mainloop()
