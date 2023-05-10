import matplotlib.pyplot as plt
import numpy as np

# https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/

# Sequences
linear_sequence = [1, 2, 3, 4, 5, 6, 7, 10, 15, 20]
exponential_sequence = np.exp(np.linspace(0, 10, 10))

fig, ax = plt.subplots()

# Plot linear sequence, and set tick labels to the same color
ax.plot(linear_sequence, color='red')
ax.tick_params(axis='y', labelcolor='red')

# Generate a new Axes instance, on the twin-X axes (same position)
ax2 = ax.twinx()

# Plot exponential sequence, set scale to logarithmic and change tick color
ax2.plot(exponential_sequence, color='green')
ax2.tick_params(axis='y', labelcolor='green')

plt.show()