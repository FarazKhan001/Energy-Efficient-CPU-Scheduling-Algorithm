# Energy-Efficient-CPU-Scheduling-Algorithm

The Energy Efficient CPU Scheduling Algorithm aims to optimize power consumption while ensuring efficient task execution. Traditional scheduling methods prioritize execution speed but overlook energy efficiency. This project introduces a new algorithm that dynamically manages CPU power by adjusting frequency and workload distribution, reducing unnecessary energy use.
•	A scheduling algorithm that minimizes energy consumption.
•	A working simulation that demonstrates energy efficiency benefits.

![image alt](https://github.com/FarazKhan001/Energy-Efficient-CPU-Scheduling-Algorithm/blob/276894b720509b7b1fbfa6d7d09c76364866f3c7/Picture1.jpg)

## Standard CPU scheduling techniques
### A.	First-Come, First-Served (FCFS)
o	Type: Non-preemptive
o	The process that arrives first gets executed first.
o	Managed using a FIFO (First-In-First-Out) queue.

Advantages:
o	Simple to implement.
o	Fair since processes are scheduled in order of arrival.
Disadvantages:
o	Convoy effect: Shorter processes may wait long due to longer processes ahead.
o	High average waiting time in some cases.


### B.	 Shortest Job Next (SJN) / Shortest Job First (SJF)
o	Type: Non-preemptive or Preemptive
o	The process with the shortest burst time is executed first.
o	If preemptive, it is called Shortest Remaining Time First (SRTF).

Advantages:
o	Low average waiting time.
Disadvantages:
o	Starvation: Longer processes may wait indefinitely.
o	Requires knowledge of burst time in advance.

### C.	Priority Scheduling
o	Type: Non-preemptive or Preemptive
o	Each process is assigned a priority.
o	The process with the highest priority executes first.
o	If two processes have the same priority, FCFS is used.

Advantages:
o	Useful for real-time systems where priorities matter.
Disadvantages:
o	Starvation: Low-priority processes may never execute.
o	Solution: Aging (increase priority over time).

### D.	Round Robin (RR)
o	Type: Preemptive
o	Each process gets a fixed time quantum.
o	If a process is not finished within its quantum, it moves to the end of the queue.

Advantages:
o	Fair scheduling: Every process gets CPU time.
o	Responsive for time-sharing systems.
Disadvantages:
o	Higher average turnaround time if the time quantum is too small.

### E.	Comparison of CPU Scheduling Algorithms
![image alt](https://github.com/FarazKhan001/Energy-Efficient-CPU-Scheduling-Algorithm/blob/276894b720509b7b1fbfa6d7d09c76364866f3c7/Screenshot%202025-03-23%20140724.png)

## Scope
•	Focus: Reducing CPU power consumption in single-core and multi-core environments.
•	Techniques Used: Dynamic Voltage and Frequency Scaling (DVFS), workload balancing, and adaptive scheduling.
•	Implementation: A simulated CPU scheduler to evaluate efficiency improvements.
 

## 	Optimal Energy-Efficient Scheduling Algorithms
Energy efficiency in CPU scheduling focuses on reducing power consumption while maintaining system performance. Some popular energy-efficient scheduling algorithms include:
### A. Dynamic Voltage and Frequency Scaling (DVFS)
🔹 Concept: Adjusts CPU frequency and voltage dynamically based on workload.
🔹 How it saves energy: Lowering the frequency reduces power consumption since power ∝ voltage²   × frequency.
🔹 Example: A CPU running at 3 GHz may scale down to 1 GHz when idle, consuming much less power.
🔹 Used in: Mobile devices, laptops, and modern CPUs with power-saving modes.

### B. Dynamic Power Management (DPM)
🔹 Concept: Puts CPU into low-power states (sleep, idle, deep sleep) when not in use.
🔹 How it saves energy: Reduces power consumption by switching off unused components.
🔹 Example: A CPU may enter a sleep state if there’s no process in the ready queue.
🔹 Used in: Embedded systems, real-time operating systems, and battery-powered devices.

### C. Energy-Aware Scheduling (EAS)
🔹 Concept: Assigns tasks to CPU cores based on their energy efficiency, rather than just performance.
🔹 How it saves energy: Tasks with lower priority or lesser CPU demand are scheduled on energy-efficient cores.
🔹 Example: In ARM big.LITTLE architecture, lightweight tasks run on LITTLE cores (low power), while heavy tasks use big cores (high performance).
🔹 Used in: Android smartphones, ARM processors.

### D. Sleep and Wake-Up Scheduling
🔹 Concept: Predicts idle periods and proactively puts the CPU to sleep.
🔹 How it saves energy: Reduces unnecessary power consumption by turning off the CPU during long idle periods.
🔹 Example: If a process is waiting for user input, the CPU enters a sleep state until the input arrives.
🔹 Used in: IoT devices, real-time systems.

### E. Green Scheduling Algorithms
🔹 Concept: Modifies traditional scheduling algorithms (like Round Robin or Shortest Job Next) to focus on power savings.
🔹 How it saves energy: Introduces energy-aware heuristics, such as executing short tasks first to allow longer sleep periods.
🔹 Example: Energy-Aware Round Robin (EARR) dynamically adjusts time quantum based on energy consumption.
🔹 Used in: Cloud computing, data centers.

### 	Power Management for Different Systems
•	Mobile Devices: DVFS + Energy-Aware Scheduling (EAS) – >Balances performance and power for extended battery life.
•	Data Centers: Dynamic Power Management (DPM) + Green Scheduling – >Reduces energy costs by optimizing resource usage.
•	Real-Time Systems: Sleep & Wake-Up Scheduling – >Maximizes battery life while ensuring real-time responsiveness.

![image alt](https://github.com/FarazKhan001/Energy-Efficient-CPU-Scheduling-Algorithm/blob/276894b720509b7b1fbfa6d7d09c76364866f3c7/Picture2.png)


## 	Functionalities
#### A)	Scheduling Algorithm
•	Implements energy-aware scheduling policies using power-efficient task assignment.
•	Uses real-time power monitoring to adjust CPU frequency dynamically.
•	Supports multiple scheduling techniques for performance comparison.
#### B)	Simulation & Benchmarking
•	Simulates different workloads to test CPU scheduling strategies.
•	Collects power and execution metrics under varied system loads.
•	Provides a logging mechanism for detailed performance analysis.
#### C)	Data Visualization & Analysis
•	Generates graphs displaying CPU energy consumption.
•	Compares scheduling algorithms using key statistical metrics.
•	Outputs detailed reports summarizing efficiency improvements.

## 	Future of Energy Efficient Scheduling
The future of Energy Efficient Scheduling will focus on optimizing power usage without sacrificing performance. Key developments include:
1.	AI and Machine Learning: Algorithms will use AI to predict workloads and adjust power consumption dynamically, ensuring energy efficiency based on real-time data.
2.	Real-Time Energy Monitoring: Systems will adapt power settings instantly, lowering voltage and frequency when the load is light and increasing them during high workloads.
3.	Green Computing: Scheduling will consider environmental impacts, reducing carbon footprints by leveraging renewable energy and minimizing power usage in data centers.
4.	Edge and IoT Devices: Energy-efficient scheduling will optimize the power usage of devices with limited resources, ensuring longer battery life while meeting real-time processing needs.
5.	Advanced DVFS: Dynamic Voltage and Frequency Scaling will become more precise, allowing for fine-tuned energy savings without compromising performance.
Overall, energy-efficient scheduling will combine AI, real-time adjustments, and greener technologies to maximize efficiency in various computing environments.


 ## Flow Diagram
![image alt](https://github.com/FarazKhan001/Energy-Efficient-CPU-Scheduling-Algorithm/blob/276894b720509b7b1fbfa6d7d09c76364866f3c7/11.jpg)

## 	Conclusion
Energy-efficient CPU scheduling plays a crucial role in optimizing power consumption while maintaining system performance. As computing systems become increasingly complex and power consumption concerns grow, energy-efficient scheduling algorithms are essential for ensuring sustainable operation. By dynamically adjusting factors like CPU frequency and voltage in response to workload changes, these algorithms can reduce energy waste without compromising on performance.
The future of energy-efficient scheduling lies in integrating advanced techniques such as AI and machine learning, which will enable real-time adjustments based on workload predictions. This will allow systems to not only conserve energy but also adapt intelligently to varying demands. Furthermore, the growing focus on green computing and edge devices means that energy-efficient scheduling will be integral in reducing the environmental impact of modern computing systems.
Overall, energy-efficient CPU scheduling is a key factor in creating more sustainable and efficient computing environments, particularly as the demand for high-performance, low-power systems continues to rise.
