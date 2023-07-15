from user import choose_mode
from filling_dictionary import *



def running():
    person, mode = choose_mode()
    if mode == 'запись':
        fill_person()
    elif mode == 'поиск':
        search()        
    elif mode == 'изменение':
        modification()
    elif mode == 'удаление':
        deletion()
    else:
        print('Неверный режим работы')


