# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный 
# предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их 
# количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —

# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open('classes.txt', 'r+', encoding = 'utf-8') as f:
    d = {}
    for l in f:
        cl = l.strip().split(': ')
        ncl = ''.join((ch if ch in '0123456789.-e' else ' ') for ch in cl[1] )
        listOfNumbers = [float(i) for i in ncl.split()]
        d[cl[0]] = sum(listOfNumbers)
        
print(d)
