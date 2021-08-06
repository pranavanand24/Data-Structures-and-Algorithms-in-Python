myDict = {'name': '"Edy','age': 24, 'gender': 'male', 'address': 'London'}

def searchDict(dict,value):
    for key in dict:
        if dict[key] == value:
            return key,value
    return 'The value does not exist'

print(searchDict(myDict, 24))

# Time Complexity - 0(n)
# Space Complexity - O(1)