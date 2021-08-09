a = input("Введите слова через пробел в нижнем регистре").split()
def int_func(v1):
    rez = str()
    for i in v1:
        rez = rez + " " + i.title()
    return rez

print(int_func(a))