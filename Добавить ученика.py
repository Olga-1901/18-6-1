import random
# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
students.sort()
classes = ['Математика', 'Русский язык', 'Информатика']
students_marks = {}
for student in students:
    students_marks[student] = {}
for class_ in classes:
    marks = [random.randint(1, 5) for i in range(3)]
    students_marks[student][class_] = marks
    for student in students:
        print(f'''{student}
        {students_marks[student]}''')

print('''Список команд:
        1. Добавить оценку ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Выход из программы''')

print('1. Добавить оценку ученика по предмету')
student = input('Введите имя ученика: ')
class_ = input('Введите предмет: ')
mark = int(input('Введите оценку: '))
if student in students_marks.keys() and class_ in students_marks[student].keys():
    students_marks[student][class_].append(mark)
    print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
else:
    print('ОШИБКА: неверное имя ученика или название предмета')




Александра
        {}
Ангелина
        {}
Аполлон
        {}
Дарья
        {}
Ярослав
        {'Математика': [3, 1, 2]}
Александра
        {}
Ангелина
        {}
Аполлон
        {}
Дарья
        {}
Ярослав
        {'Математика': [3, 1, 2], 'Русский язык': [2, 2, 2]}
Александра
        {}
Ангелина
        {}
Аполлон
        {}
Дарья
        {}
Ярослав
        {'Математика': [3, 1, 2], 'Русский язык': [2, 2, 2], 'Информатика': [4, 5, 2]}
Список команд:
        1. Добавить оценку ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Выход из программы
1. Добавить оценку ученика по предмету
Введите имя ученика: Ярослав
Введите предмет: Русский язык
Введите оценку: 4
Для Ярослав по предмету Русский язык добавлена оценка 4

Process finished with exit code 0
