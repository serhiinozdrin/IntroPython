print('Вас приветствует конвертер смайликов в емоджи 🙂😂🙁😠😈')
template = (input('Введите текст для конвертации: '))
print(template.replace(':)', '🙂').replace('XD', '😂').replace(':(', '🙁').replace('>:(', '😠').replace('>:)', '😈'))
