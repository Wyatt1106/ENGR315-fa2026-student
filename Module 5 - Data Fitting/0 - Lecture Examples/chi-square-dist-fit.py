import numpy as np
from scipy.stats import norm, chisquare
import matplotlib.pyplot as plt

"""
Example #1:
Replicating work from here: http://www.stat.yale.edu/Courses/1997-98/101/chigf.htm
"""

# load set of observation data
observations = np.loadtxt('yale-randoms.txt')

# bin the examples
bins = np.linspace(-2, 2, 9)  # 9 edges from -2 to 2 make 8 bins

# Trick from StackExchange to add infinite on each end (10 bins in total)
# https://stackoverflow.com/questions/11633874/numpy-use-bins-with-infinite-range
bins = np.r_[-np.inf, bins, np.inf]

# place observations into bins
observed_counts, observed_edges = np.histogram(observations, bins=bins, density=False)

# expected counts come from the probability of each bin under the distribution
expected_mu = 0
expected_std = 1

# the CDF difference between bin edges gives the probability of a value
# being within each bin
expected_prob = np.diff(norm.cdf(bins, loc=expected_mu, scale=expected_std))

# Expected frequency for each bin
expected_counts = expected_prob * len(observations)

# Conduct chi2 test
# ddof=2: the data were standardized with their own mean and std (2 estimated parameters)
(chi_stat, p_value) = chisquare(f_obs=observed_counts, f_exp=expected_counts, ddof=2)
print('Chi2 stat: ', chi_stat, 'p-value: ', p_value)

alpha = 0.05
if p_value < alpha:
    print('Reject null hypothesis. Counts are not equal.')
else:
    print('Fail to reject null hypothesis. No evidence the counts differ.')
