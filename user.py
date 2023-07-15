from filling_dictionary import *

def choose_mode():
    mode = input('Выберите режим для работы со справочником: запись, поиск, изменение или удаление: ')
    if mode == 'запись':
        person = fill_person()
    elif mode == 'поиск':
        person = search()
    elif mode == 'изменение':
        person = modification()
    elif mode == 'удаление':
        person = deletion()
    else:
        print('Такого режима не существует!')