#!/usr/bin/env python3

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='Squiggly Length (sL)', ylabel='Squiggly Height (sH)',
       title='Squiggly Wiggly')
ax.grid()

# SAVE the graph locally
plt.savefig("/home/student/mycode/graphing/myGraph02PNG.png")
# Save to "~/static"
plt.savefig("/home/student/static/myGraph02PNG.png")       
print("Graph created.")

fig.savefig("test.png")
plt.show()
