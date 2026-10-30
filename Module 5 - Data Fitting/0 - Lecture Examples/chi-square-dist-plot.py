from scipy.stats import chisquare, chi2
import matplotlib.pyplot as plt
import numpy as np

"""
Generate several chi2 plots based upon DoF
"""
DoF = [3, 4, 5, 7, 10]

# create x-axis for chi2 plot
for df in DoF:
    x = np.linspace(chi2.ppf(0.01, df), chi2.ppf(0.99, df), 1000)
    plt.plot(x, chi2.pdf(x, df),label='DoF='+str(df))

plt.title('Chi2 Distribution for Various Degrees of Freedom')
plt.xlabel('Chi2 Stat')
plt.legend()
plt.show()


"""
Show where a chi2 statistic falls on its distribution: the bag of candy example
5 flavors, so DoF = 5 - 1 = 4
"""
df = 4
candy_chi_stat = 52.75

x = np.linspace(0.01, 60, 1000)
plt.plot(x, chi2.pdf(x, df), label='DoF=' + str(df))
plt.axvline(candy_chi_stat, color='red', linestyle='--', label='Candy Chi2 Stat')
plt.title('Chi2 Distribution for DoF=4')
plt.xlabel('Chi2 Stat')
plt.legend()
plt.show()
