import pandas as pd

# path to overall file
path_to_file = "../../data/tensile/tensile_data.csv"

# load data into dataframe
df = pd.read_csv(path_to_file)

# print out data frame just for fun
print(df)

# get all results from one type
cold_rolled = df[df['Material_Type'] == '1045CR']

aluminum = df[df['Material_Type'] == '2024']

plastic = df[df['Material_Type'] == 'PMMA']

# print out each material type
print(cold_rolled)

print(aluminum)

print(plastic)

# combine conditions with & (and) and | (or)
# each condition must be inside its own parentheses
strong_plastic = df[(df['Material_Type'] == 'PMMA') & (df['Yield_Strength'] > 50)]
print(strong_plastic)



# Approach 1: Parse all columns to get print out a decent table
# of all mean +/- std of all materials

# Note: pandas .std() divides by n-1 (sample std) while np.std() divides by n by default.
# Use np.std(x, ddof=1) to match pandas.

# determine averages/deviations on elastic modulus of each material
cr_modulus_avg = cold_rolled['Elastic_Modulus'].mean()
cr_modulus_std = cold_rolled['Elastic_Modulus'].std()

al_modulus_avg = aluminum['Elastic_Modulus'].mean()
al_modulus_std = aluminum['Elastic_Modulus'].std()

pmma_modulus_avg = plastic['Elastic_Modulus'].mean()
pmma_modulus_std = plastic['Elastic_Modulus'].std()

# determine averages/deviations on yield strength of each material
cr_yieldstrength_avg = cold_rolled['Yield_Strength'].mean()
cr_yieldstrength_std = cold_rolled['Yield_Strength'].std()

al_yieldstrength_avg = aluminum['Yield_Strength'].mean()
al_yieldstrength_std = aluminum['Yield_Strength'].std()

pmma_yieldstrength_avg = plastic['Yield_Strength'].mean()
pmma_yieldstrength_std = plastic['Yield_Strength'].std()

# print out results
print("Material\tElastic Modulus\tYield Strength")

print("1045CR\t", round(cr_modulus_avg, 2), "+/-", round(cr_modulus_std, 2),
      "\t", round(cr_yieldstrength_avg, 2), "+/-", round(cr_yieldstrength_std, 2))

print("2024\t", round(al_modulus_avg, 2), "+/-", round(al_modulus_std, 2),
      "\t", round(al_yieldstrength_avg, 2), "+/-", round(al_yieldstrength_std, 2))

print("PMMA\t", round(pmma_modulus_avg, 2), "+/-", round(pmma_modulus_std, 2),
      "\t", round(pmma_yieldstrength_avg, 2), "+/-", round(pmma_yieldstrength_std, 2))

# add some space after the table
print("\n")

