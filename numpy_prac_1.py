import numpy as np
import pandas as pd 

# Create Data for an array with random int's between 0,100
my_data = np.random.randint(low=0, high=101, size=(3,4))

# Col names 
my_col_names = ['Eleanor', 'Chidi', 'Tahani', 'Jason']

# Creating the dataframe
my_dataframe = pd.DataFrame(data=my_data, columns=my_col_names)

# Display the entire DataFrame
print(my_dataframe, '\n')

# Display the values in Row #1
print(my_dataframe.iloc[[1]], '\n')

# Display the specific value of Col #1 Row #1 
print("Eleanor Row #1: %d" % my_dataframe["Eleanor"][1], '\n')
# print(my_dataframe['Eleanor'][1])

# New Column with the sum of col.3 & col.4 & print statement
my_dataframe["Janet"] = my_dataframe["Tahani"] + my_dataframe["Jason"]
print(my_dataframe, '\n')

# Copying a DataFrame

# Create a reference by assigning my_dataframe to a new variable
print("Experiment with a reference:")
reference_to_my_dataframe = my_dataframe

# Print the starting value of a particular cell
print(" Starting value of my_dataframe: %d" % my_dataframe['Jason'][1])
print(" Starting value of reference_to_my_dataframe: %d" % reference_to_my_dataframe['Jason'][1])

# Modify a cell in my_dataframe
my_dataframe.at[1, 'Jason'] = my_dataframe['Jason'][1] + 5
print(" Updated my_dataframe: %d" % my_dataframe['Jason'][1])
print(" Updated reference_to_my_dataframe: %d\n\n" % reference_to_my_dataframe['Jason'][1])

# Create a true copy 
print("Experiment with a true copy:")
copy_of_my_dataframe = my_dataframe.copy()

# Print the starting value of a particular cell.
print(" Starting Value of my_dataframe: %d" % my_dataframe['Eleanor'][1])
print(" Starting value of copy: %d" % copy_of_my_dataframe['Eleanor'][1])

# Modify a cell in dataframe
my_dataframe.at[1, 'Eleanor'] = my_dataframe['Eleanor'][1] + 3
print(" Updated my_dataframe: %d" % my_dataframe['Eleanor'][1])
print(" Copy does not get updated: %d" % copy_of_my_dataframe['Eleanor'][1])
