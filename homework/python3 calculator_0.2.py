print('Добро пожаловать в НеВеРоЯтНыЙ калькулятор (версия 0.2)\n'
      'Теперь я умею складывать, отнимать, умножать и делить 2 любых целых числа 💪')
number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
calculator = (input('Выберите операцию (+, -, *, /): '))

if calculator == '+' or calculator == '-' or calculator == '*' or calculator == '/':
    print('Интересные условия! Уверен, я справлюсь 💪')
else:
    print('Кажется, вы выбрали неправильную операцию... Давайте попробуем еще раз 😉')

if calculator == '+':
    print('Ваш результат: ', number_1 + number_2)
elif calculator == '-':
    print('Ваш результат: ', number_1 - number_2)
elif calculator == '*':
    print('Ваш результат: ', number_1 * number_2)
elif calculator == '/':
    if number_2 !=0:
        print('Ваш результат: ', number_1 / number_2)
    else:
        print('Кажется, вы делите на ноль 😉')







# elif calculator == '-':
    # print('Интересные условия! Уверен, я справлюсь 💪')
# elif calculator == '*':
    # print('Интересные условия! Уверен, я справлюсь 💪')
#elif calculator == '/':
    # print('Интересные условия! Уверен, я справлюсь 💪')
# else:
    # print('Кажется, вы выбрали неправильную операцию... Давайте попробуем еще раз 😉')