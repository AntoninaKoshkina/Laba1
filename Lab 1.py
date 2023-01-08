import csv

f = open('output.txt', 'w')
with open ('books.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    c = -1
    counter = 0
    author = input('Введите фамилию желаемого автора: ')
    state = input('Введите 1, если хотите ввести 20 id книг для карточек, иначе 0,и тогда будут рассмотрены первые 20 значений: ')
    cards = 20
    id_array = []
    tags_array = []
    flag = 0
    numbers = []
    if state == '1':
        for i in range(cards):
            id_array.append(input('Введите id нужной книги: '))
    else: # иначе
        flag = 1
    for row in reader:
        c += 1

        # условие 5
        year = row[6].split()
        year = year[0].split('.')
        year = year[-1]
        last_name = row[3].split()
        last_name = last_name[-1:]

        # условие 3 вариант 8
        if len(last_name) > 0:
            if (author == str(last_name[0])) and ((int(year[6])== 2015) or (int(year[6]) == 2018)):
                print(row[1])
        # условие 2
        if len(row[1]) > 30:
            counter += 1

        if c>0:
            numbers.append(int(row[8]))


    print('количество записей в таблице: ', c)
    print('количество записей названий > 30: ', counter)

f.close()
