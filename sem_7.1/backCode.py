from datetime import datetime
import datetime
import backCode
import logger

def choice ():
    print('\nДоброе время суток! Вас приветствует телефонный справочник.\n')
    result = int(input('Выберете операцию, которую необходимо выполнить:\n\
        1 - Внести новый телефон контакта\n\
        2 - Поиск\n\
        3 - Вывести весь список\n\
        4 - Закончить работу\n\
        Ваш выбор: '))
    return result

def stile():
    a = int(input('В каком формате предоставить данные: \n\
        1 - Строка;\n\
        2 - Столбец.\n\
        Ваш выбор: '))
    return a  


def search():
    print('Укажите по какому параметру будет осуществляться поиск: \n\
        1 - Фамилия;\n\
        2 - Имя;\n\
        3 - Номер телефона;\n\
        4 - Описание.\n')
    a = int(input('Ваш выбор: '))
    if a == 1:
        entry = input('Введите Фамилию: ').title()
    if a == 2:
        entry = input('Введите Имя: ').title()
    if a == 3:
        entry = input('Введите номер телефона: ')
    if a == 4:
        entry = input('Введите описание контакта (личный, рабочий, домашний и т.д.): ').title()
      
    print('Поиск будет осуществляться по : ', entry)
    return entry



def record():
    entry=[]
    surname = input('\nВведите Фамилию: ')
    entry.append(surname.title())
    name = input('Введите Имя: ')
    entry.append(name.title())
    telefon = input('Введите номер телефона: ')
    entry.append(telefon)
    description = input('Введите описание контакта (личный, рабочий, домашний и т.д.): ')
    entry.append(description.title())
    dt = datetime.datetime.now()
    entry.insert(0,dt.strftime('%H:%M - %d.%m.%Y'))
    print('Вами введена запись: ', entry)
    return entry


def run():
     temp = backCode.choice()
     if temp == 1:
          print ('Вами выбрана операция внесения в справочник нового контакта')
          entry = backCode.record()
          logger.log_to_file(entry)
          run()
     if temp == 2:
          print ('\nВами выбрана операция поиска контакта в справочнике\n' )
          entry = backCode.search()
          logger.reading_file(entry)
          run()
     if temp == 3:
          print ('\nВами выбрана операция вывода на печать всех контактов справочника\n\
              \n=== КОНТАКТЫ ТЕЛЕФОННОГО СПРАВОЧНИКА ===\n')
          logger.read_all_file()  
          run()
     if temp == 4:
          print('\n Работа телефонного справочника окончена. Всего доброго.\n')



          