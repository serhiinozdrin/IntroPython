# empty = list ()
# print(empty)

# number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(number)
# print(number[0])
# print(number[4:8:2])
# print(number[::2])

# stuff = [23, 2.5, 'Cucumber', True, None, [1, 2, 3, 4]]
# print(stuff)
# print(stuff[0] * stuff[2])

ducks = ['Hanry', 'Quacker']
new_ducks = ['Lupa', 'Pupa']
my_ducks = ducks + new_ducks + new_ducks
# print(my_ducks * 2)
# print(my_ducks)

# print(my_ducks + ['Rose'])

my_ducks.append('Rose')
# print(my_ducks)
# print(len(my_ducks))
# print(my_ducks.index('Lupa'))

# print(my_ducks.append('Lupa'))
# print(my_ducks)

# my_ducks.count('Lupa')

my_ducks.remove('Lupa')
# print(my_ducks)

del my_ducks[-2]
# print(my_ducks)

my_ducks.insert(0, 'Cucumber')
# print(my_ducks)

my_ducks.extend('Wilhelm')
# my_ducks.append('Wilhelm')
print(my_ducks)

print(list('Cucumber'))