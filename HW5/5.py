# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('numbers.txt', 'w+') as f:
    f.write(input('Введите набор чисел через пробел: '))
    f.flush()
    f.seek(0)
    l = f.read().split(' ')
    print(sum(map(float, l)))
