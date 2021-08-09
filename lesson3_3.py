def my_func(v1, v2, v3):
    v1 = float(v1)
    v2 = float(v2)
    v3 = float(v3)
    a = max(v1, v2, v3) + max(min(v1, v2), min(v1, v3), min(v2, v3) )
    return a
rez = my_func(10,20,30)
print(rez)