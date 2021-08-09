rez = 0
h = "N"


def task_5(v1):
    b = 0
    for i in v1:
        b += float(i)
    return b


while True:
    a = input("Введите числа через пробел").split()
    cnt = a.count(h)
    if cnt > 0:
        del a[a.index(h): len(a)]

    c = task_5(a)
    rez = rez + c
    print(rez)
    if cnt > 0:
        break
