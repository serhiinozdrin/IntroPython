# text = 'Cucumbrer'
# print(text.lower())
# print(text.upper())

# text = 'CuCumBer are. cool'
# print(text.capitalize())
# print(text.swapcase())

# text = '   '
# print(bool(text))
# print(text.isspace())

# text = 'abcdef.'
# print(text.isalpha())

# text = '123'
# print(text.isnumeric())

# text = 'Cucumber'
# print(text.startswith('Cucumber'))
# print(text.endswith('<'))

# text = 'cucumber cucumber banana cucumber'
# print(text.count('u'))
# print(text.replace('banana', 'cucumber').count('cucumber'))

from distutils.errors import LinkError
from re import template


text = 'abcdefg'
# print(text[0])
# print(text[2])
# print(text[-1])
# print(text[-3])

# print(text.index('d'))
# print(text.index('ef'))

# template = 'I like {0} - so I will go and buy {0}'
# liked = 'cucumber'
# print(template.format(liked))
# other_liked = 'bananas'
# print(template.format(liked))

# print(f'I like {liked * 10}')

text = 'I don\'t like bananas'
#       01234 56 
print(text[2::3])

text = '0123456789'
print(text[::2])



