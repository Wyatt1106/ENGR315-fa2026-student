**3.4.1. - Reactive Strength Index**

The Reactive Stength Index (RSI) is a measure of how rapidly an athlete can change their momentum an direction.
In this assignment you will calculate the RSI from several human subject participants on both a force plate and accelerometer.

The key parameters to determine are the "Time of Flight" a person is in the air, and the "Time of Contact" they were on the ground.
With these values the RSI can be calculated.

Complete the template "drop-jump-template" to identify the time of flight and time of contact for an individual subject. 
Addtional data can be loaded from the data/drop-jump folder.

The calculate time of flight and time of contact for the force plate data is available in a README in data/drop-jump/force-plate.
Compare your results against that dataset and then upload your final solution to gradescope.

Additional details can be found in [Exploring Amateur Performance in Athletic Tests
Using Wearable Sensors](https://www.jasonforsyth.net/assets/pdf/mitchell-sieds-camera-ready.pdf)

**3.4.2 - Tensile Strength Testing**

Complete several templates to implement various tensile testing methods. Each template should be completed in order as they build upon one another.

Step 1: Complete to calculate **stress** from load/force and cross-section area

Step 2: Copy in your previous solution and then determine **ultimate stress and strain**

Step 3: Copy in your previous solution and then calculate the **elastic modulus**

Step 4: Copy in your previous solution and then determine **yield strength** 

Submit Step 4 file to Gradescope

**3.4.3 - Writing Tensile Data**

Complete the generate_csv_file() method in the template. Solution will write all tensile data to a singular CSV file.

Before running the template, open writing_tensile_utils.py and copy in your four completed functions from Tensile Testing
(calculate_stress, calculate_max_strength_strain, calculate_elastic_modulus, calculate_percent_offset).

Submit only your writing-tensile-data-template.py file to Gradescope.
