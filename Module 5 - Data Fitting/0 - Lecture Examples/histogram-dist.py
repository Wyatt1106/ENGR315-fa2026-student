import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

"""
Numpy example
https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
"""

# Sample a Normal distribution
mu, sigma = 0, 1
samples = np.random.normal(loc=mu, scale=sigma, size=1000)

# Bin and plot samples
num_bins = 30
count, bins, ignored = plt.hist(samples, bins=num_bins, density=True, label='Sampled and Binned Normal Distribution',
                                edgecolor='k')

# Plot expected distribution
x = np.linspace(min(samples), max(samples), 100)
plt.plot(x, norm.pdf(x, loc=mu, scale=sigma), linewidth=2, color='r', label='Expected Normal Distribution')
plt.legend()
plt.show()