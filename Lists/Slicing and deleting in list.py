mylist = ['a', 'b', 'c', 'd', 'e', 'f']

mylist[0:2] = ['x','y']

print(mylist[:])

# list method for deletion

#pop

mylist.pop(1)
print(mylist)

# del

del mylist[1:3]
print(mylist)

# remove

mylist.remove('e')
print(mylist)

