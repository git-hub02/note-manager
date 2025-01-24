# Имена
list_ = {}
list_["name"] = input('напишите имя пользователя: ')
list_["date"] = input('дата создания заметок (день, месяц, год): ').split()
list_["issue_date"] = input('дата истечения заметок (день, месяц, год): ').split()
# заголовки заметок
list_["titles"] = []
for i in range (4):
    title = input(f"\nВведите заголовок заметки {i + 1}: ")
    list_["titles"].append(title)
# описание заметок
list_["contents"] = []
for k in range(4):
    content = input(f"\nВведите описание заметки {k + 1}: ")
    list_["contents"].append(content)
# статусы заметок
list_["statuses"] = []
for j in range(4):
    status = input(f"\nВведите статус заметки (активно\не активно) №{j + 1}: ")
    list_["statuses"].append(status)
# вывод данных
print("\nBы ввели следующие данные")
print(*list_["name"])
print("Заголовок 1 заметки", *list_["titles"][:1], "\nОписание 1 заметки", *list_["contents"][:1],
      "Статус 1 заметки", *list_["statuses"][:1])
print("\nЗаголовок 2 заметки", *list_["titles"][1:2], "\nОписание 2 заметки", *list_["contents"][1:2],
      "Статус 2 заметки", *list_["statuses"][1:2])
print("\nЗаголовок 3 заметки", *list_["titles"][2:3], "\nОписание 3 заметки", *list_["contents"][2:3],
      "Статус 3 заметки", *list_["statuses"][2:3])
print("\nЗаголовок 4 заметки", *list_["titles"][3:4], "\nОписание 4 заметки", *list_["contents"][3:4],
      "Статус 4 заметки", *list_["statuses"][3:4])
# показывать год или нет
while True:
    answer = input("Показывать год? (да/нет): ")
    if answer in ["Нет", "нет"]:
        print("\nВремя создания заметок", *list_["date"][0:2], "\nВремя истечения заметок", *list_["issue_date"][0:2])
        break
    if answer in ["Да", "да"]:
        print("\nВремя создания заметок", *list_["date"], "\nВремя истечения заметок", *list_["issue_date"])
        break
    else:
        print("не верный ответ попробуйте еще раз")
        continue