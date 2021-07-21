from array import *
arr1 = array('i', [1,2,3,4,5,6])

def searchInArray(array, value):
    for i in array:
        if i == value:
            return array.index(value)
    return "The Element Does Not Exist in the Array"

print(searchInArray(arr1, 3))


# Time Complexity - O(n)
# Space Complexity - O(1)