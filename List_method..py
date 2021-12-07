
names = ['David', 'Johnny', 'Dennis', 'Jason']

# add 2 names to the end of the list
names.append('Andy')
names.append('Rene')
print(names)

# add a name at position 3
names.insert(2, 'Mike')
print(names)

# remove 2 specific names
names.remove('David')
names.remove('Johnny')
print(names)

# pop the last item fro the list
print('Popped item =', names.pop())
print(names)

print('Popped item =', names.pop())
print(names)

# clear all items
names.clear()
print(names)
