**4.4.0 - Pandas Tensile Summary**

Complete six functions in the template to analyze the tensile data from Module 3 with Pandas. The data is the CSV file
you wrote in 3.4.3 (a copy is in data/tensile/tensile_data.csv). Each function is graded on its own, so they can be done in any order.

    load_tensile_data(_path)                      Load the CSV file into a DataFrame
    select_material(_df, _material)               Rows for one material (boolean selection)
    select_strong(_df, _material, _min_yield)     Rows for one material with yield strength above a value (combine two conditions with &)
    get_values(_df, _material, _column)           One column of one material as a Numpy array
    material_statistics(_df, _material, _column)  (mean, standard deviation) of one column of one material
    summary_table(_df, _columns)                  {material: {column: (mean, std)}} for every material in the data

Your functions are tested on different tensile files than the course file (other materials, other numbers of samples, rows in a different order),
so they must not assume 1045CR, 2024 and PMMA. When complete, the template prints the same table shown in lecture.

Submit only your pandas-tensile-student.py file to Gradescope (3 submissions allowed).

**4.4.1 - One Sided for One Sample Tests**

Complete the one_sided_tests function for One Sample. It is provided a list of files that contain samples from a distribution.
The function should return those file names where the sample rejects the NULL hypothesis during a one-sided t-test.
Note: your solution will need to open and load each file. It is suggested to use numpy to do this.

    def one_sided_tests(_files: list, _mean: float, _alpha: float, _less_than: bool):
        Conduct a one-sided t-test, either left or right sided. Null hypothesis is the means are equal.
        :param _files: List of file names to be tested. Assume they can be loaded directly as a numpy array
        :param _mean: The test statistic mean for the hypothesis
        :param _alpha: Desired alpha value for t-test
        :param _less_than: If true, then a left-sided (<) t-test is performed. Otherwise, a right-sided test (>)
        :return: A list of files where the null hypothesis is rejected

Your function is tested on different random files each time it is graded, so it must use every parameter.
The test at the bottom of the template creates a few files you can check against.

Submit only your one-sided-student.py file to Gradescope (3 submissions allowed).

**4.4.2 - Two Sided for Two Samples Tests**

Complete the two_sided_tests function for Two Samples. It is provided two lists of files that contain samples from a distribution.
The first file of the first list is compared with the first file of the second list, the second with the second, and so on.
The function should return those pairs of file names where the sample means differ, that is, where the NULL hypothesis is rejected
during a two-sided t-test. Use Welch's t-test (equal_var=False in ttest_ind), because the two samples in a pair may have different
sizes and spreads.
Note: your solution will need to open and load each file. It is suggested to use numpy to do this.

    def two_sided_tests(_files1: list, _files2: list, _alpha: float):
        """
        Conduct a two-sided t-test. Null hypothesis is they are equal.
        :param _files1: List of files to be tested. Assume they can be loaded directly as a numpy array
        :param _files2: List of files to be tested. Assume they can be loaded directly as a numpy array
        :param _alpha: Desired alpha value for t-test
        :return: A list of file pairs (tuples) where the null hypothesis is rejected
        """

Your function is tested on different random files each time it is graded, so it must use every parameter.
The test at the bottom of the template creates a few files you can check against.

Submit only your two-sided-student.py file to Gradescope (3 submissions allowed).
