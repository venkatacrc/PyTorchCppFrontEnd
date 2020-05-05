"""
    Simple Python code to plot the benchmark performance data.
"""
import numpy as np
import matplotlib.pyplot as plt

x = [500, 1000, 1500, 2500, 5000, 50000]      # epochs
y1 = [5.14, 8.05, 9.54, 15.83, 30.46, 275.37] # Python 
y2 = [1.99, 3.31, 5.04, 8.15, 14.82, 140.76]  # C++

fig, ax = plt.subplots()

line1, = ax.plot(x, y1, label='Python')

line2, = ax.plot(x, y2, label='C++')

ax.legend()
ax.set_xlabel('number of epochs')
ax.set_ylabel('runtime in secs(ivybridge Ubuntu 18.04)')
plt.show()
