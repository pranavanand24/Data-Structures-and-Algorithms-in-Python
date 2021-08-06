myDict = {'name': 'Edy', 'age':26, 'address': 'london', 'education': 'master'}

# pop method

print(myDict.pop('name'))

print(myDict)

# popitem

print(myDict.popitem())

print(myDict)

# clear method

del myDict['age']

print(myDict)