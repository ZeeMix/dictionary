from user import choose_mode
from filling_dictionary import filling


def running():
    person, mode = choose_mode()
    if mode == 'запись':
        filling(person)
    else:
        pass


