my_list = [7, 3, 5, 3, 2]

a = int(input("Введите число"))
cnt = my_list.count(a)
my_list.sort()
if cnt >= 1:
    pos = my_list.index(a) + cnt
    my_list.insert(pos, a)
    my_list.sort(reverse=True)
else:
    print(my_list)
    bmax = my_list[0]
    bmin = my_list[len(my_list) - 1]
    if a > bmax:
        pos = my_list.index(bmax) + 1
        my_list.insert(pos, a)
        my_list.sort(reverse=True)
    elif a < bmin:
        pos = my_list.index(bmin)
        my_list.insert(pos, a)
        my_list.sort(reverse=True)

print(my_list)
