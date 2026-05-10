import numpy as np
import matplotlib.pyplot as plt

# User Inputs
Am = int(input("Enter message amplitude: "))
Ac = int(input("Enter carrier amplitude: "))

fm = int(input("Enter message frequency (Hz): "))
fc = int(input("Enter carrier frequency (Hz): "))

kp = int(input("Enter phase sensitivity: "))

# Time axis
t = np.linspace(0, 1, 2000)

# Message and Carrier Signal
message = Am * np.sin(2 * np.pi * fm * t)

carrier = Ac * np.sin(2 * np.pi * fc * t)

# AM
am = (1 + message) * carrier

# FM
kf = 50
fm_signal = np.sin(
    2 * np.pi * fc * t +
    kf * np.cumsum(message) / len(t)
)

# PM
pm_signal = np.sin(
    2 * np.pi * fc * t +
    kp * message
)

# Plotting
plt.figure(figsize=(10, 10))

plt.subplot(5, 1, 1)
plt.plot(t, message)
plt.title("Message Signal")
plt.grid()

plt.subplot(5, 1, 2)
plt.plot(t, carrier)
plt.title("Carrier Signal")
plt.grid()

plt.subplot(5, 1, 3)
plt.plot(t, am)
plt.title("Amplitude Modulation (AM)")
plt.grid()

plt.subplot(5, 1, 4)
plt.plot(t, fm_signal)
plt.title("Frequency Modulation (FM)")
plt.grid()

plt.subplot(5, 1, 5)
plt.plot(t, carrier, label="Carrier")
plt.plot(t, pm_signal, label="PM Signal")
plt.title("Phase Modulation (PM)")
plt.legend()
plt.grid()

plt.xlim(0, 0.2)

plt.tight_layout()
plt.show()

## sample input
## amplitude 5,5
## frequency 2 20
## phase 10
