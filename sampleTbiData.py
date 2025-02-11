import numpy as np
import matplotlib.pyplot as plt

# Parameters
sampling_rate = 3.91  # Hz
duration = 300  # seconds (5 minutes)
time = np.linspace(0, duration, int(sampling_rate * duration))

# Simulated signals
np.random.seed(42)
baseline_HbO = 70 + 0.5 * np.sin(2 * np.pi * time / 60) + np.random.normal(0, 0.5, len(time))
baseline_HbR = 30 + 0.3 * np.sin(2 * np.pi * time / 60) + np.random.normal(0, 0.3, len(time))

# Task-evoked response (e.g., working memory task)
task_start = int(120 * sampling_rate)  # Task starts at 120 seconds
task_end = int(180 * sampling_rate)   # Task ends at 180 seconds
task_HbO = baseline_HbO.copy()
task_HbR = baseline_HbR.copy()

# Add TBI-specific hemodynamic response during the task
task_HbO[task_start:task_end] += -5 + np.random.normal(0, 0.5, task_end - task_start)
task_HbR[task_start:task_end] += 3 + np.random.normal(0, 0.3, task_end - task_start)

# Plotting the simulated data
plt.figure(figsize=(12, 6))
plt.plot(time, baseline_HbO, label="Baseline HbO", alpha=0.7)
plt.plot(time, baseline_HbR, label="Baseline HbR", alpha=0.7)
plt.plot(time[task_start:task_end], task_HbO[task_start:task_end], label="Task HbO (TBI)", color="red")
plt.plot(time[task_start:task_end], task_HbR[task_start:task_end], label="Task HbR (TBI)", color="blue")
plt.xlabel("Time (s)")
plt.ylabel("Hemoglobin Concentration (µM)")
plt.title("Simulated fNIRS Signal Data for TBI")
plt.legend()
plt.show()