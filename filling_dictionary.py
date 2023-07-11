def filling(person):
    with open('file/example.txt', 'a', encoding='utf-8') as file:
        for el in person:
            file.write(el + '\n')
        file.write('\n')