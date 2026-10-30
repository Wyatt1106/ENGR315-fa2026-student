import numpy as np
from scipy.stats import chisquare, chi2
import matplotlib.pyplot as plt

"""
Example #1: Bag of Candy
https://www.jmp.com/en_us/statistics-knowledge-portal/chi-square-test/chi-square-goodness-of-fit-test.html
"""

# observed number of pieces from a bag of candy. Each entry is a flavor: apple, lime, cherry, orange, grape
observed = [180, 250, 120, 225, 225]

# expected number of pieces if the bag is evenly distributed. 5 flavors, so DoF = 5 - 1 = 4
expected = [200, 200, 200, 200, 200]

# set alpha value for test
alpha = 0.05

# conduct chi2 test
# Null hypothesis is counts/distributions are "equal", alternative is they are "not equal"
(chi_stat, p_value) = chisquare(f_obs=observed, f_exp=expected)

print('Chi2 stat: ', chi_stat, 'p-value: ', p_value)

if p_value < alpha:
    print('Reject null hypothesis. Counts are not equal.')
else:
    print('Fail to reject null hypothesis. No evidence the counts differ.')

"""
Example #2: 'Random' Deck of Cards
https://lsj.readthedocs.io/en/latest/Ch10/Ch10_ChiSquare_1/
"""
# observed number of cards 'pulled' from a random deck: clubs, diamonds, hearts, spades. Should total to 200.
observed = [35, 51, 64, 50]

# expected number of cards from a random deck: clubs, diamonds, hearts, and spades. Should total to 200.
expected = [50, 50, 50, 50]

# set alpha value for test
alpha = 0.05

# conduct chi2 test
# Null hypothesis is counts/distributions are "equal", alternative is they are "not equal"
(chi_stat, p_value) = chisquare(f_obs=observed, f_exp=expected)

print('Chi2 stat: ', chi_stat, 'p-value: ', p_value)

if p_value < alpha:
    print('Reject null hypothesis. Counts are not equal.')
else:
    print('Fail to reject null hypothesis. No evidence the counts differ.')

"""
Example 3: Assessing Random Dice Rolls
https://www.stat.uchicago.edu/~yibi/teaching/stat220/17aut/Lectures/L25.pdf
"""

# observed number of dice rolls: one, two, three, four, five, six. Should total 315672.
observed = [53222, 52118, 52465, 52338, 52244, 53285]

# expected number of dice rolls: one, two, three, four, five, six. Should total 315672.
expected = [52612, 52612, 52612, 52612, 52612, 52612]

# set alpha value for test
alpha = 0.05

# conduct chi2 test
# Null hypothesis is counts/distributions are "equal", alternative is they are "not equal"
(chi_stat, p_value) = chisquare(f_obs=observed, f_exp=expected)

print('Chi2 stat: ', chi_stat, 'p-value: ', p_value)

if p_value < alpha:
    print('Reject null hypothesis. Counts are not equal.')
else:
    print('Fail to reject null hypothesis. No evidence the counts differ.')

"""
Example 4: Flip a Penny
https://researchguides.library.vanderbilt.edu/c.php?g=156859&p=1171653
"""

# observed number of penny flips: heads and tails
observed = [46, 41]

# expected number of penny flips: heads and tails
expected = [43.5, 43.5]

# set alpha value for test
alpha = 0.05

# conduct chi2 test
# Null hypothesis is counts/distributions are "equal", alternative is they are "not equal"
(chi_stat, p_value) = chisquare(f_obs=observed, f_exp=expected)

print('Chi2 stat: ', chi_stat, 'p-value: ', p_value)

if p_value < alpha:
    print('Reject null hypothesis. Counts are not equal.')
else:
    print('Fail to reject null hypothesis. No evidence the counts differ.')
