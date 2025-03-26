import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
import numpy as np

class CPUScheduler:
    def __init__(self, root):
        self.root = root
        self.root.title("CPU Scheduling Simulator")
        self.root.configure(bg="#2c3e50")

        tk.Label(root, text="CPU Scheduling Simulator", font=("Arial", 16, "bold"), fg="white", bg="#2c3e50").pack(pady=10)

        tk.Label(root, text="Enter Number of Processes:", fg="white", bg="#2c3e50").pack()
        self.process_count_entry = tk.Entry(root, width=10)
        self.process_count_entry.pack()
        tk.Button(root, text="Set Processes", command=self.create_process_entries, bg="#3498db", fg="white").pack(pady=5)

        self.process_frame = tk.Frame(root, bg="#2c3e50")
        self.process_frame.pack()

        tk.Label(root, text="Choose Scheduling Algorithm:", fg="white", bg="#2c3e50").pack()
        self.algorithm = tk.StringVar()
        self.algorithm.set("FCFS")

        algorithms = ["FCFS", "SJF", "Priority", "Round Robin"]
        for algo in algorithms:
            tk.Radiobutton(root, text=algo, variable=self.algorithm, value=algo, bg="#2c3e50", fg="white", command=self.toggle_fields).pack()

        self.quantum_label = tk.Label(root, text="Enter Time Quantum (Only for Round Robin):", fg="white", bg="#2c3e50")
        self.quantum_entry = tk.Entry(root, width=10)

        tk.Button(root, text="Run Simulation", command=self.run_simulation, bg="#27ae60", fg="white", font=("Arial", 12)).pack(pady=5)

        self.result_frame = tk.Frame(root, bg="#2c3e50")
        self.result_frame.pack()

    def create_process_entries(self):
        for widget in self.process_frame.winfo_children():
            widget.destroy()

        try:
            self.num_processes = int(self.process_count_entry.get())
            if self.num_processes <= 0:
                raise ValueError("Number of processes must be positive.")

            tk.Label(self.process_frame, text="Arrival Time", fg="white", bg="#2c3e50").grid(row=0, column=1, padx=10)
            tk.Label(self.process_frame, text="Burst Time", fg="white", bg="#2c3e50").grid(row=0, column=2, padx=10)
            tk.Label(self.process_frame, text="Priority", fg="white", bg="#2c3e50").grid(row=0, column=3, padx=10)

            self.arrival_entries = []
            self.burst_entries = []
            self.priority_entries = []

            for i in range(self.num_processes):
                tk.Label(self.process_frame, text=f"P{i+1}", fg="white", bg="#2c3e50").grid(row=i+1, column=0)
                at_entry = tk.Entry(self.process_frame, width=10)
                bt_entry = tk.Entry(self.process_frame, width=10)
                pr_entry = tk.Entry(self.process_frame, width=10)

                at_entry.grid(row=i+1, column=1, padx=10)
                bt_entry.grid(row=i+1, column=2, padx=10)
                pr_entry.grid(row=i+1, column=3, padx=10)

                self.arrival_entries.append(at_entry)
                self.burst_entries.append(bt_entry)
                self.priority_entries.append(pr_entry)

            self.toggle_fields()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def toggle_fields(self):
        if self.algorithm.get() == "Priority":
            for entry in self.priority_entries:
                entry.config(state="normal")
        else:
            for entry in self.priority_entries:
                entry.config(state="disabled")

        if self.algorithm.get() == "Round Robin":
            self.quantum_label.pack()
            self.quantum_entry.pack()
        else:
            self.quantum_label.pack_forget()
            self.quantum_entry.pack_forget()

    def run_simulation(self):
        try:
            burst_times = [int(bt.get()) for bt in self.burst_entries]
            arrival_times = [int(at.get()) for at in self.arrival_entries]
            priorities = [int(pr.get()) if self.algorithm.get() == "Priority" else 0 for pr in self.priority_entries]

            if self.algorithm.get() == "Round Robin":
                quantum = int(self.quantum_entry.get())

            if self.algorithm.get() == "FCFS":
                self.fcfs(arrival_times, burst_times)
            elif self.algorithm.get() == "SJF":
                self.sjf(arrival_times, burst_times)
            elif self.algorithm.get() == "Priority":
                self.priority_scheduling(arrival_times, burst_times, priorities)
            elif self.algorithm.get() == "Round Robin":
                self.round_robin(arrival_times, burst_times, quantum)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def fcfs(self, arrival_times, burst_times):
        processes = sorted(zip(arrival_times, burst_times), key=lambda x: x[0])
        sorted_at, sorted_bt = zip(*processes)
        self.calculate_and_display(sorted_at, sorted_bt)

    def sjf(self, arrival_times, burst_times):
        processes = sorted(zip(arrival_times, burst_times), key=lambda x: x[1])
        sorted_at, sorted_bt = zip(*processes)
        self.calculate_and_display(sorted_at, sorted_bt)

    def priority_scheduling(self, arrival_times, burst_times, priorities):
        processes = sorted(zip(priorities, arrival_times, burst_times), key=lambda x: x[0])
        _, sorted_at, sorted_bt = zip(*processes)
        self.calculate_and_display(sorted_at, sorted_bt)

    def round_robin(self, arrival_times, burst_times, quantum):
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

        self.plot_gantt_chart(start_time, end_time, n, process_order)
        self.calculate_and_display(arrival_times, burst_times, waiting_time, turnaround_time)

    def calculate_and_display(self, arrival_times, burst_times, waiting_time=None, turnaround_time=None):
        n = len(burst_times)
        if waiting_time is None and turnaround_time is None:
            waiting_time = [0] * n
            turnaround_time = [0] * n
            completion_time = [0] * n
            start_time = [0] * n
            end_time = [0] * n

            completion_time[0] = arrival_times[0] + burst_times[0]
            for i in range(1, n):
                completion_time[i] = max(completion_time[i-1], arrival_times[i]) + burst_times[i]

            for i in range(n):
                turnaround_time[i] = completion_time[i] - arrival_times[i]
                waiting_time[i] = turnaround_time[i] - burst_times[i]
                start_time[i] = waiting_time[i] + arrival_times[i]
                end_time[i] = completion_time[i]

        avg_wt = sum(waiting_time) / n
        avg_tat = sum(turnaround_time) / n

        self.plot_gantt_chart(start_time, end_time, n)

        self.display_table(arrival_times, burst_times, waiting_time, turnaround_time)

        messagebox.showinfo("Results", f"Avg Waiting Time: {avg_wt:.2f}\nAvg Turnaround Time: {avg_tat:.2f}")

    def display_table(self, arrival_times, burst_times, waiting_time, turnaround_time):
        for widget in self.result_frame.winfo_children():
            widget.destroy()

        headers = ["Process", "Arrival Time", "Burst Time", "Waiting Time", "Turnaround Time"]
        table = ttk.Treeview(self.result_frame, columns=headers, show="headings", height=8)

        for header in headers:
            table.heading(header, text=header)
            table.column(header, width=100, anchor="center")

        for i in range(len(arrival_times)):
            table.insert("", "end", values=(f"P{i+1}", arrival_times[i], burst_times[i], waiting_time[i], turnaround_time[i]))

        table.pack()

    def plot_gantt_chart(self, start, end, n, process_order=None):
        colors = plt.cm.tab10(np.linspace(0, 1, n))
        fig, ax = plt.subplots(figsize=(10, 2))  # Set a smaller figure height for a single line Gantt chart

        # Create a horizontal bar for each process on the same line
        for i in range(n):
            ax.barh(0, end[i] - start[i], left=start[i], color=colors[i], edgecolor="black", height=0.8)  # height adjusted to fit all processes

            # Label each process at the center of its corresponding bar
            ax.text(start[i] + (end[i] - start[i]) / 2, 0, f"P{i+1}", ha='center', va='center', color='white', fontsize=12, fontweight='bold')

        ax.set_yticks([0])  # Only one line, so set the y-tick to zero
        ax.set_yticklabels(["Processes"])  # Label that all processes are on the same line
        ax.set_xlabel("Time")
        ax.set_title("Gantt Chart")
        plt.tight_layout()
        plt.show()

root = tk.Tk()
scheduler = CPUScheduler(root)
root.mainloop()
