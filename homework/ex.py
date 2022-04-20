string = 'cucumber'
#         01234567
#        -87654321
print(string[0])
print(string[3])
print(string[8])  # помилка
print(string[-1])
print(string[-3])

print(string[4])
print(string.index('m'))
print(string[string.index('m')])
print(string.index('u'))
print(string.index('um'))
string.index('a')  # помилка
print(string.find('a'))