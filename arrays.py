import numpy as np
 
ini_array = np.array([[55, 66, 77], [45, 46, 47], [90, 60, 10]])
 
# printing initial array
print("initial_array : ", str(ini_array));
 
# Array to be added as column
column_to_be_added = np.array([[1], [2], [3]])
 
# Adding column to right side of array using append() method
arr = np.append(ini_array, column_to_be_added, axis=1)
 
# printing result
print ("resultant array", str(arr))

# Adding column to left side of array using append() method
arr2 = np.append(column_to_be_added, ini_array, axis=1)
 
# printing result
print ("resultant array2", str(arr2))