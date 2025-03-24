import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class CPUScheduler:
    def __init__(self, root):
        self.root = root
        self.root.title("CPU Scheduling Simulator")
        self.root.configure(bg="#2c3e50")

        tk.Label(root, text="CPU Scheduling Simulator", font=("Arial", 16, "bold"), fg="white", bg="#2c3e50").pack(pady=10)

        tk.Label(root, text="Enter Process Burst Times (Space-Separated):", fg="white", bg="#2c3e50").pack()
        self.burst_entry = tk.Entry(root, width=50)
        self.burst_entry.pack()

        self.priority_label = tk.Label(root, text="Enter Process Priorities (Lower = Higher Priority, Space-Separated):", fg="white", bg="#2c3e50")
        self.priority_label.pack()
        self.priority_entry = tk.Entry(root, width=50)
        self.priority_entry.pack()

        self.quantum_label = tk.Label(root, text="Enter Time Quantum (Only for Round Robin):", fg="white", bg="#2c3e50")
        self.quantum_label.pack()
        self.quantum_entry = tk.Entry(root, width=50)
        self.quantum_entry.pack()

        tk.Label(root, text="Choose Scheduling Algorithm:", fg="white", bg="#2c3e50").pack()

        self.algorithm = tk.StringVar()
        self.algorithm.set("FCFS")

        algorithms = ["FCFS", "SJF", "Priority", "Round Robin"]
        for algo in algorithms:
            tk.Radiobutton(root, text=algo, variable=self.algorithm, value=algo, bg="#2c3e50", fg="white", command=self.toggle_fields).pack()

        tk.Button(root, text="Run Simulation", command=self.run_simulation, bg="#3498db", fg="white", font=("Arial", 12)).pack(pady=5)

        self.output_text = tk.Text(root, width=60, height=10, bg="#ecf0f1")
        self.output_text.pack(pady=5)

        self.toggle_fields()

    def toggle_fields(self):
        if self.algorithm.get() == "Priority":
            self.priority_label.pack()
            self.priority_entry.pack()
        else:
            self.priority_label.pack_forget()
            self.priority_entry.pack_forget()

        if self.algorithm.get() == "Round Robin":
            self.quantum_label.pack()
            self.quantum_entry.pack()
        else:
            self.quantum_label.pack_forget()
            self.quantum_entry.pack_forget()

    def run_simulation(self):
        try:
            burst_times = list(map(int, self.burst_entry.get().split()))
            priorities = self.priority_entry.get().split()
            priorities = list(map(int, priorities)) if priorities else [0] * len(burst_times)

            if len(burst_times) != len(priorities) and self.algorithm.get() == "Priority":
                raise ValueError("Burst times and priorities must have the same number of values!")

            if self.algorithm.get() == "Round Robin":
                quantum = int(self.quantum_entry.get())
                if quantum <= 0:
                    raise ValueError("Time quantum must be a positive integer.")

            if self.algorithm.get() == "FCFS":
                self.fcfs(burst_times)
            elif self.algorithm.get() == "SJF":
                self.sjf(burst_times)
            elif self.algorithm.get() == "Priority":
                self.priority_scheduling(burst_times, priorities)
            elif self.algorithm.get() == "Round Robin":
                self.round_robin(burst_times, quantum)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def fcfs(self, burst_times):
        waiting_time, turnaround_time, start_time, end_time = self.calculate_times(burst_times)
        self.display_output(burst_times, waiting_time, turnaround_time)
        self.plot_gantt_chart(start_time, end_time, len(burst_times))

    def sjf(self, burst_times):
        sorted_burst = sorted(burst_times)
        self.fcfs(sorted_burst)

    def priority_scheduling(self, burst_times, priorities):
        processes = sorted(zip(priorities, burst_times), key=lambda x: x[0])
        sorted_burst = [p[1] for p in processes]
        self.fcfs(sorted_burst)

    def round_robin(self, burst_times, quantum):
        n = len(burst_times)
        remaining = burst_times[:]
        waiting_time = [0] * n
        turnaround_time = [0] * n
        current_time = 0
        start_time, end_time, process_order = [], [], []

        while any(remaining):
            for i in range(n):
                if remaining[i] > 0:
                    start_time.append(current_time)
                    if remaining[i] > quantum:
                        remaining[i] -= quantum
                        current_time += quantum
                    else:
                        current_time += remaining[i]
                        remaining[i] = 0
                        turnaround_time[i] = current_time
                    end_time.append(current_time)
                    process_order.append(f"P{i+1}")

        self.display_output(burst_times, waiting_time, turnaround_time)
        self.plot_gantt_chart(start_time, end_time, n, process_order)

    def calculate_times(self, burst_times):
        n = len(burst_times)
        waiting_time = [0] * n
        turnaround_time = [0] * n
        start_time = [0] * n
        end_time = [0] * n

        for i in range(1, n):
            waiting_time[i] = burst_times[i-1] + waiting_time[i-1]
        for i in range(n):
            turnaround_time[i] = burst_times[i] + waiting_time[i]
            start_time[i] = waiting_time[i]
            end_time[i] = turnaround_time[i]

        return waiting_time, turnaround_time, start_time, end_time

    def display_output(self, burst_times, waiting_time, turnaround_time):
        output = "Process\tBurst Time\tWaiting Time\tTurnaround Time\n"
        for i in range(len(burst_times)):
            output += f"{i+1}\t{burst_times[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}\n"
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, output)

    def plot_gantt_chart(self, start, end, n, process_order=None):
        fig, ax = plt.subplots()
        for i in range(n):
            ax.barh("Processes", end[i] - start[i], left=start[i], color="blue", edgecolor="black")
            ax.text(start[i] + (end[i] - start[i]) / 2, 0, f"P{i+1}", ha='center', va='center', color='white', fontsize=12, fontweight='bold')

        ax.set_xlabel("Time")
        ax.set_title("Gantt Chart for CPU Scheduling")
        plt.show()

root = tk.Tk()
scheduler = CPUScheduler(root)
root.mainloop()
