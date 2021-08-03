# using in operator

list = [10,20,30,40,50,60,70,80,90,100]

if 20 in list:
    print(list.index(20))

else:
    print("the value does not exist in the list")


# linear search

def searchinlist(list,value):
    for i in list:
        if i == value:
            return list.index(value)
    return 'the value does not exist in the list'

print(searchinlist(list, 20))