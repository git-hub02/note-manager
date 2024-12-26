# Имена
name = input('напишите имя пользователя: ')
title = input('напишите заголовок: ')
status = input('напишите статус: ')
date_day = input("дата создания заметки""\nдень: ")
date_month = input("месяц: ")
date_year = input("год: ")
issue_date_day = input('дата истечения заметки:''\nдень: ')
issue_date_month = input("месяц: ")
issue_date_year = input("год: ")
# списки
date_create = [date_day,[date_year],[date_month]]
issue_date = [issue_date_day,[issue_date_month],[issue_date_year]]
# показывать ли год
print("Показывать год? (да/нет)")
answer = input()
# заголовки заметок
title1 = input("заголовок 1 заметки: ")
title2 = input("заголовок 2 заметки: ")
title3 = input("заголовок 3 заметки: ")
titles = [title1,title2,title3]
# описание заметок
content1 = input('напишшите описание 1 заметки: ')
content2 = input('напишшите описание 2 заметки: ')
content3 = input('напишшите описание 3 заметки: ')
contents = [content1,content2,content3]
# вывод значений
print("\n\nBы ввели следующие данные")
print("Имя:", name)
print("Заголовоки:",titles)
print("Описания:",contents)
print("Статус:",status)
if answer == "да" or "Да": print("дата создания: ",date_day, date_month, date_year)
elif answer == "нет" or "Нет": print("дата создания: ",date_day, date_month)
if answer == "да" or "Да": print("дата создания: ",issue_date_day,issue_date_month,issue_date_year)
elif answer == "нет" or "Нет": print("дата создания: ",issue_date_day,issue_date_month)
