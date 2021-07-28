import numpy as np

twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])


def accessElements(array,rowIndex,colIndex):
    if rowIndex >= len(array) or colIndex >= len(array):
        print('Incorrect Index')

    else:
        print(array[rowIndex][colIndex])

accessElements(twoDArray,2,3)


# TimeComplexity - O(1)
# Space complexity - O(1)