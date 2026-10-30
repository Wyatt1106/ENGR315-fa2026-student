import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

"""
Step 1: Load pre-processed data that has already been filtered through the PT process
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
Step 3: Use Find Peaks
"""

# you may want to explore various parameters for the function that will help you!
peaks, _ = find_peaks(signal)
print("Within the sample we found ", len(peaks), " heart beats with find_peaks!")

"""
Step 4: Plot the results
"""

# plot all the find_peaks results on the same graph
plt.plot(signal)
plt.title('Filtered ECG Signal with Beat Annotations')

plt.plot(peaks, signal[peaks], 'X')
plt.show()
