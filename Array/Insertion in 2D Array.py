import numpy as np

twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])

newTwoDArray = np.insert(twoDArray, 0, [[1,2,3,4]], axis=1)

print(newTwoDArray)

# Axis = 1 for column and 0 for row
# Time Complexity - 0(mn)