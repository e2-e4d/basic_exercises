# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
name_counts = {}
for student in students:
    name = student['first_name']
    if name in name_counts:
        name_counts[name] += 1
    else:
        name_counts[name] = 1
for name, count in name_counts.items():
    print(f'{name}: {count}')



# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
name_counts = {}
for student in students:
    name = student['first_name']
    if name in name_counts:
        name_counts[name] +=1
    else:
        name_counts[name] = 1
max_count = max (name_counts.values())

for name, count in name_counts.items():
    if count == max_count:
        print(f'Самое частое имя среди учеников: {name}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
school_class_count = 0
for school_class in school_students:
    school_class_count += 1
    name_counts = {}
    for student in school_class:        
        name = student['first_name']        
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1
    max_count = max (name_counts.values())
    for name, count in name_counts.items():
        if count == max_count:
            print(f'Самое частое имя в классе {school_class_count}: {name}')
    

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
for school_class in school:
    male = 0
    female = 0
    for student in school_class['students']:
        name = student['first_name']
        if is_male[name]:
            male +=1
        else:
            female +=1        
    print(f'Класс {school_class['class']}: девочки {female}, мальчики {male}')


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}


max_male_count = 0
max_female_count = 0
max_male_class = {}
max_female_class = {}

for school_class in school:
    male = 0
    female = 0
    for student in school_class['students']:
        name = student['first_name']
        if is_male[name]:
            male += 1
        else:
            female += 1
    if male > female:
        school_class['sex'] = 'male'
        school_class['quantity'] = male
        if male > max_male_count:
            max_male_count = male
            max_male_class = school_class
    else:
        school_class['sex'] = 'female'
        school_class['quantity'] = female
        if female > max_female_count:
            max_female_count = female
            max_female_class = school_class

print(f'Больше всего мальчиков в классе {max_male_class['class']}')
print(f'Больше всего девочек в классе {max_female_class['class']}')

