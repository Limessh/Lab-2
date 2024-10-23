from csv import reader

# первое задание
with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    quantity=0
    for row in table:
        if len(row[1])>30:
            quantity+=1

    print(quantity)


#второе задание
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
# import xml.dom.minidom as minidom

# with open('currency.xml', 'r', encoding='latin-1') as xml_file:
#     xml_data = xml_file.read()
# xml_file = open('currency.xml', 'r')
# xml_data = xml_file.read()

    # dom = minidom.parseString(xml_data)
    # dom.normalize()

    # elements = dom.getElementsByTagName('book')
    # books_dict = {}

    # for node in elements:
    #     for child in node.childNodes:
    #         if child.nodeType == 1:
    #             if child.tagName == 'Name':
    #                 if child.firstChild.nodeType == 3:
    #                     title = child.firstChild.data
    #             if child.tagName == 'CharCode':
    #                 if child.firstChild.nodeType == 3:
    #                     price = float(child.firstChild.data)
    #     books_dict[title] = price

    #     if node.getAttribute('id') == 'bk106':
    #         print(node.getElementsByTagName('Name')[0].firstChild.data)

    # for currency in elements:
    #     name = currency.getElementsByTagName('Name')[0].firstChild.nodeValue
    #     char_code = currency.getElementsByTagName('CharCode')[0].firstChild.nodeValue
    #     books_dict[name] = char_code
    # print(books_dict)
    
#допзадание №1

with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    publisher=set()
    for row in table:
        publisher.add(f'{row[4]}')
    publisher=sorted(publisher)
    for i in range (len(publisher)):
        print(publisher[i]+'\n')

#допзадание №2
# with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
#     table = reader(csvfile, delimiter=';')
#     top_books=[]
    