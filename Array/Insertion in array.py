from array import *
arr1 = array ('i', [1,2,3,4,5,6])
arr2 = array ('i', [1,2,3,4,5,6])


arr1.insert(6,7)

arr2.insert(0,0)

print(arr1)
print(arr2)

# Time complexity for inserting element at the end of the array is : O(1)
# Time complexity for inserting element at the beginning of the array is : O(n)
# Time complexity for inserting element to the full array is : O(n)
