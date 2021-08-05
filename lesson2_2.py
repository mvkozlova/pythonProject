a = list(input("Введите последовательность"))
line_length = len(a)
j = 0
n = 1

if line_length%2 == 0:
    a[::2], a[1::2] = a[1::2], a[::2]
    print(str(a))
else:
    c = list(a.pop(int(line_length)-1))
    a[::2], a[1::2] = a[1::2], a[::2]
    a = a + c
    print(str(a))
