a = input("Введите количество товаров, которые хотите добавить")
my_dict = {'название': 'val_1', 'цена': 'val_2', 'количество': 'val_3', 'ед': 'val_4'}
my_dict2 = {'название': [], 'цена': [], 'количество': [], 'ед': []}
my_list = list()
list_name = list()
list_price = list()
list_count = list()
list_ed = list()
i = 0
while i <= int(a)-1:
    b = input("Введите название")
    c = input("Введите цену")
    d = input("Введите количество")
    e = input("Введите единицу измерения")
    my_dict['название'] = b
    my_dict['цена'] = c
    my_dict['количество'] = d
    my_dict['ед'] = e
    list_name.insert(i,b)
    list_price.insert(i,c)
    list_count.insert(i, d)
    list_ed.insert(i, e)
    i += 1
    my_dict2 = my_dict.copy()
    my_list.append((i, my_dict2))
    my_dict2['название'] = list_name
    my_dict2['цена'] = list_price
    my_dict2['количество'] = list_count
    my_dict2['ед'] = list_ed

print(my_list)
print(my_dict2)


