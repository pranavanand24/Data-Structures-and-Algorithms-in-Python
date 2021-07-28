import numpy as np

twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])

def traverseTDArray(array):
    for i in range(len(array)):
        for j in range(len(array)):
            print(array[i][j])
        

traverseTDArray(twoDArray)

# TimeComplexity - O(n^2)

# SpaceComplexity - O(1)