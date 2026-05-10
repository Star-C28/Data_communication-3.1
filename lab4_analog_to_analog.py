import numpy as np
import matplotlib.pyplot as plt

# User Inputs
fm = int(input("Enter message frequency (Hz): "))
fc = int(input("Enter carrier frequency (Hz): "))

# Time axis
t = np.linspace(0, 1, 1000)

# Message Signal
message = np.sin(2 * np.pi * fm * t)

# Carrier Signal
carrier = np.sin(2 * np.pi * fc * t)

# AM Modulation
am = (1 + message) * carrier

# FM Modulation
kf = 80
fm_signal = np.sin(
    2 * np.pi * fc * t +
    kf * np.cumsum(message) / 100
)

# PM Modulation
kp = 10
pm_signal = np.sin(
    2 * np.pi * fc * t +
    kp * message
)

# Plotting
plt.figure(figsize=(10, 8))

# Message Signal
plt.subplot(4, 1, 1)
plt.plot(t, message)
plt.title("Message Signal")
plt.grid()

# AM Signal
plt.subplot(4, 1, 2)
plt.plot(t, am)
plt.title("Amplitude Modulation (AM)")
plt.grid()

# FM Signal
plt.subplot(4, 1, 3)
plt.plot(t, fm_signal)
plt.title("Frequency Modulation (FM)")
plt.grid()

# PM Signal
plt.subplot(4, 1, 4)
plt.plot(t, pm_signal)
plt.title("Phase Modulation (PM)")
plt.grid()

# Zoom for clear view
plt.xlim(0, 0.3)

plt.tight_layout()
plt.show()

#Sample input 2 20
