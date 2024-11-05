from csv import reader
import random
import xml.dom.minidom as minidom

with open("books-en.csv", "r", encoding="windows-1251") as csvfile, open(
    "result.txt", "w"
) as output, open("currency.xml", "r", encoding="latin-1") as xml_file:

    table = list(reader(csvfile, delimiter=";"))

    # первое задание
    quantity = sum(1 for row in table if len(row[1]) > 30)
    print(quantity)

    # второе задание
    author_name = input("Введите имя автора для поиска: ")
    found = []
    for row in table:
        if row[2].lower() == author_name.lower() and int(row[3]) >= 2000:
            found.append(f"{row[2]}\n\tНазвание: {row[1]}\n\tГод: {row[3]}")

    if found:
        print(f"Найдено {len(found)} книг(а) автора {author_name} с 2000 года:")
        for i, book in enumerate(found, start=1):
            print(f"{i}.\t{book}")
    else:
        print(f"Книги автора {author_name} с 2000 года не найдены.")

    # третье задание
    count = len(table)
    random_indices = sorted(random.sample(range(count), 20))

    for i, row in enumerate(table):
        if i in random_indices:
            output.write(f"{row[2]}. {row[1]} - {row[3]} \n")

    # четвертое задание
    xml_data = xml_file.read()
    dom = minidom.parseString(xml_data)
    dom.normalize()

    elements = dom.getElementsByTagName("Valute")
    books_dict = {}

    for node in elements:
        name = ""
        charcode = ""
        for child in node.childNodes:
            if child.nodeType == 1:
                if child.tagName == "Name" and child.firstChild.nodeType == 3:
                    name = child.firstChild.data
                if child.tagName == "CharCode" and child.firstChild.nodeType == 3:
                    charcode = str(child.firstChild.data)
        if name and charcode:
            books_dict[name] = charcode

    print(books_dict)

    # допзадание №1
    publisher = set(row[4] for row in table)
    publisher = sorted(publisher)
    for pub in publisher:
        print(pub)

    # допзадание №2
    top_books = []
    for row in table[1:]:
        book = row[1]
        author = row[2]
        popularity = int(row[5])
        top_books.append((popularity, book, author))

    top_books.sort(reverse=True)

    print("\nТоп 20 популярных книг:")
    for i in range(min(20, len(top_books))):
        print(f"{i + 1}.\t{top_books[i][2]} - {top_books[i][1]}")