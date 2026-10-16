import sys
import os


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples.
    Each tuple describes one entry in the source data set.

    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing
             (date, county, state, fips, cases, deaths) information

    ____________________ DO NOT MODIFY THIS FUNCTION ____________________
    """

    # data point list
    data = []

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        try:
            (date, county, state, fips, cases, deaths) = \
                line.rstrip().split(",")
        except ValueError:
            continue

        # clean up the data to remove empty entries
        if cases == '':
            cases = 0

        if deaths == '':
            deaths = 0

        # convert elements into ints
        try:
            entry = (
                date,
                county,
                state,
                fips,
                int(cases),
                int(deaths)
            )
        except ValueError:
            print('Invalid parse of ', line)
            continue

        # place entries as tuple into list
        data.append(entry)

    return data


# ============================================================
# YOUR CODE HERE
# ============================================================


# ------------------------------------------------------------
# Load the COVID data
# ------------------------------------------------------------

# Find the folder where this Python program is located.
current_folder = os.path.dirname(os.path.abspath(__file__))

# The COVID data is located in:
# ENGR315-fa2026-student/data/covid/us-counties.csv
#
# student_template.py is located in:
# ENGR315-fa2026-student/Exams/Assignment 1 - COVID Data/
#
# Therefore, go up two folders and then into data/covid.
file_path = os.path.join(
    current_folder,
    "..",
    "..",
    "data",
    "covid",
    "us-counties.csv"
)

# Read the NYT COVID data using the provided function.
data = parse_nyt_data(file_path)


# ------------------------------------------------------------
# Separate the Harrisonburg and Rockingham County data
# ------------------------------------------------------------

harrisonburg = []
rockingham = []

for entry in data:

    county = entry[1]
    state = entry[2]

    # Only use Virginia data.
    if state == "Virginia":

        if county == "Harrisonburg city":
            harrisonburg.append(entry)

        elif county == "Rockingham":
            rockingham.append(entry)


# Sort both lists by date.
harrisonburg.sort()
rockingham.sort()


# ------------------------------------------------------------
# Calculate daily new cases
# ------------------------------------------------------------
# The NYT data contains cumulative case totals.
# Therefore:
#
# new cases = today's total cases - yesterday's total cases
# ------------------------------------------------------------

def get_daily_cases(county_data):

    daily_cases = []

    for i in range(len(county_data)):

        date = county_data[i][0]
        total_cases = county_data[i][4]

        # The first entry does not have a previous day
        # in the data for this locality.
        if i == 0:
            new_cases = total_cases

        else:
            previous_cases = county_data[i - 1][4]
            new_cases = total_cases - previous_cases

        daily_cases.append((date, new_cases))

    return daily_cases


# Calculate daily cases for both locations.
harrisonburg_daily = get_daily_cases(harrisonburg)
rockingham_daily = get_daily_cases(rockingham)


# ============================================================
# QUESTION 1
#
# When was the first positive COVID case in Harrisonburg?
# When was the first positive case in Rockingham County?
# ============================================================

def first_positive_case(county_data):

    for entry in county_data:

        date = entry[0]
        cases = entry[4]

        # Find the first date where cumulative cases
        # are greater than zero.
        if cases > 0:
            return date

    return None


# Find the first positive case for each location.
harrisonburg_first = first_positive_case(harrisonburg)
rockingham_first = first_positive_case(rockingham)


# Print answers for Question 1.
print("==================================================")
print("QUESTION 1")
print("==================================================")

print(
    "First positive COVID case in Harrisonburg:",
    harrisonburg_first
)

print(
    "First positive COVID case in Rockingham County:",
    rockingham_first
)

print()


# ============================================================
# QUESTION 2
#
# On what date was the greatest number of new cases reported
# in Harrisonburg?
#
# What date was the greatest number of new cases reported
# in Rockingham County?
# ============================================================

def greatest_new_cases(daily_data):

    greatest_date = daily_data[0][0]
    greatest_cases = daily_data[0][1]

    for date, new_cases in daily_data:

        if new_cases > greatest_cases:

            greatest_cases = new_cases
            greatest_date = date

    return greatest_date, greatest_cases


# Find the maximum daily cases for Harrisonburg.
harrisonburg_max_date, harrisonburg_max_cases = \
    greatest_new_cases(harrisonburg_daily)

# Find the maximum daily cases for Rockingham County.
rockingham_max_date, rockingham_max_cases = \
    greatest_new_cases(rockingham_daily)


# Print answers for Question 2.
print("==================================================")
print("QUESTION 2")
print("==================================================")

print("Harrisonburg:")
print("Date:", harrisonburg_max_date)
print("New cases:", harrisonburg_max_cases)

print()

print("Rockingham County:")
print("Date:", rockingham_max_date)
print("New cases:", rockingham_max_cases)

print()


# ============================================================
# QUESTION 3
#
# What was the worst seven-day period in Harrisonburg city
# for new COVID cases?
#
# What was the worst seven-day period in Rockingham County?
#
# The worst period is the seven-day period with the greatest
# total number of new cases.
# ============================================================

def worst_seven_days(daily_data):

    max_cases = 0
    start_date = ""
    end_date = ""

    # Go through every possible group of seven consecutive
    # entries in the daily data.
    for i in range(len(daily_data) - 6):

        seven_day_total = 0

        # Add the number of new cases for the seven days.
        for j in range(i, i + 7):

            seven_day_total += daily_data[j][1]

        # If this seven-day period has more cases than
        # the previous maximum, save its information.
        if seven_day_total > max_cases:

            max_cases = seven_day_total
            start_date = daily_data[i][0]
            end_date = daily_data[i + 6][0]

    return start_date, end_date, max_cases


# Find Harrisonburg's worst seven-day period.
harrisonburg_start, harrisonburg_end, harrisonburg_7day_cases = \
    worst_seven_days(harrisonburg_daily)

# Find Rockingham County's worst seven-day period.
rockingham_start, rockingham_end, rockingham_7day_cases = \
    worst_seven_days(rockingham_daily)


# Print answers for Question 3.
print("==================================================")
print("QUESTION 3")
print("==================================================")

print("Harrisonburg:")

print(
    "Worst seven-day period:",
    harrisonburg_start,
    "through",
    harrisonburg_end
)

print(
    "New cases during this period:",
    harrisonburg_7day_cases
)

print()

print("Rockingham County:")

print(
    "Worst seven-day period:",
    rockingham_start,
    "through",
    rockingham_end
)

print(
    "New cases during this period:",
    rockingham_7day_cases
)

print()