import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

"""
Step 1: Load pre-processed data that has already been filtered through the Pan Tompkins process
"""
# list of available pre-processed datasets in the data/ekg folder
available_datasets = ["mitdb_201", "mitdb_213", "mitdb_219", "nstdb_118e00", "nstdb_118e06", "qtdb_sel104"]

# select a data set from the enumerated list above
dataset = available_datasets[0]

# load saved data from numpy array
filepath = '../../../data/ekg/processed_'+dataset+'.npy'

# once loaded, place in an array called signal. This is a 1-D signal of processed
# heart beat data. No filtering/processing is required.
signal = np.load(filepath)

"""
Step 2: Determine how much data to use...
"""
# If you wish to only run on ~10s of data uncomment the line below
# if you wish to run on all data, comment out this line
signal = signal[0:3300]


"""
Step 3: Attempt simple thresholding with timeout to detect the signal
Adjust the values for threshold and timeout to change the detection method/approach
"""

# set a detection threshold (YOUR VALUE BELOW)
detection_threshold = -1

# set a heart beat time out (YOUR VALUE BELOW)
detection_time_out = -1

# track the last time we found a beat
last_detected_index = -1

# keep not of where we are in the data
current_index = 0

# store indices of all found beats
beats_detected = list()

"""
Step 4: Manually iterate through the signal and apply the threshold with timeout
"""

# loop through signal finding beats
for value in signal:
    ## Use a conditional statement to see if the signal is above a threshold...

    ## Once an index is found, place the index in the beats_detected list
    current_index += 1

print("Within the sample we found ", len(beats_detected), " heart beats with manual search!")

beats_detected = np.asarray(beats_detected, dtype=int)

"""
Step 5: Plot the results
"""

# plot the original data
plt.plot(signal)
plt.title('Filtered ECG Signal with Beat Annotations')

plt.plot(beats_detected, signal[beats_detected], 'X')
plt.show()
