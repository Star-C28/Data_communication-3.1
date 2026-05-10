
import numpy as np
import matplotlib.pyplot as plt

# User Inputs
fm = int(input("Enter message frequency (Hz): "))
fs = int(input("Enter continuous sampling frequency: "))
sample_rate = int(input("Enter number of samples: "))
levels = int(input("Enter quantization levels: "))

# Time axis
# np.linspace(start, stop, number_of_points)
t = np.linspace(0, 1, fs)

# Analog Signal
analog = np.sin(2 * np.pi * fm * t)

# Sampling
ts = np.linspace(0, 1, sample_rate)
samples = np.sin(2 * np.pi * fm * ts)

# Quantization
quantized = np.round((samples + 1) * (levels - 1) / 2)

# Number of bits required
bits = int(np.ceil(np.log2(levels)))

# Convert Quantized Values to Binary
binary = [format(int(q), f'0{bits}b') for q in quantized]

# Display Results
print("\nSampled Values:")
print(samples)

print("\nQuantized Values:")
print(quantized)

print("\nBinary Codes:")
print(binary)

# Plotting
plt.figure(figsize=(10, 7))

# Analog Signal
plt.subplot(3, 1, 1)
plt.plot(t, analog)
plt.title("Analog Signal")
plt.grid()

# Sampled Signal
plt.subplot(3, 1, 2)
plt.stem(ts, samples)
plt.title("Sampled Signal")
plt.grid()

# Quantized Signal
plt.subplot(3, 1, 3)
plt.step(ts, quantized, where='mid')
plt.title("Quantized Signal")
plt.grid()

plt.tight_layout()
plt.show()


# Enter message frequency (Hz): 5
# Enter continuous sampling frequency: 1000
# Enter number of samples: 20
# Enter quantization levels: 8

