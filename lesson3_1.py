a1 = float(input("Введите делимое"))
a2 = float(input("Введите делитель"))
def task_1 (var_1, var_2):

    if var_2 == 0:
        a = "Делить на 0 нельзя"
    else:
        a = var_1/var_2
    return a

rez = task_1(a1, a2)
print(rez)