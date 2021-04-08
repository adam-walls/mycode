#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

# example data
mu = 85  # mean of distribution
sigma = 7  # standard deviation of distribution
x = mu + sigma * np.random.randn(350)

num_bins = 45

fig, ax = plt.subplots()

# the histogram of the data
n, bins, patches = ax.hist(x, num_bins, density=True)

# add a 'best fit' line
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, y, '--')
ax.set_xlabel('It\'s a mountain!?')
ax.set_ylabel('Decimals!')
ax.set_title(r'Histogram, big smart: $\mu=87$, $\sigma=7$')

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()

#  SAVE the graph locally
plt.savefig("/home/student/mycode/graphing/myGraph01PNG.png")
# Save to "~/static"
plt.savefig("/home/student/static/myGraph01PNG.png")
print("Graph created.")


