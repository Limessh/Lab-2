# первое задание
from csv import reader
with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    quantity=0
    for row in table:
        if len(row[1])>30:
            quantity+=1

    print(quantity)


#второе задание
from csv import reader
with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    author_name = input('Введите имя автора для поиска: ')
    found=[]
    for row in table:
        if row[2].lower() == author_name.lower() and int(row[3]) >= 2000:
            found.append(f"{row[2]}\n\tНазвание: {row[1]}\n\tГод: {row[3]}")

    if found:
        print(f'Найдено {len(found)} книг(а) автора {author_name} с 2000 года:')
        for i in range (len(found)):
            print(str(i+1)+'.' + '\t' + found[i])
    else:
        print(f'Книги автора {author_name} с 2000 года не найдены.')              


#третье задание
from csv import reader
import random

with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    table_1=list(reader(csvfile, delimiter=';'))
    count=len(table_1)
    random_indices = sorted(random.sample(range(count),20))

output = open('result.txt', 'w')
with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    i=0
    j=0

    for row in table:
        i+=1
        if j<20:
            if i==random_indices[j]:
                output.write(f'{row[2]}. {row[1]} - {row[3]} \n ')
                j+=1
output.close()

#четвертое задание
# from xml.dom import minidom

# file_path = 'currency.xml'
# currency_dict = {}
# doc = minidom.parse(file_path)
# currencies = doc.getElementsByTagName('Currency')

# for currency in currencies:
#     name = currency.getElementsByTagName('Name')[0].firstChild.data
#     char_code = currency.getElementsByTagName('CharCode')[0].firstChild.data
#     currency_dict[name] = char_code

# print(currency_dict)


#допзадание №1
from csv import reader

with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    publisher=set()

    for row in table:
        publisher.add(f'{row[4]}')

    publisher=sorted(publisher)

    for i in range (len(publisher)):
        print(publisher[i]+'\n')


#допзадание №2
from csv import reader
with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    top_books=[]
    i=0
    
    for row in table:
        i+=1
        if i!=1:
            book = row[1]
            author=row[2]
            popularity = int(row[5])
            top_books.append((popularity, book, author))

top_books=sorted(top_books)[::-1]

for i in range (20):
    print(str(i+1)+'.' + '\t' + str(top_books[i][2])+ ' - ' + str(top_books[i][1])+'\n')