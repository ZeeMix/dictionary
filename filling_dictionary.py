def fill_person():
    file_path = 'dictionary/file/example.txt'

    with open(file_path, 'a', encoding='utf-8') as file:
        while True:
            last_name = input("Введите фамилию (для выхода введите 'exit'): ")
            if last_name.lower().strip() == 'exit':
                break

            first_name = input("Введите имя: ")
            middle_name = input("Введите отчество: ")
            phone = input("Введите телефон: ")

            file.write(f"{last_name}\n{first_name}\n{middle_name}\n{phone}\n\n")

    print("Данные успешно записаны в файл.")

def modification():
    old_text = input('Введите текст для замены: ').lower()
    new_text = input('Введите новый текст: ')
    file_path = 'dictionary/file/example.txt'
    
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines() 
        
    modified_lines = [line.lower().replace(old_text, new_text) for line in lines]
    
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in modified_lines:
            file.write(line)
    
    print(f'Текст "{old_text}" заменен на "{new_text}" в файле.')

def search():
    search_query = input('Введите фамилию, имя, отчество или телефон для поиска: ')
    file_path = 'dictionary/file/example.txt'

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    found_entries = []
    current_entry = ''
    
    for line in lines:
        if line.strip() == '':
            if current_entry.lower().find(search_query.lower()) != -1:
                found_entries.append(current_entry.strip())
            current_entry = ''
        else:
            current_entry += line

    if found_entries:
        print(f'Найдены записи по запросу "{search_query}":')
        for entry in found_entries:
            print(entry)
    else:
        print(f'Записи по запросу "{search_query}" не найдены.')

def deletion():
    text = input('Введите текст, который нужно удалить: ').lower()
    file_path = 'dictionary/file/example.txt'
    
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
    filtered_lines = [line for line in lines if text not in line.lower()]
    
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in filtered_lines:
            file.write(line)
    
    print(f'Удалены строки, содержащие текст "{text}".')