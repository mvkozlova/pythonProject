my_list = ['text', 456, 45.3, None, True]
my_kort = tuple('строка')
my_mn = set('abrakadabra')
my_dict = dict(k1='val_1', k2='val_2')
my_list.append(my_kort)
my_list.append(my_mn)
my_list.append(my_dict)
print(my_list)
i = 0

while len(my_list) > 0:
    print(my_list)
    t = my_list.pop(i)
    list2 = type(t)
    print(list2)

    if list2 == str:
        a = "Текст"
        print(str(i) + " = " + a + " // " + str(t))
    elif list2 == float:
        a = "float"
        print(str(i) + " = " + a + " // " + str(t))
    elif list2 == int:
        a = "Целое число"
        print(str(i) + " = " + a + " // " + str(t))
    elif list2 == bool:
        a = "Булевое"
        print(str(i) + " = " + a + " // " + str(t))
    elif list2 == type(None):
        a = "NoneType"
        print(str(i) + " = " + a + " // " + str(t))
    elif list2 == tuple:
        a = "tuple"
        print(str(i) + " = " + a + " // " + str(t))
    elif list2 == dict:
        a = "dict"
        print(str(i) + " = " + a + " // " + str(t))
    elif list2 == set:
        a = "Set"
        print(str(i) + " = " + a + " // " + str(t))
    else:
        i = i + 1
