print('Вас приветствует конвертер смайликов в емоджи 🙂😂🙁😠😈')
template = (input('Введите текст для конвертации: '))
print(template.replace('>:(', '😠').replace('>:)', '😈').replace(':)', '🙂').replace('XD', '😂').replace(':(', '🙁'))
