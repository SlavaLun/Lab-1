# Работа с таблицей книг
import csv
import random

search = str(input('Search for:'))
count_book = 0
count_book_name_over30 = 0
books_for_random = []
popular_downloads = ['0'] * 20
popular = ['0'] * 20
tegs = []
with open('books.csv', 'r') as file:
    N = file.readline()  # Считываем первую строчку с обозначением столбцов
    table = csv.reader(file, delimiter=';')
    for row in table:
        count_book += 1
        if len(row[1]) > 30:
            count_book_name_over30 += 1
        author = row[3]
        author_sn = row[4]
        if author == search or author_sn == search:  # Поиск книг по автору
            if '2015' in str(row[6]) or '2018' in str(row[6]):
                print(row[1])
        for i in range(len(popular_downloads)):  # Поиск 20 самых популярных книг
            if int(row[8]) > int(popular_downloads[i]):
                popular_downloads[i] = row[8]
                popular[i] = str(i + 1) + '. ID - ' + str(row[0]) + '; Название - ' + str(row[1]) + '; Автор - ' + str(
                    row[4]) + '; Дата поступления - ' + str(row[6]) + '; Жанр - ' + str(row[12]) \
                    + '; Выдано - ' + str(row[8]) + '; Цена - ' + str(row[7])
                break
        tgs_all = (row[12].rsplit("#"))[1:]  # Разбитие строки тегов на подстроки
        books_for_random.append('автор - ' + row[4] + '; название - ' + row[1] + '; год поступления - ' + row[6])
        for i in range(len(tgs_all)):  # Сохранение всех неповторяющихся тегов
            if (tgs_all[i][0]) == ' ':
                tgs_all[i] = tgs_all[i][1:]  # Если в строке первый символ пробел - убираем его этой строчкой
            if tgs_all[i] not in tegs:
                tegs.append(tgs_all[i])
random_books = list(x for x in random.sample(books_for_random, 20))
with open('results.txt', 'w') as f:
    for i in range(1, 21):
        f.write(str(i) + '.' + ' ' + random_books[i - 1] + '\n')
f.close()
print('Количество книг в таблице = ' + str(count_book) + '\n' 'Количество книг, название которых длиннее 30 символов = '
      + str(count_book_name_over30) + '\n' + '20 самых популярных книг:')
for i in range(0, 20):
    print(popular[i])
print('Жанры:')
for i in range(len(tegs)):
    print(tegs[i])
