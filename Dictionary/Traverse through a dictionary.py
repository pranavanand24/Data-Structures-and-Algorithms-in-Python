myDict = {'name': 'edy', 'age':26,'address':'london'}

def traverseDict(dict):
    for key in dict:
        print(key, dict[key])

traverseDict(myDict)

# time complexity - O(n)
# space complexity - O(1)
