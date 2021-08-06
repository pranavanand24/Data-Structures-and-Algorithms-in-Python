newTuple = ('a', 'b', 'c', 'd', 'e', 'f')

# in operator 

print('b' in newTuple)

# linear search

def searchTuple(ptuple,element):
    for i in ptuple:
        if i == element:
            return ptuple.index(i)
    return 'the element does not exist'

print(searchTuple(newTuple, 'f'))

# Time Complexity - O(n)
# Space Complexity - O(1)