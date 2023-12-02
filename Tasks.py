##################################################################################
# Task_1
# 1. Сортировка IP-адресов

def decFormat():
    import ipaddress

    # ip адресса для сортровки
    ips = ['192.168.11.1', '192.168.22.1', '172.16.0.1', '10.0.0.1','192.168.12.1', '100.64.0.1','192.168.19.1']
    _ipaddres = sorted(ips, key=lambda i: int(ipaddress.ip_address(i)))
    string = ''
    print("Сортировка ip адрессов")

    for ip in _ipaddres:
        string += str(ip)
        print(ip)

# decFormat()

##################################################################################
# Task_2
# 2. Сортировка по гематрии
# Гематрия – это сумма числовых значений букв, входящих
# в состав слова. В данном случае числовое значение букв
# определяется по таблице ASCII, причем учитываются только
# заглавные буквы (то есть при подсчете гематрии все буквы
# переводятся в верхний регистр). Программа должна вывести
# список слов в исходном регистре, отсортированный в соответствии с гематрией.
# Входные данные:
# Число n, затем n строк с английскими словами, состоящими из букв в разных регистрах.

def Task_2():
    print(*sorted([input() for _ in range(int(input()))],
                 key=lambda x: (sum([ord(_) - ord('A') for _ in x.upper()]), x)),
         sep='\n')

# Task_2()

##################################################################################
# Task_3
# 3. Группировка дубликатов
#Пример ввода
# h h h e e l l l o w w o o o o r r r l l d d
#Пример вывода
# [['h', 'h', 'h'], ['e', 'e'], ['l', 'l', 'l'], ['o'], ['w', 'w'], ['o', 'o', 'o', 'o'], ['r', 'r', 'r'], ['l', 'l'], ['d', 'd']]

def Task_3():
    res = []
    for i in input().split():
        if (not res) or (i != res[-1][-1]):
            res.append([i])
        else:
            res[-1].append(i)
    print(res)

# Task_3()

##################################################################################
# Task_4
# 4. Разделение списка на отрезки
# Пример ввода
# w t z k p e h t b
# 3
#Пример вывода
# [['w', 't', 'z'], ['k', 'p', 'e'], ['h', 't', 'b']]

def Task_4(n):
    cuts = [lst[x:x + n] for x in range(0, len(lst), n)]
    return cuts

# lst = input().split()
# n = int(input())
# print(Task_4(n))

##################################################################################
# Task_5
# 5 Email-адреса
# Данные об email-адресах студентов хранятся в словаре:
# Нужно дополнить код таким образом, чтобы он вывел все
# адреса в алфавитном порядке и в формате имя_пользователя@домен.

def Task_5():
    emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
              'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
              'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
              'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
              'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
              'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}

    print(*sorted({i + '@' + k for k, v in emails.items() for i in v}), sep='\n')

# Task_5()

##################################################################################
# Task_6
# 6. Коты и владельцы
# В базе данных ветеринарной клиники информация о
# пациентах-котах хранится в списке кортежей. Данные
# о кошках и их владельцах записаны в формате
# «Кличка животного, Возраст животного, Имя владельца, Фамилия владельца»:

def Task_6():
    cats = [('Мартин', 5, 'Алексей', 'Егоров'),
            ('Фродо', 3, 'Анна', 'Самохина'),
            ('Вася', 4, 'Андрей', 'Белов'),
            ('Муся', 7, 'Игорь', 'Бероев'),
            ('Изольда', 2, 'Игорь', 'Бероев'),
            ('Снейп', 1, 'Марина', 'Апраксина'),
            ('Лютик', 4, 'Виталий', 'Соломин'),
            ('Снежок', 3, 'Марина', 'Апраксина'),
            ('Марта', 5, 'Сергей', 'Колесников'),
            ('Буся', 12, 'Алена', 'Федорова'),
            ('Джонни', 10, 'Игорь', 'Андропов'),
            ('Мурзик', 1, 'Даниил', 'Невзоров'),
            ('Барсик', 2, 'Виталий', 'Соломин'),
            ('Рыжик', 7, 'Владимир', 'Медведев'),
            ('Матильда', 8, 'Андрей', 'Белов'),
            ('Гарфилд', 3, 'Александр', 'Березуев')]

    result = {}
    for cat in cats:
        temp = cat[0] + ', ' + str(cat[1])
        result.setdefault(cat[2:], []).append(temp)
    for k, v in result.items():
        print(' '.join(k) + ':', '; '.join(v))

# Task_6()

##################################################################################
# Task_6
# 6. Редкое слово
# Напишите программу, которая принимает на вход строку,
# и выводит слово, которое встречается во фразе реже всего.
# Если редких слов несколько, нужно вывести то, которое меньше
# в лексикографическом порядке. Регистр слов не учитывается,
# знаки препинания в предложениях игнорируются.
# Пример ввода:
# дом, милый дом, милый.
#
# Пример вывода:
# дом

def Task_6():
    words = {}
    for i in input().split():
        i = i.strip('.,!?:;-').lower()
        words[i] = words.get(i, 0) + 1
    print(min(words.items(), key=lambda x: (x[1], x[0]))[0])

# Task_6()

##################################################################################
# Task_7
# 7. Дубликаты
# Напишите программу, которая принимает на вход строку,
# и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Пример ввода:
# a a a b c a a d c d d
#
# Пример вывода:
# a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

def Task_7():
    sp = input().split()
    result = {}
    for i in sp:
        if i in result:
            print(f'{i}_{result[i]}', end=' ')
        else:
            print(i, end=' ')
        result[i] = result.get(i, 0) + 1

# Task_7()

##################################################################################
# Task_8
# 8. Анаграммы
# Напишите программу, которая принимает на вход
# две строки и определяет, являются ли они анаграммами.
# Знаки препинания, пробелы и регистр при этом игнорируются.
# Пример ввода:
# Цари, вино и сало.
# Лисица и ворона.
#
# Пример вывода:
# YES

def Task_8(word):
    result = {}
    for i in word.lower():
        if i.isalpha():
            result[i] = result.get(i, 0) + 1
    return result

# print("YES" if Task_8(input()) == Task_8(input()) else "NO")

##################################################################################
# Task_9
# 9. Нужно проверить, все ли числа в последовательности уникальны.
def Task_9(numbers):
    setarr = set(numbers)
    if len(num) == len(setarr):
        print("Все элементы уникальны")
        print(numbers)
    else:
        print("Есть одинаковые")
        print(numbers)

num = [1,2,3,4,5,5]
# Task_9(num)

##################################################################################
# Task_10
# 10. Напишите программу, которая принимает
# текст и выводит два слова: наиболее часто
# встречающееся и самое длинное.

def Task_10():
    import collections

    text = 'lorem ipsum dolor sit amet amet amet'
    words = text.split()
    counter = collections.Counter(words)
    most_common, occurrences = counter.most_common()[0]

    longest = max(words, key=len)
    print(most_common, longest)

# Task_10()

# Well, the average
# :) or :| or :(