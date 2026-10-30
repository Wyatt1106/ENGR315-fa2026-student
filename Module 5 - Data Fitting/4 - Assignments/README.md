**5.4.1 - Distributions**

Complete three functions in the template that fit samples to a distribution, the same way as the Module 5.1 lecture
example (distribution-fit.py). Each function is graded on its own, so they can be done in any order.

    fit_normal(_samples)              (mean, standard deviation) of the fitted normal distribution
    fit_exponential(_samples)         beta (the scale) of the fitted exponential distribution, with the location fixed at 0 (floc=0)
    normal_range(_samples, _fraction) (lower, upper) range holding the middle _fraction (e.g. 0.95) of the fitted normal distribution

Your functions are tested on different random samples each time they are graded, so they must work for any samples.
The section at the bottom of the template prints the expected results for a fixed set of samples and plots your fitted
curves against the ideal ones.

Submit only your testing-distributions-student.py file to Gradescope (3 submissions allowed).

**5.4.2 - Chi-Square Goodness of Fit**

Complete three functions in the template that run chi-square goodness of fit tests, the same way as the Module 5.2
lecture examples (chi-square-gof-categorical.py and chi-square-dist-fit.py). Each function is graded on its own.

    categorical_test(_observed, _expected, _alpha)            (chi2 statistic, p-value, reject) for counts in categories
    expected_normal_counts(_bins, _mu, _std, _num_samples)    expected count in each bin for a normal distribution (CDF differences)
    normal_fit_test(_samples, _alpha)                         (chi2 statistic, p-value, reject) for samples against their fitted normal distribution

reject is True when the null hypothesis is rejected (p-value < alpha) and False when we fail to reject it.
For normal_fit_test, use 9 bin edges from (mean - 2 * std) to (mean + 2 * std) plus -inf and inf, and ddof=2 because the
mean and standard deviation are estimated from the samples. The steps are listed in the template.

Your functions are tested on different random data each time they are graded. The section at the bottom of the template
prints the expected results for the lecture examples and a fixed set of samples.

Submit only your chi-square-gof-student.py file to Gradescope (3 submissions allowed).
