import numpy as np

twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])

newTDArray = np.delete(twoDArray,1, axis=0)

print(newTDArray)



# Time Complexity - O(mn) , where m is the number of rows and n is the number of columns

# Space Complexity - O(1)