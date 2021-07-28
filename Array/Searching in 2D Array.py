import numpy as np

twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])

def searchTDarray(array,value):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][j] == value:
                return 'the value is located at index'+" "+str(i)+" "+str(j)
    return 'the element is not found'

print(searchTDarray(twoDArray,14))

# Time Complexity - for different row and column is O(mn) and for same no of column and rows is O(n^2)
# Space Complexity - O(1)