import numpy as np
import matplotlib.pyplot as plt

# User Input
user_input = input("Enter bits: ")
bits = [int(b) for b in user_input.replace(" ", "")]

spb = 100   # Samples per bit
fc = 5      # Carrier frequency

digital = []
ask = []
fsk = []
psk = []
time = []

for i, bit in enumerate(bits):

    t = np.linspace(i, i + 1, spb)
    time.extend(t)

    # Digital Signal
    digital.extend([bit] * spb)

    # ASK Modulation
    amp = 1 if bit == 1 else 0.2
    ask.extend(amp * np.sin(2 * np.pi * fc * t))

    # FSK Modulation
    freq = 8 if bit == 1 else 3
    fsk.extend(np.sin(2 * np.pi * freq * t))

    # PSK Modulation
    phase = 0 if bit == 1 else np.pi
    psk.extend(np.sin(2 * np.pi * fc * t + phase))

# Plotting
plt.figure(figsize=(10, 8))

# Digital Signal
plt.subplot(4, 1, 1)
plt.plot(time, digital)
plt.title("Digital Signal")
plt.ylim(-0.5, 1.5)
plt.grid()

# ASK
plt.subplot(4, 1, 2)
plt.plot(time, ask)
plt.title("ASK Modulation")
plt.grid()

# FSK
plt.subplot(4, 1, 3)
plt.plot(time, fsk)
plt.title("FSK Modulation")
plt.grid()

# PSK
plt.subplot(4, 1, 4)
plt.plot(time, psk)
plt.title("PSK Modulation")
plt.grid()

plt.tight_layout()
plt.show()

# 10110010
