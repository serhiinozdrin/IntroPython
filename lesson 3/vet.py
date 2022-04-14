duck = 'eggs'
dog = 'milk'
platypus = 'eggs+milk'

visitor = platypus

if visitor == 'eggs' or visitor == 'milk':
    print('Go to left coridor')
    print('Thanks for your visit')
elif visitor == 'milk':
    print('Go to right coridor')
elif visitor == 'something':
    print('Go away')
else:
    print('Go to admin')
