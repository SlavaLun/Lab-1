# Работа с таблицей книг
import csv
import random

search = str(input('Search for:'))
publisher = []
count_book = 0
count_book_name_over30 = 0
book_for_random = []
max_popular = ['0'] * 20
popular = ['0'] * 20
with open('books-en.csv', 'r') as file:
    N = file.readline()  # Считываем первую строчку с обозначением столбцов
    table = csv.reader(file, delimiter=';')
    for row in table:
        count_book += 1
        if len(row[1]) > 30:
            count_book_name_over30 += 1
        author = row[2]
        if author == search:  # Поиск книг по автору
            if row[3] == '2015' or row[3] == '2018':
                print(row[1])
        for i in range(len(max_popular)):  # Поиск 20 самых популярных книг
            if int(row[5]) > int(max_popular[i]):
                max_popular[i] = row[5]
                popular[i] = str(i + 1) + '. ISBN - ' + str(row[0]) + '; Название - ' + str(
                    row[1]) + '; Автор - ' + str(row[2]) + '; Год выпуска - ' + str(row[3]) + '; Издательство - ' + str(
                    row[4]) + '; Скачиваний - ' + str(row[5]) + '; Цена - ' + str(row[6])
                break
        book_for_random.append('автор - ' + row[2] + '; название - ' + row[1] + '; год выпуска - ' + row[3])
        if row[4] not in publisher:  # Сохранение всех издательств без повторений
            publisher.append(row[4])
random_book = list(x for x in random.sample(book_for_random, 20))
with open('results.txt', 'w') as f:
    for i in range(1, 21):
        f.write(str(i) + '.' + ' ' + random_book[i - 1] + '\n')
f.close()
print('Количество книг в таблице = ' + str(
    count_book) + '\n' 'Количество книг, название которых длиннее 30 символов = ' + str(
    count_book_name_over30) + '\n' + 'Издательства: ' + str(publisher)[1:-1:] + '\n' + '20 самых популярных книг:')
for i in range(0, 20):
    print(popular[i])
