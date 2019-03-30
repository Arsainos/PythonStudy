from sys import argv
#Получаем данные из командной строки
script, arg1 = argv
#Проверка что всё ок подгрузилось
print("This is script: ", script)
print("Arg1 equals: ", arg1)
print("")
#читаем файл
with open(arg1, 'r') as line:
    lis = [i.rstrip() for i in line .readlines() if i.rstrip()]
#делаем частотный словарь
for i in sorted(set(lis)):
    print(i, lis.count(i))
